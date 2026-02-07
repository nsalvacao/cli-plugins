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
