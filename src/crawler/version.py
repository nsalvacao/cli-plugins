"""CLI version detection and parsing."""

from __future__ import annotations

import logging
import re

from .executor import Executor

logger = logging.getLogger("cli_crawler.version")

VERSION_PATTERNS = [
    # "git version 2.43.0"
    re.compile(r"version\s+v?(\d+\.\d+(?:\.\d+)?(?:[-.\w]*))"),
    # "pip 24.0 from ..." or "langchain-cli 0.0.37"
    re.compile(r"^\w[\w-]*\s+(\d+\.\d+(?:\.\d+)?)(?:\s|$)"),
    # "npm@11.8.0" or "@11.8.0"
    re.compile(r"@(\d+\.\d+\.\d+)"),
    # "v3.1.0-alpha.3" (standalone)
    re.compile(r"\bv(\d+\.\d+\.\d+[-.\w]*)"),
    # "2.43.0" on its own line
    re.compile(r"^(\d+\.\d+(?:\.\d+)?[-.\w]*)\s*$"),
]

VERSION_COMMANDS = ["--version", "-V", "version", "-v"]


def detect_version(cli_name: str, executor: Executor) -> str:
    """Try version commands, parse version string."""
    for vcmd in VERSION_COMMANDS:
        cmd = [cli_name, vcmd] if vcmd != "version" else [cli_name, vcmd]
        result = executor.run(cmd, timeout=3)

        if result.exit_code == 0 or result.stdout.strip():
            text = result.stdout.strip()
            version = _parse_version(text)
            if version:
                logger.debug("Version for %s: %s (via %s)", cli_name, version, vcmd)
                return version

        # Also check stderr (some CLIs output version there)
        if result.stderr.strip() and not result.stderr.startswith("TIMEOUT"):
            version = _parse_version(result.stderr.strip())
            if version:
                return version

    logger.warning("Could not detect version for %s", cli_name)
    return ""


def _parse_version(text: str) -> str:
    """Extract version string from text."""
    # Try each line
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        for pattern in VERSION_PATTERNS:
            m = pattern.search(stripped)
            if m:
                return m.group(1)
    return ""
