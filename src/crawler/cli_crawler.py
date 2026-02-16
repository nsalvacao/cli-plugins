"""Compatibility crawler entrypoint and basic help execution helpers (T013)."""

from __future__ import annotations

from .config import CLIConfig, CrawlerConfig
from .executor import Executor
from .models import CLIMap, ExecutionResult
from .pipeline import crawl_all, crawl_cli, main


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
    from pathlib import Path

    return crawl_all(config, Path(output_dir))


__all__ = [
    "crawl_all",
    "crawl_cli",
    "crawl_configured",
    "crawl_single",
    "main",
    "run_root_help",
]
