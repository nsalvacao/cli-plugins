"""Main parser dispatcher: routes to manpage or section-based parser."""

from __future__ import annotations

import logging

from .models import Command, EnvVar, Flag, ParseResult, PositionalArg
from .parsers.commands import parse_command_section
from .parsers.envvars import extract_envvars_from_text, parse_envvar_section
from .parsers.examples import parse_examples
from .parsers.flags import parse_flags_section
from .parsers.manpage import is_manpage, parse_manpage
from .parsers.sections import SectionType, segment_help_text
from .parsers.usage import extract_usage_from_text, parse_usage

logger = logging.getLogger("cli_crawler.parser")


def parse_help_output(
    text: str,
    cli_name: str,
    command_path: str,
    force_manpage: bool = False,
) -> ParseResult:
    """Main parse entry point. Dispatches to manpage or section-based parser."""
    if not text.strip():
        return ParseResult(
            command=Command(path=command_path),
            warnings=["Empty help output"],
        )

    if force_manpage or is_manpage(text):
        return _parse_manpage(text, cli_name, command_path)

    return _parse_sectioned(text, cli_name, command_path)


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
    cmd = Command(path=command_path)
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
                            cmd.description = stripped
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
                            subcommand_descriptions[pc.name] = pc.description

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
    if global_flags:
        # At root level, we return global flags as the command's flags
        # The pipeline will separate them into CLIMap.global_flags
        cmd.flags = global_flags + all_flags
    else:
        cmd.flags = all_flags

    # Extract env vars from flag descriptions too
    inline_envvars = extract_envvars_from_text(text)
    env_vars.extend(inline_envvars)
    cmd.env_vars = _deduplicate_envvars(env_vars)

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
