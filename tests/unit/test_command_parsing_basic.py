"""Basic command hierarchy parsing tests (T011)."""

from __future__ import annotations

from crawler.parser import parse_help_output


def test_parse_docker_root_command_hierarchy(docker_help) -> None:
    result = parse_help_output(docker_help, "docker", "docker")
    subcommands = set(result.subcommand_names)

    assert "run" in subcommands
    assert "container" in subcommands
    assert len(subcommands) >= 20


def test_parse_claude_flow_root_commands(claude_flow_help) -> None:
    result = parse_help_output(claude_flow_help, "claude-flow", "claude-flow")
    subcommands = set(result.subcommand_names)

    assert "agent" in subcommands
    assert "swarm" in subcommands
    assert "memory" in subcommands
