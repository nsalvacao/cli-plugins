"""Help pattern detection: determines how a CLI exposes its help."""

from __future__ import annotations

import logging
import re

from .config import CLIConfig
from .executor import Executor, format_auth_required_error, is_auth_required_failure
from .models import ExecutionResult, HelpDetectionResult
from .parsers.manpage import is_manpage

logger = logging.getLogger("cli_crawler.detector")

# Help invocation sequence (safety-ordered)
HELP_SEQUENCE = [
    ("--help", []),
    ("-h", []),
    ("help", []),
    (None, []),  # bare invocation
]

# Keywords that indicate help output
HELP_KEYWORDS = re.compile(
    r"\b(usage|options|commands|flags|help|available|arguments|synopsis)\b",
    re.IGNORECASE,
)

SAFE_BARE_FALLBACK_SUBCOMMANDS = {
    "help",
    "version",
    "--version",
    "-v",
}

MUTATING_SUBCOMMAND_TOKENS = {
    "add",
    "apply",
    "branch",
    "checkout",
    "cherry-pick",
    "clean",
    "clone",
    "commit",
    "init",
    "merge",
    "mv",
    "pull",
    "push",
    "rebase",
    "reset",
    "restore",
    "rm",
    "stash",
    "switch",
    "tag",
}


def detect_help_pattern(
    cli_name: str,
    executor: Executor,
    config: CLIConfig,
) -> HelpDetectionResult:
    """Try help patterns in order, return first that produces usable output."""
    auth_result: HelpDetectionResult | None = None

    # If config has a help_pattern override, try it first
    if config.help_pattern:
        cmd = [cli_name, config.help_pattern]
        result = executor.run_with_retry(cmd)
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern=config.help_pattern,
                result=result,
                is_manpage=is_manpage(result.stdout),
            )
        if is_auth_required_failure(result) and auth_result is None:
            auth_result = _auth_required_result(cli_name, result)

    best_result: HelpDetectionResult | None = None

    for pattern_name, extra_args in HELP_SEQUENCE:
        if pattern_name:
            cmd = [cli_name, pattern_name] + extra_args
        else:
            cmd = [cli_name]

        # Use shorter timeout for bare invocation (might hang)
        timeout = 2 if pattern_name is None else None
        result = executor.run_with_retry(cmd, timeout=timeout)

        if _is_help_output(result.stdout):
            pattern_label = pattern_name or "bare"
            logger.debug("Help detected for %s via %s", cli_name, pattern_label)
            return HelpDetectionResult(
                pattern=pattern_label,
                result=result,
                is_manpage=is_manpage(result.stdout),
            )
        if is_auth_required_failure(result) and auth_result is None:
            auth_result = _auth_required_result(cli_name, result)

        # Keep track of best non-empty result as fallback
        if result.stdout.strip() and not best_result:
            pattern_label = pattern_name or "bare"
            best_result = HelpDetectionResult(
                pattern=pattern_label,
                result=result,
                is_manpage=is_manpage(result.stdout),
            )

    # Return best available or empty
    if best_result:
        logger.warning("No clear help output for %s, using best guess", cli_name)
        return best_result
    if auth_result:
        return auth_result

    return HelpDetectionResult(
        pattern="unknown",
        result=ExecutionResult(
            stdout="",
            stderr="No help output found",
            exit_code=-1,
            command=[cli_name],
        ),
    )


def detect_subcommand_help(
    cli_name: str,
    subcommand_path: list[str],
    executor: Executor,
    help_pattern: str,
) -> HelpDetectionResult:
    """Get help for a specific subcommand."""
    # Build command: cli_name subcmd1 subcmd2 --help
    base_cmd = [cli_name] + subcommand_path
    auth_result: HelpDetectionResult | None = None
    last_result = ExecutionResult(
        stdout="",
        stderr="",
        exit_code=1,
        command=base_cmd,
    )

    # Primary: append help pattern
    if help_pattern not in ("bare", "unknown"):
        cmd = base_cmd + [help_pattern]
        result = executor.run_with_retry(cmd)
        last_result = result
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern=help_pattern,
                result=result,
                is_manpage=is_manpage(result.stdout),
            )
        if is_auth_required_failure(result) and auth_result is None:
            auth_result = _auth_required_result(" ".join(base_cmd), result)

    # Fallback: try -h (git subcommands prefer this for compact output)
    if help_pattern != "-h":
        cmd = base_cmd + ["-h"]
        result = executor.run_with_retry(cmd)
        last_result = result
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern="-h",
                result=result,
                is_manpage=is_manpage(result.stdout),
            )
        if is_auth_required_failure(result) and auth_result is None:
            auth_result = _auth_required_result(" ".join(base_cmd), result)

    # Fallback: help subcmd pattern
    cmd = [cli_name, "help"] + subcommand_path
    result = executor.run_with_retry(cmd)
    last_result = result
    if _is_help_output(result.stdout):
        return HelpDetectionResult(
            pattern="help",
            result=result,
            is_manpage=is_manpage(result.stdout),
        )
    if is_auth_required_failure(result) and auth_result is None:
        auth_result = _auth_required_result(" ".join(base_cmd), result)

    # Last resort: bare subcommand (only for explicitly safe paths).
    if _should_try_bare_subcommand_fallback(subcommand_path):
        result = executor.run(base_cmd, timeout=2)
        last_result = result
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern="bare",
                result=result,
                is_manpage=is_manpage(result.stdout),
            )
        if is_auth_required_failure(result):
            auth_result = auth_result or _auth_required_result(" ".join(base_cmd), result)
    else:
        safety_warning = (
            "SAFETY_GUARD: Bare subcommand fallback skipped for potentially "
            f"mutating command '{' '.join(base_cmd)}'."
        )
        logger.warning("%s", safety_warning)
        if auth_result:
            return auth_result
        stderr_parts = [last_result.stderr.strip(), safety_warning]
        stderr = " | ".join(part for part in stderr_parts if part)
        return HelpDetectionResult(
            pattern="unknown",
            result=ExecutionResult(
                stdout="",
                stderr=stderr,
                exit_code=last_result.exit_code,
                command=last_result.command,
                timed_out=last_result.timed_out,
                duration=last_result.duration,
            ),
            is_manpage=False,
        )

    if auth_result:
        return auth_result

    return HelpDetectionResult(
        pattern="unknown",
        result=last_result,
    )


def _should_try_bare_subcommand_fallback(subcommand_path: list[str]) -> bool:
    """Gate bare subcommand fallback to explicitly safe, non-mutating paths."""
    tokens = [_normalize_subcommand_token(token) for token in subcommand_path if token.strip()]
    if not tokens:
        return False

    if tokens[0] == "help":
        return True

    if any(token in MUTATING_SUBCOMMAND_TOKENS for token in tokens):
        return False

    return all(token in SAFE_BARE_FALLBACK_SUBCOMMANDS for token in tokens)


def _normalize_subcommand_token(token: str) -> str:
    """Normalize a subcommand token for safety checks."""
    return token.strip().lower()


def _is_help_output(text: str) -> bool:
    """Heuristic: does this text look like help output?"""
    if not text or len(text.strip()) < 20:
        return False

    lines = text.strip().splitlines()
    if len(lines) < 3:
        return False

    # Count help-related keywords
    keyword_count = len(HELP_KEYWORDS.findall(text[:2000]))
    return keyword_count >= 2


def _auth_required_result(command_hint: str, result: ExecutionResult) -> HelpDetectionResult:
    """Build a structured auth-required detection result."""
    return HelpDetectionResult(
        pattern="auth_required",
        result=ExecutionResult(
            stdout="",
            stderr=format_auth_required_error(command_hint),
            exit_code=result.exit_code or 1,
            command=result.command,
            timed_out=result.timed_out,
            duration=result.duration,
        ),
        is_manpage=False,
    )
