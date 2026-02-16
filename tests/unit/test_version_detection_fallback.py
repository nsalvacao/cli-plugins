"""Unit tests for robust version detection fallback (T084)."""

from __future__ import annotations

from crawler.models import ExecutionResult
from crawler.version import _parse_version, detect_version


class _FakeExecutor:
    def __init__(self, results: dict[str, ExecutionResult]) -> None:
        self._results = results

    def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        key = " ".join(command)
        return self._results.get(
            key,
            ExecutionResult(stdout="", stderr="", exit_code=1, command=command),
        )


def test_parse_version_for_yq_style_line() -> None:
    text = "yq (https://github.com/mikefarah/yq/) version v4.44.3"
    assert _parse_version(text) == "4.44.3"


def test_detect_version_skips_zero_placeholder_and_uses_next_candidate() -> None:
    cli_name = "yq"
    executor = _FakeExecutor(
        {
            "yq --version": ExecutionResult(
                stdout="yq 0.0.0",
                stderr="",
                exit_code=0,
                command=["yq", "--version"],
            ),
            "yq -V": ExecutionResult(
                stdout="jq-1.7",
                stderr="",
                exit_code=0,
                command=["yq", "-V"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "1.7"


def test_detect_version_returns_empty_when_only_zero_placeholders() -> None:
    cli_name = "yq"
    executor = _FakeExecutor(
        {
            "yq --version": ExecutionResult(
                stdout="yq 0.0.0",
                stderr="",
                exit_code=0,
                command=["yq", "--version"],
            ),
            "yq -V": ExecutionResult(
                stdout="yq 0.0.0",
                stderr="",
                exit_code=0,
                command=["yq", "-V"],
            ),
            "yq version": ExecutionResult(
                stdout="yq 0.0.0",
                stderr="",
                exit_code=0,
                command=["yq", "version"],
            ),
            "yq -v": ExecutionResult(
                stdout="yq 0.0.0",
                stderr="",
                exit_code=0,
                command=["yq", "-v"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_skips_suffix_placeholder_and_uses_real_version() -> None:
    cli_name = "tool"
    executor = _FakeExecutor(
        {
            "tool --version": ExecutionResult(
                stdout="tool version 0.0.0-dev",
                stderr="",
                exit_code=0,
                command=["tool", "--version"],
            ),
            "tool -V": ExecutionResult(
                stdout="tool version v2.4.1",
                stderr="",
                exit_code=0,
                command=["tool", "-V"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "2.4.1"


def test_detect_version_treats_unknown_placeholder_as_missing() -> None:
    cli_name = "tool"
    executor = _FakeExecutor(
        {
            "tool --version": ExecutionResult(
                stdout="tool unknown",
                stderr="",
                exit_code=0,
                command=["tool", "--version"],
            ),
            "tool -V": ExecutionResult(
                stdout="",
                stderr="",
                exit_code=1,
                command=["tool", "-V"],
            ),
            "tool version": ExecutionResult(
                stdout="",
                stderr="",
                exit_code=1,
                command=["tool", "version"],
            ),
            "tool -v": ExecutionResult(
                stdout="",
                stderr="",
                exit_code=1,
                command=["tool", "-v"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_prefers_cli_version_over_dependency_version_in_same_output() -> None:
    cli_name = "yq"
    executor = _FakeExecutor(
        {
            "yq --version": ExecutionResult(
                stdout="jq-1.7\nyq version v4.44.3",
                stderr="",
                exit_code=0,
                command=["yq", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "4.44.3"


def test_detect_version_prefers_cli_leading_name_version_over_dependency_pattern() -> None:
    cli_name = "yq"
    executor = _FakeExecutor(
        {
            "yq --version": ExecutionResult(
                stdout="jq-1.7\nyq 4.44.3",
                stderr="",
                exit_code=0,
                command=["yq", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "4.44.3"


def test_detect_version_prefers_structural_cli_version_over_contextual_dependency_version() -> None:
    cli_name = "tool"
    executor = _FakeExecutor(
        {
            "tool --version": ExecutionResult(
                stdout="tool uses libfoo version 1.2.3\ntool version 2.0.0",
                stderr="",
                exit_code=0,
                command=["tool", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "2.0.0"


def test_detect_version_does_not_treat_prefixed_name_as_same_cli() -> None:
    cli_name = "uv"
    executor = _FakeExecutor(
        {
            "uv --version": ExecutionResult(
                stdout="uvx version 0.1.0",
                stderr="",
                exit_code=0,
                command=["uv", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_ignores_cli_name_inside_hyphenated_foreign_token() -> None:
    cli_name = "jq"
    executor = _FakeExecutor(
        {
            "jq --version": ExecutionResult(
                stdout="yq-jq-helper version 1.2.3",
                stderr="",
                exit_code=0,
                command=["jq", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_does_not_treat_prefixed_name_with_at_version_as_same_cli() -> None:
    cli_name = "uv"
    executor = _FakeExecutor(
        {
            "uv --version": ExecutionResult(
                stdout="uvx@0.1.0",
                stderr="",
                exit_code=0,
                command=["uv", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_ignores_foreign_version_v_prefix_line() -> None:
    cli_name = "jq"
    executor = _FakeExecutor(
        {
            "jq --version": ExecutionResult(
                stdout="yq-jq-helper version v1.2.3",
                stderr="",
                exit_code=0,
                command=["jq", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == ""


def test_detect_version_prefers_structural_cli_v_line_over_contextual_at_version() -> None:
    cli_name = "tool"
    executor = _FakeExecutor(
        {
            "tool --version": ExecutionResult(
                stdout="tool uses libfoo@1.2.3\ntool v2.0.0",
                stderr="",
                exit_code=0,
                command=["tool", "--version"],
            ),
        }
    )

    assert detect_version(cli_name, executor) == "2.0.0"
