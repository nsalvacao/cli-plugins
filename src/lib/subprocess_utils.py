"""Shared subprocess utilities: safe execution, no shell=True, SAFE_ENV.

This module provides a standalone subprocess wrapper for code outside
the crawler package. The crawler uses ``src/crawler/executor.py`` (which
has richer config, retry, and ANSI-stripping); this module is a simpler,
config-free alternative for generator and lib code.
"""

from __future__ import annotations

import logging
import os
import subprocess
import time
from typing import NamedTuple

logger = logging.getLogger(__name__)

# Environment overrides that suppress colour output and interactive pagers,
# ensuring deterministic text output across all platforms.
# NOTE: ``src/crawler/executor.py`` defines an equivalent SAFE_ENV for crawler
# use.  If you add or remove keys here, update executor.py accordingly.
SAFE_ENV: dict[str, str] = {
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


class SubprocessResult(NamedTuple):
    """Return value of :func:`run_safe`."""

    exit_code: int
    stdout: str
    stderr: str
    timed_out: bool = False
    duration: float = 0.0


def run_safe(
    cmd: list[str],
    timeout: int = 30,
    extra_env: dict[str, str] | None = None,
) -> SubprocessResult:
    """Execute *cmd* safely.

    Rules enforced:
    - ``cmd`` MUST be a non-empty list (never a shell string).
    - ``shell=False`` always — no shell interpretation of metacharacters.
    - SAFE_ENV merged with ``os.environ`` to suppress colour and pagers.
    - UTF-8 encoding with ``errors="replace"`` for robustness.
    - Timeout converts to a structured error result (does not raise).

    Args:
        cmd: Command and arguments as a list.  Must not be empty.
        timeout: Seconds before the process is killed.
        extra_env: Additional env vars merged on top of SAFE_ENV.

    Returns:
        :class:`SubprocessResult` with exit_code, stdout, stderr, timed_out, duration.

    Raises:
        ValueError: If *cmd* is empty.
    """
    if not cmd:
        raise ValueError("cmd must be a non-empty list of strings")

    env = {**os.environ, **SAFE_ENV, **(extra_env or {})}
    start = time.monotonic()

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            encoding="utf-8",
            errors="replace",
        )
        duration = time.monotonic() - start
        return SubprocessResult(
            exit_code=proc.returncode,
            stdout=proc.stdout or "",
            stderr=proc.stderr or "",
            duration=duration,
        )

    except subprocess.TimeoutExpired:
        duration = time.monotonic() - start
        logger.warning("Timeout after %.1fs: %s", duration, cmd[0])
        return SubprocessResult(
            exit_code=-1,
            stdout="",
            stderr=f"TIMEOUT after {timeout}s",
            timed_out=True,
            duration=duration,
        )

    except FileNotFoundError:
        duration = time.monotonic() - start
        logger.debug("Command not found: %s", cmd[0])
        return SubprocessResult(
            exit_code=-1,
            stdout="",
            stderr=f"Command not found: {cmd[0]}",
            duration=duration,
        )

    except OSError as e:
        duration = time.monotonic() - start
        logger.debug("OS error running %s: %s", cmd[0], e)
        return SubprocessResult(
            exit_code=-1,
            stdout="",
            stderr=str(e),
            duration=duration,
        )
