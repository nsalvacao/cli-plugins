"""Basic crawler smoke tests (T009)."""

from __future__ import annotations

from crawler.config import CLIConfig
from crawler.pipeline import crawl_cli


def test_git_initial_crawl_root_help(tmp_path) -> None:
    """Initial crawl should parse git root help without crashing."""
    output_path = tmp_path / "git.json"
    config = CLIConfig(name="git", timeout=5, max_depth=1, max_concurrent=2)

    cli_map = crawl_cli("git", config, output_path=output_path, include_raw=False, strict=False)

    assert cli_map.cli_name == "git"
    assert output_path.exists()
    assert int(cli_map.metadata.get("total_commands", "0")) >= 10
    assert cli_map.metadata.get("help_pattern") in {"--help", "-h", "help", "bare"}
