"""Config inventory auditing for config/output/plugins drift detection."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from crawler.config import CrawlerConfig, load_config


def _load_crawler_config(config_path: Path) -> CrawlerConfig:
    if config_path.exists():
        return load_config(str(config_path))
    return CrawlerConfig()


def _collect_crawled_clis(output_dir: Path) -> set[str]:
    if not output_dir.exists():
        return set()
    clis: set[str] = set()
    for path in output_dir.glob("*.json"):
        if path.name.endswith(".raw.json"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        cli_name = payload.get("cli_name")
        if isinstance(cli_name, str) and cli_name.strip():
            clis.add(cli_name.strip())
    return clis


def _collect_plugin_clis(plugins_dir: Path) -> set[str]:
    if not plugins_dir.exists():
        return set()
    clis: set[str] = set()
    for child in plugins_dir.iterdir():
        if not child.is_dir() or not child.name.startswith("cli-"):
            continue
        cli_name = child.name[len("cli-") :]
        if cli_name:
            clis.add(cli_name)
    return clis


def _suggest_minimal_overrides(config: CrawlerConfig) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Keep only operational overrides that differ from defaults."""
    defaults = config.defaults
    suggestions: dict[str, dict[str, Any]] = {}
    no_overrides: list[str] = []

    for cli_name, cfg in sorted(config.clis.items()):
        overrides: dict[str, Any] = {}

        if cfg.environment != defaults.environment:
            overrides["environment"] = cfg.environment
        if cfg.help_pattern:
            overrides["help_pattern"] = cfg.help_pattern
        if cfg.max_depth != defaults.max_depth:
            overrides["max_depth"] = cfg.max_depth
        if cfg.max_concurrent != defaults.max_concurrent:
            overrides["max_concurrent"] = cfg.max_concurrent
        if cfg.plugins and cfg.plugins.discovery_command:
            overrides["plugins"] = {"discovery_command": cfg.plugins.discovery_command}

        if overrides:
            suggestions[cli_name] = overrides
        else:
            no_overrides.append(cli_name)

    return suggestions, no_overrides


def build_config_audit_report(
    config_path: Path,
    output_dir: Path,
    plugins_dir: Path,
) -> dict[str, Any]:
    """Build a config drift report across config, output, and plugins inventory."""
    config = _load_crawler_config(config_path)

    configured = set(config.clis.keys())
    crawled = _collect_crawled_clis(output_dir)
    generated_plugins = _collect_plugin_clis(plugins_dir)
    discovered = crawled | generated_plugins

    suggested_overrides, entries_without_overrides = _suggest_minimal_overrides(config)

    report: dict[str, Any] = {
        "configured_clis": sorted(configured),
        "crawled_clis": sorted(crawled),
        "plugin_clis": sorted(generated_plugins),
        "missing_in_config": sorted(discovered - configured),
        "stale_in_config": sorted(configured - discovered),
        "missing_output": sorted(configured - crawled),
        "missing_plugin": sorted(configured - generated_plugins),
        "suggested_minimal_overrides": suggested_overrides,
        "config_entries_without_overrides": sorted(entries_without_overrides),
    }

    return report


def write_config_audit_report(report: dict[str, Any], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="config-audit",
        description="Audit drift between config.yaml, output/*.json, and plugins/cli-* inventory.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to config YAML (default: config.yaml)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Directory with crawl JSON files (default: output/)",
    )
    parser.add_argument(
        "--plugins-dir",
        type=Path,
        default=Path("plugins"),
        help="Directory with generated plugins (default: plugins/)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("output/config-audit.json"),
        help="JSON report output path (default: output/config-audit.json)",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    report = build_config_audit_report(args.config, args.output_dir, args.plugins_dir)
    write_config_audit_report(report, args.report)

    print(f"Config audit report written to: {args.report}")
    print(f"  configured_clis: {len(report['configured_clis'])}")
    print(f"  crawled_clis:    {len(report['crawled_clis'])}")
    print(f"  plugin_clis:     {len(report['plugin_clis'])}")
    print(f"  missing_in_config: {len(report['missing_in_config'])}")
    print(f"  stale_in_config:   {len(report['stale_in_config'])}")
    print(f"  missing_output:    {len(report['missing_output'])}")
    print(f"  missing_plugin:    {len(report['missing_plugin'])}")


if __name__ == "__main__":
    main()
