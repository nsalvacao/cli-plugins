"""Recursive subcommand discovery with cycle detection and parallelism."""

from __future__ import annotations

import concurrent.futures
import logging
from dataclasses import dataclass, field
from typing import Optional

from .config import CLIConfig
from .detector import detect_subcommand_help
from .executor import Executor
from .models import Command, ParseResult
from .parser import parse_help_output

logger = logging.getLogger("cli_crawler.discovery")


@dataclass
class CrawlState:
    visited: set[str] = field(default_factory=set)  # full command strings
    raw_outputs: dict[str, str] = field(default_factory=dict)  # path -> raw text
    depth: int = 0
    errors: int = 0
    warnings: list[str] = field(default_factory=list)


def discover_and_crawl(
    cli_name: str,
    parent_path: str,
    subcommand_names: list[str],
    executor: Executor,
    config: CLIConfig,
    state: CrawlState,
    help_pattern: str,
    current_depth: int = 1,
    parent_descriptions: dict[str, str] | None = None,
) -> dict[str, Command]:
    """Recursively crawl subcommands with cycle detection and depth limiting."""
    if current_depth > config.max_depth:
        logger.info("Max depth %d reached at %s", config.max_depth, parent_path)
        return {}

    if not subcommand_names:
        return {}

    if parent_descriptions is None:
        parent_descriptions = {}

    results: dict[str, Command] = {}

    # Use thread pool for parallel crawling within same CLI
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=min(config.max_concurrent, len(subcommand_names))
    ) as pool:
        futures = {}
        for subcmd_name in subcommand_names:
            full_path = f"{parent_path} {subcmd_name}"
            if full_path in state.visited:
                logger.debug("Skipping visited: %s", full_path)
                continue
            state.visited.add(full_path)

            future = pool.submit(
                _crawl_single_subcommand,
                cli_name, parent_path, subcmd_name,
                executor, config, state, help_pattern,
                current_depth, parent_descriptions,
            )
            futures[future] = subcmd_name

        for future in concurrent.futures.as_completed(futures):
            subcmd_name = futures[future]
            try:
                result = future.result()
                if result:
                    name, cmd = result
                    results[name] = cmd
            except Exception as e:
                state.errors += 1
                state.warnings.append(
                    f"Error crawling {parent_path} {subcmd_name}: {e}"
                )
                logger.warning("Error crawling %s %s: %s",
                               parent_path, subcmd_name, e)

    return results


def _crawl_single_subcommand(
    cli_name: str,
    parent_path: str,
    subcmd_name: str,
    executor: Executor,
    config: CLIConfig,
    state: CrawlState,
    help_pattern: str,
    current_depth: int,
    parent_descriptions: dict[str, str],
) -> Optional[tuple[str, Command]]:
    """Crawl one subcommand. Returns (name, Command) or None on failure."""
    full_path = f"{parent_path} {subcmd_name}"
    subcommand_parts = full_path.split()[1:]  # remove cli_name

    logger.info("Crawling: %s (depth=%d)", full_path, current_depth)

    # Get help for this subcommand
    detection = detect_subcommand_help(
        cli_name, subcommand_parts, executor, help_pattern,
    )

    if not detection.result.stdout.strip():
        state.warnings.append(f"No help output for: {full_path}")
        return None

    # Detect when subcommand returns identical help as parent (echoed parent)
    parent_raw = state.raw_outputs.get(parent_path, "")
    is_echoed = (
        parent_raw
        and detection.result.stdout.strip() == parent_raw.strip()
    )

    if is_echoed:
        logger.info("Echoed parent help detected for %s, using parent listing", full_path)
        # Build a minimal command using the one-liner from the parent listing
        desc = parent_descriptions.get(subcmd_name, "")
        cmd = Command(
            path=full_path,
            description=desc,
            confidence=0.6,
        )
        state.raw_outputs[full_path] = detection.result.stdout
        return subcmd_name, cmd

    # Parse the help output
    parse_result = parse_help_output(
        detection.result.stdout, cli_name, full_path,
        force_manpage=detection.is_manpage,
    )

    # Store raw output
    state.raw_outputs[full_path] = detection.result.stdout

    # Track warnings
    state.warnings.extend(parse_result.warnings)

    cmd = parse_result.command

    # If cmd description is identical to parent's, prefer the parent listing one-liner
    if subcmd_name in parent_descriptions:
        parent_desc_oneliner = parent_descriptions[subcmd_name]
        if cmd.description == state.raw_outputs.get(parent_path, "").splitlines()[0].strip():
            cmd.description = parent_desc_oneliner

    # Recursively crawl sub-subcommands
    if parse_result.subcommand_names:
        cmd.subcommands = discover_and_crawl(
            cli_name, full_path, parse_result.subcommand_names,
            executor, config, state, help_pattern,
            current_depth + 1,
            parse_result.subcommand_descriptions,
        )

    return subcmd_name, cmd


def discover_plugins(
    cli_name: str,
    executor: Executor,
    config: CLIConfig,
) -> list[str]:
    """Run plugin discovery command if configured."""
    if not config.plugins or not config.plugins.discovery_command:
        return []

    cmd_parts = config.plugins.discovery_command.split()
    result = executor.run(cmd_parts, timeout=10)

    if result.exit_code != 0 or not result.stdout.strip():
        logger.warning("Plugin discovery failed for %s: %s",
                        cli_name, result.stderr)
        return []

    # Parse plugin names from output (one per line, first word)
    plugins: list[str] = []
    for line in result.stdout.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            name = stripped.split()[0]
            # Clean up common prefixes
            name = name.lstrip("- ")
            if name:
                plugins.append(name)

    logger.info("Discovered %d plugins for %s: %s",
                len(plugins), cli_name, plugins)
    return plugins
