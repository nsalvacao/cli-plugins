"""Helpers for canonical CLI identity across OS-specific executable names."""

from __future__ import annotations

import re

WINDOWS_EXECUTABLE_SUFFIXES = (
    ".exe",
    ".cmd",
    ".bat",
    ".com",
    ".ps1",
    ".psm1",
)


def canonical_cli_name(cli_name: str) -> str:
    """Return canonical CLI identity (e.g. ``git.exe`` -> ``git``)."""
    value = (cli_name or "").strip().strip('"').strip("'")
    if not value:
        return ""

    # Keep only the executable leaf if a full path is provided.
    leaf = re.split(r"[\\/]", value)[-1] or value
    lower_leaf = leaf.lower()

    for suffix in WINDOWS_EXECUTABLE_SUFFIXES:
        if lower_leaf.endswith(suffix) and len(leaf) > len(suffix):
            leaf = leaf[: -len(suffix)]
            break

    return leaf.lower().strip()


def plugin_slug(cli_name: str) -> str:
    """Return deterministic plugin slug from canonical CLI identity."""
    canonical = canonical_cli_name(cli_name)
    base = canonical or (cli_name or "").strip().lower()
    slug = re.sub(r"\s+", "-", base)
    slug = re.sub(r"[^a-z0-9+._-]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "unknown-cli"
