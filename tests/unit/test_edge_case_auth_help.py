"""Unit tests for EC-02: help requiring authentication should fail clearly."""

from __future__ import annotations

from pathlib import Path

import pytest

from crawler.config import CLIConfig
from crawler.detector import detect_help_pattern
from crawler.executor import is_auth_required_failure
from crawler.models import ExecutionResult, HelpDetectionResult
from crawler.pipeline import crawl_cli


def _auth_detection(cli_name: str) -> HelpDetectionResult:
    return HelpDetectionResult(
        pattern="auth_required",
        result=ExecutionResult(
            stdout="",
            stderr=(
                "AUTH_REQUIRED: Help command requires authentication for "
                f"'{cli_name}'. Run '{cli_name} auth login' and retry."
            ),
            exit_code=1,
            command=[cli_name, "--help"],
        ),
    )


def test_auth_required_help_returns_clear_warning_without_hanging(
    monkeypatch, tmp_path: Path
) -> None:
    cli_name = "private-cli"
    config = CLIConfig(name=cli_name, raw_threshold=10_000)

    monkeypatch.setattr("crawler.pipeline.detect_version", lambda *_args, **_kwargs: "")
    monkeypatch.setattr(
        "crawler.pipeline.detect_help_pattern",
        lambda *_args, **_kwargs: _auth_detection(cli_name),
    )
    monkeypatch.setattr(
        "crawler.pipeline.discover_and_crawl",
        lambda *_args, **_kwargs: {},
    )

    cli_map = crawl_cli(
        cli_name,
        config,
        output_path=tmp_path / f"{cli_name}.json",
        strict=False,
    )

    assert cli_map.cli_name == cli_name
    assert cli_map.commands == {}
    assert int(cli_map.metadata.get("parse_warnings", "0")) >= 1
    assert float(cli_map.metadata.get("confidence_score", "1.0")) <= 0.30
    assert (
        cli_map.metadata.get("help_error", "").startswith("AUTH_REQUIRED:")
        or "AUTH_REQUIRED:" in cli_map.metadata.get("help_error", "")
    )


def test_auth_required_help_raises_in_strict_mode(monkeypatch, tmp_path: Path) -> None:
    cli_name = "private-cli"
    config = CLIConfig(name=cli_name, raw_threshold=10_000)

    monkeypatch.setattr("crawler.pipeline.detect_version", lambda *_args, **_kwargs: "")
    monkeypatch.setattr(
        "crawler.pipeline.detect_help_pattern",
        lambda *_args, **_kwargs: _auth_detection(cli_name),
    )

    with pytest.raises(RuntimeError, match="AUTH_REQUIRED:"):
        crawl_cli(
            cli_name,
            config,
            output_path=tmp_path / f"{cli_name}.json",
            strict=True,
        )


def test_auth_detection_uses_stderr_only_to_avoid_help_false_positives() -> None:
    result = ExecutionResult(
        stdout="Usage: demo [OPTIONS]\n--token <value>  optional token flag\n--help  show help",
        stderr="",
        exit_code=1,
        command=["demo", "--help"],
    )
    assert not is_auth_required_failure(result)


def test_detect_help_pattern_continues_after_auth_failure_on_first_pattern() -> None:
    cli_name = "demo"
    valid_help = "\n".join(
        [
            "Usage: demo [OPTIONS]",
            "Options:",
            "  -h, --help  Show help",
            "Commands:",
            "  run  Execute command",
        ]
    )

    class _FakeExecutor:
        def run_with_retry(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
            del timeout
            if command == [cli_name, "--help"]:
                return ExecutionResult(
                    stdout="",
                    stderr="authentication required",
                    exit_code=1,
                    command=command,
                )
            if command == [cli_name, "-h"]:
                return ExecutionResult(
                    stdout=valid_help,
                    stderr="",
                    exit_code=0,
                    command=command,
                )
            return ExecutionResult(stdout="", stderr="", exit_code=1, command=command)

        def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
            return self.run_with_retry(command, timeout)

    detection = detect_help_pattern(cli_name, _FakeExecutor(), CLIConfig(name=cli_name))
    assert detection.pattern == "-h"
