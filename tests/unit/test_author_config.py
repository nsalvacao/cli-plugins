"""Unit tests for configurable plugin author metadata (T029)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from generator.plugin_generator import compute_stats, generate_plugin_json, load_cli_map

FIXTURE_PATH = Path(__file__).resolve().parents[2] / "output" / "claude-flow.json"


@pytest.fixture
def cf_map() -> dict:
    if not FIXTURE_PATH.exists():
        pytest.skip("output/claude-flow.json not available")
    return load_cli_map(FIXTURE_PATH)


def test_author_omitted_when_not_configured(cf_map: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CLI_PLUGINS_AUTHOR", raising=False)
    stats = compute_stats(cf_map)

    plugin_obj = json.loads(generate_plugin_json(cf_map, stats))

    assert "author" not in plugin_obj


def test_author_loaded_from_environment(cf_map: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CLI_PLUGINS_AUTHOR", "Community Maintainers")
    stats = compute_stats(cf_map)

    plugin_obj = json.loads(generate_plugin_json(cf_map, stats))

    assert plugin_obj["author"] == {"name": "Community Maintainers"}


def test_explicit_author_overrides_environment(
    cf_map: dict, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("CLI_PLUGINS_AUTHOR", "Env Author")
    stats = compute_stats(cf_map)

    plugin_obj = json.loads(generate_plugin_json(cf_map, stats, author="Flag Author"))

    assert plugin_obj["author"] == {"name": "Flag Author"}
