"""Man page (roff format) parser for git-style help output.

Git subcommands output man pages via --help. These have a completely different
structure from standard help: NAME, SYNOPSIS, DESCRIPTION, OPTIONS sections
with specific indentation patterns.
"""

from __future__ import annotations

import re

from ..models import Command, EnvVar, Flag

# Man page section header: ALL CAPS at column 0
MANPAGE_SECTION_RE = re.compile(r"^([A-Z][A-Z ]+?)\s*$")

# Man page flag entry (in OPTIONS section):
#        -a, --all
#            Description follows, indented further
MANPAGE_FLAG_RE = re.compile(
    r"^\s{4,8}"
    r"(?:(-[a-zA-Z0-9]),?\s+)?"  # optional short
    r"(--[\w][\w-]*)"  # long flag
    r"(?:[=\s]<([^>]+)>)?"  # optional value
    r"(?:,\s*(--[\w][\w-]*))?"  # optional second long flag
    r"\s*$"
)

# Man page short-only flag
MANPAGE_SHORT_RE = re.compile(r"^\s{4,8}(-[a-zA-Z0-9])\s*$")

# Synopsis continuation
SYNOPSIS_CMD_RE = re.compile(r"^\s+(\S.+)$")


def is_manpage(text: str) -> bool:
    """Detect if text is a man page format."""
    lines = text.splitlines()
    if not lines:
        return False

    # Man page header: "GIT-COMMIT(1)    Git Manual    GIT-COMMIT(1)"
    first_line = lines[0].strip()
    if re.match(r"^[A-Z][A-Z0-9_-]+\(\d+\)", first_line):
        return True

    # Check for NAME + SYNOPSIS sections
    has_name = False
    has_synopsis = False
    for line in lines[:30]:
        stripped = line.strip()
        if stripped == "NAME":
            has_name = True
        elif stripped == "SYNOPSIS":
            has_synopsis = True
    return has_name and has_synopsis


def parse_manpage(text: str, cli_name: str, command_path: str) -> tuple[Command, list[str]]:
    """Parse a man page format help output.

    Returns (Command, list_of_warning_strings).
    """
    sections = _segment_manpage(text)
    warnings: list[str] = []

    # Extract description from NAME section
    description = ""
    name_content = sections.get("NAME", "")
    if name_content:
        # Format: "git-commit - Record changes to the repository"
        m = re.search(r"-\s+(.+)", name_content)
        if m:
            description = m.group(1).strip()

    # Extract usage from SYNOPSIS
    usage = ""
    synopsis = sections.get("SYNOPSIS", "")
    if synopsis:
        usage = _parse_synopsis(synopsis)

    # Extract flags from OPTIONS
    flags: list[Flag] = []
    options_content = sections.get("OPTIONS", "")
    if options_content:
        flags = _parse_manpage_options(options_content)

    # Extract env vars from ENVIRONMENT
    env_vars: list[EnvVar] = []
    env_content = sections.get("ENVIRONMENT", "")
    if env_content:
        env_vars = _parse_manpage_envvars(env_content)

    # Extract examples from EXAMPLES
    examples: list[str] = []
    examples_content = sections.get("EXAMPLES", "")
    if examples_content:
        examples = _parse_manpage_examples(examples_content)

    cmd = Command(
        path=command_path,
        description=description,
        usage_pattern=usage,
        flags=flags,
        env_vars=env_vars,
        examples=examples,
        confidence=0.85 if flags else 0.60,
    )

    return cmd, warnings


def _segment_manpage(text: str) -> dict[str, str]:
    """Split man page into sections by ALL CAPS headers at column 0."""
    sections: dict[str, str] = {}
    current_header = ""
    current_lines: list[str] = []
    lines = text.splitlines()

    # Skip the first line if it's the man page title bar
    start = 0
    if lines and re.match(r"^[A-Z][A-Z0-9_-]+\(\d+\)", lines[0].strip()):
        start = 1

    for i in range(start, len(lines)):
        line = lines[i]
        m = MANPAGE_SECTION_RE.match(line)
        if m and not line.startswith(" "):
            # Save previous section
            if current_header:
                sections[current_header] = "\n".join(current_lines)
            current_header = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)

    # Save last section
    if current_header:
        sections[current_header] = "\n".join(current_lines)

    return sections


def _parse_synopsis(content: str) -> str:
    """Extract usage pattern from SYNOPSIS section."""
    lines = content.splitlines()
    parts: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if parts:
                break
            continue
        # Remove man page bold/italic markers if any
        cleaned = re.sub(r"\*(.+?)\*", r"\1", stripped)
        parts.append(cleaned)

    return " ".join(parts)


def _parse_manpage_options(content: str) -> list[Flag]:
    """Parse OPTIONS section of a man page.

    Man page format:
           -a, --all
               Stage all modified and deleted files.

           --amend
               Replace the tip of the current branch.
    """
    flags: list[Flag] = []
    lines = content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i]

        # Try to match a flag line
        flag_match = MANPAGE_FLAG_RE.match(line)
        short_match = MANPAGE_SHORT_RE.match(line) if not flag_match else None

        if flag_match or short_match:
            if flag_match:
                short = flag_match.group(1)
                long_flag = flag_match.group(2)
                value = flag_match.group(3)
            else:
                short = short_match.group(1)  # type: ignore
                long_flag = None
                value = None

            # Collect description from following indented lines
            desc_parts: list[str] = []
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                next_stripped = next_line.strip()
                if not next_stripped:
                    # Blank line might separate flag from next entry
                    # Check if next non-empty line is a new flag
                    k = j + 1
                    while k < len(lines) and not lines[k].strip():
                        k += 1
                    if k < len(lines):
                        next_real = lines[k]
                        if MANPAGE_FLAG_RE.match(next_real) or MANPAGE_SHORT_RE.match(next_real):
                            break
                        elif next_real.strip() and len(next_real) - len(next_real.lstrip()) >= 8:
                            # Still part of description (paragraph break)
                            desc_parts.append("")
                            j += 1
                            continue
                    break
                indent = len(next_line) - len(next_line.lstrip())
                if indent >= 8:  # description indent in man pages
                    desc_parts.append(next_stripped)
                else:
                    break
                j += 1

            description = " ".join(p for p in desc_parts if p)

            if long_flag:
                is_bool = value is None and not _desc_implies_value(description)
                flags.append(
                    Flag(
                        name=long_flag,
                        short=short,
                        type="bool" if is_bool else "string",
                        description=description,
                        confidence=0.85,
                    )
                )
            elif short:
                flags.append(
                    Flag(
                        name=short,
                        short=short,
                        type="bool",
                        description=description,
                        confidence=0.70,
                    )
                )

            i = j
        else:
            i += 1

    return flags


def _desc_implies_value(desc: str) -> bool:
    """Check if description implies the flag takes a value."""
    indicators = [
        "specify",
        "set to",
        "path",
        "file",
        "directory",
        "name",
        "number",
        "format",
        "mode",
        "strategy",
    ]
    desc_lower = desc.lower()
    return any(ind in desc_lower for ind in indicators)


def _parse_manpage_envvars(content: str) -> list[EnvVar]:
    """Parse ENVIRONMENT section of man page."""
    env_vars: list[EnvVar] = []
    lines = content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip()) if stripped else 0

        # Env var entries are at ~7 space indent, descriptions at ~11
        if stripped and indent <= 8 and re.match(r"^[A-Z_][A-Z0-9_]+$", stripped):
            # Collect description
            desc_parts: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].strip():
                if len(lines[j]) - len(lines[j].lstrip()) > indent:
                    desc_parts.append(lines[j].strip())
                else:
                    break
                j += 1
            env_vars.append(EnvVar(name=stripped, description=" ".join(desc_parts)))
            i = j
        else:
            i += 1

    return env_vars


def _parse_manpage_examples(content: str) -> list[str]:
    """Parse EXAMPLES section of man page."""
    examples: list[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith(".") and not stripped.startswith("'"):
            indent = len(line) - len(line.lstrip())
            if indent >= 8 and re.match(r"^[\w$./]", stripped):
                # Remove leading $ if present
                if stripped.startswith("$ "):
                    stripped = stripped[2:]
                examples.append(stripped)
    return examples
