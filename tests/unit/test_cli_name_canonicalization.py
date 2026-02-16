"""Unit tests for executable-suffix CLI canonicalization (T133)."""

from __future__ import annotations

import json

from crawler.models import ExecutionResult
from crawler.version import detect_version
from generator.plugin_generator import generate_plugin


class _VersionExecutor:
    def __init__(self, results: dict[str, ExecutionResult]) -> None:
        self.results = results
        self.calls: list[list[str]] = []

    def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        self.calls.append(command)
        key = " ".join(command)
        return self.results.get(
            key,
            ExecutionResult(stdout="", stderr="", exit_code=1, command=command),
        )


def test_detect_version_canonicalizes_executable_suffix_but_keeps_invocation_command() -> None:
    executor = _VersionExecutor(
        {
            "git.exe --version": ExecutionResult(
                stdout="git version 2.53.0.windows.1",
                stderr="",
                exit_code=0,
                command=["git.exe", "--version"],
            ),
        }
    )

    version = detect_version("git.exe", executor)

    assert version == "2.53.0.windows.1"
    assert executor.calls
    assert executor.calls[0][0] == "git.exe"


def test_generate_plugin_uses_canonical_slug_for_executable_cli_names(tmp_path) -> None:
    cli_map = {
        "cli_name": "git.exe",
        "cli_version": "2.53.0.windows.1",
        "metadata": {"help_pattern": "--help"},
        "global_flags": [],
        "commands": {
            "status": {
                "path": "git.exe status",
                "description": "Show status",
                "flags": [],
                "subcommands": {},
            }
        },
    }

    root = generate_plugin(cli_map, tmp_path, "output/git-exe-win.json")

    assert root.name == "cli-git"
    plugin_json = json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert plugin_json["name"] == "cli-git"

    skill_path = root / "skills" / "cli-git" / "SKILL.md"
    assert skill_path.exists()
    skill_text = skill_path.read_text(encoding="utf-8")
    assert "name: cli-git" in skill_text
    assert "**git.exe**" in skill_text

    rescan_text = (root / "scripts" / "rescan.sh").read_text(encoding="utf-8")
    assert 'CLI_NAME="git.exe"' in rescan_text
