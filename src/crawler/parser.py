"""Main parser dispatcher: routes to manpage or section-based parser."""

from __future__ import annotations

import logging
import re
from dataclasses import replace

from .models import Command, EnvVar, Flag, ParseResult, PositionalArg
from .parsers.commands import parse_command_section
from .parsers.envvars import extract_envvars_from_text, parse_envvar_section
from .parsers.examples import parse_examples
from .parsers.flags import parse_flags_section
from .parsers.manpage import is_manpage, parse_manpage
from .parsers.sections import SectionType, segment_help_text
from .parsers.usage import extract_usage_from_text, extract_usage_line_options, parse_usage

logger = logging.getLogger("cli_crawler.parser")
EMBEDDED_HELP_HEADER_RE = re.compile(
    r"^\s*([a-zA-Z][\w.+-]*)\s+-\s+.*\bcommand(?:-|\s)?line\b",
    re.IGNORECASE,
)


def parse_help_output(
    text: str,
    cli_name: str,
    command_path: str,
    force_manpage: bool = False,
) -> ParseResult:
    """Main parse entry point. Dispatches to manpage or section-based parser."""
    text, embedded_warning = _truncate_embedded_help(text, cli_name)

    if not text.strip():
        return ParseResult(
            command=Command(path=command_path, name=command_path.split()[-1]),
            warnings=["Empty help output"],
        )

    if force_manpage or is_manpage(text):
        result = _parse_manpage(text, cli_name, command_path)
    else:
        result = _parse_sectioned(text, cli_name, command_path)

    if embedded_warning:
        result.warnings.append(embedded_warning)
    return result


def _parse_manpage(text: str, cli_name: str, command_path: str) -> ParseResult:
    """Parse man page format."""
    cmd, warnings = parse_manpage(text, cli_name, command_path)
    return ParseResult(
        command=cmd,
        subcommand_names=[],  # man pages don't list subcommands
        raw_help=text,
        warnings=warnings,
    )


def _parse_sectioned(text: str, cli_name: str, command_path: str) -> ParseResult:
    """Parse standard sectioned help output."""
    sections = segment_help_text(text)
    warnings: list[str] = []
    subcommand_names: list[str] = []
    subcommand_descriptions: dict[str, str] = {}

    # Initialize command
    cmd = Command(path=command_path, name=command_path.split()[-1])
    all_flags: list[Flag] = []
    global_flags: list[Flag] = []
    env_vars: list[EnvVar] = []

    # Try to extract usage from top of text (before sections)
    cmd.usage_pattern = extract_usage_from_text(text, cli_name)

    for section in sections:
        try:
            if section.type == SectionType.DESCRIPTION:
                if not cmd.description:
                    # First non-empty line that isn't a usage pattern
                    for line in section.content.splitlines():
                        stripped = line.strip()
                        if stripped and not stripped.lower().startswith("usage:"):
                            cleaned = _clean_description(stripped, command_path)
                            if cleaned:
                                cmd.description = cleaned
                                break

            elif section.type == SectionType.USAGE:
                usage = parse_usage(section.content)
                if usage:
                    cmd.usage_pattern = usage

            elif section.type == SectionType.COMMANDS:
                parsed_cmds = parse_command_section(section.content, group=section.header)
                for pc in parsed_cmds:
                    if pc.is_alias:
                        cmd.aliases.append(pc.name)
                    else:
                        subcommand_names.append(pc.name)
                        if pc.description:
                            cleaned = _clean_description(
                                pc.description,
                                f"{command_path} {pc.name}",
                                drop_circular_name=False,
                            )
                            if cleaned:
                                subcommand_descriptions[pc.name] = cleaned

            elif section.type == SectionType.FLAGS:
                flags = parse_flags_section(section.content)
                all_flags.extend(flags)

            elif section.type == SectionType.GLOBAL_FLAGS:
                flags = parse_flags_section(section.content)
                global_flags.extend(flags)

            elif section.type == SectionType.INHERITED_FLAGS:
                # Inherited flags = parent's global flags, mark as inherited
                flags = parse_flags_section(section.content)
                global_flags.extend(flags)

            elif section.type == SectionType.EXAMPLES:
                examples = parse_examples(section.content, cli_name)
                cmd.examples.extend(examples)

            elif section.type == SectionType.ENVIRONMENT:
                evars = parse_envvar_section(section.content)
                env_vars.extend(evars)

            elif section.type == SectionType.ARGUMENTS:
                args = _parse_arguments(section.content)
                cmd.positional_args.extend(args)

            elif section.type == SectionType.ALIASES:
                parsed_cmds = parse_command_section(section.content, group="aliases")
                for pc in parsed_cmds:
                    cmd.aliases.append(pc.name)

        except Exception as e:
            warnings.append(f"Error parsing section '{section.header}': {e}")
            logger.warning("Parse error in %s section '%s': %s", command_path, section.header, e)

    # If this is root level, global_flags go to CLIMap level;
    # local flags stay with command
    if not all_flags and not global_flags:
        inline_flags = extract_usage_line_options(text)
        if inline_flags:
            all_flags.extend(inline_flags)
            warnings.append(
                f"Recovered {len(inline_flags)} flags from sectionless usage/help lines."
            )

    all_flags = _deduplicate_flags(all_flags)
    global_flags = _deduplicate_flags(global_flags)
    if global_flags:
        # At root level, we return global flags as the command's flags
        # The pipeline will separate them into CLIMap.global_flags
        cmd.flags = _deduplicate_flags(global_flags + all_flags)
    else:
        cmd.flags = all_flags

    # Extract env vars from flag descriptions too
    inline_envvars = extract_envvars_from_text(text)
    env_vars.extend(inline_envvars)
    cmd.env_vars = _deduplicate_envvars(env_vars)
    cmd.description = _clean_description(cmd.description, command_path)

    # Compute confidence
    cmd.confidence = _compute_confidence(cmd, text)

    return ParseResult(
        command=cmd,
        subcommand_names=subcommand_names,
        subcommand_descriptions=subcommand_descriptions,
        raw_help=text,
        warnings=warnings,
    )


def _compute_confidence(cmd: Command, raw_text: str) -> float:
    """Compute overall confidence based on parse quality."""
    score = 0.5

    if cmd.description:
        score += 0.1
    if cmd.usage_pattern:
        score += 0.1
    if cmd.flags:
        score += 0.15
    if cmd.examples:
        score += 0.05
    if len(raw_text) > 100:
        score += 0.05

    return min(score, 1.0)


def _parse_arguments(content: str) -> list[PositionalArg]:
    """Parse rich-click style positional arguments section.

    Format: name  [METAVAR]  description
    Brackets around metavar indicate optional argument.
    """
    import re

    arg_re = re.compile(
        r"^\s*(\w[\w-]*)"  # arg name
        r"\s{2,}"  # gap
        r"(?:\[(\w+)\]\s+)?"  # optional [METAVAR]
        r"(.+)$"  # description
    )
    results: list[PositionalArg] = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        m = arg_re.match(stripped)
        if m:
            name = m.group(1)
            metavar = m.group(2)
            desc = m.group(3).strip()
            # [METAVAR] indicates optional, no brackets = required
            required = metavar is None
            results.append(
                PositionalArg(
                    name=name,
                    required=required,
                    description=desc,
                )
            )
    return results


def _deduplicate_envvars(env_vars: list[EnvVar]) -> list[EnvVar]:
    """Remove duplicate env vars, keeping first occurrence."""
    seen: set[str] = set()
    result: list[EnvVar] = []
    for ev in env_vars:
        if ev.name not in seen:
            seen.add(ev.name)
            result.append(ev)
    return result


def _truncate_embedded_help(text: str, cli_name: str) -> tuple[str, str | None]:
    """Trim foreign embedded tool help blocks from wrapper CLIs (e.g., yq embedding jq)."""
    lines = text.splitlines()
    if not lines:
        return text, None

    primary_names: set[str] = {cli_name.lower()}
    usage_cmd = _extract_usage_command(lines)
    if usage_cmd:
        primary_names.add(usage_cmd)

    for idx, line in enumerate(lines):
        m = EMBEDDED_HELP_HEADER_RE.match(line)
        if not m:
            continue
        foreign_name = m.group(1).lower()
        if foreign_name in primary_names:
            continue

        kept = "\n".join(lines[:idx]).rstrip()
        if kept:
            warning = (
                "Embedded help boundary detected for "
                f"'{foreign_name}' at line {idx + 1}; foreign block ignored."
            )
            return kept, warning

    return text, None


def _extract_usage_command(lines: list[str]) -> str | None:
    """Extract root command token from first usage line."""
    usage_re = re.compile(r"^\s*(?:usage)\s*:?\s*(\S+)", re.IGNORECASE)
    for line in lines:
        m = usage_re.match(line)
        if not m:
            continue
        token = m.group(1).strip().lower()
        if token:
            return token
    return None


def _deduplicate_flags(flags: list[Flag]) -> list[Flag]:
    """Deduplicate flags by long/name with deterministic precedence."""
    deduped: list[Flag] = []
    index_by_key: dict[str, int] = {}

    for flag in flags:
        key = (flag.long_name or flag.name or "").strip()
        if not key:
            continue

        if key not in index_by_key:
            index_by_key[key] = len(deduped)
            deduped.append(flag)
            continue

        idx = index_by_key[key]
        merged = _merge_flag_metadata(deduped[idx], flag)
        if _flag_rank(flag) > _flag_rank(deduped[idx]):
            merged = _merge_flag_metadata(flag, deduped[idx])
        deduped[idx] = merged

    return deduped


def _merge_flag_metadata(primary: Flag, secondary: Flag) -> Flag:
    """Merge flag metadata, preferring primary while filling missing fields."""
    return replace(
        primary,
        long_name=primary.long_name or secondary.long_name,
        short_name=primary.short_name or secondary.short_name,
        default=primary.default if primary.default is not None else secondary.default,
        choices=primary.choices or secondary.choices,
        description=primary.description or secondary.description,
        confidence=max(primary.confidence, secondary.confidence),
    )


def _flag_rank(flag: Flag) -> tuple[int, int, int, float]:
    """Rank flag richness for deterministic replacement preference."""
    return (
        1 if flag.short_name else 0,
        1 if flag.default is not None else 0,
        len(flag.description or ""),
        flag.confidence,
    )


_DESC_NOISE_PATTERNS = [
    re.compile(r"^\s*(?:fatal|error)\s*:", re.IGNORECASE),
    re.compile(r"\baccepts?\s+\d+\s+arg(?:ument)?s?\b", re.IGNORECASE),
    re.compile(r"\balready initialized\b", re.IGNORECASE),
    re.compile(r"^\s*\[(?:warn|warning|info|error)\]\s*", re.IGNORECASE),
]


def _clean_description(
    description: str,
    command_path: str,
    *,
    drop_circular_name: bool = True,
) -> str:
    """Filter noisy runtime/status messages from descriptions."""
    desc = (description or "").strip()
    if not desc:
        return ""

    normalized = re.sub(r"\s+", " ", desc).strip().lower()
    leaf = command_path.split()[-1].strip().lower()
    full = command_path.strip().lower()

    if normalized.startswith("usage:"):
        return ""
    if drop_circular_name and normalized in {leaf, full}:
        return ""

    for pattern in _DESC_NOISE_PATTERNS:
        if pattern.search(desc):
            return ""

    return desc
