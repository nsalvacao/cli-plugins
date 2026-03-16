from __future__ import annotations

import sys
from pathlib import Path

import pytest

from generator import plugin_generator


@pytest.mark.unit
def test_generate_plugin_reports_missing_input_file(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    missing_json = tmp_path / "missing.json"
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate-plugin", str(missing_json)],
    )

    with pytest.raises(SystemExit) as exc_info:
        plugin_generator.main()

    captured = capsys.readouterr()
    assert exc_info.value.code == plugin_generator.CLI_USER_ERROR_EXIT_CODE
    assert captured.out == ""
    assert captured.err == f"Error: input JSON file not found: {missing_json}\n"


@pytest.mark.unit
def test_generate_plugin_reports_invalid_json_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    invalid_json = tmp_path / "invalid.json"
    invalid_json.write_text('{"cli_name": ', encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate-plugin", str(invalid_json)],
    )

    with pytest.raises(SystemExit) as exc_info:
        plugin_generator.main()

    captured = capsys.readouterr()
    assert exc_info.value.code == plugin_generator.CLI_USER_ERROR_EXIT_CODE
    assert captured.out == ""
    assert captured.err.startswith(f"Error: invalid JSON in input file {invalid_json}:")
