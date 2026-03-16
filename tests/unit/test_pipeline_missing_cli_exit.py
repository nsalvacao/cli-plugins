"""Regression tests for root CLI missing exit behavior."""

from __future__ import annotations

import pytest

from crawler import pipeline
from crawler.config import CLIConfig
from crawler.models import ExecutionResult, HelpDetectionResult


def test_crawl_cli_raises_when_root_cli_binary_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """crawl_cli should fail fast when root CLI binary is not found."""
    missing_cli = "definitely-missing-cli"
    detection_result = HelpDetectionResult(
        pattern="unknown",
        result=ExecutionResult(
            stdout="",
            stderr=f"Command not found: {missing_cli}",
            exit_code=-1,
            command=[missing_cli, "--help"],
        ),
    )

    config = CLIConfig(name=missing_cli)

    monkeypatch.setattr(pipeline, "detect_version", lambda _cli_name, _executor: "")
    monkeypatch.setattr(
        pipeline,
        "detect_help_pattern",
        lambda _cli_name, _executor, _config: detection_result,
    )

    with pytest.raises(pipeline.RootCLIBinaryNotFoundError):
        pipeline.crawl_cli(missing_cli, config)


def test_main_exits_non_zero_when_root_cli_binary_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """cli-crawler entrypoint should return deterministic non-zero status."""
    missing_cli = "definitely-missing-cli"
    monkeypatch.setattr(pipeline.sys, "argv", ["cli-crawler", missing_cli])

    def _raise_missing(*_args: object, **_kwargs: object) -> object:
        raise pipeline.RootCLIBinaryNotFoundError("missing binary")

    monkeypatch.setattr(pipeline, "crawl_cli", _raise_missing)

    with pytest.raises(SystemExit) as exc:
        pipeline.main()

    assert exc.value.code == pipeline.ROOT_CLI_NOT_FOUND_EXIT_CODE
