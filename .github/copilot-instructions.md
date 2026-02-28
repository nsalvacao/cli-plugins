# Copilot Coding Agent — Onboarding Instructions

## Project Overview

**cli-plugins** crawls CLI `--help` output and generates structured Claude Code plugins with expert command knowledge. Think "OpenAPI for CLIs."

**Pipeline:** CLI binary → `cli-crawler` (JSON) → `generate-plugin` (plugin directory) → Claude Code consumes the plugin.

Three entry-point commands are defined in `pyproject.toml [project.scripts]`:

| Command            | Module                          | Purpose                              |
| ------------------ | ------------------------------- | ------------------------------------ |
| `cli-crawler`      | `src/crawler/pipeline.py:main`  | Crawl and parse CLI help output      |
| `generate-plugin`  | `src/generator/plugin_generator.py:main` | Build Claude plugin from crawler JSON |
| `config-audit`     | `src/config/audit.py:main`      | Detect inventory drift               |

## Repository Layout

```
src/
  crawler/       # Core crawling pipeline, executor, parsers, models
  generator/     # Plugin generation from crawler JSON
  config/        # Config audit / drift detection
  lib/           # Shared utilities (subprocess_utils, cli_identity, logger)
plugins/         # Generated Claude Code plugin directories (cli-<name>/)
docs/            # CONTRIBUTING.md, README
config.yaml      # Operational overrides for CLI crawling defaults
cli_crawler.py   # Legacy top-level entry point (imports from src/crawler)
pyproject.toml   # Build config, dependencies, tool settings
```

## Setup and Installation

```bash
# Recommended (if uv is available)
uv sync

# Alternative (pip)
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Dev dependencies (pytest, ruff, black, radon) are declared in `[project.optional-dependencies] dev` in `pyproject.toml`.

## Linting, Formatting, and Testing

```bash
# Lint
ruff check src/

# Format check
ruff format --check src/

# Auto-fix lint issues
ruff check --fix src/

# Auto-fix formatting
ruff format src/

# Run tests (when tests/ directory exists)
pytest tests/ -v --tb=short -x
```

### Known CI issue

The CI workflow (`.github/workflows/ci.yml`) runs `ruff check src/ tests/` and `pytest tests/`, but the `tests/` directory is listed in `.gitignore` and is **not committed to the repository**. This causes CI to fail with:

```
E902 No such file or directory (os error 2)
--> tests:1:1
```

**Workaround when running locally:** omit `tests/` from ruff commands if the directory does not exist: `ruff check src/` instead of `ruff check src/ tests/`.

## Ruff Configuration (in `pyproject.toml`)

- **Target:** Python 3.11
- **Line length:** 100
- **Source roots:** `src`, `tests`
- **Enabled rules:** E, F, W, I (isort), UP, B, SIM
- **Ignored rules:** E501 (line length), E741, SIM108, SIM102, SIM103, B007

## Coding Conventions

### Python Style

- **`from __future__ import annotations`** must be the first import (after the module docstring) in every Python file.
- **Python 3.10+ type syntax:** use `str | None` (not `Optional[str]`), `list[str]` (not `List[str]`).
- **No external runtime dependencies** for core functionality (crawler, generator, config-audit use stdlib only).
- **Keep files under 500 lines.**

### Docstrings

- Module-level docstring at the top of every `.py` file.
- Function/class docstrings use Google-style (`Args:`, `Returns:`, `Raises:` sections).
- Imperative mood for the first line.

### Data Models

- Use `@dataclass` for all data structures (see `src/crawler/models.py`).
- Use `field(default_factory=list)` for mutable defaults.
- `models.py` is the single source of truth for data shapes.

### Security

- **Never use `shell=True`** in subprocess calls. Always pass commands as lists.
- PowerShell arguments are single-quoted via `_quote_ps_arg()` in `src/crawler/executor.py` to prevent command injection.
- `SAFE_ENV` dictionary (defined in both `src/crawler/executor.py` and `src/lib/subprocess_utils.py`) standardises subprocess environment to suppress colours and pagers: `NO_COLOR=1`, `PAGER=cat`, `TERM=dumb`, `LANG=C`, `LC_ALL=C`, `GIT_PAGER=cat`, `MANPAGER=cat`, `MANWIDTH=120`, `COLUMNS=120`.
- If you update SAFE_ENV in one file, update the other to match (both files note this requirement).

### Logging

- Use `logging.getLogger(__name__)` or `logging.getLogger("cli_crawler.<module>")`.
- Never use `print()` for diagnostic output; use the logger.

### Tests

- Test files go in `tests/` (not in root or `src/`), named `test_*.py`.
- Pytest markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.e2e`, `@pytest.mark.performance`.
- Unit tests use descriptive docstrings.

### Commits

- Follow [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.

## CI Workflows

| File                            | Purpose                                        |
| ------------------------------- | ---------------------------------------------- |
| `.github/workflows/ci.yml`     | Lint (ruff) + test (pytest) on Python 3.11/3.12 |
| `.github/workflows/codeql-analysis.yml` | Weekly CodeQL security scanning         |

## What Not to Touch

- `plugins/` — these are **generated** artifacts; regenerate them via `generate-plugin`, do not hand-edit.
- `output/` — crawler output; gitignored.
- `.gitignore` excludes many dev-only directories (`.claude/`, `specs/`, `tests/`, `.dev/`, `.agent/`, etc.). Be aware of these when creating files.
