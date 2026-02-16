"""Unit tests for sectionless usage-line option extraction (T091)."""

from __future__ import annotations

from crawler.parser import parse_help_output


def test_sectionless_python_style_help_recovers_representative_flags() -> None:
    help_text = """
usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...

Options and arguments (and corresponding environment variables):
-b     issue warnings about str(bytes_instance), str(bytearray_instance)
-B     don't write .pyc files on import
-c cmd : program passed in as string
-m mod : run library module as script
--check-hash-based-pycs always|default|never : control how Python invalidates hash-based .pyc files
--version : print the Python version number and exit
"""

    result = parse_help_output(help_text, "python3", "python3")
    names = [flag.name for flag in result.command.flags]

    assert "-b" in names
    assert "-c" in names
    assert "-m" in names
    assert "--check-hash-based-pycs" in names
    assert "--version" in names
    assert len(result.command.flags) >= 5


def test_sectionless_fallback_normalizes_leading_colon_in_descriptions() -> None:
    help_text = """
usage: python [option] ...

Options and arguments (and corresponding environment variables):
-B     : don't write .pyc files on import
-E     : ignore PYTHON* environment variables
--version : print the Python version number and exit
"""

    result = parse_help_output(help_text, "python", "python")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert by_name["-B"].description.startswith("don't write")
    assert not by_name["-B"].description.startswith(":")
    assert by_name["-E"].description.startswith("ignore PYTHON")
    assert not by_name["-E"].description.startswith(":")


def test_sectionless_fallback_enriches_long_options_from_colon_style_lines() -> None:
    help_text = """
usage: python3 [option] ... [--help-env] [--help-all]

Options and arguments (and corresponding environment variables):
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env: print help about Python environment variables and exit
--help-all: print complete help information and exit
"""

    result = parse_help_output(help_text, "python3", "python3")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert by_name["--help-env"].description.startswith("print help about Python")
    assert by_name["--help-all"].description.startswith("print complete help")
    assert by_name["--help-env"].type == "bool"
    assert by_name["--help-all"].type == "bool"

    check_hash = by_name["--check-hash-based-pycs"]
    assert check_hash.description.startswith("control how Python invalidates")
    assert check_hash.choices == ["always", "default", "never"]


def test_sectionless_fallback_does_not_split_placeholder_colon_as_description() -> None:
    help_text = """
Usage: curl [options...] <url>
 -u, --user <user:password> Server user and password
"""

    result = parse_help_output(help_text, "curl", "curl")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert by_name["--user"].description == "Server user and password"
    assert by_name["--user"].type == "string"


def test_sectionless_fallback_handles_aligned_short_long_alias_columns() -> None:
    help_text = """
Usage: curl [options...] <url>
 -u,  --user <user:password>  Server user and password
"""

    result = parse_help_output(help_text, "curl", "curl")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert "--user" in by_name
    assert by_name["--user"].short_name == "-u"
    assert by_name["--user"].description == "Server user and password"


def test_sectionless_fallback_parses_attached_and_combined_short_forms() -> None:
    help_text = """
Usage: tool [options]
 -DNAME=VALUE          define a key-value pair
 -Xlint:all            enable all lint warnings
 -O2                   set optimization level 2
 -abc                  enable combined shorthand flags
"""

    result = parse_help_output(help_text, "tool", "tool")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert "-D" in by_name
    assert by_name["-D"].type == "string"
    assert by_name["-D"].description.startswith("define a key-value pair")

    x_flag = by_name.get("-Xlint:all") or by_name.get("-X")
    assert x_flag is not None
    assert x_flag.type == "string"
    assert x_flag.description.startswith("enable all lint warnings")

    assert "-O" in by_name
    assert by_name["-O"].type == "string"
    assert by_name["-O"].description.startswith("set optimization level 2")

    assert "-abc" in by_name
    assert by_name["-abc"].type == "bool"
    assert by_name["-abc"].description.startswith("enable combined shorthand flags")


def test_sectionless_fallback_keeps_word_like_short_tokens_without_collapsing() -> None:
    help_text = """
Usage: java [options]
 -help                 print help
 -classpath <path>     set class search path
"""

    result = parse_help_output(help_text, "java", "java")
    by_name = {flag.name: flag for flag in result.command.flags}

    assert "-help" in by_name
    assert "-classpath" in by_name
    assert "-h" not in by_name
    assert "-c" not in by_name
