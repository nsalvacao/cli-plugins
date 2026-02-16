"""Integration regression test for pnpm CLIMap + plugin generation (T081)."""

from __future__ import annotations

import shutil

import pytest

from crawler.config import CLIConfig
from crawler.pipeline import crawl_cli
from generator.plugin_generator import generate_plugin, load_cli_map


def test_pnpm_climap_and_plugin_quality_regression(tmp_path) -> None:
    if shutil.which("pnpm") is None:
        pytest.skip("pnpm binary is not available on PATH")

    output_path = tmp_path / "pnpm.json"
    cli_map = crawl_cli(
        "pnpm",
        CLIConfig(name="pnpm", timeout=5, max_depth=2, max_concurrent=4),
        output_path=output_path,
        include_raw=False,
        strict=False,
    )

    assert output_path.exists()
    assert int(cli_map.metadata.get("total_commands", "0")) >= 12

    loaded = load_cli_map(output_path)
    plugin_root = generate_plugin(loaded, tmp_path / "plugins", str(output_path))
    commands_md = (plugin_root / "skills" / "cli-pnpm" / "references" / "commands.md").read_text(
        encoding="utf-8"
    )
    examples_md = (plugin_root / "skills" / "cli-pnpm" / "references" / "examples.md").read_text(
        encoding="utf-8"
    )
    skill_md = (plugin_root / "skills" / "cli-pnpm" / "SKILL.md").read_text(encoding="utf-8")

    assert "pnpm add" in commands_md
    assert "pnpm install" in commands_md
    assert "pnpm run" in commands_md
    assert "```bash" in examples_md
    assert "_No examples extracted._" not in skill_md
