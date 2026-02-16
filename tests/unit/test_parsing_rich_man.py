"""Rich-Click and manpage parsing quality tests (T012)."""

from __future__ import annotations

import re

from crawler.parser import parse_help_output
from crawler.parsers.manpage import parse_manpage


def _richclick_expected_flag_lines(text: str) -> int:
    """Approximate count of rich-click option lines containing long flags."""
    return sum(1 for line in text.splitlines() if re.search(r"\|\s*--[\w-]+", line))


def test_richclick_extraction_rate_above_half(
    langchain_help,
    langchain_app_new_help,
    langchain_serve_help,
) -> None:
    fixtures = [
        ("langchain", "langchain", langchain_help),
        ("langchain", "langchain app new", langchain_app_new_help),
        ("langchain", "langchain serve", langchain_serve_help),
    ]

    extracted_total = 0
    expected_total = 0

    for cli_name, command_path, text in fixtures:
        result = parse_help_output(text, cli_name, command_path)
        extracted_total += len(result.command.flags)
        expected_total += _richclick_expected_flag_lines(text)

    assert expected_total > 0
    assert extracted_total / expected_total >= 0.5


def test_manpage_examples_extracted_for_npm_style_content() -> None:
    text = """NPM-INSTALL(1)                   npm manual                   NPM-INSTALL(1)

NAME
       npm-install - Install a package

SYNOPSIS
       npm install [<package-spec> ...]

EXAMPLES
       npm install
           Install dependencies from package.json.

       $ npm install sax
           Install the sax package.
"""
    cmd, _ = parse_manpage(text, "npm", "npm install")
    assert "npm install" in cmd.examples
    assert "npm install sax" in cmd.examples
