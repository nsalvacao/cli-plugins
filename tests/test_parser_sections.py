"""Tests for section header detection and text segmentation."""

from crawler.parsers.sections import segment_help_text, detect_section_type, SectionType


class TestDetectSectionType:
    def test_all_caps_commands(self):
        assert detect_section_type("COMMANDS") == SectionType.COMMANDS
        assert detect_section_type("CORE COMMANDS") == SectionType.COMMANDS

    def test_title_case_commands(self):
        assert detect_section_type("Commands:") == SectionType.COMMANDS
        assert detect_section_type("Common Commands:") == SectionType.COMMANDS

    def test_all_caps_flags(self):
        assert detect_section_type("FLAGS") == SectionType.FLAGS
        assert detect_section_type("OPTIONS") == SectionType.FLAGS

    def test_global_flags(self):
        assert detect_section_type("GLOBAL FLAGS") == SectionType.GLOBAL_FLAGS
        assert detect_section_type("Global Options:") == SectionType.GLOBAL_FLAGS

    def test_inherited_flags(self):
        assert detect_section_type("INHERITED FLAGS") == SectionType.INHERITED_FLAGS

    def test_usage(self):
        assert detect_section_type("USAGE") == SectionType.USAGE
        assert detect_section_type("Usage:") == SectionType.USAGE

    def test_examples(self):
        assert detect_section_type("EXAMPLES") == SectionType.EXAMPLES
        assert detect_section_type("Examples:") == SectionType.EXAMPLES

    def test_all_commands(self):
        assert detect_section_type("All commands:") == SectionType.COMMANDS

    def test_git_prose_at_col0(self):
        assert detect_section_type("start a working area (see also: git help tutorial)") == SectionType.COMMANDS

    def test_indented_line_not_section(self):
        # Indented lines should NOT match git prose patterns
        assert detect_section_type("   clone     Clone a repository") is None

    def test_none_for_regular_text(self):
        assert detect_section_type("This is just a description") is None
        assert detect_section_type("") is None


class TestSegmentHelpText:
    def test_docker_sections(self, docker_help):
        sections = segment_help_text(docker_help)
        types = [s.type for s in sections]
        assert SectionType.COMMANDS in types
        # Docker has multiple command sections
        cmd_sections = [s for s in sections if s.type == SectionType.COMMANDS]
        assert len(cmd_sections) >= 2  # Common Commands + Management Commands + ...

    def test_gh_sections(self, gh_help):
        sections = segment_help_text(gh_help)
        types = [s.type for s in sections]
        assert SectionType.COMMANDS in types
        assert SectionType.FLAGS in types
        assert SectionType.EXAMPLES in types

    def test_git_sections(self, git_help):
        sections = segment_help_text(git_help)
        cmd_sections = [s for s in sections if s.type == SectionType.COMMANDS]
        assert len(cmd_sections) >= 3  # Multiple prose categories

    def test_npm_sections(self, npm_help):
        sections = segment_help_text(npm_help)
        types = [s.type for s in sections]
        assert SectionType.COMMANDS in types  # "All commands:"

    def test_uv_sections(self, uv_help):
        sections = segment_help_text(uv_help)
        types = [s.type for s in sections]
        assert SectionType.COMMANDS in types
        # uv has multiple flag sections (Cache options, Python options, Global options)
        flag_sections = [s for s in sections if s.type in (SectionType.FLAGS, SectionType.GLOBAL_FLAGS)]
        assert len(flag_sections) >= 2

    def test_git_manpage(self, git_commit_help):
        from crawler.parsers.manpage import is_manpage
        assert is_manpage(git_commit_help)

    def test_richclick_box_stripping(self, langchain_help):
        sections = segment_help_text(langchain_help)
        types = [s.type for s in sections]
        assert SectionType.COMMANDS in types
        assert SectionType.FLAGS in types

    def test_richclick_arguments_section(self, langchain_app_new_help):
        sections = segment_help_text(langchain_app_new_help)
        types = [s.type for s in sections]
        assert SectionType.ARGUMENTS in types
        assert SectionType.FLAGS in types
