"""Performance smoke tests (T053)."""

from __future__ import annotations

import shutil
import time
from pathlib import Path

import pytest

from crawler.config import CLIConfig
from crawler.parser import parse_help_output
from crawler.pipeline import crawl_cli
from generator.plugin_generator import generate_plugin, load_cli_map


@pytest.mark.performance
def test_parse_1000_line_fixture_under_5_seconds() -> None:
    help_text = "\n".join(
        ["Usage: perf-cli [OPTIONS] COMMAND"]
        + [f"--flag-{i}  Description {i}" for i in range(1000)]
    )

    start = time.monotonic()
    result = parse_help_output(help_text, "perf-cli", "perf-cli")
    duration = time.monotonic() - start

    assert duration < 5.0
    assert result.command.usage_pattern


@pytest.mark.performance
def test_docker_crawl_and_generate_under_30_seconds(tmp_path: Path) -> None:
    if shutil.which("docker") is None:
        pytest.skip("docker CLI is not installed in this environment")

    output_path = tmp_path / "docker.json"
    plugin_root_dir = tmp_path / "plugins"
    config = CLIConfig(
        name="docker",
        timeout=5,
        max_depth=2,
        max_concurrent=4,
        raw_threshold=10_000,
    )

    start = time.monotonic()
    cli_map = crawl_cli(
        "docker",
        config,
        output_path=output_path,
        include_raw=False,
        strict=False,
    )
    plugin_root = generate_plugin(load_cli_map(output_path), plugin_root_dir, str(output_path))
    duration = time.monotonic() - start

    assert duration < 30.0
    assert output_path.exists()
    assert output_path.with_suffix(".raw.json").exists()
    assert plugin_root.exists()
    assert int(cli_map.metadata.get("total_commands", "0")) >= 20
