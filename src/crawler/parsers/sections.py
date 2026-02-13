"""Section header detection and text segmentation.

Handles 7 format families: ALL CAPS, ALL CAPS+colon, Title Case+colon,
Grouped Title, Git prose headings, man page sections, and rich-click boxes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum


class SectionType(Enum):
    USAGE = "usage"
    DESCRIPTION = "description"
    COMMANDS = "commands"
    FLAGS = "flags"
    GLOBAL_FLAGS = "global_flags"
    INHERITED_FLAGS = "inherited_flags"
    ARGUMENTS = "arguments"
    EXAMPLES = "examples"
    ENVIRONMENT = "environment"
    ALIASES = "aliases"
    HELP_TOPICS = "help_topics"
    SEE_ALSO = "see_also"
    UNKNOWN = "unknown"


@dataclass
class Section:
    type: SectionType
    header: str
    content: str
    indent_level: int


# Patterns ordered by specificity (first match wins within priority group).
# Tuples of (compiled_regex, SectionType).
_SECTION_PATTERNS: list[tuple[re.Pattern, SectionType]] = []


def _p(pattern: str, stype: SectionType) -> None:
    _SECTION_PATTERNS.append((re.compile(pattern, re.IGNORECASE), stype))


# --- ALL CAPS / Title Case section headers ---

# Usage / Synopsis
_p(r"^\s*(?:USAGE|usage|Usage|SYNOPSIS|Synopsis)\s*:?\s*$", SectionType.USAGE)

# Description
_p(r"^\s*(?:DESCRIPTION|Description|ABOUT|About)\s*:?\s*$", SectionType.DESCRIPTION)

# Global flags (must match before generic flags)
_p(
    r"^\s*(?:GLOBAL\s+FLAGS|GLOBAL\s+OPTIONS|Global\s+[Ff]lags|Global\s+[Oo]ptions)\s*:?\s*$",
    SectionType.GLOBAL_FLAGS,
)

# Inherited flags (gh subcommands)
_p(r"^\s*(?:INHERITED\s+FLAGS|Inherited\s+[Ff]lags)\s*:?\s*$", SectionType.INHERITED_FLAGS)

# Command sections (many variants)
_p(
    r"^\s*(?:"
    r"CORE\s+COMMANDS|PRIMARY\s+COMMANDS|ADDITIONAL\s+COMMANDS|"
    r"ADVANCED\s+COMMANDS|UTILITY\s+COMMANDS|ANALYSIS\s+COMMANDS|"
    r"MANAGEMENT\s+COMMANDS|ALIAS\s+COMMANDS|GITHUB\s+ACTIONS\s+COMMANDS|"
    r"GENERAL\s+COMMANDS|TARGETED\s+COMMANDS|"
    r"Common\s+Commands|Management\s+Commands|Swarm\s+Commands|"
    r"COMMANDS|Commands|SUBCOMMANDS|Subcommands|"
    r"Available\s+[Cc]ommands|All\s+[Cc]ommands"
    r")\s*:?\s*$",
    SectionType.COMMANDS,
)

# Flags / Options (generic, after global/inherited)
_p(
    r"^\s*(?:"
    r"FLAGS|OPTIONS|GENERAL\s+OPTIONS|General\s+Options|Options|Flags|"
    r"[A-Z][a-z]+\s+[Oo]ptions"  # "Cache options", "Python options"
    r")\s*:?\s*$",
    SectionType.FLAGS,
)

# Arguments
_p(r"^\s*(?:ARGUMENTS|Arguments)\s*:?\s*$", SectionType.ARGUMENTS)

# Examples
_p(r"^\s*(?:EXAMPLES|Examples)\s*:?\s*$", SectionType.EXAMPLES)

# Environment
_p(r"^\s*(?:ENVIRONMENT|Environment|ENVIRONMENT\s+VARIABLES?)\s*:?\s*$", SectionType.ENVIRONMENT)

# Aliases
_p(r"^\s*(?:ALIASES|Aliases)\s*:?\s*$", SectionType.ALIASES)

# Help topics
_p(r"^\s*(?:HELP\s+TOPICS|Help\s+Topics)\s*:?\s*$", SectionType.HELP_TOPICS)

# See also / Learn more
_p(r"^\s*(?:SEE\s+ALSO|See\s+[Aa]lso|LEARN\s+MORE|Learn\s+[Mm]ore)\s*:?\s*$", SectionType.SEE_ALSO)

# Git prose-style category headings (these are NOT added to _SECTION_PATTERNS
# because they require indentation check — handled separately in detect_section_type)
_GIT_PROSE_PATTERNS = [
    re.compile(r"^[a-z].*\(see also:.*\)\s*$"),
    re.compile(r"^[a-z][a-z, ]+your common history\s*$"),
]

# Box-drawing format (rich-click)
_BOX_HEADER_RE = re.compile(r"^\s*\+-\s*(.+?)\s*-+\+\s*$")
_BOX_BORDER_RE = re.compile(r"^\s*\+[-─]+\+\s*$")


def detect_section_type(line: str) -> SectionType | None:
    """Match a line against section patterns. Returns None if no match."""
    stripped = line.strip()
    if not stripped:
        return None

    # Standard patterns (work on stripped text)
    for pattern, stype in _SECTION_PATTERNS:
        if pattern.match(stripped):
            return stype

    # Git prose patterns: ONLY match at column 0 (no indentation)
    indent = len(line) - len(line.lstrip())
    if indent == 0:
        for pattern in _GIT_PROSE_PATTERNS:
            if pattern.match(stripped):
                return SectionType.COMMANDS

    return None


def segment_help_text(text: str) -> list[Section]:
    """Split help text into typed sections."""
    # Preprocess box-drawing format (rich-click) to standard format
    text = _strip_rich_boxes(text)
    lines = text.splitlines()
    sections: list[Section] = []
    current_header = ""
    current_type = SectionType.UNKNOWN
    current_lines: list[str] = []
    current_indent = 0
    preamble_lines: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Try to detect section header
        stype = detect_section_type(line)

        # For git-style lowercase prose, only match if followed by indented commands
        if stype == SectionType.COMMANDS and _is_git_prose(stripped):
            if not _followed_by_indented_commands(lines, i):
                stype = None

        if stype is not None:
            # Save previous section
            if current_lines or current_header:
                content = "\n".join(current_lines)
                sections.append(
                    Section(
                        type=current_type,
                        header=current_header,
                        content=content,
                        indent_level=current_indent,
                    )
                )
            elif preamble_lines:
                # Save preamble as description
                content = "\n".join(preamble_lines)
                sections.append(
                    Section(
                        type=SectionType.DESCRIPTION,
                        header="",
                        content=content,
                        indent_level=0,
                    )
                )
                preamble_lines = []

            current_header = stripped
            current_type = stype
            current_indent = len(line) - len(line.lstrip())
            current_lines = []
        else:
            if not sections and not current_header:
                # Before first section header — treat as preamble/usage
                if stripped:
                    preamble_lines.append(line)
            else:
                current_lines.append(line)
        i += 1

    # Save last section
    if current_lines or current_header:
        content = "\n".join(current_lines)
        sections.append(
            Section(
                type=current_type,
                header=current_header,
                content=content,
                indent_level=current_indent,
            )
        )
    elif preamble_lines and not sections:
        content = "\n".join(preamble_lines)
        sections.append(
            Section(
                type=SectionType.DESCRIPTION,
                header="",
                content=content,
                indent_level=0,
            )
        )

    return sections


def _is_git_prose(line: str) -> bool:
    """Check if a line looks like a git prose category heading."""
    return bool(line) and line[0].islower() and not line.startswith("-")


def _followed_by_indented_commands(lines: list[str], idx: int) -> bool:
    """Check if lines after idx contain indented command-like entries."""
    for j in range(idx + 1, min(idx + 5, len(lines))):
        stripped = lines[j].strip()
        if not stripped:
            continue
        indent = len(lines[j]) - len(lines[j].lstrip())
        if indent >= 2 and re.match(r"^\S+\s{2,}", stripped):
            return True
    return False


def _strip_rich_boxes(text: str) -> str:
    """Preprocess rich-click box-drawing format to standard format.

    Transforms:
        +- Commands ---+  →  Commands:
        | run    desc   |  →    run    desc
        +---------------+  →  (removed)

    Also merges multi-line continuations within boxes (lines with
    heavy indentation that continue the previous line's description).
    """
    if "+-" not in text:
        return text

    lines = text.splitlines()
    result: list[str] = []
    has_boxes = False

    for line in lines:
        stripped = line.strip()

        # Box header: +- Options ---+
        m = _BOX_HEADER_RE.match(stripped)
        if m:
            header = m.group(1).strip().rstrip(":")
            result.append(f"{header}:")
            has_boxes = True
            continue

        # Box border (closing): +---+
        if _BOX_BORDER_RE.match(stripped):
            has_boxes = True
            continue

        # Box content: | content |
        if stripped.startswith("|") and stripped.endswith("|") and len(stripped) > 2:
            inner = stripped[1:-1]
            inner_stripped = inner.strip()
            if inner_stripped:
                inner_indent = len(inner) - len(inner.lstrip())
                # Continuation: heavily indented, doesn't start with flag/arg
                if inner_indent > 10 and not inner_stripped.startswith("-") and result:
                    prev = result[-1]
                    if prev.strip():
                        result[-1] = prev.rstrip() + " " + inner_stripped
                        has_boxes = True
                        continue
                result.append(f"  {inner.lstrip()}")
            else:
                result.append("")
            has_boxes = True
            continue

        # Regular line (outside boxes)
        result.append(line)

    if has_boxes:
        return "\n".join(result)
    return text
