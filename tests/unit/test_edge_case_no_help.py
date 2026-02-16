"""Unit test for EC-01: CLI without standard --help should degrade gracefully."""

from __future__ import annotations

import logging
from pathlib import Path

from crawler.config import CLIConfig
from crawler.models import ExecutionResult, HelpDetectionResult
from crawler.pipeline import crawl_cli


def test_no_standard_help_returns_partial_climap_and_warning(
    monkeypatch, tmp_path: Path, caplog
) -> None:
    cli_name = "mystery-cli"
    config = CLIConfig(name=cli_name, raw_threshold=10_000)

    detection = HelpDetectionResult(
        pattern="unknown",
        result=ExecutionResult(
            stdout="",
            stderr="unknown option: --help",
            exit_code=2,
            command=[cli_name, "--help"],
        ),
    )

    monkeypatch.setattr("crawler.pipeline.detect_version", lambda *_args, **_kwargs: "")
    monkeypatch.setattr("crawler.pipeline.detect_help_pattern", lambda *_args, **_kwargs: detection)
    monkeypatch.setattr(
        "crawler.pipeline.discover_and_crawl",
        lambda *_args, **_kwargs: {},
    )

    caplog.set_level(logging.WARNING)

    output_path = tmp_path / f"{cli_name}.json"
    cli_map = crawl_cli(cli_name, config, output_path=output_path, strict=False)

    assert output_path.exists()
    assert cli_map.cli_name == cli_name
    assert cli_map.commands == {}
    assert int(cli_map.metadata.get("parse_warnings", "0")) >= 1
    assert float(cli_map.metadata.get("confidence_score", "1.0")) <= 0.40
    assert any("degraded mode" in msg.lower() for msg in caplog.messages)
