# CLI Plugins

> **OpenAPI mindset for CLIs**: crawl real `--help` output, build structured CLI maps, and generate Claude Code plugins with reliable command knowledge.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/nsalvacao/cli-plugins/actions/workflows/ci.yml/badge.svg)](https://github.com/nsalvacao/cli-plugins/actions/workflows/ci.yml)

---

## TL;DR

- **Input**: any CLI binary available in your environment (`docker`, `git`, `gh`, `uv`, `pnpm`, etc.)
- **Phase 1**: `cli-crawler` parses help output into `output/<cli>.json`
- **Phase 2**: `generate-plugin` converts that JSON into `plugins/cli-<name>/`
- **Result**: Claude Code gets concrete, tool-specific command intelligence instead of guessing flags

---

## Why This Exists

LLMs are strong at reasoning, but weak on precise, current CLI syntax unless the exact tool/version is in context.

Typical failure modes when relying on model memory alone:

- hallucinated flags
- wrong argument order
- outdated commands after CLI updates
- missing required options hidden in subcommand help

This project creates a deterministic bridge between **real CLI help** and **AI plugin context**.

---

## Why Not Just `--help`?

`--help` is necessary, but not sufficient as a direct context source for agents:

| Approach | Works for humans | Works for agents at scale | Main issue |
| --- | --- | --- | --- |
| Manual copy/paste from `--help` | Yes | No | token-heavy, inconsistent, stale quickly |
| `man`/online docs | Yes | Sometimes | fragmented formats, weak machine structure |
| Raw CLI help in prompt | Sometimes | Poorly | noisy, hard to navigate, expensive context |
| **CLI Plugins (this project)** | Yes | **Yes** | structured, compact, regenerable |

---

## Real Differentiators

1. **Format-agnostic parsing**
Parses multiple help styles (Cobra, Click, Rich-Click, Git/manpage, POSIX-like patterns) with deterministic heuristics.

2. **Progressive disclosure by default**
Generates compact `SKILL.md` plus on-demand references (`commands.md`, `examples.md`) to reduce context pressure.

3. **Safety-first help detection**
Includes protections such as auth-required precedence and non-mutating fallback policy for subcommand probing.

4. **Cross-platform resilience (Windows/WSL)**
Supports executable-name canonicalization (e.g., `.exe` identity handling) while preserving runnable invocation.

5. **Global-only CLI quality fallback**
When a CLI has no subcommands, plugin output still provides meaningful usage examples and stable version labeling.

6. **Inventory drift visibility**
`config-audit` compares `config.yaml`, `output/*.json`, and `plugins/cli-*` to highlight stale/missing artifacts.

7. **Idempotent generation**
Re-runs overwrite generated outputs cleanly and predictably.

8. **No runtime external dependencies**
Core runtime (`cli-crawler`, `generate-plugin`, `config-audit`) uses project code and stdlib-friendly implementation.

---

## How It Works

```text
CLI binary
   -> cli-crawler
   -> output/<cli>.json (+ optional output/<cli>.raw.json)
   -> generate-plugin
   -> plugins/cli-<slug>/
```

### Main Commands

- `cli-crawler`: crawl and parse CLI help output
- `generate-plugin`: build Claude plugin from crawler JSON
- `config-audit`: detect inventory drift and suggest minimal config overrides

---

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/nsalvacao/cli-plugins.git
cd cli-plugins

# Option A (recommended)
uv sync

# Option B
# python3 -m venv .venv-wsl
# source .venv-wsl/bin/activate
# pip install -e ".[dev]"
```

### 2. Crawl a CLI

```bash
uv run cli-crawler docker -o output/docker.json --raw -v
```

### 3. Generate Plugin

```bash
uv run generate-plugin output/docker.json
```

Plugin output:

```text
plugins/cli-docker/
```

### 4. Install/Use in Claude Code

```bash
cp -r plugins/cli-docker ~/.claude/plugins/cli-docker
```

Or test directly:

```bash
claude --plugin-dir plugins/cli-docker
```

---

## Generated Plugin Layout

```text
plugins/cli-my-tool/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── cli-my-tool/
│       ├── SKILL.md
│       └── references/
│           ├── commands.md
│           └── examples.md
├── commands/
│   └── scan-cli.md
└── scripts/
    └── rescan.sh
```

`rescan.sh` is generated per plugin and re-runs crawl + generation for that CLI.

---

## Configuration Policy (`config.yaml`)

Use `config.yaml` for **operational overrides**, not as a full inventory catalog.

Example:

```yaml
defaults:
  timeout: 5
  max_depth: 5
  max_concurrent: 5
  retry: 1
  environment: wsl
  raw_threshold: 10000

clis:
  docker:
    max_depth: 6
  kubectl:
    timeout: 8
    plugins:
      discovery_command: kubectl plugin list
```

Recommended minimal override fields:

- `environment`
- `help_pattern`
- `max_depth`
- `max_concurrent`
- `plugins.discovery_command`

---

## Inventory Audit and Drift Detection

Run:

```bash
uv run config-audit \
  --config config.yaml \
  --output-dir output \
  --plugins-dir plugins \
  --report output/config-audit.json
```

The report highlights:

- `missing_in_config`
- `stale_in_config`
- `missing_output`
- `missing_plugin`
- `suggested_minimal_overrides`

---

## Quality and Workflow

This repo follows a strict loop for each batch:

1. plan and define atomic tasks
2. tests first (RED)
3. implementation (GREEN)
4. full regression run (`pytest tests/`)
5. E2E with a **new CLI**
6. update tracking in specs/control files
7. atomic commit + PR + review

Common checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest tests/
```

---

## Roadmap

### Planned: Grouped Plugins (Multi-CLI per Domain)

A major next step is to support grouping multiple related CLIs into a single plugin (for example, one domain plugin for several DevOps CLIs).

Expected impact:

- drastically fewer installed plugins
- simpler activation/maintenance model
- better domain-level discoverability
- lower operational overhead for large toolchains

This is planned through the group taxonomy and inference backlog (deterministic first, ML fallback), then future grouped-plugin generation.

### Also Planned

- observability and confidence scoring expansion
- dashboard UI for inventory, operations, and plugin inspection
- PyPI release hardening and publish workflow

---

## Contributing

See `docs/CONTRIBUTING.md`.

---

## License

[MIT](LICENSE)

---

## References

- [Claude Code Plugins](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [OpenAPI Specification](https://swagger.io/specification/)
