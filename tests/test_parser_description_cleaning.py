"""Tests for parser description cleaning of runtime/status noise."""

from __future__ import annotations

from crawler.parser import parse_help_output


def test_runtime_error_description_is_discarded() -> None:
    text = """
error: unrecognized subcommand '--help'

Usage: ruff [OPTIONS] COMMAND [ARGS]...

Commands:
  check   Run checks on code
"""
    result = parse_help_output(text, "ruff", "ruff")
    assert result.command.description == ""


def test_state_message_description_is_discarded() -> None:
    text = """
[WARN] Swarm already initialized

Usage: claude-flow swarm [OPTIONS] COMMAND [ARGS]...

Commands:
  status  Get swarm status
"""
    result = parse_help_output(text, "claude-flow", "claude-flow swarm")
    assert result.command.description == ""


def test_circular_description_is_discarded() -> None:
    text = """
demo

Usage: demo [OPTIONS]
"""
    result = parse_help_output(text, "demo", "demo")
    assert result.command.description == ""


def test_regular_description_is_kept() -> None:
    text = """
Fast and reliable package manager.

Usage: uv [OPTIONS] COMMAND [ARGS]...
"""
    result = parse_help_output(text, "uv", "uv")
    assert result.command.description == "Fast and reliable package manager."


def test_subcommand_oneliner_equal_to_name_is_preserved() -> None:
    text = """
Usage: demo [OPTIONS] COMMAND [ARGS]...

Commands:
  deploy  deploy
"""
    result = parse_help_output(text, "demo", "demo")
    assert "deploy" in result.subcommand_descriptions
    assert result.subcommand_descriptions["deploy"] == "deploy"
