"""Flag/option parsing handling 6+ format families.

Formats handled:
1. Standard:    -m, --message <msg>    commit message
2. Long only:       --config string    Location of...
3. Bool:        -D, --debug            Enable debug mode
4. Negatable:   --[no-]verify          Run hooks
5. Multi-line:  --quiet...\n                   Use quiet output (clap/uv)
6. Bracket:     [-S|--save|--no-save]  (npm)
"""

from __future__ import annotations

import re
from typing import Optional

from ..models import Flag

# --- Core flag regex patterns ---

# Standard flag: -m, --message <msg>    description
# Also handles: -m, --message=<msg>     description
FLAG_STANDARD_RE = re.compile(
    r"^\s*"
    r"(?:(-[a-zA-Z0-9]),?\s+)?"          # optional short: -m,
    r"(--[\w][\w-]*)"                     # long: --message
    r"(?:"
    r"[\s=]"                              # separator: space or =
    r"[<\[]?([^>\]\s,]+)[>\]]?"           # value: <msg> or [msg] or msg
    r")?"
    r"\s{2,}"                             # gap (at least 2 spaces)
    r"(.+)$"                              # description
)

# Go-style with type name: --config string    Location of...
# Also handles rich-click uppercase types: --port INTEGER, --host TEXT
FLAG_GO_TYPE_RE = re.compile(
    r"^\s*"
    r"(?:(-[a-zA-Z0-9]),?\s+)?"
    r"(--[\w][\w-]*)"
    r"\s+(string|int|uint|uint16|float|bool|list|map|duration|decimal"
    r"|STRING|INT|INTEGER|FLOAT|BOOL|BOOLEAN|TEXT|PATH|FILE|FILENAME"
    r"|DIRECTORY|DIR|URL|NUMBER|COUNT|LEVEL|UUID|CHOICE)\s+"
    r"(.+)$"
)

# Negatable flag: --[no-]verify
FLAG_NEGATABLE_RE = re.compile(
    r"^\s*"
    r"(?:(-[a-zA-Z0-9]),?\s+)?"
    r"(--\[no-\][\w][\w-]*)"
    r"(?:\s+<([^>]+)>)?"
    r"(?:\s{2,}(.+))?$"
)

# Short-only flag: -v    verbose
FLAG_SHORT_ONLY_RE = re.compile(
    r"^\s*(-[a-zA-Z0-9])\s{2,}(.+)$"
)

# Flag line with no description (clap multi-line): --quiet...
FLAG_NODESCRIP_RE = re.compile(
    r"^\s*"
    r"(?:(-[a-zA-Z0-9]),?\s+)?"
    r"(--[\w][\w-]*)"
    r"(\.{3})?"                           # variadic marker
    r"(?:\s+<([^>]+)>)?"
    r"\s*$"
)

# --- Extraction patterns for metadata within descriptions ---

CHOICES_BRACKET_RE = re.compile(r"\[possible values?:\s*([^\]]+)\]", re.IGNORECASE)
CHOICES_PIPE_RE = re.compile(r"\b([a-z][\w-]*(?:\|[a-z][\w-]*)+)\b")
CHOICES_PAREN_RE = re.compile(r'\("([^"]+)"(?:,\s*"([^"]+)")*\)')
DEFAULT_RE = re.compile(r"\(default[:\s]+\"?([^\")\s]+)\"?\)", re.IGNORECASE)
DEFAULT_BRACKET_RE = re.compile(r"\[default:\s*([^\]]+)\]", re.IGNORECASE)
ENV_VAR_RE = re.compile(r"\[env:\s*([A-Z_][A-Z0-9_]*)=?\]")


# npm bracket format: [-S|--save|--no-save|--save-prod]
FLAG_BRACKET_RE = re.compile(
    r"\["
    r"(-[a-zA-Z0-9]\|)?"                   # optional short: -S|
    r"(--[\w-]+(?:\|--[\w-]+)*)"            # long flags: --save|--no-save
    r"(?:\s+<([^>]+(?:\|[^>]+)*)>)?"        # optional value: <hoisted|nested>
    r"\]"
)

# Rich-click reversed format: --version  -v   Print the current CLI version.
# (long flag first, then optional short, then description)
FLAG_RICHCLICK_RE = re.compile(
    r"^\s*"
    r"(--[\w][\w-]*)"                       # long first: --version
    r"\s+"
    r"(-[a-zA-Z0-9])"                       # short second: -v
    r"\s{2,}"                               # gap to description
    r"(.+)$"                                # description
)

# Rich-click negatable pair: --pip  --no-pip  Pip install the template(s)
FLAG_RICHCLICK_NEGATABLE_RE = re.compile(
    r"^\s*"
    r"(--[\w][\w-]*)"                       # first flag: --pip
    r"\s{2,}"
    r"(--[\w][\w-]*)"                       # second flag: --no-pip
    r"\s{2,}"                               # gap to description
    r"(.+)$"                                # description
)


def parse_flags_section(content: str) -> list[Flag]:
    """Parse a flags/options section content into Flag objects."""
    lines = _merge_multiline_flags(content.splitlines())
    flags: list[Flag] = []

    for line in lines:
        # Try bracket format first (npm style) — can have multiple brackets per line
        bracket_flags = _try_parse_brackets(line)
        if bracket_flags:
            flags.extend(bracket_flags)
            continue

        flag = _try_parse_flag(line)
        if flag:
            flags.append(flag)

    return flags


def _try_parse_brackets(line: str) -> list[Flag]:
    """Parse npm-style bracket flags: [-S|--save|--no-save] [--flag <val>]."""
    results: list[Flag] = []
    for m in FLAG_BRACKET_RE.finditer(line):
        short_part = m.group(1)
        long_part = m.group(2)
        value = m.group(3)

        short = short_part.rstrip("|") if short_part else None
        long_flags = [f for f in long_part.split("|") if f.startswith("--")]

        # Value with pipes is choices, not a single value
        choices = None
        if value and "|" in value:
            choices = value.split("|")

        is_bool = value is None and choices is None

        for lf in long_flags:
            results.append(Flag(
                name=lf,
                short=short if lf == long_flags[0] else None,
                type="bool" if is_bool else "string",
                choices=choices,
                confidence=0.80,
            ))
            short = None  # short only applies to first flag

    return results


def _try_parse_flag(line: str) -> Optional[Flag]:
    """Try all flag patterns against a line. Returns Flag or None."""
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None

    # Try negatable first (most specific)
    m = FLAG_NEGATABLE_RE.match(line)
    if m:
        return _build_flag(
            short=m.group(1), long=m.group(2),
            value=m.group(3), description=m.group(4) or "",
            confidence=0.85,
        )

    # Try rich-click negatable pair: --pip  --no-pip  description
    m = FLAG_RICHCLICK_NEGATABLE_RE.match(line)
    if m:
        flag1, desc = m.group(1), m.group(3)
        # Use the first flag as primary, note the pair in description
        return Flag(
            name=flag1, type="bool",
            description=desc.strip(),
            confidence=0.85,
        )

    # Try Go-type pattern (includes rich-click uppercase: INTEGER, TEXT)
    m = FLAG_GO_TYPE_RE.match(line)
    if m:
        go_type = m.group(3)
        is_bool = go_type.lower() in ("bool", "boolean")
        return _build_flag(
            short=m.group(1), long=m.group(2),
            value=None if is_bool else go_type,
            description=m.group(4),
            confidence=0.90,
            force_bool=is_bool,
        )

    # Try rich-click reversed: --version  -v  description
    m = FLAG_RICHCLICK_RE.match(line)
    if m:
        return _build_flag(
            short=m.group(2), long=m.group(1),
            value=None, description=m.group(3),
            confidence=0.90,
        )

    # Try standard pattern
    m = FLAG_STANDARD_RE.match(line)
    if m:
        return _build_flag(
            short=m.group(1), long=m.group(2),
            value=m.group(3), description=m.group(4),
            confidence=0.90 if m.group(1) else 0.85,
        )

    # Try short-only
    m = FLAG_SHORT_ONLY_RE.match(line)
    if m:
        return Flag(
            name=m.group(1), short=m.group(1),
            type="bool", description=m.group(2).strip(),
            confidence=0.70,
        )

    # Try no-description line (will be merged with next)
    m = FLAG_NODESCRIP_RE.match(line)
    if m:
        return _build_flag(
            short=m.group(1), long=m.group(2),
            value=m.group(4), description="",
            confidence=0.60,
        )

    return None


def _build_flag(
    short: Optional[str],
    long: str,
    value: Optional[str],
    description: str,
    confidence: float,
    force_bool: bool = False,
) -> Flag:
    """Build a Flag with type inference and metadata extraction."""
    # Type inference (v1: bool vs string)
    if force_bool:
        flag_type = "bool"
    elif value is None and not _description_implies_value(description):
        flag_type = "bool"
    else:
        flag_type = "string"

    # Extract metadata from description
    default = _extract_default(description)
    choices = _extract_choices(description)

    return Flag(
        name=long,
        short=short,
        type=flag_type,
        required=False,
        default=default,
        choices=choices,
        description=description.strip(),
        confidence=confidence,
    )


def _description_implies_value(desc: str) -> bool:
    """Check if description implies the flag takes a value."""
    value_indicators = ["specify", "set to", "path to", "name of", "number of",
                        "file", "directory", "url", "string", "value"]
    desc_lower = desc.lower()
    return any(ind in desc_lower for ind in value_indicators)


def _extract_default(description: str) -> Optional[str]:
    """Extract default value from description."""
    m = DEFAULT_RE.search(description)
    if m:
        return m.group(1)
    m = DEFAULT_BRACKET_RE.search(description)
    if m:
        return m.group(1).strip()
    return None


def _extract_choices(description: str) -> Optional[list[str]]:
    """Extract choices from description."""
    # [possible values: auto, always, never]
    m = CHOICES_BRACKET_RE.search(description)
    if m:
        return [c.strip() for c in m.group(1).split(",")]

    # json|yaml|text (only if it looks like a choice list in context)
    m = CHOICES_PIPE_RE.search(description)
    if m:
        parts = m.group(1).split("|")
        if 2 <= len(parts) <= 10:
            return parts

    return None


def extract_env_vars_from_flags(flags: list[Flag]) -> list[str]:
    """Extract env var names mentioned in flag descriptions."""
    env_vars = []
    for flag in flags:
        for m in ENV_VAR_RE.finditer(flag.description):
            env_vars.append(m.group(1))
    return env_vars


def _merge_multiline_flags(lines: list[str]) -> list[str]:
    """Pre-process clap-style multi-line flags into single logical lines.

    Pattern: flag line with no description, followed by heavily indented description.
    Example (uv/clap):
        -q, --quiet...
                Use quiet output
    Becomes:
        -q, --quiet...    Use quiet output
    """
    merged: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if this is a flag line with no description
        if stripped and (stripped.startswith("-") or stripped.startswith("--")):
            m = FLAG_NODESCRIP_RE.match(line)
            if m:
                # Look ahead for description on next line(s)
                desc_parts: list[str] = []
                j = i + 1
                while j < len(lines):
                    next_line = lines[j]
                    next_stripped = next_line.strip()
                    if not next_stripped:
                        break
                    next_indent = len(next_line) - len(next_line.lstrip())
                    line_indent = len(line) - len(line.lstrip())
                    # Description must be indented more than the flag
                    if next_indent > line_indent + 2 and not next_stripped.startswith("-"):
                        desc_parts.append(next_stripped)
                        j += 1
                    else:
                        break
                if desc_parts:
                    merged.append(f"{line}    {' '.join(desc_parts)}")
                    i = j
                    continue

        merged.append(line)
        i += 1

    return merged
