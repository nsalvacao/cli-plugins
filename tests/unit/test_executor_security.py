"""Security audit tests for executor._build_command — T067."""

from crawler.config import CLIConfig
from crawler.executor import Executor, _quote_ps_arg


def _executor(env: str = "wsl") -> Executor:
    return Executor(CLIConfig(name="test", environment=env))


# ── Linux/WSL passthrough ─────────────────────────────────────────────────────


def test_linux_command_passthrough():
    cmd = ["git", "status"]
    assert _executor("wsl")._build_command(cmd) == cmd


def test_linux_command_unchanged_with_special_chars():
    cmd = ["echo", "hello; rm -rf /"]
    assert _executor("wsl")._build_command(cmd) == cmd


# ── PowerShell wrapping ───────────────────────────────────────────────────────


def test_windows_wraps_in_powershell():
    result = _executor("windows")._build_command(["git", "status"])
    assert result[0] == "powershell.exe"
    assert "-Command" in result


def test_windows_uses_call_operator():
    result = _executor("windows")._build_command(["git", "status"])
    ps_cmd = result[-1]
    assert ps_cmd.startswith("& ")


def test_windows_arg_with_spaces_is_quoted():
    cmd = ["git", "commit", "-m", "feat: add space handling"]
    ps_cmd = _executor("windows")._build_command(cmd)[-1]
    assert "'feat: add space handling'" in ps_cmd


def test_windows_arg_with_single_quote_is_escaped():
    cmd = ["echo", "it's a test"]
    ps_cmd = _executor("windows")._build_command(cmd)[-1]
    # Single quote must be escaped as '' in PowerShell
    assert "it''s a test" in ps_cmd


def test_windows_no_raw_join_prevents_injection():
    """Verify args are NOT raw-joined (CVE: command injection via spaces)."""
    cmd = ["git", "log", "--format=%H %s"]
    ps_cmd = _executor("windows")._build_command(cmd)[-1]
    # Raw join would give: "git log --format=%H %s" — no quoting
    # Safe version wraps each arg in single quotes
    assert "'--format=%H %s'" in ps_cmd


# ── _quote_ps_arg helper ──────────────────────────────────────────────────────


def test_quote_ps_arg_plain():
    assert _quote_ps_arg("git") == "'git'"


def test_quote_ps_arg_with_spaces():
    assert _quote_ps_arg("my arg") == "'my arg'"


def test_quote_ps_arg_escapes_single_quote():
    assert _quote_ps_arg("it's") == "'it''s'"


def test_quote_ps_arg_empty_string():
    assert _quote_ps_arg("") == "''"
