"""Tests for config inventory auditing and minimal override suggestions."""

from __future__ import annotations

import json
from pathlib import Path

from config.audit import build_config_audit_report, write_config_audit_report


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_build_config_audit_report_handles_empty_dirs(tmp_path: Path) -> None:
    config_path = tmp_path / "config.yaml"
    output_dir = tmp_path / "output"
    plugins_dir = tmp_path / "plugins"

    _write(
        config_path,
        """defaults:
  timeout: 5
  max_depth: 5
  max_concurrent: 5
  environment: wsl
clis:
""",
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    plugins_dir.mkdir(parents=True, exist_ok=True)

    report = build_config_audit_report(config_path, output_dir, plugins_dir)

    assert report["missing_in_config"] == []
    assert report["stale_in_config"] == []
    assert report["missing_output"] == []
    assert report["missing_plugin"] == []
    assert report["suggested_minimal_overrides"] == {}
    assert report["config_entries_without_overrides"] == []


def test_build_config_audit_report_detects_inventory_drift(tmp_path: Path) -> None:
    config_path = tmp_path / "config.yaml"
    output_dir = tmp_path / "output"
    plugins_dir = tmp_path / "plugins"

    _write(
        config_path,
        """defaults:
  timeout: 5
  max_depth: 5
  max_concurrent: 5
  environment: wsl
clis:
  git:
    max_depth: 7
  docker:
    group: containers
""",
    )

    _write(
        output_dir / "git.json",
        json.dumps({"cli_name": "git", "commands": {}, "metadata": {}, "global_flags": []}),
    )
    _write(
        output_dir / "gh.json",
        json.dumps({"cli_name": "gh", "commands": {}, "metadata": {}, "global_flags": []}),
    )
    _write(output_dir / "gh.raw.json", "{}")

    (plugins_dir / "cli-git").mkdir(parents=True, exist_ok=True)
    (plugins_dir / "cli-npm").mkdir(parents=True, exist_ok=True)
    (plugins_dir / "not-a-plugin").mkdir(parents=True, exist_ok=True)

    report = build_config_audit_report(config_path, output_dir, plugins_dir)

    assert report["configured_clis"] == ["docker", "git"]
    assert report["crawled_clis"] == ["gh", "git"]
    assert report["plugin_clis"] == ["git", "npm"]

    assert report["missing_in_config"] == ["gh", "npm"]
    assert report["stale_in_config"] == ["docker"]
    assert report["missing_output"] == ["docker"]
    assert report["missing_plugin"] == ["docker"]

    assert report["suggested_minimal_overrides"] == {"git": {"max_depth": 7}}
    assert report["config_entries_without_overrides"] == ["docker"]


def test_build_config_audit_report_tracks_environment_and_plugin_discovery_overrides(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "config.yaml"
    output_dir = tmp_path / "output"
    plugins_dir = tmp_path / "plugins"

    _write(
        config_path,
        """defaults:
  timeout: 5
  max_depth: 5
  max_concurrent: 5
  environment: wsl
clis:
  gh:
    plugins:
      discovery_command: gh extension list
  gemini:
    environment: windows
""",
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    plugins_dir.mkdir(parents=True, exist_ok=True)

    report = build_config_audit_report(config_path, output_dir, plugins_dir)
    overrides = report["suggested_minimal_overrides"]

    assert overrides["gh"]["plugins"]["discovery_command"] == "gh extension list"
    assert overrides["gemini"]["environment"] == "windows"


def test_write_config_audit_report_writes_json(tmp_path: Path) -> None:
    report_path = tmp_path / "output" / "config-audit.json"
    report = {
        "configured_clis": ["git"],
        "crawled_clis": ["git"],
        "plugin_clis": ["git"],
        "missing_in_config": [],
        "stale_in_config": [],
        "missing_output": [],
        "missing_plugin": [],
        "suggested_minimal_overrides": {},
        "config_entries_without_overrides": [],
    }

    write_config_audit_report(report, report_path)
    loaded = json.loads(report_path.read_text(encoding="utf-8"))
    assert loaded["configured_clis"] == ["git"]


def test_build_config_audit_report_ignores_non_climap_json_files(tmp_path: Path) -> None:
    config_path = tmp_path / "config.yaml"
    output_dir = tmp_path / "output"
    plugins_dir = tmp_path / "plugins"

    _write(
        config_path,
        """defaults:
  timeout: 5
  max_depth: 5
  max_concurrent: 5
  environment: wsl
clis:
  git:
""",
    )

    _write(
        output_dir / "git.json",
        json.dumps({"cli_name": "git", "commands": {}, "metadata": {}, "global_flags": []}),
    )
    _write(
        output_dir / "config-audit.json",
        json.dumps({"missing_in_config": [], "stale_in_config": []}),
    )
    (plugins_dir / "cli-git").mkdir(parents=True, exist_ok=True)

    report = build_config_audit_report(config_path, output_dir, plugins_dir)

    assert report["crawled_clis"] == ["git"]
    assert report["missing_in_config"] == []
