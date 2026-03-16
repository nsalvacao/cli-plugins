"""Regression tests for root CLI missing exit behavior."""

from __future__ import annotations

from crawler import pipeline
from crawler.config import CLIConfig
from crawler.models import ExecutionResult, HelpDetectionResult


def test_crawl_cli_raises_when_root_cli_binary_is_missing() -> None:
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

    original_detect_version = pipeline.detect_version
    original_detect_help_pattern = pipeline.detect_help_pattern
    try:
        pipeline.detect_version = lambda _cli_name, _executor: ""
        pipeline.detect_help_pattern = (
            lambda _cli_name, _executor, _config: detection_result
        )

        try:
            pipeline.crawl_cli(missing_cli, config)
        except pipeline.RootCLIBinaryNotFoundError:
            pass
        else:
            msg = "Expected RootCLIBinaryNotFoundError for missing root CLI binary."
            raise AssertionError(msg)
    finally:
        pipeline.detect_version = original_detect_version
        pipeline.detect_help_pattern = original_detect_help_pattern


def test_main_exits_non_zero_when_root_cli_binary_is_missing() -> None:
    """cli-crawler entrypoint should return deterministic non-zero status."""
    missing_cli = "definitely-missing-cli"
    original_argv = pipeline.sys.argv
    original_crawl_cli = pipeline.crawl_cli
    try:
        pipeline.sys.argv = ["cli-crawler", missing_cli]

        def _raise_missing(*_args: object, **_kwargs: object) -> object:
            raise pipeline.RootCLIBinaryNotFoundError("missing binary")

        pipeline.crawl_cli = _raise_missing

        try:
            pipeline.main()
        except SystemExit as exc:
            assert exc.code == 2
        else:
            raise AssertionError("Expected SystemExit with non-zero exit code.")
    finally:
        pipeline.crawl_cli = original_crawl_cli
        pipeline.sys.argv = original_argv
