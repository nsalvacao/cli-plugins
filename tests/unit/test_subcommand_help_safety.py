"""Unit tests for non-mutating subcommand help fallback safety (T131)."""

from __future__ import annotations

from crawler.detector import detect_subcommand_help
from crawler.models import ExecutionResult


class _RecordingExecutor:
    def __init__(self, cli_name: str, bare_help_output: str = "") -> None:
        self.cli_name = cli_name
        self.bare_help_output = bare_help_output
        self.calls: list[list[str]] = []

    def run_with_retry(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        self.calls.append(command)
        if command == [self.cli_name, "help"]:
            return ExecutionResult(
                stdout="Usage: tool help\nOptions:\n  -h, --help  show help",
                stderr="",
                exit_code=0,
                command=command,
            )
        return ExecutionResult(stdout="", stderr="", exit_code=1, command=command)

    def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        self.calls.append(command)
        stdout = self.bare_help_output if command == [self.cli_name, "help"] else ""
        return ExecutionResult(
            stdout=stdout, stderr="", exit_code=0 if stdout else 1, command=command
        )


class _MappingExecutor:
    def __init__(self, mapping: dict[tuple[str, ...], ExecutionResult]) -> None:
        self.mapping = mapping
        self.calls: list[list[str]] = []

    def run_with_retry(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        self.calls.append(command)
        return self.mapping.get(
            tuple(command),
            ExecutionResult(stdout="", stderr="", exit_code=1, command=command),
        )

    def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        del timeout
        self.calls.append(command)
        return self.mapping.get(
            tuple(command),
            ExecutionResult(stdout="", stderr="", exit_code=1, command=command),
        )


def test_mutating_subcommand_does_not_use_bare_fallback() -> None:
    cli_name = "git.exe"
    executor = _RecordingExecutor(cli_name=cli_name)

    detection = detect_subcommand_help(
        cli_name=cli_name,
        subcommand_path=["init"],
        executor=executor,
        help_pattern="--help",
    )

    assert detection.pattern == "unknown"
    assert "SAFETY_GUARD" in detection.result.stderr
    assert [cli_name, "init"] not in executor.calls
    assert [cli_name, "init", "--help"] in executor.calls
    assert [cli_name, "init", "-h"] in executor.calls
    assert [cli_name, "help", "init"] in executor.calls


def test_explicit_help_subcommand_can_use_bare_fallback() -> None:
    cli_name = "tool"
    executor = _RecordingExecutor(
        cli_name=cli_name,
        bare_help_output="Usage: tool help\nOptions:\n  --verbose  be verbose",
    )

    detection = detect_subcommand_help(
        cli_name=cli_name,
        subcommand_path=["help"],
        executor=executor,
        help_pattern="--help",
    )

    assert detection.pattern == "bare"
    assert detection.result.stdout.startswith("Usage: tool help")
    assert [cli_name, "help"] in executor.calls


def test_version_subcommand_can_use_bare_fallback() -> None:
    cli_name = "tool"
    executor = _MappingExecutor(
        {
            (cli_name, "version"): ExecutionResult(
                stdout="Usage: tool version\nOptions:\n  --short  short output",
                stderr="",
                exit_code=0,
                command=[cli_name, "version"],
            )
        }
    )

    detection = detect_subcommand_help(
        cli_name=cli_name,
        subcommand_path=["version"],
        executor=executor,
        help_pattern="--help",
    )

    assert detection.pattern == "bare"
    assert detection.result.stdout.startswith("Usage: tool version")
    assert [cli_name, "version"] in executor.calls


def test_mutating_subcommand_keeps_auth_required_when_bare_is_blocked() -> None:
    cli_name = "git.exe"
    auth_result = ExecutionResult(
        stdout="",
        stderr="authentication required",
        exit_code=1,
        command=[cli_name, "init", "--help"],
    )
    executor = _MappingExecutor(
        {
            (cli_name, "init", "--help"): auth_result,
            (cli_name, "init", "-h"): auth_result,
            (cli_name, "help", "init"): auth_result,
        }
    )

    detection = detect_subcommand_help(
        cli_name=cli_name,
        subcommand_path=["init"],
        executor=executor,
        help_pattern="--help",
    )

    assert detection.pattern == "auth_required"
    assert detection.result.stderr.startswith("AUTH_REQUIRED:")
    assert [cli_name, "init"] not in executor.calls
