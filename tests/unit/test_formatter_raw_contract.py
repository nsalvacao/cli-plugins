"""Regression coverage for formatter raw-output contract."""

from __future__ import annotations

import json

from crawler.config import CLIConfig
from crawler.formatter import write_output
from crawler.models import CLIMap, Command


def test_write_output_with_raw_flag_embeds_raw_help_in_commands(tmp_path) -> None:
    """`--raw` must inline raw text into command nodes instead of sidecar output."""
    cli_map = CLIMap(
        cli_name="tool",
        commands={
            "alpha": Command(
                path="tool alpha",
                name="alpha",
                subcommands={
                    "beta": Command(path="tool alpha beta", name="beta"),
                },
            ),
        },
    )
    raw_outputs = {
        "tool alpha": "alpha raw help",
        "tool alpha beta": "beta raw help",
    }
    output_path = tmp_path / "tool.json"

    write_output(
        cli_map=cli_map,
        raw_outputs=raw_outputs,
        output_path=output_path,
        _config=CLIConfig(name="tool"),
        include_raw=True,
    )

    payload = json.loads(output_path.read_text(encoding="utf-8"))
    alpha = payload["commands"]["alpha"]
    beta = alpha["subcommands"]["beta"]

    assert alpha["raw_help"] == "alpha raw help"
    assert beta["raw_help"] == "beta raw help"
    assert "raw_file" not in payload
    assert not output_path.with_suffix(".raw.json").exists()
