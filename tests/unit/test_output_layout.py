"""Unit tests for deterministic output layout and path resolution."""

from __future__ import annotations

import json
from pathlib import Path

from crawler.config import CLIConfig
from crawler.formatter import write_output
from crawler.models import CLIMap
from crawler.pipeline import _resolve_output_path


def test_resolve_output_path_accepts_directory(tmp_path: Path) -> None:
    resolved = _resolve_output_path(tmp_path, "docker")
    assert resolved == tmp_path / "docker.json"


def test_resolve_output_path_accepts_json_file(tmp_path: Path) -> None:
    explicit_file = tmp_path / "custom-output.json"
    resolved = _resolve_output_path(explicit_file, "docker")
    assert resolved == explicit_file


def test_resolve_output_path_treats_plain_value_as_directory(tmp_path: Path) -> None:
    plain = tmp_path / "artifacts"
    resolved = _resolve_output_path(plain, "docker")
    assert resolved == plain / "docker.json"


def test_write_output_writes_main_and_raw_sidecar(tmp_path: Path) -> None:
    output_path = tmp_path / "docker.json"
    cli_map = CLIMap(cli_name="docker", cli_version="1.0", metadata={}, commands={})
    raw_outputs = {"docker": "Usage: docker [OPTIONS] COMMAND"}

    write_output(
        cli_map,
        raw_outputs,
        output_path,
        CLIConfig(name="docker", raw_threshold=99999999),
        include_raw=False,
    )

    main_file = tmp_path / "docker.json"
    raw_file = tmp_path / "docker.raw.json"
    assert main_file.exists()
    assert raw_file.exists()

    main_data = json.loads(main_file.read_text(encoding="utf-8"))
    raw_data = json.loads(raw_file.read_text(encoding="utf-8"))
    assert main_data["raw_file"] == "docker.raw.json"
    assert raw_data["docker"].startswith("Usage: docker")
