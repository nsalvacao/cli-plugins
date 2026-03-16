"""Compatibility wrappers for legacy ``cli_crawler`` entrypoints."""

from __future__ import annotations

import sys
from pathlib import Path

from . import pipeline as _pipeline
from .config import CLIConfig, CrawlerConfig
from .executor import Executor
from .models import CLIMap, ExecutionResult
from .pipeline import crawl_all, crawl_cli

_RAW_FLAG = "--raw"
_LEGACY_RAW_FLAG = "--include-raw"


def _normalize_legacy_args(argv: list[str]) -> tuple[list[str], list[str]]:
    """Normalize legacy flags to canonical ``cli-crawler`` arguments."""
    normalized: list[str] = []
    warnings: list[str] = []
    raw_enabled = False
    legacy_raw_seen = False

    for arg in argv:
        if arg == _RAW_FLAG:
            raw_enabled = True
            normalized.append(arg)
            continue
        if arg == _LEGACY_RAW_FLAG:
            legacy_raw_seen = True
            if not raw_enabled:
                normalized.append(_RAW_FLAG)
                raw_enabled = True
            continue
        normalized.append(arg)

    if legacy_raw_seen:
        if _RAW_FLAG in argv:
            warnings.append(
                f"{_LEGACY_RAW_FLAG} is deprecated and ignored when {_RAW_FLAG} is also provided."
            )
        else:
            warnings.append(f"{_LEGACY_RAW_FLAG} is deprecated; treating it as {_RAW_FLAG}.")

    return normalized, warnings


def _legacy_entrypoint_warning(program_name: str) -> str | None:
    """Return a warning when executed via legacy file-based entrypoint."""
    if Path(program_name).name == "cli_crawler.py":
        return "Legacy entrypoint detected. Prefer the canonical command: cli-crawler."
    return None


def main() -> None:
    """Compatibility entrypoint that delegates to ``crawler.pipeline.main``."""
    original_argv = sys.argv[:]
    normalized_args, warnings = _normalize_legacy_args(original_argv[1:])
    legacy_warning = _legacy_entrypoint_warning(original_argv[0])
    if legacy_warning:
        warnings.insert(0, legacy_warning)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    sys.argv = [original_argv[0], *normalized_args]
    try:
        _pipeline.main()
    finally:
        sys.argv = original_argv


def run_root_help(cli_name: str, config: CLIConfig | None = None) -> ExecutionResult:
    """Execute `<cli> --help` with crawler defaults."""
    cfg = config or CLIConfig(name=cli_name)
    executor = Executor(cfg)
    return executor.run_with_retry([cli_name, "--help"])


def crawl_single(
    cli_name: str,
    config: CLIConfig | None = None,
) -> CLIMap:
    """Compatibility helper for crawling one CLI."""
    cfg = config or CLIConfig(name=cli_name)
    return crawl_cli(cli_name, cfg)


def crawl_configured(config: CrawlerConfig, output_dir: str = "output") -> list[CLIMap]:
    """Compatibility helper for crawling all configured CLIs."""
    return crawl_all(config, Path(output_dir))


__all__ = [
    "crawl_all",
    "crawl_cli",
    "crawl_configured",
    "crawl_single",
    "main",
    "run_root_help",
]
