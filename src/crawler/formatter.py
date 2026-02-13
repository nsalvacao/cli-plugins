"""JSON output generation with raw file separation."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from .config import CLIConfig
from .models import CLIMap, Command, EnvVar, Flag, PositionalArg

logger = logging.getLogger("cli_crawler.formatter")


def write_output(
    cli_map: CLIMap,
    raw_outputs: dict[str, str],
    output_path: Path,
    config: CLIConfig,
    include_raw: bool = False,
) -> None:
    """Write main JSON and optionally separate raw JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Serialize main JSON
    data = serialize_cli_map(cli_map)

    # Handle raw text
    if include_raw:
        # Embed raw text in each command node
        _embed_raw(data.get("tree", {}), raw_outputs, cli_map.cli_name)
    elif raw_outputs:
        total_raw = sum(len(v) for v in raw_outputs.values())
        if total_raw > config.raw_threshold:
            # Write separate raw file
            raw_path = output_path.with_suffix(".raw.json")
            raw_data = {path: text for path, text in sorted(raw_outputs.items())}
            raw_path.write_text(
                json.dumps(raw_data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            data["raw_file"] = raw_path.name
            logger.info("Raw text written to %s (%d bytes)", raw_path, total_raw)

    # Write main JSON
    output_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info("Output written to %s", output_path)


def serialize_cli_map(cli_map: CLIMap) -> dict[str, Any]:
    """Serialize CLIMap to dict for JSON output."""
    return {
        "cli_name": cli_map.cli_name,
        "cli_version": cli_map.cli_version,
        "metadata": cli_map.metadata,
        "global_flags": [
            _serialize_flag(f) for f in sorted(cli_map.global_flags, key=lambda f: f.name)
        ],
        "environment_variables": [
            _serialize_envvar(e) for e in sorted(cli_map.environment_variables, key=lambda e: e.name)
        ],
        "commands": {name: _serialize_command(cmd) for name, cmd in sorted(cli_map.commands.items())},
    }


def _serialize_command(cmd: Command) -> dict[str, Any]:
    """Recursive serialization of Command tree."""
    data: dict[str, Any] = {
        "path": cmd.path,
        "description": cmd.description,
    }

    # Only include non-empty/non-default fields (token efficiency)
    if cmd.usage_pattern:
        data["usage_pattern"] = cmd.usage_pattern
    if cmd.aliases:
        data["aliases"] = cmd.aliases
    if cmd.group:
        data["group"] = cmd.group
    if cmd.deprecated:
        data["deprecated"] = True
    if cmd.hidden:
        data["hidden"] = True
    if cmd.dynamic:
        data["dynamic"] = True
    if cmd.positional_args:
        data["positional_args"] = [_serialize_positional_arg(a) for a in cmd.positional_args]
    if cmd.flags:
        data["flags"] = [_serialize_flag(f) for f in sorted(cmd.flags, key=lambda f: f.name)]
    if cmd.env_vars:
        data["env_vars"] = [
            _serialize_envvar(e) for e in sorted(cmd.env_vars, key=lambda e: e.name)
        ]
    if cmd.examples:
        data["examples"] = cmd.examples
    if not cmd.global_flags_inherited:
        data["global_flags_inherited"] = False
    if cmd.subcommands:
        data["subcommands"] = {
            name: _serialize_command(sub) for name, sub in sorted(cmd.subcommands.items())
        }

    data["confidence"] = round(cmd.confidence, 2)

    return data


def _serialize_flag(flag: Flag) -> dict[str, Any]:
    """Serialize flag with token-efficient output."""
    data: dict[str, Any] = {"name": flag.name}

    if flag.short_name:
        data["short"] = flag.short_name
    if flag.long_name:
        data["long"] = flag.long_name
    data["type"] = flag.type
    if flag.required:
        data["required"] = True
    if flag.default is not None:
        data["default"] = flag.default
    if flag.choices:
        data["choices"] = flag.choices
    if flag.description:
        data["description"] = flag.description

    data["confidence"] = round(flag.confidence, 2)

    return data


def _serialize_positional_arg(arg: PositionalArg) -> dict[str, Any]:
    data: dict[str, Any] = {"name": arg.name}
    if arg.required:
        data["required"] = True
    if arg.description:
        data["description"] = arg.description
    return data


def _serialize_envvar(ev: EnvVar) -> dict[str, Any]:
    data: dict[str, Any] = {"name": ev.name}
    if ev.description:
        data["description"] = ev.description
    return data





def _embed_raw(tree: dict, raw_outputs: dict[str, str], cli_name: str) -> None:
    """Embed raw help text into each command node in the tree."""
    for name, cmd_data in tree.items():
        path = cmd_data.get("path", "")
        if path in raw_outputs:
            cmd_data["raw_help"] = raw_outputs[path]
        if "subcommands" in cmd_data:
            _embed_raw(cmd_data["subcommands"], raw_outputs, cli_name)
