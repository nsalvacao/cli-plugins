"""Environment variable extraction from help output."""

from __future__ import annotations

import re

from ..models import EnvVar

# Inline in flag descriptions: [env: UV_NO_CACHE=]
ENV_INLINE_RE = re.compile(r"\[env:\s*([A-Z_][A-Z0-9_]*)=?\]")

# Dedicated section entry: GIT_DIR    description
ENV_SECTION_RE = re.compile(
    r"^\s*\$?([A-Z][A-Z0-9_]{2,})\s{2,}(.+)$"
)

# Env var mentioned in text
ENV_MENTION_RE = re.compile(r"\b([A-Z][A-Z0-9_]{2,})\b")


def parse_envvar_section(content: str) -> list[EnvVar]:
    """Parse a dedicated ENVIRONMENT section."""
    env_vars: list[EnvVar] = []
    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        m = ENV_SECTION_RE.match(line)
        if m:
            name = m.group(1)
            desc = m.group(2).strip()
            env_vars.append(EnvVar(name=name, description=desc))

    return env_vars


def extract_envvars_from_text(text: str) -> list[EnvVar]:
    """Extract env vars mentioned inline in text (e.g., flag descriptions)."""
    env_vars: list[EnvVar] = []
    seen: set[str] = set()

    for m in ENV_INLINE_RE.finditer(text):
        name = m.group(1)
        if name not in seen:
            seen.add(name)
            env_vars.append(EnvVar(name=name))

    return env_vars
