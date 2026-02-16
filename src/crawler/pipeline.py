"""Top-level pipeline: detector -> executor -> parser -> formatter."""

from __future__ import annotations

import logging
import time
from datetime import UTC, datetime
from pathlib import Path

from .config import CLIConfig, CrawlerConfig
from .detector import detect_help_pattern
from .discovery import CrawlState, discover_and_crawl, discover_plugins
from .executor import Executor
from .formatter import write_output
from .models import CLIMap, Flag
from .parser import parse_help_output
from .version import detect_version

logger = logging.getLogger("cli_crawler")


def _resolve_output_path(output: str | Path, cli_name: str) -> Path:
    """Resolve CLI output target.

    Accepts either:
    - a directory path (legacy behavior) -> <dir>/<cli_name>.json
    - a JSON file path -> exact file path
    """
    output_path = Path(output)
    if output_path.exists() and output_path.is_dir():
        return output_path / f"{cli_name}.json"
    if output_path.suffix.lower() == ".json":
        return output_path
    return output_path / f"{cli_name}.json"


def crawl_cli(
    cli_name: str,
    config: CLIConfig,
    output_path: Path | None = None,
    include_raw: bool = False,
    strict: bool = False,
) -> CLIMap:
    """Full pipeline for one CLI."""
    start = time.monotonic()
    logger.info("=== Crawling: %s ===", cli_name)

    # 1. Create executor
    executor = Executor(config)

    # 2. Detect version
    version = detect_version(cli_name, executor)
    logger.info("Version: %s", version or "(unknown)")

    # 3. Detect help pattern
    detection = detect_help_pattern(cli_name, executor, config)
    help_error = ""
    if detection.pattern == "auth_required":
        help_error = detection.result.stderr.strip() or (
            "AUTH_REQUIRED: Help command requires authentication."
        )
        logger.error(help_error)
        if strict:
            raise RuntimeError(help_error)

    if detection.pattern == "unknown":
        logger.warning("No standard help output for %s; running in degraded mode.", cli_name)
        if strict:
            raise RuntimeError(f"No help output found for {cli_name}")

    logger.info("Help pattern: %s (manpage=%s)", detection.pattern, detection.is_manpage)

    root_help = "" if detection.pattern == "auth_required" else detection.result.stdout
    parse_input, progressive_loading, raw_line_count, parsed_line_count = (
        _apply_progressive_loading(
            root_help,
            config.raw_threshold,
        )
    )
    progressive_warning = ""
    if progressive_loading:
        progressive_warning = (
            "Progressive loading enabled for "
            f"{cli_name}: parsed {parsed_line_count}/{raw_line_count} help lines."
        )
        logger.warning(progressive_warning)

    # 4. Parse root help
    parse_result = parse_help_output(
        parse_input,
        cli_name,
        cli_name,
        force_manpage=detection.is_manpage,
    )

    # 5. Build initial state
    state = CrawlState(visited={cli_name})
    state.set_raw_output(cli_name, root_help)
    state.extend_warnings(parse_result.warnings)
    if detection.pattern == "unknown":
        state.add_warning(f"No standard help output for {cli_name}; using partial CLIMap.")
    if help_error:
        state.add_warning(help_error)
    if progressive_warning:
        state.add_warning(progressive_warning)

    # 6. Separate global flags from local flags
    global_flags, local_flags = _separate_global_flags(
        parse_result.command.flags,
        parse_input,
    )

    # 7. Discover plugins if configured
    plugin_cmds: list[str] = []
    if config.plugins:
        plugin_cmds = discover_plugins(cli_name, executor, config)

    # 8. Recursively crawl subcommands
    all_subcmd_names = parse_result.subcommand_names + plugin_cmds
    logger.info(
        "Discovered %d subcommands + %d plugins",
        len(parse_result.subcommand_names),
        len(plugin_cmds),
    )

    subtree = discover_and_crawl(
        cli_name,
        cli_name,
        all_subcmd_names,
        executor,
        config,
        state,
        detection.pattern,
        parent_descriptions=parse_result.subcommand_descriptions,
    )

    # Mark plugin commands as dynamic
    for plugin_name in plugin_cmds:
        if plugin_name in subtree:
            subtree[plugin_name].dynamic = True

    # 9. Compute meta
    duration = time.monotonic() - start
    meta = _compute_meta(subtree, duration, state, global_flags)
    meta["confidence_score"] = (
        f"{_compute_confidence_score(parse_result.command.confidence, detection.pattern, state, progressive_loading):.2f}"
    )
    meta["progressive_loading"] = "true" if progressive_loading else "false"
    meta["raw_line_count"] = str(raw_line_count)
    meta["parsed_line_count"] = str(parsed_line_count)
    if help_error:
        meta["help_error"] = help_error

    # 10. Assemble CLIMap
    # 10. Assemble CLIMap
    cli_map = CLIMap(
        cli_name=cli_name,
        cli_version=version,
        metadata={
            "scanned_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "help_pattern": detection.pattern,
            **meta,  # flatten meta stats into metadata
        },
        global_flags=global_flags,
        environment_variables=parse_result.command.env_vars,
        commands=subtree,
    )

    # 11. Write output
    if output_path:
        write_output(cli_map, state.raw_outputs, output_path, config, include_raw)

    logger.info(
        "=== Done: %s (%d commands, %d flags, %.1fs) ===",
        cli_name,
        int(meta.get("total_commands", 0)),
        int(meta.get("total_flags", 0)),
        duration,
    )

    return cli_map


def crawl_all(
    config: CrawlerConfig,
    output_dir: Path,
    include_raw: bool = False,
    strict: bool = False,
) -> list[CLIMap]:
    """Crawl all CLIs in config sequentially."""
    results: list[CLIMap] = []
    output_dir.mkdir(parents=True, exist_ok=True)

    for cli_name, cli_config in config.clis.items():
        output_path = output_dir / f"{cli_name}.json"
        try:
            cli_map = crawl_cli(
                cli_name,
                cli_config,
                output_path,
                include_raw,
                strict,
            )
            results.append(cli_map)
        except Exception as e:
            logger.error("Failed to crawl %s: %s", cli_name, e)
            if strict:
                raise

    return results


def _apply_progressive_loading(
    raw_text: str,
    threshold_lines: int,
) -> tuple[str, bool, int, int]:
    """Return parse input with optional line-based truncation for very long help."""
    if not raw_text:
        return "", False, 0, 0

    lines = raw_text.splitlines()
    raw_line_count = len(lines)
    if threshold_lines <= 0 or raw_line_count <= threshold_lines:
        return raw_text, False, raw_line_count, raw_line_count

    truncated = "\n".join(lines[:threshold_lines]).rstrip()
    truncated = (
        f"{truncated}\n\n[... truncated by cli-crawler after {threshold_lines} lines "
        f"(original: {raw_line_count}) ...]"
    )
    return truncated, True, raw_line_count, threshold_lines


def _compute_confidence_score(
    base_confidence: float,
    help_pattern: str,
    state: CrawlState,
    progressive_loading: bool,
) -> float:
    """Compute a crawl-level confidence score with degradation penalties."""
    score = max(0.0, min(base_confidence, 1.0))

    if help_pattern == "auth_required":
        score = min(score, 0.25)
    elif help_pattern == "unknown":
        score = min(score, 0.35)

    score -= min(0.25, len(state.warnings) * 0.05)
    if progressive_loading:
        score -= 0.05

    return max(0.0, min(score, 1.0))


def _separate_global_flags(
    all_flags: list[Flag],
    raw_text: str,
) -> tuple[list[Flag], list[Flag]]:
    """Separate global flags from local flags based on section markers in raw text."""
    # Check if the raw text has explicit global flags sections
    lower_text = raw_text.lower()
    has_global_section = any(
        marker in lower_text
        for marker in [
            "global flags",
            "global options",
            "inherited flags",
        ]
    )

    if not has_global_section:
        # All flags are "local" (at root level, they become global by default)
        return all_flags, []

    # Flags that were parsed from global/inherited sections
    # The parser already merged them; we treat all root flags as global
    return all_flags, []


def _compute_meta(
    tree: dict,
    duration: float,
    state: CrawlState,
    global_flags: list[Flag],
) -> dict[str, str]:
    """Compute metadata stats."""
    total_commands = 0
    total_flags = len(global_flags)
    max_depth = 0

    def _walk(subtree: dict, depth: int) -> None:
        nonlocal total_commands, total_flags, max_depth
        for cmd in subtree.values():
            total_commands += 1
            total_flags += len(cmd.flags)
            max_depth = max(max_depth, depth)
            if cmd.subcommands:
                _walk(cmd.subcommands, depth + 1)

    _walk(tree, 1)

    return {
        "total_commands": str(total_commands),
        "total_flags": str(total_flags),
        "max_depth": str(max_depth),
        "parse_errors": str(state.errors),
        "parse_warnings": str(len(state.warnings)),
        "duration_seconds": f"{duration:.2f}",
    }


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point for ``cli-crawler``."""
    import argparse

    try:
        from importlib.metadata import version

        pkg_version = version("cli-plugins")
    except Exception:
        pkg_version = "0.0.0-dev"

    parser = argparse.ArgumentParser(
        prog="cli-crawler",
        description="Crawl CLI --help outputs and produce structured CLIMap JSON.",
    )
    parser.add_argument("--version", action="version", version=f"cli-crawler {pkg_version}")
    parser.add_argument(
        "cli_name",
        help="Name of the CLI to crawl (e.g. docker, git, gh)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output",
        help=(
            "Output path for CLIMap JSON. Accepts either a directory "
            "(default: output/) or a .json file path."
        ),
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Include raw --help text in output",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on errors instead of logging warnings",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose (DEBUG) logging",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    # Load config for this CLI (use defaults if not in config.yaml)
    from .config import CrawlerConfig, load_config

    config_path = Path("config.yaml")
    if config_path.exists():
        config = load_config(str(config_path))
    else:
        config = CrawlerConfig()
    cli_config = config.clis.get(args.cli_name, CLIConfig(name=args.cli_name))

    output_path = _resolve_output_path(args.output, args.cli_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cli_map = crawl_cli(
        args.cli_name,
        cli_config,
        output_path,
        include_raw=args.raw,
        strict=args.strict,
    )
    print(f"CLIMap written to: {output_path}")
    print(f"  Commands: {cli_map.metadata.get('total_commands', 0)}")
    print(f"  Flags:    {cli_map.metadata.get('total_flags', 0)}")
    print(f"  Duration: {cli_map.metadata.get('duration_seconds', 0)}s")


if __name__ == "__main__":
    main()
