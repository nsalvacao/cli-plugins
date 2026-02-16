# CLI Plugins

> **OpenAPI for CLIs** -- Automatically crawl any CLI's `--help` output and generate structured Claude Code plugins that give AI agents expert-level command knowledge.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-100%20passed-brightgreen.svg)](#running-tests)

---

## The Problem

AI coding assistants lack precise knowledge of CLI tools -- especially newer ones released after training cutoffs. When asked to construct a `docker buildx` command or debug a `claude-flow swarm` invocation, they guess at flag names, invent non-existent options, and miss required arguments. Manual documentation is token-expensive and quickly outdated.

## The Solution

**CLI Plugins** solves this with a two-phase pipeline:

```
CLI binary  -->  Crawler  -->  JSON map  -->  Generator  -->  Claude Code Plugin
(git, docker...)   (Phase 1)    (output/)     (Phase 2)       (plugins/cli-*)
```

1. **Crawler** executes `--help` recursively across all subcommands, parsing flags, descriptions, examples, env vars, and usage patterns into a structured JSON map.
2. **Generator** transforms that JSON into a self-contained Claude Code plugin with progressive disclosure: a lean SKILL.md overview backed by full reference files.

The result: Claude Code gains precise, complete, up-to-date knowledge of any CLI tool -- including ones it has never seen.

## Highlights

- **Universal parser** -- Handles 7 CLI format families (Go/Cobra, Python/Click, Rich-Click, Node/Commander, Git, POSIX, man pages) without hardcoded format detection
- **691 commands crawled** across 7 CLIs with 5,109 flags and 316 usage examples
- **Progressive disclosure** -- SKILL.md stays lean (~700 words); detailed flag tables and examples load on-demand from `references/`
- **Echoed parent detection** -- Automatically identifies when a CLI returns parent help for subcommands, preventing duplicated data
- **Zero dependencies** -- Crawler and generator use Python stdlib only
- **100% test coverage** -- 100 tests across crawler and generator (66 + 34)
- **Idempotent** -- Re-running overwrites cleanly, no stale files

## Pre-Built Plugins

Ready-to-use plugins for popular CLIs:

| Plugin | Commands | Flags | Examples | Size |
|--------|----------|-------|----------|------|
| `cli-claude-flow` | 51 | 15 | 17 | ~10 KB |
| `cli-docker` | 271 | 1,419 | 7 | ~116 KB |
| `cli-git` | 22 | 441 | 126 | ~128 KB |
| `cli-gh` | 212 | 1,097 | 166 | ~110 KB |
| `cli-npm` | 67 | 411 | 0 | ~30 KB |
| `cli-uv` | 54 | 1,684 | 0 | ~193 KB |
| `cli-langchain` | 14 | 42 | 0 | ~8 KB |

## Quick Start

```bash
# Prerequisites: Python 3.11+, uv
git clone https://github.com/nsalvacao/cli-plugins.git
cd cli-plugins
uv sync

# Crawl a CLI
uv run python cli_crawler.py git -o output/git.json --include-raw

# Generate the plugin
uv run python scripts/generate_plugin.py output/git.json

# Plugin ready at plugins/cli-git/
```

## Installing a Plugin

Copy a generated plugin to Claude Code's plugin directory:

```bash
cp -r plugins/cli-docker ~/.claude/plugins/cli-docker
```

Or test locally without installing:

```bash
claude --plugin-dir plugins/cli-docker
```

The plugin auto-activates when Claude Code detects relevant CLI questions.

## Creating a Plugin for Any CLI

### Step 1: Configure (optional)

Add CLI-specific settings to `config.yaml`:

```yaml
clis:
  my-tool:
    max_depth: 5        # Subcommand depth (default: 5)
    group: my-category  # Grouping label
    timeout: 10         # Per-command timeout in seconds
    plugins:
      discovery_command: my-tool plugin list
```

**Minimal override policy (recommended)**:
- Keep only operational overrides that differ from defaults: `environment`, `help_pattern`, `max_depth`, `max_concurrent`, `plugins.discovery_command`.
- Do **not** mirror inventory in `config.yaml` (avoid listing every crawled/generated CLI just to keep a catalog).
- Use `output/*.json` and `plugins/cli-*` as inventory sources of truth.

### Step 2: Crawl

```bash
uv run python cli_crawler.py my-tool -o output/my-tool.json -v --include-raw
```

### Step 3: Generate

```bash
uv run python scripts/generate_plugin.py output/my-tool.json
```

### Step 4: Use

```bash
claude --plugin-dir plugins/cli-my-tool
```

## Generated Plugin Structure

```
plugins/cli-my-tool/
├── .claude-plugin/
│   └── plugin.json                        # Plugin manifest
├── skills/
│   └── cli-my-tool/
│       ├── SKILL.md                       # Lean overview (~700 words)
│       └── references/
│           ├── commands.md                # Full command tree with flags
│           └── examples.md                # Usage examples
├── commands/
│   └── scan-cli.md                        # /scan-cli slash command
└── scripts/
    └── rescan.sh                          # Re-crawl and regenerate
```

**Progressive disclosure**: SKILL.md is always loaded when the skill triggers. Reference files load on-demand when Claude needs detailed flag tables or examples, keeping context window usage minimal.

## Architecture

### Crawler (`crawler/`)

| Module | Purpose |
|--------|---------|
| `pipeline.py` | Top-level orchestrator |
| `detector.py` | Auto-detect help pattern (`--help`, `-h`, `help`, manpage) |
| `discovery.py` | Recursive subcommand crawl with cycle detection |
| `executor.py` | Safe subprocess execution with timeout |
| `parser.py` | Main parse dispatcher |
| `parsers/sections.py` | Section segmentation (7 format families) |
| `parsers/flags.py` | Flag extraction with type inference |
| `parsers/commands.py` | Subcommand list parsing |
| `parsers/usage.py` | Usage pattern extraction |
| `parsers/examples.py` | Example extraction |
| `parsers/envvars.py` | Environment variable extraction |
| `parsers/manpage.py` | Man page format parser |
| `models.py` | Data structures (`CLIMap`, `Command`, `Flag`, etc.) |
| `config.py` | YAML config loader |
| `formatter.py` | JSON serialization |
| `version.py` | Version detection |

### Generator (`scripts/generate_plugin.py`)

Single-file generator using Python stdlib only. Reads crawler JSON and produces a complete Claude Code plugin directory.

### Supported CLI Format Families

| Family | Examples | Detection |
|--------|----------|-----------|
| Go/Cobra | docker, gh, kubectl | `Available Commands:` / `Flags:` |
| Python/Click | uv, pip | `Commands:` / `Options:` |
| Python/Rich-Click | claude-flow, langchain | Box-drawing borders + sections |
| Node/Commander | npm | Man page style |
| Git | git | Man page + porcelain/plumbing groups |
| Generic POSIX | curl, grep | `-flag  description` format |
| Man pages | git-commit, npm-install | `.TH` / `NAME` / `SYNOPSIS` |

## Development

### Project Layout

```
cli-plugins/
├── cli_crawler.py          # CLI entry point
├── config.yaml             # CLI configurations
├── crawler/                # Crawler modules (Phase 1)
├── scripts/
│   └── generate_plugin.py  # Plugin generator (Phase 2)
├── tests/                  # All tests
│   ├── test_*.py           # Unit + integration tests
│   └── fixtures/           # Raw help text samples
├── output/                 # Crawler JSON output (gitignored)
├── plugins/                # Generated plugins
└── docs/                   # Documentation
```

### Running Tests

```bash
# All tests
uv run python -m pytest tests/ -v

# Crawler tests only
uv run python -m pytest tests/ -v -k "not generate"

# Generator tests only
uv run python -m pytest tests/test_generate_plugin.py -v
```

### Re-scanning a CLI

Each plugin includes a `scripts/rescan.sh`:

```bash
bash plugins/cli-docker/scripts/rescan.sh
```

Or manually:

```bash
uv run python cli_crawler.py docker -o output/docker.json --include-raw -v
uv run python scripts/generate_plugin.py output/docker.json
```

### Batch Crawl

```bash
uv run python cli_crawler.py --all --config config.yaml
```

### Config Audit (Inventory Drift)

Audit drift between `config.yaml`, `output/*.json`, and `plugins/cli-*`:

```bash
config-audit --config config.yaml --output-dir output --plugins-dir plugins --report output/config-audit.json
```

Alternative without installing console scripts:

```bash
uv run python -m config.audit --config config.yaml --output-dir output --plugins-dir plugins --report output/config-audit.json
```

This report includes:
- `missing_in_config`
- `stale_in_config`
- `missing_output`
- `missing_plugin`
- `suggested_minimal_overrides`

## Design Decisions

- **Python stdlib only** -- No external dependencies for crawler or generator
- **Idempotent generation** -- Re-running overwrites cleanly, no stale files
- **Echoed parent detection** -- When a CLI returns parent help for a subcommand, the crawler creates a minimal entry using the parent's one-liner description instead of duplicating flags/examples
- **Progressive disclosure** -- SKILL.md stays lean; full details in reference files loaded on-demand
- **Format-agnostic parsing** -- Section-based segmentation handles Go, Python, Node, and POSIX conventions without hardcoded format detection
- **Domain-aware trigger phrases** -- Plugin descriptions use natural language with grouped command areas, not keyword stuffing

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Target CLI tools must be installed and on PATH

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for development setup and guidelines.

## Author

**Nuno Salvacao**
- GitHub: [@nsalvacao](https://github.com/nsalvacao)
- LinkedIn: [nsalvacao](https://www.linkedin.com/in/nsalvacao/)
- Email: nuno.salvacao@gmail.com

## License

[MIT](LICENSE)

## References

- [Claude Code Plugins](https://docs.anthropic.com/en/docs/claude-code/plugins) -- Official plugin documentation
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills) -- Skill authoring guide
- [OpenAPI Specification](https://swagger.io/specification/) -- The inspiration: structured API contracts, but for CLIs
