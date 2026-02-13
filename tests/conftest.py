"""Shared fixtures and golden file loader."""

from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_fixture(cli: str, name: str) -> str:
    path = FIXTURES_DIR / cli / name
    if not path.exists():
        pytest.skip(f"Fixture not found: {path}")
    return path.read_text(encoding="utf-8")


@pytest.fixture
def git_help():
    return load_fixture("git", "help.txt")


@pytest.fixture
def git_commit_help():
    return load_fixture("git", "commit_help.txt")


@pytest.fixture
def git_commit_h():
    return load_fixture("git", "commit_h.txt")


@pytest.fixture
def docker_help():
    return load_fixture("docker", "help.txt")


@pytest.fixture
def docker_run_help():
    return load_fixture("docker", "run_help.txt")


@pytest.fixture
def gh_help():
    return load_fixture("gh", "help.txt")


@pytest.fixture
def gh_pr_help():
    return load_fixture("gh", "pr_help.txt")


@pytest.fixture
def npm_help():
    return load_fixture("npm", "help.txt")


@pytest.fixture
def npm_install_help():
    return load_fixture("npm", "install_help.txt")


@pytest.fixture
def uv_help():
    return load_fixture("uv", "help.txt")


@pytest.fixture
def uv_pip_install_help():
    return load_fixture("uv", "pip_install_help.txt")


@pytest.fixture
def pip_help():
    return load_fixture("pip", "help.txt")


@pytest.fixture
def claude_flow_help():
    return load_fixture("claude-flow", "help.txt")


@pytest.fixture
def langchain_help():
    return load_fixture("langchain", "help.txt")


@pytest.fixture
def langchain_app_new_help():
    return load_fixture("langchain", "app_new_help.txt")


@pytest.fixture
def langchain_serve_help():
    return load_fixture("langchain", "serve_help.txt")
