"""Unit tests for progressive disclosure output (T040)."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from generator.plugin_generator import (
    compute_stats,
    generate_plugin,
    generate_skill_md,
    load_cli_map,
)

DOCKER_JSON = Path(__file__).resolve().parents[2] / "output" / "docker.json"


def _approx_token_count(text: str) -> int:
    """Approximate tokenizer-neutral token count."""
    return len(re.findall(r"\w+|[^\w\s]", text))


@pytest.fixture
def docker_map() -> dict:
    if not DOCKER_JSON.exists():
        pytest.skip("output/docker.json not available")
    return load_cli_map(DOCKER_JSON)


def test_skill_md_compact_view_budget_and_examples(docker_map: dict) -> None:
    stats = compute_stats(docker_map)
    skill_md = generate_skill_md(docker_map, stats)

    assert _approx_token_count(skill_md) <= 800
    assert skill_md.count("```bash") <= 5
    assert "references/commands.md" in skill_md
    assert "references/examples.md" in skill_md


def test_references_keep_full_details_while_skill_is_compact(
    docker_map: dict, tmp_path: Path
) -> None:
    plugin_root = generate_plugin(docker_map, tmp_path, str(DOCKER_JSON))
    skill_md = (plugin_root / "skills" / "cli-docker" / "SKILL.md").read_text(encoding="utf-8")
    commands_md = (
        plugin_root / "skills" / "cli-docker" / "references" / "commands.md"
    ).read_text(encoding="utf-8")
    examples_md = (
        plugin_root / "skills" / "cli-docker" / "references" / "examples.md"
    ).read_text(encoding="utf-8")

    assert _approx_token_count(skill_md) <= 800
    assert "docker run" in commands_md
    assert commands_md.count("| Flag |") >= 1
    assert examples_md.count("```bash") > skill_md.count("```bash")
