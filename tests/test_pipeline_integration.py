"""Integration tests: full pipeline on golden files."""

import json
from pathlib import Path

from crawler.parser import parse_help_output
from crawler.parsers.manpage import is_manpage


class TestFullParse:
    def test_parse_git_root(self, git_help):
        result = parse_help_output(git_help, "git", "git")
        assert len(result.subcommand_names) >= 15
        assert "commit" in result.subcommand_names
        assert "push" in result.subcommand_names
        assert "clone" in result.subcommand_names

    def test_parse_docker_root(self, docker_help):
        result = parse_help_output(docker_help, "docker", "docker")
        assert len(result.subcommand_names) >= 20
        assert "run" in result.subcommand_names
        assert "container" in result.subcommand_names

    def test_parse_gh_root(self, gh_help):
        result = parse_help_output(gh_help, "gh", "gh")
        assert len(result.subcommand_names) >= 10
        assert "pr" in result.subcommand_names
        assert "issue" in result.subcommand_names
        assert result.command.examples  # gh has examples

    def test_parse_npm_root(self, npm_help):
        result = parse_help_output(npm_help, "npm", "npm")
        assert len(result.subcommand_names) >= 30  # npm has 60+ commands

    def test_parse_uv_root(self, uv_help):
        result = parse_help_output(uv_help, "uv", "uv")
        assert len(result.subcommand_names) >= 5
        assert "run" in result.subcommand_names
        assert result.command.flags  # uv has global options

    def test_parse_git_commit_manpage(self, git_commit_help):
        assert is_manpage(git_commit_help)
        result = parse_help_output(git_commit_help, "git", "git commit", force_manpage=True)
        assert result.command.flags
        assert result.command.description

    def test_parse_docker_run(self, docker_run_help):
        result = parse_help_output(docker_run_help, "docker", "docker run")
        assert result.command.flags
        assert len(result.command.flags) >= 20  # docker run has many flags

    def test_parse_npm_install(self, npm_install_help):
        result = parse_help_output(npm_install_help, "npm", "npm install")
        assert result.command.flags  # bracket-style flags

    def test_parse_claude_flow(self, claude_flow_help):
        result = parse_help_output(claude_flow_help, "claude-flow", "claude-flow")
        assert len(result.subcommand_names) >= 5
        assert result.command.examples  # claude-flow has examples

    def test_parse_langchain_root(self, langchain_help):
        result = parse_help_output(langchain_help, "langchain", "langchain")
        assert len(result.subcommand_names) >= 4
        assert "app" in result.subcommand_names
        assert "serve" in result.subcommand_names
        assert "template" in result.subcommand_names

    def test_parse_langchain_app_new(self, langchain_app_new_help):
        result = parse_help_output(langchain_app_new_help, "langchain", "langchain app new")
        assert result.command.flags
        names = [f.name for f in result.command.flags]
        assert "--package" in names
        assert "--pip" in names
        assert result.command.positional_args  # has [NAME] arg
        assert result.command.description
        assert "usage:" not in result.command.description.lower()

    def test_parse_langchain_serve(self, langchain_serve_help):
        result = parse_help_output(langchain_serve_help, "langchain", "langchain serve")
        assert result.command.flags
        names = [f.name for f in result.command.flags]
        assert "--port" in names
        assert "--host" in names


class TestOutputSchema:
    def test_json_output_exists(self):
        """Verify output files from previous e2e runs."""
        output_dir = Path("output")
        if not output_dir.exists():
            return  # skip if no output
        for f in output_dir.glob("*.json"):
            if f.name.endswith(".raw.json"):
                continue
            data = json.loads(f.read_text(encoding="utf-8"))
            # Verify required top-level keys
            assert "cli_name" in data
            assert "cli_version" in data
            assert "metadata" in data
            assert "commands" in data

            # Verify meta structure
            meta = data["metadata"]
            assert "scanned_at" in meta
            assert "help_pattern" in meta
            assert "total_commands" in meta
            assert "total_flags" in meta
            assert "duration_seconds" in meta
