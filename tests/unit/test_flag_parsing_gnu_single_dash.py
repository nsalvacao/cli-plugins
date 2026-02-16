"""Unit tests for GNU single-dash long-option parsing (T118)."""

from __future__ import annotations

from crawler.parsers.flags import parse_flags_section


def test_parse_gnu_single_dash_long_options_and_pass_through_families() -> None:
    content = """
  -print-file-name=<lib>   Display the full path to library <lib>.
  -dumpmachine             Display the compiler's target processor.
  -Wa,<options>            Pass comma-separated <options> on to the assembler.
  -Wp,<options>            Pass comma-separated <options> on to the preprocessor.
  -Wl,<options>            Pass comma-separated <options> on to the linker.
  -Xassembler <arg>        Pass <arg> on to the assembler.
  -Xpreprocessor <arg>     Pass <arg> on to the preprocessor.
  -Xlinker <arg>           Pass <arg> on to the linker.
  -std=<standard>          Assume that the input sources are for <standard>.
"""
    flags = parse_flags_section(content)
    by_name = {flag.name: flag for flag in flags}

    assert "-print-file-name" in by_name
    assert by_name["-print-file-name"].type == "string"
    assert by_name["-print-file-name"].description.startswith("Display the full path")

    assert "-dumpmachine" in by_name
    assert by_name["-dumpmachine"].type == "bool"

    assert "-Wa" in by_name
    assert by_name["-Wa"].type == "string"
    assert by_name["-Wa"].description.startswith("Pass comma-separated")

    assert "-Wp" in by_name
    assert by_name["-Wp"].type == "string"

    assert "-Wl" in by_name
    assert by_name["-Wl"].type == "string"

    assert "-Xassembler" in by_name
    assert by_name["-Xassembler"].type == "string"

    assert "-Xpreprocessor" in by_name
    assert by_name["-Xpreprocessor"].type == "string"

    assert "-Xlinker" in by_name
    assert by_name["-Xlinker"].type == "string"

    assert "-std" in by_name
    assert by_name["-std"].type == "string"


def test_parse_gnu_single_dash_preserves_bool_and_one_letter_value_forms() -> None:
    content = """
  -pipe                    Use pipes rather than intermediate files.
  -save-temps              Do not delete intermediate files.
  -L dir                   Add dir to include search path.
  -l library               Link against library.
"""
    flags = parse_flags_section(content)
    by_name = {flag.name: flag for flag in flags}

    assert by_name["-pipe"].type == "bool"
    assert by_name["-save-temps"].type == "bool"
    assert by_name["-L"].type == "string"
    assert by_name["-l"].type == "string"
