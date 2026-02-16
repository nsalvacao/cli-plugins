"""Integration regression test for gcc CLIMap + plugin generation (T120)."""

from __future__ import annotations

import shutil

import pytest

from crawler.config import CLIConfig
from crawler.pipeline import crawl_cli
from generator.plugin_generator import generate_plugin, load_cli_map


def test_gcc_climap_and_plugin_quality_regression(tmp_path) -> None:
    if shutil.which("gcc") is None:
        pytest.skip("gcc binary is not available on PATH")

    output_path = tmp_path / "gcc.json"
    cli_map = crawl_cli(
        "gcc",
        CLIConfig(name="gcc", timeout=8, max_depth=1, max_concurrent=2),
        output_path=output_path,
        include_raw=False,
        strict=False,
    )

    assert output_path.exists()
    assert len(cli_map.global_flags) >= 20

    names = {flag.name for flag in cli_map.global_flags}
    assert "-print-file-name" in names
    assert "-dumpmachine" in names
    assert "-Wa" in names
    assert "-Xassembler" in names
    assert "-std" in names

    by_name = {flag.name: flag for flag in cli_map.global_flags}
    assert by_name["-dumpmachine"].type == "bool"
    assert by_name["-pipe"].type == "bool"
    assert by_name["-Wa"].type == "string"
    assert by_name["-Xassembler"].type == "string"
    assert by_name["-std"].type == "string"

    loaded = load_cli_map(output_path)
    plugin_root = generate_plugin(loaded, tmp_path / "plugins", str(output_path))
    commands_md = (
        plugin_root / "skills" / "cli-gcc" / "references" / "commands.md"
    ).read_text(encoding="utf-8")

    assert "-print-file-name" in commands_md
    assert "-Wa" in commands_md
    assert "-Xassembler" in commands_md
    assert "-std" in commands_md
