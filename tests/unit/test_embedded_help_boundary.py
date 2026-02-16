"""Unit tests for embedded-help boundary filtering (T089)."""

from __future__ import annotations

from crawler.parser import parse_help_output


def test_parser_ignores_foreign_embedded_help_block() -> None:
    help_text = """
usage: yq [options] <jq filter> [input file...]

options:
  -h, --help         show this help message and exit
  --yaml-output      emit YAML
  --yq-native-flag   yq-only option

jq - commandline JSON processor [version 1.7]
Usage: jq [options] <jq filter> [file...]
  --jq-only-flag     embedded jq flag that must be ignored
  --version          jq version
"""

    result = parse_help_output(help_text, "yq", "yq")
    names = [flag.name for flag in result.command.flags]

    assert "--yq-native-flag" in names
    assert "--jq-only-flag" not in names
    assert any("Embedded help boundary" in w for w in result.warnings)
