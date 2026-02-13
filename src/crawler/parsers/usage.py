"""Usage line extraction from help output."""

from __future__ import annotations

import re

# Usage line patterns
USAGE_PREFIX_RE = re.compile(
    r"^\s*(?:usage|Usage|USAGE)\s*:?\s*(.+)$",
    re.IGNORECASE,
)

USAGE_CONTINUATION_RE = re.compile(r"^\s{4,}\S")


def parse_usage(content: str) -> str:
    """Extract usage pattern from a USAGE section content."""
    lines = content.splitlines()
    parts: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if parts:
                break
            continue

        if not parts:
            # First non-empty line is the usage pattern
            parts.append(stripped)
        elif USAGE_CONTINUATION_RE.match(line):
            # Continuation line (indented)
            parts.append(stripped)
        else:
            break

    return " ".join(parts) if parts else ""


def extract_usage_from_text(text: str, cli_name: str) -> str:
    """Find usage line anywhere in text (for CLIs that put it at top)."""
    for line in text.splitlines():
        m = USAGE_PREFIX_RE.match(line)
        if m:
            usage = m.group(1).strip()
            if usage:
                return usage
    return ""
