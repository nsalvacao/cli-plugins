"""Recursive subcommand discovery with cycle detection and parallelism."""

from __future__ import annotations

import concurrent.futures
import logging
import threading
from dataclasses import dataclass, field

from .config import CLIConfig
from .detector import detect_subcommand_help
from .executor import Executor
from .models import Command
from .parser import parse_help_output

logger = logging.getLogger("cli_crawler.discovery")


@dataclass
class CrawlState:
    visited: set[str] = field(default_factory=set)  # full command strings
    raw_outputs: dict[str, str] = field(default_factory=dict)  # path -> raw text
    depth: int = 0
    errors: int = 0
    warnings: list[str] = field(default_factory=list)
    lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def mark_visited(self, command_path: str) -> bool:
        """Atomically mark a command as visited.

        Returns True when the command was newly added, False if it was already visited.
        """
        with self.lock:
            if command_path in self.visited:
                return False
            self.visited.add(command_path)
            return True

    def set_raw_output(self, command_path: str, output: str) -> None:
        """Atomically store raw help output for a command path."""
        with self.lock:
            self.raw_outputs[command_path] = output

    def get_raw_output(self, command_path: str) -> str:
        """Atomically fetch raw help output for a command path."""
        with self.lock:
            return self.raw_outputs.get(command_path, "")

    def increment_errors(self) -> None:
        """Atomically increment parse/crawl error counter."""
        with self.lock:
            self.errors += 1

    def add_warning(self, warning: str) -> None:
        """Atomically append a warning."""
        with self.lock:
            self.warnings.append(warning)

    def extend_warnings(self, warnings: list[str]) -> None:
        """Atomically append many warnings."""
        if not warnings:
            return
        with self.lock:
            self.warnings.extend(warnings)


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
            if not state.mark_visited(full_path):
                logger.debug("Skipping visited: %s", full_path)
                continue

            future = pool.submit(
                _crawl_single_subcommand,
                cli_name,
                parent_path,
                subcmd_name,
                executor,
                config,
                state,
                help_pattern,
                current_depth,
                parent_descriptions,
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
                state.increment_errors()
                state.add_warning(f"Error crawling {parent_path} {subcmd_name}: {e}")
                logger.warning("Error crawling %s %s: %s", parent_path, subcmd_name, e)

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
) -> tuple[str, Command] | None:
    """Crawl one subcommand. Returns (name, Command) or None on failure."""
    full_path = f"{parent_path} {subcmd_name}"
    subcommand_parts = full_path.split()[1:]  # remove cli_name

    logger.info("Crawling: %s (depth=%d)", full_path, current_depth)

    # Get help for this subcommand
    detection = detect_subcommand_help(
        cli_name,
        subcommand_parts,
        executor,
        help_pattern,
    )

    if not detection.result.stdout.strip():
        stderr_msg = detection.result.stderr.strip()
        if detection.pattern == "auth_required" and stderr_msg:
            state.add_warning(stderr_msg)
            logger.warning("Auth required for %s help: %s", full_path, stderr_msg)
        elif stderr_msg:
            state.add_warning(stderr_msg)
            logger.warning("No usable help for %s: %s", full_path, stderr_msg)
        state.add_warning(f"No help output for: {full_path}")
        return None

    # Detect when subcommand returns identical help as parent (echoed parent)
    parent_raw = state.get_raw_output(parent_path)
    is_echoed = parent_raw and detection.result.stdout.strip() == parent_raw.strip()

    if is_echoed:
        logger.info("Echoed parent help detected for %s, using parent listing", full_path)
        # Build a minimal command using the one-liner from the parent listing
        desc = parent_descriptions.get(subcmd_name, "")
        cmd = Command(
            path=full_path,
            name=subcmd_name,
            description=desc,
            confidence=0.6,
        )
        state.set_raw_output(full_path, detection.result.stdout)
        return subcmd_name, cmd

    # Parse the help output
    parse_result = parse_help_output(
        detection.result.stdout,
        cli_name,
        full_path,
        force_manpage=detection.is_manpage,
    )

    # Store raw output
    state.set_raw_output(full_path, detection.result.stdout)

    # Track warnings
    state.extend_warnings(parse_result.warnings)

    cmd = parse_result.command

    # If cmd description is identical to parent's, prefer the parent listing one-liner
    if subcmd_name in parent_descriptions:
        parent_desc_oneliner = parent_descriptions[subcmd_name]
        parent_lines = state.get_raw_output(parent_path).splitlines()
        parent_first_line = parent_lines[0].strip() if parent_lines else ""
        if parent_first_line and cmd.description == parent_first_line:
            cmd.description = parent_desc_oneliner

    # Recursively crawl sub-subcommands
    if parse_result.subcommand_names:
        cmd.subcommands = discover_and_crawl(
            cli_name,
            full_path,
            parse_result.subcommand_names,
            executor,
            config,
            state,
            help_pattern,
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
        logger.warning("Plugin discovery failed for %s: %s", cli_name, result.stderr)
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

    logger.info("Discovered %d plugins for %s: %s", len(plugins), cli_name, plugins)
    return plugins
