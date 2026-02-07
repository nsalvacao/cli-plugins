"""Example block extraction from help output."""

from __future__ import annotations

import re

# Lines starting with $ (with optional leading whitespace)
EXAMPLE_DOLLAR_RE = re.compile(r"^\s*\$\s+(.+)$")

# Lines starting with CLI name (common in examples without $)
EXAMPLE_COMMAND_RE = re.compile(r"^\s{2,}(\S+\s+\S+.*)$")


def parse_examples(content: str, cli_name: str = "") -> list[str]:
    """Extract example commands from an examples section."""
    lines = content.splitlines()
    examples: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # $ prefix style
        m = EXAMPLE_DOLLAR_RE.match(line)
        if m:
            examples.append(m.group(1).strip())
            continue

        # Indented command line (must start with a known command or look like one)
        if stripped and not stripped.startswith("#") and not stripped.startswith("//"):
            indent = len(line) - len(line.lstrip())
            if indent >= 2:
                # Looks like a command: starts with word followed by args
                if re.match(r"^[\w./-]+\s", stripped) or (cli_name and stripped.startswith(cli_name)):
                    examples.append(stripped)

    return examples
