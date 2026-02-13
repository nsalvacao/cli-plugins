"""Unit tests for src/lib/subprocess_utils.py — T007."""

import pytest

from lib.subprocess_utils import SAFE_ENV, SubprocessResult, run_safe


def test_run_safe_returns_result_for_valid_command():
    result = run_safe(["echo", "hello"])
    assert isinstance(result, SubprocessResult)
    assert result.exit_code == 0
    assert "hello" in result.stdout


def test_run_safe_empty_cmd_raises():
    with pytest.raises(ValueError, match="non-empty"):
        run_safe([])


def test_run_safe_timeout():
    result = run_safe(["python3", "-c", "import time; time.sleep(10)"], timeout=1)
    assert result.timed_out is True
    assert result.exit_code == -1
    assert "TIMEOUT" in result.stderr


def test_run_safe_command_not_found():
    result = run_safe(["nonexistent_cmd_xyz_abc"])
    assert result.exit_code == -1
    assert "not found" in result.stderr.lower()


def test_run_safe_duration_is_positive():
    result = run_safe(["echo", "timing"])
    assert result.duration >= 0.0


def test_safe_env_disables_color_and_pager():
    assert SAFE_ENV["NO_COLOR"] == "1"
    assert SAFE_ENV["PAGER"] == "cat"
    assert SAFE_ENV["TERM"] == "dumb"


def test_run_safe_no_shell_injection():
    """List-form args: shell metacharacters are treated as literals, not executed."""
    result = run_safe(["echo", "safe; rm -rf /"])
    assert "safe; rm -rf /" in result.stdout
    assert result.exit_code == 0


def test_run_safe_extra_env_is_merged():
    result = run_safe(
        [
            "python3",
            "-c",
            "import os; print('\\n'.join(f'{k}={v}' for k, v in os.environ.items()))",
        ],
        extra_env={"TEST_CUSTOM_VAR": "sentinel_value"},
    )
    assert "TEST_CUSTOM_VAR=sentinel_value" in result.stdout
