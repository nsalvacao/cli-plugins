"""Usage line extraction from help output."""

from __future__ import annotations

import re

from ..models import Flag

# Usage line patterns
USAGE_PREFIX_RE = re.compile(
    r"^\s*(?:usage|Usage|USAGE)\s*:?\s*(.+)$",
    re.IGNORECASE,
)

USAGE_CONTINUATION_RE = re.compile(r"^\s{4,}\S")
OPTION_LINE_START_RE = re.compile(r"^\s*-(?:-|[A-Za-z0-9])")
LONG_OPTION_RE = re.compile(r"--[\w][\w-]*")
DESC_SPLIT_RE = re.compile(r"\s{2,}|\s:\s|\t+")
DESCRIPTION_CONTINUATION_RE = re.compile(r"^\s+\S")
PLACEHOLDER_DESC_SPLIT_RE = re.compile(r"^(?P<spec>.+?[>\]])\s+(?P<desc>.+)$")


def parse_usage(content: str) -> str:
    """Extract usage pattern from a USAGE section content."""
    lines = content.splitlines()
    parts: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if parts:
                break
            continue

        if not parts:
            # First non-empty line is the usage pattern
            parts.append(stripped)
        elif USAGE_CONTINUATION_RE.match(line):
            # Continuation line (indented)
            parts.append(stripped)
        else:
            break

    return " ".join(parts) if parts else ""


def extract_usage_from_text(text: str, cli_name: str) -> str:
    """Find usage line anywhere in text (for CLIs that put it at top)."""
    for line in text.splitlines():
        m = USAGE_PREFIX_RE.match(line)
        if m:
            usage = m.group(1).strip()
            if usage:
                return usage
    return ""


def extract_usage_line_options(text: str) -> list[Flag]:
    """Extract options from sectionless help formats (e.g., python3-style)."""
    flags: list[Flag] = []
    lines = text.splitlines()

    for idx, line in enumerate(lines):
        if not OPTION_LINE_START_RE.match(line):
            continue

        stripped = line.strip()
        if not stripped:
            continue

        spec, desc = _split_option_spec_and_description(stripped)
        if not desc:
            desc = _extract_continuation_description(lines, idx)

        tokens = _extract_option_tokens(spec)
        if not tokens:
            continue

        long_tokens = [t for t in tokens if t.startswith("--")]
        short_tokens = [t for t in tokens if t.startswith("-") and not t.startswith("--")]
        primary_long = long_tokens[0] if long_tokens else None
        primary_short = short_tokens[0] if short_tokens else None
        primary_name = primary_long or primary_short
        if not primary_name:
            continue

        value_hint = _extract_value_hint(spec, primary_name)
        choices = _extract_choices_from_hint(value_hint)
        flag_type = "string" if value_hint else "bool"

        flags.append(
            Flag(
                name=primary_name,
                long_name=primary_long,
                short_name=primary_short,
                type=flag_type,
                choices=choices,
                description=desc,
                confidence=0.55,
            )
        )

    return flags


def _extract_value_hint(spec: str, primary_name: str) -> str | None:
    """Extract value hint from option spec fragment."""
    # Attached value encoded in primary token itself (e.g., -Xlint:all, -DNAME=VALUE, -O2).
    compact = primary_name[1:] if primary_name.startswith("-") else primary_name
    if ":" in compact:
        suffix = compact.split(":", 1)[1].strip()
        if suffix:
            return suffix
    if "=" in compact:
        suffix = compact.split("=", 1)[1].strip()
        if suffix:
            return suffix
    if len(compact) > 1 and compact[0].isalnum() and compact[1:].isdigit():
        return compact[1:]

    # Explicit placeholders.
    placeholder_match = re.search(r"<([^>]+)>|\[([^\]]+)\]", spec)
    if placeholder_match:
        return (placeholder_match.group(1) or placeholder_match.group(2) or "").strip()

    # Pattern: `-c cmd`, `--flag value`
    remainder = re.sub(
        rf"^.*?{re.escape(primary_name)}\s*",
        "",
        spec,
        count=1,
    ).strip()
    if remainder.startswith(":"):
        remainder = remainder[1:].strip()
    if not remainder:
        return None

    token = remainder.split()[0].strip(":;,")
    if not token or token.startswith("-"):
        return None
    if not re.search(r"[A-Za-z0-9_<\[]", token):
        return None
    return token


def _extract_choices_from_hint(value_hint: str | None) -> list[str] | None:
    """Extract choice list from value hint token."""
    if not value_hint or "|" not in value_hint:
        return None
    values = [p.strip("[]<>(),:") for p in value_hint.split("|")]
    values = [v for v in values if v]
    return values or None


def _normalize_option_description(raw: str) -> str:
    """Normalize fallback option descriptions from sectionless help lines."""
    desc = (raw or "").strip()
    if not desc:
        return ""

    # Remove noisy leading separators often seen in python-style help.
    desc = re.sub(r"^[\s:;\-–—]+", "", desc).strip()
    desc = re.sub(r"\s+", " ", desc)
    return desc


def _split_option_spec_and_description(stripped: str) -> tuple[str, str]:
    """Split a sectionless option line into spec and description."""
    parts = DESC_SPLIT_RE.split(stripped, maxsplit=1)
    if len(parts) > 1:
        spec, desc = _rebalance_alias_split(parts[0].strip(), parts[1].strip())
        return spec, _normalize_option_description(desc)

    spec, desc, matched = _split_colon_description_outside_placeholders(stripped)
    if matched:
        return spec, _normalize_option_description(desc)

    m = PLACEHOLDER_DESC_SPLIT_RE.match(stripped)
    if m:
        spec = m.group("spec").strip()
        if _extract_option_tokens(spec):
            return spec, _normalize_option_description(m.group("desc"))

    return stripped, ""


def _extract_continuation_description(lines: list[str], option_index: int) -> str:
    """Extract description from continuation lines below an option row."""
    descriptions: list[str] = []

    for line in lines[option_index + 1 :]:
        stripped = line.strip()
        if not stripped:
            break
        if OPTION_LINE_START_RE.match(line):
            break
        if not DESCRIPTION_CONTINUATION_RE.match(line):
            break

        normalized = _normalize_option_description(stripped)
        if normalized:
            descriptions.append(normalized)

    return " ".join(descriptions).strip()


def _split_colon_description_outside_placeholders(
    stripped: str,
) -> tuple[str, str, bool]:
    """Split `spec: description` while ignoring colons inside `<...>` or `[...]`."""
    angle_depth = 0
    square_depth = 0

    for idx, ch in enumerate(stripped):
        if ch == "<":
            angle_depth += 1
        elif ch == ">" and angle_depth > 0:
            angle_depth -= 1
        elif ch == "[":
            square_depth += 1
        elif ch == "]" and square_depth > 0:
            square_depth -= 1
        elif ch == ":" and angle_depth == 0 and square_depth == 0:
            next_char = stripped[idx + 1 : idx + 2]
            if next_char and not next_char.isspace():
                continue
            spec = stripped[:idx].strip()
            if not spec or not _extract_option_tokens(spec):
                continue
            desc = stripped[idx + 1 :].strip()
            return spec, desc, True

    return "", "", False


def _rebalance_alias_split(spec: str, desc: str) -> tuple[str, str]:
    """Rebalance early column split for `-x,  --long ...` sectionless lines."""
    existing_tokens = _extract_option_tokens(spec)
    if any(token.startswith("--") for token in existing_tokens):
        return spec, desc

    short_tokens = [t for t in existing_tokens if t.startswith("-") and not t.startswith("--")]
    if not short_tokens:
        return spec, desc

    candidate = desc.lstrip()
    if not candidate.startswith("--"):
        return spec, desc

    tokens = candidate.split()
    if not tokens or not LONG_OPTION_RE.match(tokens[0]):
        return spec, desc

    consumed = 1
    if len(tokens) > 1 and _looks_like_option_value_token(tokens[1]):
        consumed += 1

    merged_spec = " ".join([spec, *tokens[:consumed]]).strip()
    merged_desc = " ".join(tokens[consumed:]).strip()
    if not merged_desc:
        merged_desc = desc

    return merged_spec, merged_desc


def _extract_option_tokens(spec: str) -> list[str]:
    """Extract deterministic option tokens from sectionless option specs."""
    tokens: list[str] = []

    for match in LONG_OPTION_RE.finditer(spec):
        tokens.append(match.group(0))

    for fragment in re.split(r"[,\s]+", spec):
        short_token = _normalize_short_option_fragment(fragment)
        if short_token:
            tokens.append(short_token)

    # Stable de-duplication while preserving first-seen order.
    seen: set[str] = set()
    result: list[str] = []
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        result.append(token)
    return result


def _normalize_short_option_fragment(fragment: str) -> str | None:
    """Normalize short-option fragments, including attached and combined forms."""
    token = (fragment or "").strip().strip(",;")
    if not token or token.startswith("--") or not token.startswith("-"):
        return None

    body = token[1:]
    if not body or not body[0].isalnum():
        return None

    if len(body) == 1:
        return f"-{body}"

    # Lowercase alpha clusters are treated as combined short shorthand (e.g., -abc).
    if body.isalpha() and body.islower() and len(body) <= 3:
        return f"-{body}"

    # Keep multi-letter option names intact to avoid collisions (-help, -classpath).
    if body.isalpha() and len(body) > 1:
        return f"-{body}"

    # Attached value forms map to canonical short (e.g., -O2 -> -O, -DNAME=VALUE -> -D).
    if "=" in body:
        return f"-{body[0]}"
    if len(body) > 1 and body[1:].isdigit():
        return f"-{body[0]}"

    # Extended forms with non-alpha payload keep full token for deterministic behavior.
    if ":" in body:
        return f"-{body}"

    # Fallback to canonical short.
    return f"-{body[0]}"


def _looks_like_option_value_token(token: str) -> bool:
    """Detect value-hint tokens that are part of an option spec."""
    if not token:
        return False

    if token.startswith("<") or token.startswith("["):
        return True

    if "|" in token:
        return True

    value_keywords = {
        "arg",
        "args",
        "bool",
        "boolean",
        "category",
        "count",
        "file",
        "float",
        "int",
        "integer",
        "name",
        "number",
        "path",
        "string",
        "url",
        "value",
    }
    lowered = token.lower().strip(":,;")
    if lowered in value_keywords:
        return True

    return token.isupper() and len(token) > 1
