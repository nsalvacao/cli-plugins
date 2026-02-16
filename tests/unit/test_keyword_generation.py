"""Unit tests for semantic keyword generation (T028)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from generator.plugin_generator import generate_semantic_keywords


def test_keywords_are_semantic_not_first_words() -> None:
    """Keywords should include domain terms from descriptions, not generic first words."""
    cli_map = {
        "cli_name": "acme",
        "metadata": {},
        "commands": {
            "scan": {
                "description": (
                    "Manage command lifecycle for security analysis and compliance reporting"
                ),
                "subcommands": {
                    "deep": {
                        "description": "Run forensic analysis for incident response workflows",
                        "subcommands": {},
                        "flags": [],
                    }
                },
                "flags": [],
            },
            "deploy": {
                "description": "Manage releases with canary rollout and rollback automation",
                "subcommands": {},
                "flags": [],
            },
        },
    }

    keywords = generate_semantic_keywords(cli_map, max_keywords=7)

    assert keywords[0] == "acme"
    assert "manage" not in keywords
    assert "command" not in keywords
    assert any(
        token in keywords
        for token in ("security", "compliance", "forensic", "rollout", "automation")
    )


def test_keywords_include_top_command_groups_from_fixture() -> None:
    fixture = Path(__file__).resolve().parents[2] / "output" / "claude-flow.json"
    if not fixture.exists():
        pytest.skip("output/claude-flow.json not available")

    cli_map = json.loads(fixture.read_text(encoding="utf-8"))
    keywords = generate_semantic_keywords(cli_map, max_keywords=8)
    top_groups = [
        name.lower() for name, data in cli_map["commands"].items() if data.get("subcommands")
    ]

    assert "claude-flow" in keywords
    assert top_groups, "fixture should expose at least one command group with subcommands"
    assert any(group in keywords for group in top_groups)
