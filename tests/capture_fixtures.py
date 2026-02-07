#!/usr/bin/env python3
"""Capture golden files from live CLIs for testing."""

import os
import subprocess
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent / "fixtures"

SAFE_ENV = {
    **os.environ,
    "NO_COLOR": "1",
    "PAGER": "cat",
    "TERM": "dumb",
    "LANG": "C",
    "LC_ALL": "C",
    "GIT_PAGER": "cat",
    "MANPAGER": "cat",
    "MANWIDTH": "120",
}

CAPTURES = {
    "git": {
        "help.txt": ["git", "--help"],
        "commit_help.txt": ["git", "commit", "--help"],
        "commit_h.txt": ["git", "commit", "-h"],
        "version.txt": ["git", "--version"],
    },
    "docker": {
        "help.txt": ["docker", "--help"],
        "container_help.txt": ["docker", "container", "--help"],
        "run_help.txt": ["docker", "run", "--help"],
        "version.txt": ["docker", "--version"],
    },
    "gh": {
        "help.txt": ["gh", "--help"],
        "pr_help.txt": ["gh", "pr", "--help"],
        "pr_create_help.txt": ["gh", "pr", "create", "--help"],
        "version.txt": ["gh", "--version"],
    },
    "npm": {
        "help.txt": ["npm", "--help"],
        "install_help.txt": ["npm", "install", "--help"],
        "version.txt": ["npm", "--version"],
    },
    "uv": {
        "help.txt": ["uv", "--help"],
        "pip_help.txt": ["uv", "pip", "--help"],
        "pip_install_help.txt": ["uv", "pip", "install", "--help"],
        "version.txt": ["uv", "--version"],
    },
    "pip": {
        "help.txt": ["pip", "--help"],
        "install_help.txt": ["pip", "install", "--help"],
        "version.txt": ["pip", "--version"],
    },
    "claude-flow": {
        "help.txt": ["npx", "claude-flow", "--help"],
        "agent_help.txt": ["npx", "claude-flow", "agent", "--help"],
        "version.txt": ["npx", "claude-flow", "--version"],
    },
}


def capture_all():
    for cli, files in CAPTURES.items():
        cli_dir = FIXTURES_DIR / cli
        cli_dir.mkdir(parents=True, exist_ok=True)
        for filename, cmd in files.items():
            filepath = cli_dir / filename
            print(f"Capturing: {' '.join(cmd)} -> {filepath}")
            try:
                result = subprocess.run(
                    cmd, capture_output=True, text=True,
                    timeout=10, env=SAFE_ENV,
                    encoding="utf-8", errors="replace",
                )
                text = result.stdout
                if not text.strip() and result.stderr.strip():
                    text = result.stderr
                filepath.write_text(text, encoding="utf-8")
            except (subprocess.TimeoutExpired, FileNotFoundError) as e:
                print(f"  SKIP: {e}")


if __name__ == "__main__":
    capture_all()
    print("Done!")
