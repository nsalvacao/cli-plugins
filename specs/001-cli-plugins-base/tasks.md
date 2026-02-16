# Tasks: CLI Plugins Core Project

**Input**: Design documents from `/specs/001-cli-plugins-base/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification (spec.md) implicitly requests a strong testing approach (100% test coverage, independent tests, acceptance scenarios). Therefore, test tasks are included to facilitate a TDD approach.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- **[NEW]**: Task added by speckit.analyze remediation (2026-02-13)
- **[MOVED]**: Task relocated from original phase for ordering correctness
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project — adjust based on plan.md structure
- **⚠️ Structural decision (T001)**: source code currently in `crawler/` (POC); T001 decides migration to `src/crawler/`

---

## Phase 1: Setup + Pre-Launch Blockers

**Purpose**: Project initialization, known structure bugs, and CI/CD — MUST complete before any user story work. CI/CD moved here from Phase 6 per constitution §CI/CD Automatizado and execution-plan A7 ("BLOCKS EVERYTHING").

- [x] **T001 Createeeee project directories** - `src/crawler`, `src/generator`, `src/config`, `src/lib`, `tests/unit`, `tests/integration`, `tests/end_to_end` — decision: migrate existing `crawler/` → `src/crawler/` (preserve git history with `git mv`)
- [x] **T002 Initialize pyproject.toml** - Python project in repository root (exists — bugs fixed in T038)
- [x] **T038 Fix known `pyproject.toml` bugs** - move `classifiers` from `[project.urls]` to `[project]`; fix `readme` path from `docs/README.md` to `README.md`; add `[build-system]` section with `hatchling` — verify with `uv build && twine check dist/*` *(Blocker B1 — evaluation-results_v2)* ([NEW])
- [x] **T039 Register `generate-plugin` as CLI entry point** - in `pyproject.toml` `[project.scripts]`: `generate-plugin = "generator.plugin_generator:main"` — verify `pip install -e . && generate-plugin --help` works *(Blocker B2)* ([NEW])
- [x] **T003 Configure basic `config.yaml`** - in `src/config/config.yaml`
- [x] **T004 Configure linting and formatting (Black, Ruff)** - in `pyproject.toml` — add `[tool.black]` and `[tool.ruff]` sections; verify `ruff check src/ tests/` runs clean ([P])
- [x] **T005 Setup Pytest for testing** - in `pyproject.toml` — add `[tool.pytest.ini_options]` with testpaths, markers for unit/integration/e2e ([P])
- [x] **T032 Create CI/CD pipeline** - `.github/workflows/ci.yml` — pytest matrix on Python 3.11+3.12, ruff lint, black check; runs on push and PR; add CI badge to `README.md` *(constitution §CI/CD Automatizado; execution-plan A7)* ([MOVED from Phase 6])
- [x] **T066 Add __version__ and --version flags** - via `src/__init__.py` sourced from `pyproject.toml`; add `--version` flag to `cli-crawler` and `generate-plugin` entry points *(evaluation-results A5, L3)* ([P] [NEW])

**Checkpoint — Phase 1 AC**: `pip install -e '.[dev]'` succeeds; `pytest` discovers tests; `ruff check src/` exits 0; `npx ci` green; `cli-crawler --version` outputs version string.

---

## Phase 2: Foundational (Blocking Prerequisites + Parser Quality)

**Purpose**: Core infrastructure and parser quality gates MUST be complete before ANY user story can be implemented. Semantic keywords and author config moved here from Phase 6 — both are launch blockers per evaluation-results_v2.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] **T006 Create CLIMap schema** - CLI, CLIMap, Command, Flag, Plugin entities in `src/crawler/models.py` — reconcile with data-model.md (see T044)
- [x] **T044 Reconcile schema inconsistency** - `data-model.md` defines `Flag.long_name` + `Flag.short_name` separately; `crawler/models.py` uses `name` + `short`. Decide canonical naming, update both `models.py` and `data-model.md` to match. Add migration note. *(M3)* ([P] [NEW])
- [x] **T007 Implement safe subprocess execution utility** - in `src/lib/subprocess_utils.py` — `subprocess.run` with tokenised args only, no `shell=True`, timeout enforcement, SAFE_ENV (disable colour/pager)
- [x] **T067 Security review** - audit `crawler/executor._build_command` Windows PowerShell path — confirm no shell-injection risk when joining command array for PowerShell; add unit test covering edge case *(evaluation-results §5 WARN, L4)* ([P] [NEW])
- [x] **T008 Configure basic logging infrastructure** - in `src/lib/logger.py` — use Python stdlib `logging` module only; NO external packages (FR-008, constitution §Zero Dependencies); structured levels (DEBUG/INFO/WARNING/ERROR); configurable via env var `CLI_PLUGINS_LOG_LEVEL`
- [x] **T028 Implement semantic keyword generation for plugins** - in `src/generator/plugin_generator.py` — keywords derived from CLI name + top command group names + domain terms extracted from description (NOT first words of command descriptions) *(FR-012; Blocker B5)* ([MOVED from Phase 6] [P])
- [x] **T029 Implement author configuration for plugins** - in `src/generator/plugin_generator.py` — `--author` CLI flag or `CLI_PLUGINS_AUTHOR` env var; omit `author` field entirely when not specified; community generators must not carry hardcoded attribution *(FR-011; Blocker B6)* ([MOVED from Phase 6] [P])
- [x] **T040 Implement progressive disclosure** - in `src/generator/plugin_generator.py` — SKILL.md compact view (≤800 tokens: top-level commands + global flags + 5 examples); `references/commands.md` (full flag tables, loaded on demand); `references/examples.md` (all examples, loaded on demand) *(FR-004; constitution §Auto-Geração e Otimização)* ([NEW])
- [x] **T041 Improve Rich-Click parser** - in `src/crawler/parsers/` to correctly extract flags from box-drawing (`╭─╮│`) formatted output — currently extracts 7 flags from 51 commands (cli-claude-flow 2.55/5); target: >50% extraction rate for Rich-Click CLIs *(SC-003; evaluation-results I4; CRITICAL C2)* ([NEW])
- [x] **T042 Improve man page example extraction** - in `src/crawler/parsers/manpage.py` — fix zero-examples issue for npm-style man page CLIs; target: extract documented examples from `EXAMPLES` section *(SC-003; evaluation-results §1.4)* ([P] [NEW])
- [x] **T043 Add thread-safety locks to `CrawlState`** - in `src/crawler/discovery.py` — `threading.Lock()` on `visited`, `errors`, `warnings` sets to prevent race conditions under `ThreadPoolExecutor` *(SC-008; evaluation-results R8)* ([P] [NEW])
- [x] **T045 Fix error messages captured as descriptions** - extend `_clean_description` in `src/crawler/parser.py` with patterns: runtime errors (`fatal:`, `error:`, `accepts N arg(s)`), circular names (description == command name), state messages (`already initialized`) *(Blocker B3; evaluation-results §8 B3)* ([P] [NEW])
- [x] **T046 Fix git plugin code fence formatting** - in `src/generator/plugin_generator.py` — ensure description text does not leak outside fenced ` ``` ` blocks in `examples.md` output *(Blocker B4; evaluation-results §8 B4)* ([P] [NEW])

**Checkpoint — Phase 2 AC**: All schema entities importable; subprocess utils pass security tests; Rich-Click flag extraction rate >50% for `claude-flow`; `plugin.json` has semantic keywords and no hardcoded author; SKILL.md + `references/` structure generated correctly for docker; zero error-message descriptions in regenerated git/gh plugins.

---

## Phase 3: User Story 1 — Obter Conhecimento Preciso de uma CLI (Priority: P1) 🎯 MVP

**Goal**: O assistente de IA pode dar comandos e flags precisos para qualquer CLI instalada, sem "alucinar" ou dar informações desatualizadas.

**Independent Test**: Instalar plugin `docker` gerado e usar Claude Code para perguntar sobre `docker run --gpus`. O assistente deve responder com a flag correcta.

### Tests for User Story 1 (write FIRST — ensure they FAIL before implementation)

- [x] **T009 Unit test for initial CLI crawling (e.g., `git --help`)** - in `tests/unit/test_cli_crawler_basic.py` ([P] [US1])
- [x] **T010 Unit test for basic flag extraction** - in `tests/unit/test_flag_parsing_basic.py` ([P] [US1])
- [x] **T011 Unit test for basic command hierarchy parsing** - in `tests/unit/test_command_parsing_basic.py` ([P] [US1])
- [x] **T012 Unit test for Rich-Click/man page parsing quality** - in `tests/unit/test_parsing_rich_man.py` — AC: Rich-Click extraction rate >50%; man page examples extracted for npm-equivalent fixture ([P] [US1])
- [x] **T047 Unit test for EC-01** - CLI without standard `--help` → parser emits warning, returns partial CLIMap, does not crash; in `tests/unit/test_edge_case_no_help.py` ([P] [NEW] [US1])
- [x] **T048 Unit test for EC-02** - CLI requiring auth for `--help` (simulated via timeout/exit-code) → clear error message, no hang; in `tests/unit/test_edge_case_auth_help.py` ([P] [NEW] [US1])
- [x] **T049 Unit test for EC-05** - `--help` output >10 000 lines → progressive loading triggered, SKILL.md compact, references/ on-demand; in `tests/unit/test_edge_case_long_help.py` ([P] [NEW] [US1])
- [x] **T079 Unit test for pnpm grouped-help format** - in `tests/unit/test_parser_pnpm_grouped_help.py` — AC: parse sentence-case section headers (e.g., `Manage your dependencies:`), extract comma-alias command lines (`i, install`), and recover wrapped descriptions ([P] [NEW] [US1])
- [x] **T082 Unit test for embedded-help flag deduplication (yq+jq style)** - in `tests/unit/test_flag_dedup_embedded_help.py` — AC: duplicate long flags (`--help`, `--version`) are deduplicated with deterministic precedence ([P] [NEW] [US1])
- [x] **T084 Unit test for robust version detection fallback** - in `tests/unit/test_version_detection_fallback.py` — AC: yq-style version outputs parse correctly (avoid `0.0.0` default when version text is present) ([P] [NEW] [US1])
- [ ] **T086 Unit test for recursion loop guard in discovery** - (`tests/unit/test_discovery_loop_guard.py`) — AC: self-referential trees (bun-style) stay bounded; crawl terminates without combinatorial explosion ([P] [NEW] [US1])
- [ ] **T088 Unit test for examples fallback on flag-only CLIs** - in `tests/unit/test_examples_fallback_flag_only.py` — AC: generated `examples.md`/SKILL compact section are non-empty for CLIs with zero subcommands (node-style) ([P] [NEW] [US1])
- [x] **T089 Unit test for embedded-help boundary filtering** - (`tests/unit/test_embedded_help_boundary.py`) — AC: foreign embedded tool flags/env vars (e.g., jq block inside yq help) are not merged into parent CLIMap ([P] [NEW] [US1])
- [x] **T091 Unit test for usage-line option extraction** - (`tests/unit/test_usage_line_option_extraction.py`) — AC: option-heavy CLIs without classic sections (python3-style) still extract representative root flags ([P] [NEW] [US1])
- [x] **T093 Extend version fallback tests for placeholder suffixes (`0.0.0-dev`, `unknown`)** - in `tests/unit/test_version_detection_fallback.py` — AC: placeholders do not short-circuit detection of real versions ([P] [NEW] [US1])
- [x] **T095 Unit test for sectionless fallback description normalization** - in `tests/unit/test_usage_line_option_extraction.py` — AC: recovered flag descriptions do not keep leading punctuation (`:`) and preserve meaningful text ([P] [NEW] [US1])
- [x] **T097 Unit test for sectionless long-option enrichment** - in `tests/unit/test_usage_line_option_extraction.py` — AC: bracket-only long options from usage preamble (e.g., `--help-env`, `--help-all`) are retained with non-empty descriptions when discoverable in body ([P] [NEW] [US1])
- [x] **T099 Unit test for sectionless attached-value/combined-short option parsing** - in `tests/unit/test_usage_line_option_extraction.py` — AC: flags like `-DNAME=VALUE`, `-Xlint:all`, `-O2`, `-abc` are recognized deterministically without dropping valid options ([P] [NEW] [US1])
- [x] **T101 Unit test for version source preference** - in `tests/unit/test_version_detection_fallback.py` — AC: when output contains dependency versions (`jq-1.7`) and CLI self-version, parser prefers CLI version; dependency pattern acts as last-resort fallback ([P] [NEW] [US1])
- [x] **T118 Unit test for GNU single-dash long-option parsing** - in `tests/unit/test_flag_parsing_gnu_single_dash.py` — AC: parse `-print-file-name=<lib>`, `-dumpmachine`, `-Wa,<options>`, `-Xassembler <arg>`, `-std=<standard>` from gcc-style help without collapsing/removing valid options ([P] [NEW] [US1])
- [ ] **T121 Unit test for sectionless single-space descriptions + numeric pseudo-flag filtering** - in `tests/unit/test_usage_line_option_extraction.py` — AC: lines like `-v verbose output` keep description text; non-option bullets like `-2024 release` are not parsed as flags ([P] [NEW] [US1])

### Implementation for User Story 1

- [x] **T013 Implement basic CLI crawling logic to execute `CLI --help`** - in `src/crawler/cli_crawler.py` ([US1])
- [x] **T014 Implement core parsing logic for basic CLI formats (Go/Cobra, Python/Click)** - in `src/crawler/parser.py` ([US1])
- [x] **T015 Implement pipeline orchestrator to manage crawl and parse steps** - in `src/crawler/pipeline.py` ([US1])
- [x] **T016 Implement CLIMap-to-AI-Plugin conversion** - in `src/generator/plugin_generator.py` — delegates progressive disclosure to T040 implementation ([US1])
- [x] **T050 Implement EC-01 handling** - graceful degradation for non-standard `--help` (warnings emitted to logger, partial CLIMap returned, confidence_score penalised); in `src/crawler/cli_crawler.py` ([P] [NEW] [US1])
- [x] **T051 Implement EC-02 handling** - detect auth-required `--help` (exit-code, timeout, stderr patterns) → fail with structured error, no process hang; in `src/crawler/executor.py` / `subprocess_utils.py` ([P] [NEW] [US1])
- [x] **T052 Implement EC-05 handling** - when raw `--help` > configurable line threshold (default 10 000), activate chunked progressive loading in pipeline; store full detail in `references/` only; in `src/crawler/pipeline.py` ([P] [NEW] [US1])
- [x] **T080 Implement parser support for pnpm-style grouped help** - in `src/crawler/parsers/sections.py` + `src/crawler/parsers/commands.py` — detect category headers like `Manage your dependencies:` as command sections and parse multi-line/wrapped tabular command descriptions ([NEW] [US1])
- [ ] **T017 Integration test for `CLI --help → CLIMap JSON` (docker)** - in `tests/integration/test_docker_climap_generation.py` ([P] [US1])
- [ ] **T018 E2E test for `CLI → CLIMap → Plugin` (mocking AI Assistant interaction)** - in `tests/end_to_end/test_docker_plugin_e2e.py` ([P] [US1])
- [x] **T053 Performance smoke test** - `docker` crawl + generate completes in <30 s; parsing a 1 000-line help fixture in <5 s; in `tests/performance/test_smoke_perf.py` *(SC-004 early validation — prevents late discovery)* ([P] [NEW])
- [x] **T081 Integration/E2E regression for pnpm** - in `tests/integration/test_pnpm_climap_generation.py` and/or `tests/end_to_end/test_pnpm_plugin_e2e.py` — AC: `cli-crawler pnpm` extracts >=12 commands and generated plugin contains `pnpm add`, `pnpm install`, `pnpm run` ([P] [NEW] [US1])
- [x] **T083 Implement embedded-help deduplication strategy in parser/serialization** - (`src/crawler/parser.py` and/or `src/crawler/formatter.py`) so repeated flags from wrapper+embedded tool help do not duplicate in plugin output (deterministic merge rule) ([NEW] [US1])
- [ ] **T085 Implement recursion/echo loop guard for self-referential subcommand trees** - in `src/crawler/discovery.py`/`src/crawler/pipeline.py` — AC: bun-style recursive help cannot explode node count; crawl stays bounded by structural fingerprints + depth ([NEW] [US1])
- [ ] **T087 Implement examples fallback for flag-only CLIs** - in `src/generator/plugin_generator.py` — AC: when no command tree exists, synthesize compact examples from root usage/global flags instead of `_No examples extracted._` ([NEW] [US1])
- [x] **T090 Implement embedded-help boundary filter in parser (`src/crawler/parser.py`** - and/or `src/crawler/parsers/sections.py`) — AC: stop/segment parsing when secondary tool help starts (yq+jq style), preserving parent-only metadata ([NEW] [US1])
- [x] **T092 Implement usage-line option extraction fallback for sectionless CLIs** - in `src/crawler/parser.py`/`src/crawler/parsers/usage.py` — AC: python3-style help yields non-zero root flags and usable plugin references ([NEW] [US1])
- [x] **T094 Expand placeholder-version handling** - in `src/crawler/version.py` — AC: values like `0.0.0-dev`/`unknown` treated as non-informative, allowing fallback to real versions when available ([NEW] [US1])
- [x] **T096 Implement description normalization in sectionless option fallback** - (`src/crawler/parsers/usage.py` / `src/crawler/parser.py`) — AC: strip leading `:` artifacts; avoid empty/noisy descriptions in generated plugin references ([NEW] [US1])
- [x] **T098 Implement sectionless long-option enrichment (`src/crawler/parsers/usage.py`)** - AC: when usage preamble declares long options, correlate with body/help lines to populate descriptions and avoid sparse long-only entries ([NEW] [US1])
- [x] **T100 Implement robust sectionless option atom parsing** - in `src/crawler/parsers/usage.py` — AC: attached-value and combined-short forms are parsed without relying on strict word-boundary regex; preserve deterministic output ordering ([NEW] [US1])
- [x] **T102 Implement CLI-name-aware version preference** - in `src/crawler/version.py` — AC: prefer versions attributable to target CLI; keep `pkg-<version>` pattern as last-resort to avoid dependency-version false positives ([NEW] [US1])
- [x] **T119 Extend `src/crawler/parsers/flags.py` to support GNU single-dash long options** - and pass-through families (`-print-*`, `-dump*`, `-Wa,`, `-Wp,`, `-Wl,`, `-Xassembler`, `-Xpreprocessor`, `-Xlinker`) with deterministic normalization and no duplicate erosion ([NEW] [US1])
- [x] **T120 Integration/E2E regression for gcc** - in `tests/integration/test_gcc_climap_generation.py` and/or `tests/end_to_end/test_gcc_plugin_e2e.py` — AC: `cli-crawler gcc` extracts representative compiler flags (>=20) including `-print-file-name`, `-Wa,`, `-Xassembler`, `-std=`, and generated plugin references remain coherent ([P] [NEW] [US1])
- [ ] **T122 Harden sectionless usage parsing** - in `src/crawler/parsers/usage.py` for single-space description inference and strict option gating (first token after `-` must be alpha for short-option paths) to prevent numeric false positives ([NEW] [US1])
- [ ] **T123 Unit test for short-option attached metavars in sectionless fallback** - in `tests/unit/test_usage_line_option_extraction.py` — AC: perl-style `-Idirectory` normalizes to `-I` (`type=string`) and `-V[:configvar]` normalizes to `-V` with optional string hint ([P] [NEW] [US1])
- [ ] **T124 Improve short-option attached metavars parsing** - in `src/crawler/parsers/usage.py` — AC: normalize suffix-encoded metavars deterministically while preserving option coverage and type inference quality for short attached forms ([NEW] [US1])
- [ ] **T125 Unit test for vendor-prefixed multiword version lines** - in `tests/unit/test_version_detection_fallback.py` — AC: detect CLI version from outputs like `GNU Make 4.3` when crawling `make`, without regressing CLI-attributed preference rules ([P] [NEW] [US1])
- [ ] **T126 Extend version parser for multiword vendor-prefixed names** - in `src/crawler/version.py` — AC: parse version from lines like `GNU Make <ver>` / `Foo Bar <ver>` as fallback when explicit `<cli> version` is absent, preserving anti-false-positive safeguards from T101-T102
- [ ] **T127 Unit test for bool inference in wrapped long flags without values** - in `tests/unit/test_flag_parsing_make_wrapped.py` — AC: make-style entries like `-e, --environment-overrides` and `-v, --version` remain `bool` when no explicit value token exists
- [ ] **T128 Improve bool/string inference for wrapped long flags** - in `src/crawler/parsers/flags.py` — AC: avoid promoting no-value long flags to `string` solely due wrapped descriptions; keep deterministic parsing for both inline and continuation formats
- [ ] **T129 Unit test for GNU bracketed optional-assignment option forms** - in `tests/unit/test_flag_parsing_gnu_single_dash.py` — AC: parse options like `-fcompare-debug[=<opts>]` and `-fplugin-arg-<name>-<key>[=<value>]` without silently dropping valid GNU flags ([P] [NEW] [US1])
- [ ] **T130 Extend GNU single-dash token parser for bracketed optional-assignment suffixes** - in `src/crawler/parsers/flags.py` — AC: normalize and retain bracketed optional-assignment GNU options while preserving existing T118-T120 behavior and deterministic deduplication ([NEW] [US1])
- [x] **T131 Unit test for non-mutating subcommand help fallback** - in `tests/unit/test_subcommand_help_safety.py` — AC: when `--help`/`-h`/`help <subcmd>` fail to produce help text (git.exe-on-WSL style), crawler must not execute bare mutating subcommands (`init`, `reset`, etc.) as fallback ([P] [NEW] [US1])
- [x] **T132 Implement safe subcommand help fallback policy** - in `src/crawler/detector.py` (and call sites if needed) — AC: remove/gate bare subcommand fallback behind non-mutating safety rules and return `unknown`/warning instead of executing potentially state-changing commands ([NEW] [US1])
- [x] **T133 Unit test for executable-suffix CLI canonicalization (`.exe`)** - in `tests/unit/test_cli_name_canonicalization.py` — AC: canonical CLI identity strips executable suffix for version attribution and plugin slug/id generation, while preserving original invocation command for execution ([P] [NEW] [US1])
- [x] **T134 Implement CLI canonicalization layer for executable names** - in `src/crawler/version.py` and `src/generator/plugin_generator.py` (plus shared helper if required) — AC: `git.exe` can map to canonical `git` for version parsing and generated plugin naming avoids extension-bearing IDs (`cli-git`, not `cli-git.exe`) without regressing existing CLI names ([NEW] [US1])
- [ ] **T135 Unit test for compact paired short-option rows in sectionless fallback** - in `tests/unit/test_usage_line_option_extraction.py` — AC: zip-style rows containing paired options (`-f ... -u ...`, `-q ... -v ...`) produce separate flag entries with non-empty, option-specific descriptions ([P] [NEW] [US1])
- [ ] **T136 Improve sectionless parser for compact paired short-option rows** - in `src/crawler/parsers/usage.py` — AC: split and normalize multi-option short-flag rows without reducing existing sectionless parsing quality or determinism ([NEW] [US1])
- [ ] **T137 Unit test for root help auth-precedence over best-result fallback** - in `tests/unit/test_edge_case_auth_help.py` (or dedicated detector test) — AC: when early help probes return auth-required failures, detector should not return a generic best-result fallback that masks `auth_required` semantics ([P] [NEW] [US1])
- [ ] **T138 Harden root help detection auth precedence** - in `src/crawler/detector.py` — AC: prefer structured `auth_required` outcome over non-help fallback candidates when auth signals are present, preserving existing success-path detection behavior ([NEW] [US1])
- [ ] **T139 Unit test for global-only CLI documentation fallbacks** - in `tests/unit/test_progressive_disclosure.py` (or dedicated generator test) — AC: when CLIMap has zero commands (e.g., `awk`), SKILL.md must render a non-empty version label (`unknown`), a meaningful top-level usage line, and `references/examples.md` must contain at least one generated usage example ([P] [NEW] [US1])
- [ ] **T140 Implement generator fallbacks for global-only CLIs** - in `src/generator/plugin_generator.py` — AC: avoid `v.` rendering, emit stable command-format fallback (`<cli> --help` / `<cli> --version`) when no commands exist, and synthesize examples from global/root context so plugin quality remains useful for command-line-only tools ([NEW] [US1])

**Checkpoint — US1 AC**: T009–T018, T047–T053 all pass; `pytest` exits 0; `docker` plugin generates with correct SKILL.md + `references/` structure; progressive disclosure active; Rich-Click extraction >50%; zero error-message descriptions; crawl+generate <30 s.

---

## Phase 4: User Story 2 — Manter Plugins de CLI Atualizados Automaticamente (Priority: P2)

**Goal**: Os plugins de CLI são automaticamente actualizados quando a CLI subjacente muda.

**Independent Test**: Alterar uma flag numa CLI de teste, re-executar crawler e gerador, verificar se o plugin reflecte a mudança.

### Tests for User Story 2

- [ ] **T019 Unit test for CLI version detection** - in `tests/unit/test_version_detection.py` ([P] [US2])
- [ ] **T020 Unit test for plugin outdated status logic** - in `tests/unit/test_plugin_status.py` ([P] [US2])

### Implementation for User Story 2

- [ ] **T021 Implement CLI version detection** - in `src/crawler/cli_crawler.py` ([US2])
- [ ] **T022 Implement logic to signal/regenerate outdated plugins (based on version comparison)** - in `src/generator/plugin_generator.py` ([US2])
- [ ] **T023 Integration test for `uv` CLI update and plugin regeneration** - in `tests/integration/test_uv_plugin_update.py` ([P] [US2])

**Checkpoint — US2 AC**: T019–T023 pass; US1 remains unbroken; version change in fixture CLI triggers regeneration.

---

## Phase 5: User Story 3 — Explorar CLIs Através de Interface Estruturada (Priority: P2)

**Goal**: Poder explorar qualquer CLI através de um formato estruturado e machine-readable (CLIMap JSON).

**Independent Test**: Gerar CLIMap JSON para `docker`, inspeccioná-lo com um JSON validator externo.

### Tests for User Story 3

- [ ] **T024 Unit test for CLIMap JSON schema validation** - in `tests/unit/test_climap_schema_validation.py` — validates against canonical schema from T044-reconciled `data-model.md` ([P] [US3])

### Implementation for User Story 3

- [ ] **T025 Implement robust CLIMap JSON serialisation/deserialisation** - in `src/crawler/models.py` ([US3])
- [ ] **T026 Ensure CLIMap output adheres strictly to reconciled `data-model.md` schema** - (post-T044) ([US3])
- [ ] **T027 Integration test for external tool (JSON validator / Python `jsonschema`)** - consumption of CLIMap in `tests/integration/test_climap_external_validation.py` ([P] [US3])

**Checkpoint — US3 AC**: T024–T027 pass; all US1–US3 independently functional and non-regressive.

---

## Phase 6: Polish, Cross-Cutting Concerns & Launch Readiness

**Purpose**: Improvements affecting multiple user stories, distribution, launch quality gates, and post-launch backlog. Constitution §TDD applies — tests for all Phase 6 features written FIRST.

### Tests for Phase 6 implementations (write FIRST)

- [x] **T054 Unit test for semantic keyword generation (T028)** - in `tests/unit/test_keyword_generation.py` — AC: keywords are domain-relevant, not first-word extractions; no stopwords ([P] [NEW])
- [x] **T055 Unit test for author configuration (T029)** - in `tests/unit/test_author_config.py` — AC: `--author` flag sets author; omitting flag produces no `author` field in `plugin.json` ([P] [NEW])
- [ ] **T056 Unit test for observability/structured logging (T030)** - in `tests/unit/test_observability.py` — AC: pipeline emits structured log entries with level, stage, CLI name, duration ([P] [NEW])
- [ ] **T057 Unit test for confidence score calculation (T034)** - in `tests/unit/test_confidence_calculator.py` — AC: score in [0.0, 1.0]; known-good fixture produces score >0.8; ambiguous type fixture produces score <0.6 ([P] [NEW])
- [ ] **T058 Unit test for token optimizer (T035)** - in `tests/unit/test_token_optimizer.py` — AC: SKILL.md output for docker is <800 tokens; references/commands.md is not loaded in compact path ([P] [NEW])

### Implementations

- [ ] **T030 Implement detailed observability** - in `src/lib/observability.py` — structured logging (stdlib only), per-stage metrics (crawl/parse/generate), basic tracing for bottleneck identification
- [ ] **T031 Integrate logging, metrics, tracing across crawler and generator components**
- [ ] **T033 Code cleanup and refactoring across the codebase** - fix `_separate_global_flags` no-op (both paths return same result); add `TypedDict` annotations to `src/crawler/formatter.py` serialisation shapes; add `py.typed` marker
- [ ] **T034 Implement confidence score calculation logic** - in `src/crawler/confidence_calculator.py` — per-flag score (FR-010); penalise ambiguous types, empty descriptions, runtime-error descriptions ([P])
- [ ] **T035 Benchmark and optimise token cost** - in `src/generator/token_optimizer.py` — validate SC-002 (≥5× reduction vs raw `--help`); document comparison table ([P])
- [ ] **T036 Benchmark and optimise crawl/parsing performance** - in `tests/performance/test_performance.py` — validate SC-004 (<30 s for docker), SC-009 (<5 s for 10 000-line fixture), SC-008 (50 CLIs in batches of 10 in parallel) ([P])
- [ ] **T037 Update `README.md`** - add demo GIF (`vhs`), "Why Not Just `--help`?" section, comparison table vs tldr/cheat.sh/man/jc, PyPI badges, shorten to <250 lines *(SC-007)*

### Distribution & Launch Readiness

- [ ] **T059 Verify pyproject.toml PyPI publish readiness (post-T038)** - `uv build && twine check dist/*` produces no errors; all metadata renders correctly on PyPI test server ([NEW])
- [ ] **T060 Test clean install on fresh Python 3.11 venv** - `pip install cli-plugins && cli-crawler docker -o docker.json && generate-plugin docker.json` succeeds end-to-end *(SC-005)* ([P] [NEW])
- [ ] **T061 Publish to PyPI** - `twine upload dist/*`; verify `pip install cli-plugins` works from PyPI *(SC-005)* ([NEW])

### CLI Coverage Expansion

- [ ] **T062 Crawl 13+ additional CLIs and fix parser issues found** - `kubectl`, `terraform`, `aws`, `gcloud`, `az`, `cargo`, `go`, `rustup`, `helm`, `poetry`, `pdm`, `rye`, `mise`, `pnpm` — AC: each produces valid CLIMap JSON, no crashes *(SC-001; execution-plan A11)* ([NEW])

### Quality Validation Gates

- [ ] **T063 SC-006 manual validation** - test 10 representative CLI tasks with real Claude Code + generated plugin (docker, git, gh, uv); document results; AC: ≥90% correct answers without hallucination or unnecessary clarification *(SC-006)* ([P] [NEW])
- [ ] **T064 SC-010 reliability test** - crawl 20 CLIs sequentially and in parallel batches; measure success rate; AC: >99% crawl success rate *(SC-010)* ([P] [NEW])

### Documentation & Contracts

- [ ] **T065 Update `specs/001-cli-plugins-base/contracts/plugin-contract.md` to reflect** - actual Markdown output format (SKILL.md + references/commands.md + references/examples.md + plugin.json) — remove YAML structural references which do not match the real generator output *(M4)* ([P] [NEW])

### Configuration Hygiene (Operational, Repetitive)

- [x] **T069 Define and document minimal-override policy for `config.yaml`** - in `README.md` (and/or `docs/config-policy.md`): keep only CLI-specific overrides that differ from defaults (`environment`, `help_pattern`, `max_depth`, `max_concurrent`, `plugins.discovery_command`); avoid inventory-style static entries duplicated from `output/*.json`/`plugins/` ([NEW])
- [x] **T070 Implement config inventory audit tool (`scripts/config_audit.py` or** - `src/config/audit.py` + CLI hook) that compares configured CLIs (`config.yaml`) vs crawled CLIs (`output/*.json`, excluding `*.raw.json`) vs generated plugins (`plugins/cli-*`); output categories: `missing_in_config`, `stale_in_config`, `missing_output`, `missing_plugin`, plus suggested minimal overrides ([P] [NEW])
- [x] **T071 Add unit tests for config audit logic** - in `tests/unit/test_config_audit.py` covering empty dirs, partial overlap, stale config entries, and CLIs present only in output/plugins ([P] [NEW])
- [x] **T072 Add repeatable runbook/checklist** - in `README.md` and `CLAUDE.local.md`: run config audit after each crawl batch and before PR; store latest report in `output/config-audit.json` ([NEW])

### CLI Group Inference (No-LLM, Deterministic + Classical ML)

- [ ] **T073 Define canonical CLI group taxonomy + evidence schema** - in `src/config/group_taxonomy.yaml` (or `src/config/group_taxonomy.py`) and document allowed groups/evidence signals in `README.md` (no LLM/agent dependency) ([NEW])
- [ ] **T074 Add RED tests for deterministic group inference** - in `tests/unit/test_group_inference_deterministic.py` using fixtures from `output/*.json`: validate group inference from explicit config group, command lexicon, flags, and package metadata hints ([P] [NEW])
- [ ] **T075 Implement deterministic group inference engine** - in `src/config/group_inference.py` (rule-based scoring + fuzzy matching via `rapidfuzz`) and integrate with `config-audit` report ([NEW])
- [ ] **T076 Add RED tests for classical-ML fallback** - in `tests/unit/test_group_inference_ml.py`: TF-IDF feature extraction from CLIMap text, confidence thresholding, and deterministic-first precedence ([P] [NEW])
- [ ] **T077 Implement classical-ML fallback** - scikit-learn `TfidfVectorizer` + `LogisticRegression`/`LinearSVC`) in `src/config/group_classifier.py` with train/eval utility script `scripts/train_group_classifier.py` ([NEW])
- [ ] **T078 Extend audit/report contract and docs** - include `group_inferred`, `group_confidence`, `group_evidence`, `group_conflict_with_config` in `output/config-audit.json` and update operational runbook in `README.md` + `CLAUDE.local.md` ([NEW])

## Phase 7: Dashboard UI & Operations Cockpit (Research → Architecture → Build) (Priority: P3)

**Goal**: Expor as capacidades da solução via UI ergonómica (gestão, observabilidade, ações, inventário) com operação segura e auditável.

**Independent Test**: Operador abre dashboard, valida inventário de CLIs/plugins, executa ação (`cli-crawler`/`generate-plugin`/`config-audit`) e observa resultado/logs sem usar terminal.

### Discovery & Architecture (skill-driven)

- [ ] **T103 Run structured discovery for dashboard scope using skills** - `requirements-discovery` + `discovery-pack`; produce `specs/002-dashboard-ui/discovery.md` with personas, JTBD, primary workflows, non-goals, risks, and success metrics ([NEW])
- [ ] **T104 Produce architecture blueprint** - via `blueprint-maturation` + `architect-review`; deliver `specs/002-dashboard-ui/plan.md` + ADR candidates for backend/frontend stack, data flow (`output/`, `plugins/`, audit reports), security model, and deployment topology ([P] [NEW])
- [ ] **T105 Produce UX/IA specification** - via `frontend-design`; create `specs/002-dashboard-ui/ux-spec.md` with navigation map, panel wireframes, accessibility constraints (WCAG AA), and responsive breakpoints (desktop/mobile) ([P] [NEW])

### Tests for Phase 7 (write FIRST)

- [ ] **T106 Add backend API contract tests** - in `tests/integration/test_dashboard_api_contracts.py` for inventory summary, plugin detail, observability metrics, and action status endpoints ([P] [NEW])
- [ ] **T107 Add Playwright E2E tests** - in `tests/end_to_end/test_dashboard_e2e.py` covering inventory exploration, plugin inspection, action trigger, and execution-log/result validation ([P] [NEW])
- [ ] **T108 Add accessibility/responsive tests** - in `tests/end_to_end/test_dashboard_accessibility.py` — keyboard navigation, landmarks/labels, contrast checks, and mobile viewport sanity ([P] [NEW])

### Implementation

- [ ] **T109 Implement dashboard backend read API** - in `src/dashboard/api.py` (or equivalent) aggregating inventory/health from `output/*.json`, `plugins/cli-*`, `output/config-audit.json`, and observability metrics ([NEW])
- [ ] **T110 Implement controlled action service** - in `src/dashboard/actions.py` for `cli-crawler`, `generate-plugin`, and `config-audit` with status lifecycle, timeout guards, and structured execution logs ([NEW])
- [ ] **T111 Implement frontend app shell** - in `web/dashboard/` with ergonomic navigation (sidebar + top status bar + quick actions), design tokens, and responsive layout ([NEW])
- [ ] **T112 Build inventory management panels** - in `web/dashboard/src/features/inventory/` with CLI/plugin lists, health badges, and drift indicators (`stale_in_config`, `missing_output`, `missing_plugin`) ([P] [NEW])
- [ ] **T113 Build observability panels** - in `web/dashboard/src/features/observability/` with run durations, success/failure trends, warning/error timeline, and filter controls ([P] [NEW])
- [ ] **T114 Build operations/actions console** - in `web/dashboard/src/features/actions/` to trigger workflows, stream logs, and surface generated artifacts ([P] [NEW])
- [ ] **T115 Build plugin workbench views** - in `web/dashboard/src/features/plugins/` (command tree, flags table, examples preview, run-to-run diff) ([NEW])
- [ ] **T116 Integrate backend/frontend contracts** - typed models (e.g., `web/dashboard/src/lib/api-types.ts`) and schema validation to prevent UI/API drift ([NEW])
- [ ] **T117 Document dashboard operations and troubleshooting** - in `docs/dashboard.md` + `README.md` (startup, env vars, safety notes, rollback path) ([NEW])

**Checkpoint — Phase 7 AC**: Dashboard loads in desktop/mobile, inventory and observability panels render real project data, actions execute safely with visible status/logs, and E2E + accessibility tests pass.

### Future Backlog (DEFERRED — post-v1.0)

- [ ] **T068 co-author-injection** - add `Co-Authored-By: <author>` trailer to generated `scripts/rescan.sh` commit template (Option A from `.ideas/co-author-injection.md`); low priority, implement after v1.0 stabilises *(L1)* ([DEFERRED] [NEW])

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup + Blockers)**: No dependencies — start immediately. CI/CD (T032) must be green before Phase 2 begins.
- **Phase 2 (Foundational)**: Depends on Phase 1 completion — BLOCKS all user stories. Includes parser quality gate (T041, T042) and progressive disclosure (T040).
- **User Stories (Phases 3–5)**: All depend on Phase 2 completion; can proceed in parallel if staffed. Priority order: US1 (P1) → US2/US3 (P2).
- **Polish (Phase 6)**: Depends on all desired user stories being complete. Tests for Phase 6 tasks written before their implementations.
- **Phase 7 (Dashboard UI)**: Discovery (`T103–T105`) can start after current US1 hardening; implementation depends on observability + inventory baselines from Phase 6 (`T030–T031`, `T070–T072`, `T078`).

### Task-Level Dependencies (key)

- T038 → T039 (entry points only after pyproject.toml is fixed)
- T006 + T044 → T025, T026 (schema reconciled before serialisation)
- T040 → T016 (progressive disclosure before plugin conversion)
- T041, T042 → T012 (parser improvements before parser quality test is meaningful)
- T043 → T036 (thread safety before parallel performance benchmark)
- T045, T046 → T049, T050, T051 (parser fixes before edge-case implementation)
- T079 → T080 → T081 (pnpm grouped-help regression path: RED parser test → parser implementation → integration/E2E gate)
- T082 → T083 (embedded-help dedup test before dedup implementation)
- T089 → T090 (embedded-help boundary filtering: RED contamination test before parser boundary implementation)
- T091 → T092 (sectionless usage-line option extraction: RED test before parser fallback implementation)
- T093 → T094 (placeholder-version suffix tests before expanded fallback logic)
- T095 → T096 (description normalization for sectionless fallback)
- T097 → T098 (long-option enrichment for sectionless fallback)
- T099 → T100 (attached-value/combined-short parsing tests before robust option-atom parser update)
- T101 → T102 (version-source preference tests before CLI-name-aware version selection)
- T118 → T119 → T120 (gcc/GNU single-dash flags: RED unit → parser extension → integration/E2E gate)
- T121 → T122 (sectionless single-space + numeric pseudo-flag hardening)
- T123 → T124 (perl-style short attached metavars normalization hardening)
- T125 → T126 (vendor-prefixed multiword version parsing hardening)
- T127 → T128 (wrapped long-flag bool/string inference hardening)
- T129 → T130 (GNU bracketed optional-assignment flag-form hardening)
- T131 → T132 (subcommand help fallback safety hardening)
- T133 → T134 (executable-suffix CLI canonicalization hardening)
- T135 → T136 (compact paired short-option row parsing hardening)
- T137 → T138 (root help auth-precedence hardening)
- T139 → T140 (global-only CLI doc quality hardening)
- T028, T029 → T054, T055 (implementations before their unit tests — Phase 6 tests write after Phase 2 impl)
- T059 → T060 → T061 (PyPI readiness → clean install test → publish)
- T069 → T070 → T071 → T072 (minimal config policy before automated drift audit + operational checklist)
- T070/T071/T072 → T062 (stabilise config/inventory hygiene before large CLI coverage expansion)
- T073 → T074 → T075 → T076 → T077 → T078 (taxonomy-first, deterministic inference first, ML fallback second)
- T075/T078 → future grouped-plugin generation epic (multi-CLI plugin per inferred domain/group)
- T103 → T104 → T105 (discovery before architecture before UX spec)
- T103/T104/T105 → T106/T107/T108 (contracts and E2E tests written from approved spec set)
- T030/T031 + T070/T072 + T078 → T109/T110 (dashboard backend depends on observability + inventory audit baselines)
- T106 → T109/T110 (backend contracts before implementation)
- T107/T108 → T111/T112/T113/T114/T115 (UX + accessibility tests before frontend feature implementation)
- T109/T110/T111/T112/T113/T114/T115 → T116 → T117 (integration typing, then operational documentation)

### Parallel Opportunities

- All `[P]`-marked tasks within a phase can run concurrently
- Phase 2 parser tasks (T041, T042, T043, T044, T045, T046) are all parallel after T006+T007
- Phase 6 test tasks (T054–T058) all parallel; Phase 6 implementations all parallel after their tests
- CLI expansion (T062) and quality validation (T063, T064) can run in parallel after US1 complete

---

## Implementation Strategy

### MVP First (User Story 1 + Phase 1+2 prereqs)

1. Complete Phase 1: Setup + Blockers (T001–T005, T032, T038, T039, T066)
2. Complete Phase 2: Foundational + Parser Quality — **CRITICAL, blocks all stories**
3. Complete Phase 3: US1 (with edge cases + smoke perf test)
4. **STOP AND VALIDATE**: All Phase 3 ACs met; regenerate docker/git/gh plugins; check scores >3.5/5
5. Ship PyPI (T059–T061) + Launch (T037 + T062 + T063 + T064)

### Incremental Delivery

1. Phase 1 + 2 → Foundational ready (parser quality improved)
2. US1 → MVP with 3+ high-quality plugins → Demo GIF → HN Launch
3. US2 → Auto-update → Demo
4. US3 → Structured interface → Demo
5. Phase 6 Polish → PyPI → 20+ Plugins → Full Launch

### Notes

- `[P]` = different files, no shared state, safe to parallelise
- `[NEW]` = added by speckit.analyze cross-artifact analysis (2026-02-13)
- `[MOVED]` = relocated from original phase for ordering correctness (T028, T029 from Phase 6→2; T032 from Phase 6→1)
- Verify tests FAIL before implementing
- Commit after each task or logical group (micro-commits, constitution §Micro-Commits)
- Stop at any checkpoint to validate story independently
- `CLAUDE.local.md` is the source of truth for current task status
