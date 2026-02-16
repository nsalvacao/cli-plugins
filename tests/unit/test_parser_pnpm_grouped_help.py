"""pnpm grouped-help parsing tests (T079)."""

from __future__ import annotations

from crawler.parser import parse_help_output
from crawler.parsers.sections import SectionType, segment_help_text


def test_pnpm_group_headers_are_detected_as_command_sections(pnpm_help) -> None:
    sections = segment_help_text(pnpm_help)
    command_sections = [s for s in sections if s.type == SectionType.COMMANDS]

    assert len(command_sections) >= 3
    headers = {s.header for s in command_sections}
    assert "Manage your dependencies:" in headers
    assert "Review your dependencies:" in headers
    assert "Run your scripts:" in headers


def test_pnpm_root_extracts_grouped_commands_and_alias_rows(pnpm_help) -> None:
    result = parse_help_output(pnpm_help, "pnpm", "pnpm")
    subcommands = set(result.subcommand_names)

    assert len(subcommands) >= 12
    assert "add" in subcommands
    assert "install" in subcommands
    assert "run" in subcommands
    assert "config" in subcommands
    assert "remove" in subcommands


def test_pnpm_wrapped_description_is_recovered(pnpm_help) -> None:
    result = parse_help_output(pnpm_help, "pnpm", "pnpm")
    desc = result.subcommand_descriptions.get("add", "")

    assert "By default" in desc
    assert "prod dependency" in desc
