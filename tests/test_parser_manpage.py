"""Tests for man page parser."""

from crawler.parsers.manpage import is_manpage, parse_manpage


class TestManpageDetection:
    def test_detect_git_manpage(self, git_commit_help):
        assert is_manpage(git_commit_help)

    def test_not_manpage_docker(self, docker_help):
        assert not is_manpage(docker_help)

    def test_not_manpage_gh(self, gh_help):
        assert not is_manpage(gh_help)


class TestManpageParsing:
    def test_git_commit_description(self, git_commit_help):
        cmd, warnings = parse_manpage(git_commit_help, "git", "git commit")
        assert cmd.path == "git commit"
        assert "record" in cmd.description.lower() or "commit" in cmd.description.lower()

    def test_git_commit_flags(self, git_commit_help):
        cmd, _ = parse_manpage(git_commit_help, "git", "git commit")
        assert len(cmd.flags) > 10
        flag_names = [f.name for f in cmd.flags]
        assert "--amend" in flag_names or "--message" in flag_names or "--all" in flag_names

    def test_git_commit_usage(self, git_commit_help):
        cmd, _ = parse_manpage(git_commit_help, "git", "git commit")
        assert cmd.usage_pattern  # should have SYNOPSIS

    def test_confidence(self, git_commit_help):
        cmd, _ = parse_manpage(git_commit_help, "git", "git commit")
        assert cmd.confidence >= 0.60

    def test_npm_style_examples_are_extracted(self):
        manpage_text = """NPM-INSTALL(1)                   npm manual                   NPM-INSTALL(1)

NAME
       npm-install - Install a package

SYNOPSIS
       npm install [<package-spec> ...]

EXAMPLES
       npm install
           Install dependencies from package.json.

       $ npm install sax
           Install the sax package.

       For more information, see npm help install.
"""

        cmd, _ = parse_manpage(manpage_text, "npm", "npm install")
        assert "npm install" in cmd.examples
        assert "npm install sax" in cmd.examples
        assert all(not ex.lower().startswith("for more information") for ex in cmd.examples)
        assert all(
            "install dependencies from package.json." not in ex.lower() for ex in cmd.examples
        )

    def test_examples_with_left_aligned_prose_still_extract_commands(self):
        manpage_text = """TOOL(1)                      user manual                     TOOL(1)

NAME
       tool - Demo tool

SYNOPSIS
       tool [OPTIONS]

EXAMPLES
This section shows practical usage.
       tool run --fast
           Run quickly.
       $ tool check
           Validate current project.
"""

        cmd, _ = parse_manpage(manpage_text, "tool", "tool")
        assert "tool run --fast" in cmd.examples
        assert "tool check" in cmd.examples
