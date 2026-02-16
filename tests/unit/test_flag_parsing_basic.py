"""Basic flag parsing tests (T010)."""

from __future__ import annotations

from crawler.parsers.flags import parse_flags_section


def test_parse_standard_and_short_flags() -> None:
    content = """
  -m, --message <msg>    Commit message
  --amend                Amend previous commit
"""
    flags = parse_flags_section(content)
    names = {f.name for f in flags}

    assert "--message" in names
    assert "--amend" in names
    msg = next(f for f in flags if f.name == "--message")
    assert msg.short_name == "-m"
    assert msg.type == "string"


def test_parse_bool_flag_type_inference() -> None:
    content = """
  -v, --verbose          Enable verbose output
"""
    flags = parse_flags_section(content)
    assert len(flags) == 1
    assert flags[0].name == "--verbose"
    assert flags[0].type == "bool"
