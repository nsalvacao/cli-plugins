"""Top-level pipeline: detector -> executor -> parser -> formatter."""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .config import CLIConfig, CrawlerConfig
from .detector import detect_help_pattern
from .discovery import CrawlState, discover_and_crawl, discover_plugins
from .executor import Executor
from .formatter import write_output
from .models import CLIMap, Meta, Flag
from .parser import parse_help_output
from .version import detect_version

logger = logging.getLogger("cli_crawler")


def crawl_cli(
    cli_name: str,
    config: CLIConfig,
    output_path: Optional[Path] = None,
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
    if detection.pattern == "unknown":
        logger.error("No help output found for %s", cli_name)
        if strict:
            raise RuntimeError(f"No help output found for {cli_name}")

    logger.info("Help pattern: %s (manpage=%s)", detection.pattern, detection.is_manpage)

    # 4. Parse root help
    parse_result = parse_help_output(
        detection.result.stdout, cli_name, cli_name,
        force_manpage=detection.is_manpage,
    )

    # 5. Build initial state
    state = CrawlState(visited={cli_name})
    state.raw_outputs[cli_name] = detection.result.stdout
    state.warnings.extend(parse_result.warnings)

    # 6. Separate global flags from local flags
    global_flags, local_flags = _separate_global_flags(
        parse_result.command.flags, detection.result.stdout,
    )

    # 7. Discover plugins if configured
    plugin_cmds: list[str] = []
    if config.plugins:
        plugin_cmds = discover_plugins(cli_name, executor, config)

    # 8. Recursively crawl subcommands
    all_subcmd_names = parse_result.subcommand_names + plugin_cmds
    logger.info("Discovered %d subcommands + %d plugins",
                len(parse_result.subcommand_names), len(plugin_cmds))

    subtree = discover_and_crawl(
        cli_name, cli_name, all_subcmd_names,
        executor, config, state, detection.pattern,
        parent_descriptions=parse_result.subcommand_descriptions,
    )

    # Mark plugin commands as dynamic
    for plugin_name in plugin_cmds:
        if plugin_name in subtree:
            subtree[plugin_name].dynamic = True

    # 9. Compute meta
    duration = time.monotonic() - start
    meta = _compute_meta(subtree, duration, state, global_flags)

    # 10. Assemble CLIMap
    cli_map = CLIMap(
        cli=cli_name,
        version=version,
        scanned_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        help_pattern=detection.pattern,
        global_flags=global_flags,
        env_vars=parse_result.command.env_vars,
        tree=subtree,
        meta=meta,
    )

    # 11. Write output
    if output_path:
        write_output(cli_map, state.raw_outputs, output_path, config, include_raw)

    logger.info("=== Done: %s (%d commands, %d flags, %.1fs) ===",
                cli_name, meta.total_commands, meta.total_flags, duration)

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
                cli_name, cli_config, output_path, include_raw, strict,
            )
            results.append(cli_map)
        except Exception as e:
            logger.error("Failed to crawl %s: %s", cli_name, e)
            if strict:
                raise

    return results


def _separate_global_flags(
    all_flags: list[Flag],
    raw_text: str,
) -> tuple[list[Flag], list[Flag]]:
    """Separate global flags from local flags based on section markers in raw text."""
    # Check if the raw text has explicit global flags sections
    lower_text = raw_text.lower()
    has_global_section = any(marker in lower_text for marker in [
        "global flags", "global options", "inherited flags",
    ])

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
) -> Meta:
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

    return Meta(
        total_commands=total_commands,
        total_flags=total_flags,
        max_depth=max_depth,
        parse_errors=state.errors,
        parse_warnings=state.warnings,
        duration_seconds=duration,
    )
