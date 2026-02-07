"""Help pattern detection: determines how a CLI exposes its help."""

from __future__ import annotations

import logging
import re

from .config import CLIConfig
from .executor import Executor
from .models import HelpDetectionResult, ExecutionResult
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


def detect_help_pattern(
    cli_name: str,
    executor: Executor,
    config: CLIConfig,
) -> HelpDetectionResult:
    """Try help patterns in order, return first that produces usable output."""

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

    return HelpDetectionResult(
        pattern="unknown",
        result=ExecutionResult(
            stdout="", stderr="No help output found",
            exit_code=-1, command=[cli_name],
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

    # Primary: append help pattern
    if help_pattern not in ("bare", "unknown"):
        cmd = base_cmd + [help_pattern]
        result = executor.run_with_retry(cmd)
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern=help_pattern,
                result=result,
                is_manpage=is_manpage(result.stdout),
            )

    # Fallback: try -h (git subcommands prefer this for compact output)
    if help_pattern != "-h":
        cmd = base_cmd + ["-h"]
        result = executor.run_with_retry(cmd)
        if _is_help_output(result.stdout):
            return HelpDetectionResult(
                pattern="-h",
                result=result,
                is_manpage=is_manpage(result.stdout),
            )

    # Fallback: help subcmd pattern
    cmd = [cli_name, "help"] + subcommand_path
    result = executor.run_with_retry(cmd)
    if _is_help_output(result.stdout):
        return HelpDetectionResult(
            pattern="help",
            result=result,
            is_manpage=is_manpage(result.stdout),
        )

    # Last resort: bare subcommand
    result = executor.run(base_cmd, timeout=2)
    if _is_help_output(result.stdout):
        return HelpDetectionResult(
            pattern="bare",
            result=result,
            is_manpage=is_manpage(result.stdout),
        )

    return HelpDetectionResult(
        pattern="unknown",
        result=result,
    )


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
