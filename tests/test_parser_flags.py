"""Tests for flag/option parsing across all format families."""

from crawler.parsers.flags import parse_flags_section, _extract_choices, _extract_default


class TestFlagParsing:
    def test_standard_flag(self):
        flags = parse_flags_section("  -m, --message <msg>    commit message")
        assert len(flags) == 1
        assert flags[0].name == "--message"
        assert flags[0].short == "-m"
        assert flags[0].type == "string"

    def test_boolean_flag(self):
        flags = parse_flags_section("  -D, --debug    Enable debug mode")
        assert len(flags) == 1
        assert flags[0].name == "--debug"
        assert flags[0].type == "bool"

    def test_long_only_flag(self):
        flags = parse_flags_section("      --config string      Location of client config files")
        assert len(flags) == 1
        assert flags[0].name == "--config"
        assert flags[0].type == "string"

    def test_negatable_flag(self):
        flags = parse_flags_section("      --[no-]verify    Run hooks")
        assert len(flags) == 1
        assert "--[no-]verify" in flags[0].name

    def test_npm_bracket_flags(self):
        flags = parse_flags_section("[-S|--save|--no-save|--save-prod]")
        assert len(flags) >= 2
        names = [f.name for f in flags]
        assert "--save" in names
        assert "--no-save" in names

    def test_npm_bracket_with_value(self):
        flags = parse_flags_section("[--install-strategy <hoisted|nested|shallow|linked>]")
        assert len(flags) == 1
        assert flags[0].name == "--install-strategy"
        assert flags[0].choices == ["hoisted", "nested", "shallow", "linked"]

    def test_multiple_flags(self):
        content = """  -v, --verbose    Give more output
  -q, --quiet      Give less output
      --no-color   Suppress colored output"""
        flags = parse_flags_section(content)
        assert len(flags) == 3

    def test_docker_run_flags(self, docker_run_help):
        from crawler.parsers.sections import segment_help_text, SectionType
        sections = segment_help_text(docker_run_help)
        flag_sections = [s for s in sections if s.type == SectionType.FLAGS]
        if flag_sections:
            flags = parse_flags_section(flag_sections[0].content)
            assert len(flags) > 10  # docker run has many flags

    def test_gh_flags(self, gh_help):
        from crawler.parsers.sections import segment_help_text, SectionType
        sections = segment_help_text(gh_help)
        flag_sections = [s for s in sections if s.type == SectionType.FLAGS]
        if flag_sections:
            flags = parse_flags_section(flag_sections[0].content)
            names = [f.name for f in flags]
            assert "--help" in names or "--version" in names


class TestChoicesExtraction:
    def test_possible_values(self):
        choices = _extract_choices("[possible values: auto, always, never]")
        assert choices == ["auto", "always", "never"]

    def test_pipe_choices(self):
        choices = _extract_choices("Format: json|yaml|text")
        assert choices == ["json", "yaml", "text"]

    def test_no_choices(self):
        assert _extract_choices("Just a regular description") is None


class TestRichClickFormat:
    def test_reversed_long_short(self):
        flags = parse_flags_section("  --version  -v        Print the current CLI version.")
        assert len(flags) == 1
        assert flags[0].name == "--version"
        assert flags[0].short == "-v"
        assert flags[0].type == "bool"

    def test_negatable_pair(self):
        flags = parse_flags_section("  --pip                --no-pip               Pip install the template(s)")
        assert len(flags) == 1
        assert flags[0].name == "--pip"
        assert flags[0].type == "bool"

    def test_uppercase_type_integer(self):
        flags = parse_flags_section("  --port        INTEGER  The port to run the server on")
        assert len(flags) == 1
        assert flags[0].name == "--port"
        assert flags[0].type == "string"  # v1: non-bool = string

    def test_uppercase_type_text(self):
        flags = parse_flags_section("  --host        TEXT     The host to run the server on")
        assert len(flags) == 1
        assert flags[0].name == "--host"
        assert flags[0].type == "string"

    def test_langchain_serve_flags(self, langchain_serve_help):
        from crawler.parsers.sections import segment_help_text, SectionType
        sections = segment_help_text(langchain_serve_help)
        flag_sections = [s for s in sections if s.type == SectionType.FLAGS]
        assert flag_sections
        flags = parse_flags_section(flag_sections[0].content)
        names = [f.name for f in flags]
        assert "--port" in names
        assert "--host" in names
        assert "--help" in names


class TestDefaultExtraction:
    def test_default_quoted(self):
        assert _extract_default('(default "info")') == "info"

    def test_default_number(self):
        assert _extract_default("(default: 5)") == "5"

    def test_no_default(self):
        assert _extract_default("No default here") is None
