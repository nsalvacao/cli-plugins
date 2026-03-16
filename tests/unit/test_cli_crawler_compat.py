"""Compatibility tests for legacy ``cli_crawler`` wrappers."""

from __future__ import annotations

import sys

import pytest

from crawler import cli_crawler


def test_main_maps_include_raw_to_raw(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Legacy ``--include-raw`` should map to canonical ``--raw``."""
    monkeypatch.setattr(sys, "argv", ["cli_crawler.py", "git", "--include-raw"])
    captured_argv: list[str] = []

    def _fake_pipeline_main() -> None:
        captured_argv.extend(sys.argv)

    monkeypatch.setattr(cli_crawler._pipeline, "main", _fake_pipeline_main)

    cli_crawler.main()

    assert captured_argv == ["cli_crawler.py", "git", "--raw"]
    stderr = capsys.readouterr().err
    assert "cli-crawler" in stderr
    assert "--include-raw is deprecated; treating it as --raw." in stderr


def test_main_prefers_raw_when_both_raw_flags_are_present(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """When both flags are present, keep one canonical ``--raw`` only."""
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli_crawler.py", "git", "--raw", "--include-raw"],
    )
    captured_argv: list[str] = []

    def _fake_pipeline_main() -> None:
        captured_argv.extend(sys.argv)

    monkeypatch.setattr(cli_crawler._pipeline, "main", _fake_pipeline_main)

    cli_crawler.main()

    assert captured_argv == ["cli_crawler.py", "git", "--raw"]
    stderr = capsys.readouterr().err
    assert "--include-raw is deprecated and ignored when --raw is also provided." in stderr
