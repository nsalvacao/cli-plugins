"""Unit tests for embedded-help flag deduplication (T082)."""

from __future__ import annotations

from crawler.parser import parse_help_output


def test_embedded_help_deduplicates_help_and_version_flags() -> None:
    help_text = """
Usage: yq [options] <jq filter> [files ...]

Options:
  -h, --help      show this help message and exit
  --version       show program's version number and exit
  --yaml-output   emit YAML output

jq - commandline JSON processor [version 1.7]
Usage: jq [options] <jq filter> [file...]
  --help          show jq help
  --version       show jq version
"""

    result = parse_help_output(help_text, "yq", "yq")
    names = [flag.name for flag in result.command.flags]

    assert names.count("--help") == 1
    assert names.count("--version") == 1
    assert "--yaml-output" in names

    help_flag = next(flag for flag in result.command.flags if flag.name == "--help")
    assert help_flag.short_name == "-h"
