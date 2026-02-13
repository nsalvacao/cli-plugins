# AGENTS.md — AI Developer Guidelines

> **Context**: This project is developed by multiple AI agents (Google Antigravity, Claude Code, Copilot, Codex) operating across **Windows** and **WSL (Linux)** environments.
> **Goal**: Ensure seamless collaboration, cross-platform compatibility, and rigorous quality standards regardless of the OS or agent used.

---

## 1. Environment Setup (Dual-OS Strategy)

Since the repository is shared between Windows and WSL (mounted filesystem), **binary incompatibility** prevents sharing a single virtual environment.

### 🪟 Windows Agents (Antigravity, VS Code Copilot)
*   **Virtual Environment**: `.venv`
*   **Creation**: `python -m venv .venv`
*   **Activation**: `.venv\Scripts\Activate.ps1`
*   **Interpreter Path**: `d:\GitHub\cli-plugins\.venv\Scripts\python.exe`

### 🐧 WSL Agents (Claude Code, Copilot CLI)
*   **Virtual Environment**: `.venv-wsl`
*   **Creation**: `python3 -m venv .venv-wsl`
*   **Activation**: `source .venv-wsl/bin/activate`
*   **Interpreter Path**: `/mnt/d/GitHub/cli-plugins/.venv-wsl/bin/python`

> **CRITICAL**: Never attempt to use the "other" OS's venv. If you are in WSL, ignore `.venv`. If in Windows, ignore `.venv-wsl`.

---

## 2. Cross-Platform Coding Rules

To ensure the code runs identically on both Windows and Linux:
1.  **Paths**: ALWAYS use `pathlib.Path`. never hardcode backslashes (`\`) or forward slashes (`/`).
    *   ✅ `Path("src") / "crawler" / "models.py"`
    *   ❌ `"src\\crawler\\models.py"`
2.  **Line Endings**: Prefer **LF** (`\n`) for code files. Git handles this, but when writing files directly, verify line endings if editing existing files.
3.  **Subprocesses**:
    *   Use `subprocess.run(["cmd", "arg"])` (list form).
    *   Avoid `shell=True` unless absolutely necessary (and specific to the OS shell).
    *   Use `shlex.quote` or `shlex.join` when constructing command strings for logging/display.
4.  **Encoding**: Always specify `encoding="utf-8"` when opening text files. `open(..., encoding="utf-8")`.

---

## 3. Standard Workflow (The Loop)

Every agent must follow this **10-step cycle** for every task:

1.  **PLAN**: Analyze the request (Sequential Thinking).
2.  **DEFINE TODOs**: Breakdown the work into atomic steps.
3.  **TDD (Write Tests)**: Write failing tests *before* implementation (**RED** state).
4.  **DEVELOP**: Write minimal code to pass the tests (**GREEN** state).
5.  **TEST + ITERATE**: Refine code, add edge cases, ensure robustness.
6.  **VERIFY GLOBAL CONSISTENCY**: Run full suite (`pytest tests/`) to check for regressions.
7.  **E2E TEST (NEW CLI)**:
    *   Pick a CLI tool *not yet tested* (check D:\GitHub\cli-plugins\output) and available in WIN or WSL environment.
    *   Run `cli-crawler <tool>` -> `generate-plugin <tool>`.
    *   Verify the output manually in D:\GitHub\cli-plugins\output and D:\GitHub\cli-plugins\plugins to prove the solution works in the wild.
8.  **MARK TASK**: Check off `[x]` in `specs/001-cli-plugins-base/tasks.md` (or relevant task file).
9.  **ATOMIC COMMIT**: Commit *only* related changes with a conventional message.
10. **PUSH + PR**: Push to branch, open PR (if applicable), and **WAIT FOR REVIEW**.

---

## 4. Common Commands Reference

| Task | Windows (PowerShell) | WSL (Bash) |
| :--- | :--- | :--- |
| **Install Env** | `python -m venv .venv` | `python3 -m venv .venv-wsl` |
| **Activate** | `.venv\Scripts\Activate.ps1` | `source .venv-wsl/bin/activate` |
| **Install Deps** | `pip install -e ".[dev]"` | `pip install -e ".[dev]"` |
| **Run Tests** | `pytest tests/` | `pytest tests/` |
| **Lint Check** | `ruff check .` | `ruff check .` |
| **Format** | `ruff format .` | `ruff format .` |
| **Clean Output** | `Remove-Item output/*.json` | `rm output/*.json` |

---
*If you are an AI agent reading this, acknowledge your environment (Windows or WSL) and proceed accordingly.*
