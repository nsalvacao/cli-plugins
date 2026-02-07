"""Subcommand list parsing handling 4 format families.

Formats handled:
1. Tabular:       run         Create and run...      (docker, uv, pip)
2. Colon:         auth:       Authenticate...        (gh)
3. CSV:           access, adduser, audit, ...         (npm)
4. Plugin marker: buildx*     Docker Buildx           (docker)
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

# --- Regex patterns ---

# Tabular: "  command    Description text"
CMD_TABULAR_RE = re.compile(
    r"^\s+"
    r"([\w][\w.-]*)"            # command name (word chars, dots, hyphens)
    r"(\*)?"                    # optional plugin marker
    r"\s{2,}"                   # gap
    r"(.+)$"                    # description
)

# Colon-delimited: "  auth:    Authenticate..."
CMD_COLON_RE = re.compile(
    r"^\s+"
    r"(\S+):"                   # command name with colon
    r"\s+"                      # gap
    r"(.+)$"                    # description
)

# CSV flat list: "  access, adduser, audit, bugs, cache, ..."
CMD_CSV_RE = re.compile(
    r"^\s+"
    r"([\w-]+(?:[,]\s*[\w-]+)+)"  # comma-separated words
    r",?\s*$"
)

# Alias pattern: "Alias for ..."
ALIAS_RE = re.compile(r"[Aa]lias\s+for\s+[\"']?(.+?)[\"']?\s*$")


@dataclass
class ParsedCommand:
    name: str
    description: str = ""
    group: Optional[str] = None
    is_plugin: bool = False
    is_alias: bool = False
    alias_target: Optional[str] = None


def parse_command_section(content: str, group: Optional[str] = None) -> list[ParsedCommand]:
    """Parse a commands section, auto-detecting format."""
    lines = content.splitlines()
    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return []

    # Try each format, pick the one with most matches
    results_tabular = _try_tabular(lines, group)
    results_colon = _try_colon(lines, group)
    results_csv = _try_csv(lines, group)

    # Pick best result by match count
    candidates = [
        (results_tabular, "tabular"),
        (results_colon, "colon"),
        (results_csv, "csv"),
    ]
    best = max(candidates, key=lambda x: len(x[0]) if x[0] else 0)
    return best[0] if best[0] else []


def _try_tabular(lines: list[str], group: Optional[str]) -> list[ParsedCommand]:
    """Try tabular format parsing."""
    results: list[ParsedCommand] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        m = CMD_TABULAR_RE.match(line)
        if m:
            name = m.group(1)
            is_plugin = bool(m.group(2))
            desc = m.group(3).strip()

            # Skip common non-command lines
            if _is_noise(name):
                continue

            is_alias = bool(ALIAS_RE.search(desc))
            alias_target = None
            if is_alias:
                am = ALIAS_RE.search(desc)
                if am:
                    alias_target = am.group(1)

            results.append(ParsedCommand(
                name=name, description=desc, group=group,
                is_plugin=is_plugin, is_alias=is_alias,
                alias_target=alias_target,
            ))
    return results


def _try_colon(lines: list[str], group: Optional[str]) -> list[ParsedCommand]:
    """Try colon-delimited format parsing (gh style)."""
    results: list[ParsedCommand] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        m = CMD_COLON_RE.match(line)
        if m:
            name = m.group(1)
            desc = m.group(2).strip()

            if _is_noise(name):
                continue

            is_alias = bool(ALIAS_RE.search(desc))
            alias_target = None
            if is_alias:
                am = ALIAS_RE.search(desc)
                if am:
                    alias_target = am.group(1)

            results.append(ParsedCommand(
                name=name, description=desc, group=group,
                is_alias=is_alias, alias_target=alias_target,
            ))
    return results


def _try_csv(lines: list[str], group: Optional[str]) -> list[ParsedCommand]:
    """Try CSV flat list format parsing (npm style)."""
    results: list[ParsedCommand] = []
    for line in lines:
        m = CMD_CSV_RE.match(line)
        if m:
            names = [n.strip() for n in m.group(1).split(",") if n.strip()]
            for name in names:
                if not _is_noise(name):
                    results.append(ParsedCommand(name=name, group=group))
        else:
            # Also try inline comma-separated words without leading whitespace requirement
            stripped = line.strip()
            if stripped and "," in stripped and not stripped.startswith("-"):
                parts = [p.strip() for p in stripped.split(",") if p.strip()]
                if len(parts) >= 3 and all(re.match(r"^[\w-]+$", p) for p in parts):
                    for name in parts:
                        if not _is_noise(name):
                            results.append(ParsedCommand(name=name, group=group))
    return results


def _is_noise(name: str) -> bool:
    """Filter out non-command lines that regex might match."""
    noise = {
        "use", "see", "for", "or", "and", "the", "to", "a",
        "more", "information", "available", "specify", "note",
    }
    if name.lower() in noise:
        return True
    if name.startswith("--") or name.startswith("-"):
        return True
    if not re.match(r"^[\w][\w.-]*$", name):
        return True
    return False
