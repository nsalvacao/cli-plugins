"""Command execution with env vars, timeout, retry, ANSI stripping, cross-OS."""

from __future__ import annotations

import logging
import os
import re
import subprocess
import time

from .config import CLIConfig
from .models import ExecutionResult

logger = logging.getLogger("cli_crawler.executor")

ANSI_RE = re.compile(r"\[[0-9;]*[a-zA-Z]|\][^]*|\[.*?[@-~]")


def _quote_ps_arg(arg: str) -> str:
    """Single-quote a PowerShell argument, escaping embedded single quotes as ''.

    PowerShell single-quoted strings are literal — no variable or command
    substitution occurs, which prevents injection via special characters.
    Embedded single quotes are escaped by doubling them (PowerShell convention).
    """
    return "'" + arg.replace("'", "''") + "'"


SAFE_ENV = {
    "NO_COLOR": "1",
    "PAGER": "cat",
    "TERM": "dumb",
    "LANG": "C",
    "LC_ALL": "C",
    "GIT_PAGER": "cat",
    "MANPAGER": "cat",
    "MANWIDTH": "120",
    "COLUMNS": "120",
}


class Executor:
    """Execute CLI commands with safety guards."""

    def __init__(self, config: CLIConfig):
        self.config = config

    def run(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        """Execute command, merge stderr, strip ANSI, handle timeout."""
        actual_cmd = self._build_command(command)
        env = self._build_env()
        effective_timeout = timeout or self.config.timeout

        logger.debug("Running: %s (timeout=%ds)", " ".join(actual_cmd), effective_timeout)
        start = time.monotonic()

        try:
            proc = subprocess.run(
                actual_cmd,
                capture_output=True,
                text=True,
                timeout=effective_timeout,
                env=env,
                encoding="utf-8",
                errors="replace",
            )
            duration = time.monotonic() - start
            stdout = self._strip_ansi(proc.stdout or "")
            stderr = self._strip_ansi(proc.stderr or "")

            # Merge stderr into stdout if stdout is empty but stderr has content
            if not stdout.strip() and stderr.strip():
                stdout = stderr

            return ExecutionResult(
                stdout=stdout,
                stderr=stderr,
                exit_code=proc.returncode,
                command=command,
                duration=duration,
            )

        except subprocess.TimeoutExpired:
            duration = time.monotonic() - start
            logger.warning("Timeout after %.1fs: %s", duration, " ".join(command))
            return ExecutionResult(
                stdout="",
                stderr=f"TIMEOUT after {effective_timeout}s",
                exit_code=-1,
                command=command,
                timed_out=True,
                duration=duration,
            )

        except FileNotFoundError:
            duration = time.monotonic() - start
            logger.warning("Command not found: %s", command[0])
            return ExecutionResult(
                stdout="",
                stderr=f"Command not found: {command[0]}",
                exit_code=-1,
                command=command,
                duration=duration,
            )

        except OSError as e:
            duration = time.monotonic() - start
            logger.warning("OS error running %s: %s", command[0], e)
            return ExecutionResult(
                stdout="",
                stderr=str(e),
                exit_code=-1,
                command=command,
                duration=duration,
            )

    def run_with_retry(self, command: list[str], timeout: int | None = None) -> ExecutionResult:
        """Run with retry logic (only retries on timeout)."""
        result = self.run(command, timeout)
        if result.timed_out and self.config.retry > 0:
            logger.info("Retrying after timeout: %s", " ".join(command))
            time.sleep(2)  # backoff
            result = self.run(command, timeout)
        return result

    def _build_command(self, command: list[str]) -> list[str]:
        """Wrap in powershell.exe for Windows environment, with safe quoting.

        Uses the PowerShell '&' call operator with individually single-quoted
        arguments to prevent command injection via spaces or special characters
        in argument values.
        """
        if self.config.environment == "windows":
            quoted_args = " ".join(_quote_ps_arg(a) for a in command)
            ps_cmd = f"& {quoted_args}"
            return [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                ps_cmd,
            ]
        return command

    def _build_env(self) -> dict[str, str]:
        """Merge SAFE_ENV with current environment."""
        env = os.environ.copy()
        env.update(SAFE_ENV)
        return env

    def _strip_ansi(self, text: str) -> str:
        """Remove ANSI escape codes and BOM."""
        text = text.lstrip("\ufeff")  # strip BOM
        return ANSI_RE.sub("", text)
