"""Tests for subcommand list parsing across all format families."""

from crawler.parsers.commands import parse_command_section


class TestTabularFormat:
    def test_docker_commands(self):
        content = """  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers"""
        cmds = parse_command_section(content)
        assert len(cmds) == 3
        assert cmds[0].name == "run"
        assert "container" in cmds[0].description.lower()

    def test_plugin_marker(self):
        content = """  buildx*     Docker Buildx
  compose*    Docker Compose
  container   Manage containers"""
        cmds = parse_command_section(content)
        assert len(cmds) == 3
        plugins = [c for c in cmds if c.is_plugin]
        assert len(plugins) == 2
        assert plugins[0].name == "buildx"


class TestColonFormat:
    def test_gh_commands(self):
        content = """  auth:          Authenticate gh and git with GitHub
  browse:        Open repositories, issues, pull requests
  pr:            Work with GitHub pull requests"""
        cmds = parse_command_section(content)
        assert len(cmds) == 3
        assert cmds[0].name == "auth"

    def test_alias_detection(self):
        content = """  co:            Alias for "pr checkout" """
        cmds = parse_command_section(content)
        assert len(cmds) == 1
        assert cmds[0].is_alias
        assert cmds[0].alias_target == "pr checkout"


class TestCSVFormat:
    def test_npm_commands(self):
        content = """    access, adduser, audit, bugs, cache, ci, completion,
    config, dedupe, deprecate, diff, dist-tag, docs, doctor,"""
        cmds = parse_command_section(content)
        assert len(cmds) >= 10
        names = [c.name for c in cmds]
        assert "access" in names
        assert "audit" in names


class TestIntegration:
    def test_docker_help(self, docker_help):
        from crawler.parsers.sections import segment_help_text, SectionType
        sections = segment_help_text(docker_help)
        cmd_sections = [s for s in sections if s.type == SectionType.COMMANDS]
        all_cmds = []
        for section in cmd_sections:
            all_cmds.extend(parse_command_section(section.content, group=section.header))
        assert len(all_cmds) >= 20  # docker has many commands

    def test_git_help(self, git_help):
        from crawler.parsers.sections import segment_help_text, SectionType
        sections = segment_help_text(git_help)
        cmd_sections = [s for s in sections if s.type == SectionType.COMMANDS]
        all_cmds = []
        for section in cmd_sections:
            all_cmds.extend(parse_command_section(section.content, group=section.header))
        names = [c.name for c in all_cmds]
        assert "clone" in names
        assert "commit" in names
        assert "push" in names
