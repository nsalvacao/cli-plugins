"""Configuration loader with simple YAML subset parser (no dependencies)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class PluginConfig:
    discovery_command: str = ""


@dataclass
class CLIConfig:
    name: str
    timeout: int = 5
    max_depth: int = 5
    max_concurrent: int = 5
    retry: int = 1
    environment: str = "wsl"
    raw_threshold: int = 10000
    group: str | None = None
    help_pattern: str | None = None
    plugins: PluginConfig | None = None


@dataclass
class CrawlerConfig:
    defaults: CLIConfig = field(default_factory=lambda: CLIConfig(name="defaults"))
    clis: dict[str, CLIConfig] = field(default_factory=dict)


def load_config(path: str) -> CrawlerConfig:
    """Load config from YAML file."""
    text = Path(path).read_text(encoding="utf-8")
    raw = _parse_simple_yaml(text)
    return _build_config(raw)


def _build_config(raw: dict) -> CrawlerConfig:
    """Convert raw dict to typed CrawlerConfig."""
    defaults_raw = raw.get("defaults", {})
    defaults = CLIConfig(
        name="defaults",
        timeout=int(defaults_raw.get("timeout", 5)),
        max_depth=int(defaults_raw.get("max_depth", 5)),
        max_concurrent=int(defaults_raw.get("max_concurrent", 5)),
        retry=int(defaults_raw.get("retry", 1)),
        environment=str(defaults_raw.get("environment", "wsl")),
        raw_threshold=int(defaults_raw.get("raw_threshold", 10000)),
    )

    clis = {}
    for cli_name, cli_raw in raw.get("clis", {}).items():
        if not isinstance(cli_raw, dict):
            cli_raw = {}
        plugins = None
        if "plugins" in cli_raw and isinstance(cli_raw["plugins"], dict):
            plugins = PluginConfig(
                discovery_command=cli_raw["plugins"].get("discovery_command", "")
            )
        clis[cli_name] = CLIConfig(
            name=cli_name,
            timeout=int(cli_raw.get("timeout", defaults.timeout)),
            max_depth=int(cli_raw.get("max_depth", defaults.max_depth)),
            max_concurrent=int(cli_raw.get("max_concurrent", defaults.max_concurrent)),
            retry=int(cli_raw.get("retry", defaults.retry)),
            environment=str(cli_raw.get("environment", defaults.environment)),
            raw_threshold=int(cli_raw.get("raw_threshold", defaults.raw_threshold)),
            group=cli_raw.get("group"),
            help_pattern=cli_raw.get("help_pattern"),
            plugins=plugins,
        )

    return CrawlerConfig(defaults=defaults, clis=clis)


def _parse_simple_yaml(text: str) -> dict:
    """Parse a simple YAML subset: scalars, nested dicts (2-space indent), comments.

    Supports only the subset needed for config.yaml:
    - key: value (string, int, bool scalars)
    - Nested dicts via indentation (2-space)
    - # comments
    - No anchors, refs, flow syntax, lists, or multi-line strings
    """
    result: dict = {}
    stack: list[tuple[int, dict]] = [(-1, result)]
    lines = text.splitlines()

    for line in lines:
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(stripped)

        # Pop stack to find parent at correct indentation
        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()

        match = re.match(r"^(\S[\w\-.*]*)\s*:\s*(.*?)(?:\s*#.*)?$", stripped)
        if not match:
            continue

        key = match.group(1)
        value_str = match.group(2).strip()

        parent = stack[-1][1]

        if value_str:
            # Scalar value
            parent[key] = _parse_scalar(value_str)
        else:
            # Nested dict
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))

    return result


def _parse_scalar(value: str) -> str | int | float | bool:
    """Parse a YAML scalar value."""
    # Remove surrounding quotes
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]

    # Booleans
    if value.lower() in ("true", "yes", "on"):
        return True
    if value.lower() in ("false", "no", "off"):
        return False

    # Numbers
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass

    return value
