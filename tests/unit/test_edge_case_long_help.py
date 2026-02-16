"""Unit test for EC-05: huge help output triggers progressive loading."""

from __future__ import annotations

from pathlib import Path

from crawler.config import CLIConfig
from crawler.models import Command, ExecutionResult, HelpDetectionResult, ParseResult
from crawler.pipeline import crawl_cli


def test_long_help_activates_progressive_loading(monkeypatch, tmp_path: Path) -> None:
    cli_name = "huge-cli"
    threshold = 10_000
    long_help = "\n".join(
        ["Usage: huge-cli [OPTIONS] COMMAND"] + [f"line {i}" for i in range(12_050)]
    )

    detection = HelpDetectionResult(
        pattern="--help",
        result=ExecutionResult(
            stdout=long_help,
            stderr="",
            exit_code=0,
            command=[cli_name, "--help"],
        ),
    )

    seen: dict[str, int] = {}

    def _fake_parse(text: str, _cli: str, command_path: str, force_manpage: bool = False) -> ParseResult:
        del force_manpage
        seen["parsed_lines"] = len(text.splitlines())
        return ParseResult(
            command=Command(
                path=command_path,
                name=command_path.split()[-1],
                description="parsed from progressive chunk",
                confidence=0.8,
            ),
            warnings=[],
        )

    monkeypatch.setattr("crawler.pipeline.detect_version", lambda *_args, **_kwargs: "1.0.0")
    monkeypatch.setattr("crawler.pipeline.detect_help_pattern", lambda *_args, **_kwargs: detection)
    monkeypatch.setattr("crawler.pipeline.parse_help_output", _fake_parse)
    monkeypatch.setattr(
        "crawler.pipeline.discover_and_crawl",
        lambda *_args, **_kwargs: {},
    )

    cli_map = crawl_cli(
        cli_name,
        CLIConfig(name=cli_name, raw_threshold=threshold),
        output_path=tmp_path / f"{cli_name}.json",
        strict=False,
    )

    assert cli_map.metadata.get("progressive_loading") == "true"
    assert cli_map.metadata.get("raw_line_count") == str(len(long_help.splitlines()))
    assert cli_map.metadata.get("parsed_line_count") == str(threshold)
    # +2 allows the truncation note/footer lines added by the pipeline wrapper.
    assert seen["parsed_lines"] <= threshold + 2
