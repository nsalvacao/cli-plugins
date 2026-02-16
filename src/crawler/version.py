"""CLI version detection and parsing."""

from __future__ import annotations

import logging
import re

from lib.cli_identity import canonical_cli_name

from .executor import Executor

logger = logging.getLogger("cli_crawler.version")

VERSION_TOKEN = r"\d+\.\d+(?:\.\d+)?(?:[-.\w]*)"
VERSION_KEYWORD_RE = re.compile(rf"version\s+v?({VERSION_TOKEN})", re.IGNORECASE)
LEADING_NAME_RE = re.compile(rf"^([A-Za-z][\w.+-]*)\s+({VERSION_TOKEN})(?:\s|$)")
AT_VERSION_RE = re.compile(rf"@({VERSION_TOKEN})")
HYPHENATED_NAME_RE = re.compile(rf"\b([A-Za-z][\w.+-]*)-({VERSION_TOKEN})\b")
STANDALONE_V_RE = re.compile(rf"\bv({VERSION_TOKEN})\b")
BARE_VERSION_RE = re.compile(rf"^({VERSION_TOKEN})\s*$")

VERSION_COMMANDS = ["--version", "-V", "version", "-v"]


def detect_version(cli_name: str, executor: Executor) -> str:
    """Try version commands, parse version string."""
    placeholder_version = ""
    for vcmd in VERSION_COMMANDS:
        cmd = [cli_name, vcmd] if vcmd != "version" else [cli_name, vcmd]
        result = executor.run(cmd, timeout=3)

        if result.exit_code == 0 or result.stdout.strip():
            text = result.stdout.strip()
            version = _parse_version(text, cli_name=cli_name)
            if version:
                if _is_placeholder_version(version):
                    placeholder_version = placeholder_version or version
                else:
                    logger.debug("Version for %s: %s (via %s)", cli_name, version, vcmd)
                    return version

        # Also check stderr (some CLIs output version there)
        if result.stderr.strip() and not result.stderr.startswith("TIMEOUT"):
            version = _parse_version(result.stderr.strip(), cli_name=cli_name)
            if version:
                if _is_placeholder_version(version):
                    placeholder_version = placeholder_version or version
                else:
                    return version

    if placeholder_version:
        logger.warning(
            "Detected placeholder version %s for %s; returning unknown version instead",
            placeholder_version,
            cli_name,
        )
        return ""

    logger.warning("Could not detect version for %s", cli_name)
    return ""


def _is_placeholder_version(version: str) -> bool:
    """Detect non-informative placeholder versions."""
    normalized = version.strip().lower()
    if not normalized:
        return True

    # "0", "0.0", "0.0.0", "0.0.0-dev", "0.0.0+unknown"
    if re.fullmatch(r"0(?:\.0+)*(?:[-+][\w.-]+)?", normalized):
        return True

    if normalized in {"unknown", "dev", "development", "snapshot", "nightly"}:
        return True

    return False


def _parse_version(text: str, cli_name: str | None = None) -> str:
    """Extract best version candidate from text.

    Preference order:
    1. Candidates strongly attributable to the target CLI.
    2. Generic version candidates.
    3. Dependency-style `<name>-<version>` fallback.
    """
    candidates = _collect_version_candidates(text, cli_name)
    if not candidates:
        return ""

    placeholder_candidate = ""
    for _score, version in sorted(candidates, key=lambda item: item[0], reverse=True):
        if _is_placeholder_version(version):
            placeholder_candidate = placeholder_candidate or version
            continue
        return version

    return placeholder_candidate


def _collect_version_candidates(text: str, cli_name: str | None) -> list[tuple[int, str]]:
    """Collect scored version candidates from text lines."""
    scored: dict[str, int] = {}
    mention_re = _build_cli_mention_re(cli_name)

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        line_mentions_cli = bool(mention_re and mention_re.search(line))
        has_structural_cli_version = _line_has_structural_cli_version(line, cli_name)
        has_foreign_version_subject = _line_has_foreign_version_subject(line, cli_name)
        has_foreign_subject = _line_has_foreign_subject(line, cli_name)

        if not has_foreign_version_subject:
            keyword_score = 220
            if line_mentions_cli:
                keyword_score = 300
            if has_structural_cli_version:
                keyword_score = 380
            _add_scored_match(
                scored,
                VERSION_KEYWORD_RE.search(line),
                score_if_match=keyword_score,
                group_index=1,
            )

        m = LEADING_NAME_RE.search(line)
        if m:
            source_name = m.group(1)
            if cli_name and not _is_cli_name_match(source_name, cli_name):
                continue
            score = 360 if _is_cli_name_match(source_name, cli_name) else 200
            _add_scored_value(scored, m.group(2), score)

        if not (has_foreign_subject and not line_mentions_cli and not has_structural_cli_version):
            for m in AT_VERSION_RE.finditer(line):
                score = 180
                if line_mentions_cli:
                    score = 280
                if has_structural_cli_version:
                    score = 340
                _add_scored_value(scored, m.group(1), score)

        if not (has_foreign_subject and not line_mentions_cli and not has_structural_cli_version):
            for m in STANDALONE_V_RE.finditer(line):
                score = 170
                if line_mentions_cli:
                    score = 250
                if has_structural_cli_version:
                    score = 360
                _add_scored_value(scored, m.group(1), score)

        _add_scored_match(
            scored,
            BARE_VERSION_RE.search(line),
            score_if_match=160,
            group_index=1,
        )

        for m in HYPHENATED_NAME_RE.finditer(line):
            source_name = m.group(1)
            score = 220 if _is_cli_name_match(source_name, cli_name) else 20
            _add_scored_value(scored, m.group(2), score)

    return [(score, version) for version, score in scored.items()]


def _add_scored_match(
    scored: dict[str, int],
    match: re.Match[str] | None,
    score_if_match: int,
    group_index: int,
) -> None:
    """Add regex match group to scored candidates map."""
    if not match:
        return
    _add_scored_value(scored, match.group(group_index), score_if_match)


def _add_scored_value(scored: dict[str, int], version: str, score: int) -> None:
    """Keep max score for each candidate version."""
    if not version:
        return
    current = scored.get(version)
    if current is None or score > current:
        scored[version] = score


def _build_cli_mention_re(cli_name: str | None) -> re.Pattern[str] | None:
    """Build regex that detects explicit CLI mentions in a line."""
    aliases = _cli_name_aliases(cli_name)
    if not aliases:
        return None
    escaped_aliases = sorted((re.escape(alias) for alias in aliases), key=len, reverse=True)
    joined = "|".join(escaped_aliases)
    return re.compile(rf"(?<![A-Za-z0-9_.+-])(?:{joined})(?![A-Za-z0-9_.+-])", re.IGNORECASE)


def _line_has_structural_cli_version(line: str, cli_name: str | None) -> bool:
    """Check if a line structurally looks like `<cli> version ...`."""
    for alias in _cli_name_aliases(cli_name):
        escaped = re.escape(alias)
        pattern = re.compile(
            rf"^\s*{escaped}(?![A-Za-z0-9_.+-])(?:\s+version\b|\s+v?\d|[@:/-]v?\d)",
            re.IGNORECASE,
        )
        if pattern.search(line):
            return True
    return False


def _cli_name_aliases(cli_name: str | None) -> tuple[str, ...]:
    """Return candidate aliases for a CLI identity (`git.exe`, `git`, path leaf)."""
    if not cli_name:
        return ()

    raw = (cli_name or "").strip().strip('"').strip("'")
    if not raw:
        return ()

    leaf = re.split(r"[\\/]", raw)[-1] or raw
    canonical = canonical_cli_name(raw)

    aliases: list[str] = []
    seen: set[str] = set()
    for candidate in (raw, leaf, canonical):
        normalized = candidate.strip().lower()
        if not normalized or normalized in seen:
            continue
        aliases.append(candidate.strip())
        seen.add(normalized)
    return tuple(aliases)


def _line_has_foreign_version_subject(line: str, cli_name: str | None) -> bool:
    """Detect `<other-tool> version ...` subjects that should not boost confidence."""
    if not cli_name:
        return False
    m = re.search(r"^\s*([A-Za-z][\w.+-]*)\s+version\b", line, re.IGNORECASE)
    if not m:
        return False
    return not _is_cli_name_match(m.group(1), cli_name)


def _line_has_foreign_subject(line: str, cli_name: str | None) -> bool:
    """Detect a foreign leading subject token in a line."""
    if not cli_name:
        return False
    m = re.search(r"^\s*([A-Za-z][\w.+-]*)", line)
    if not m:
        return False
    subject = m.group(1)
    if subject.lower() in {"version", "v"}:
        return False
    return not _is_cli_name_match(subject, cli_name)


def _is_cli_name_match(source_name: str, cli_name: str | None) -> bool:
    """Check whether parsed source name likely refers to the target CLI."""
    if not cli_name:
        return False

    source_norm = _normalize_cli_token(source_name)
    cli_norm = _normalize_cli_token(cli_name)
    if not source_norm or not cli_norm:
        return False

    if source_norm == cli_norm:
        return True

    # Numeric variants (python/python3, python3/python312).
    if source_norm.startswith(cli_norm) and source_norm[len(cli_norm) :].isdigit():
        return True
    if cli_norm.startswith(source_norm) and cli_norm[len(source_norm) :].isdigit():
        return True

    source_lower = source_name.lower()
    cli_lower = canonical_cli_name(cli_name) or cli_name.lower()
    cli_alias_suffixes = {"cli", "command", "tool"}
    for sep in ("-", "_", "."):
        if source_lower.startswith(f"{cli_lower}{sep}"):
            suffix = source_lower[len(cli_lower) + 1 :]
            if suffix in cli_alias_suffixes:
                return True

    return False


def _normalize_cli_token(value: str) -> str:
    """Normalize CLI token for loose comparisons."""
    canonical = canonical_cli_name(value)
    return re.sub(r"[^a-z0-9]+", "", canonical)
