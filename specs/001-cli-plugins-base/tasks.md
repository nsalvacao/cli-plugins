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

- [ ] T001 Create project directories: `src/crawler`, `src/generator`, `src/config`, `src/lib`, `tests/unit`, `tests/integration`, `tests/end_to_end` — **decision**: migrate existing `crawler/` → `src/crawler/` (preserve git history with `git mv`)
- [ ] T002 Initialize Python project with `pyproject.toml` in repository root *(exists — bugs fixed in T038)*
- [ ] T038 [NEW] Fix known `pyproject.toml` bugs: move `classifiers` from `[project.urls]` to `[project]`; fix `readme` path from `docs/README.md` to `README.md`; add `[build-system]` section with `hatchling` — verify with `uv build && twine check dist/*` *(Blocker B1 — evaluation-results_v2)*
- [ ] T039 [NEW] Register `generate-plugin` as CLI entry point in `pyproject.toml` `[project.scripts]`: `generate-plugin = "generator.plugin_generator:main"` — verify `pip install -e . && generate-plugin --help` works *(Blocker B2)*
- [ ] T003 Configure basic `config.yaml` in `src/config/config.yaml`
- [ ] T004 [P] Configure linting and formatting (Black, Ruff) in `pyproject.toml` — add `[tool.black]` and `[tool.ruff]` sections; verify `ruff check src/ tests/` runs clean
- [ ] T005 [P] Setup Pytest for testing in `pyproject.toml` — add `[tool.pytest.ini_options]` with testpaths, markers for unit/integration/e2e
- [ ] T032 [MOVED from Phase 6] Create CI/CD pipeline: `.github/workflows/ci.yml` — pytest matrix on Python 3.11+3.12, ruff lint, black check; runs on push and PR; add CI badge to `README.md` *(constitution §CI/CD Automatizado; execution-plan A7)*
- [ ] T066 [P] [NEW] Add `__version__` to package via `src/__init__.py` sourced from `pyproject.toml`; add `--version` flag to `cli-crawler` and `generate-plugin` entry points *(evaluation-results A5, L3)*

**Checkpoint — Phase 1 AC**: `pip install -e '.[dev]'` succeeds; `pytest` discovers tests; `ruff check src/` exits 0; `npx ci` green; `cli-crawler --version` outputs version string.

---

## Phase 2: Foundational (Blocking Prerequisites + Parser Quality)

**Purpose**: Core infrastructure and parser quality gates MUST be complete before ANY user story can be implemented. Semantic keywords and author config moved here from Phase 6 — both are launch blockers per evaluation-results_v2.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T006 Create CLIMap schema (`CLI`, `CLIMap`, `Command`, `Flag`, `Plugin` entities) in `src/crawler/models.py` — reconcile with data-model.md (see T044)
- [ ] T044 [P] [NEW] Reconcile schema inconsistency: `data-model.md` defines `Flag.long_name` + `Flag.short_name` separately; `crawler/models.py` uses `name` + `short`. Decide canonical naming, update both `models.py` and `data-model.md` to match. Add migration note. *(M3)*
- [ ] T007 Implement safe subprocess execution utility in `src/lib/subprocess_utils.py` — `subprocess.run` with tokenised args only, no `shell=True`, timeout enforcement, SAFE_ENV (disable colour/pager)
- [ ] T067 [P] [NEW] Security review: audit `crawler/executor._build_command` Windows PowerShell path — confirm no shell-injection risk when joining command array for PowerShell; add unit test covering edge case *(evaluation-results §5 WARN, L4)*
- [ ] T008 Configure basic logging infrastructure in `src/lib/logger.py` — **use Python stdlib `logging` module only; NO external packages** (FR-008, constitution §Zero Dependencies); structured levels (DEBUG/INFO/WARNING/ERROR); configurable via env var `CLI_PLUGINS_LOG_LEVEL`
- [ ] T028 [MOVED from Phase 6] [P] Implement semantic keyword generation for plugins in `src/generator/plugin_generator.py` — keywords derived from CLI name + top command group names + domain terms extracted from description (NOT first words of command descriptions) *(FR-012; Blocker B5)*
- [ ] T029 [MOVED from Phase 6] [P] Implement author configuration for plugins in `src/generator/plugin_generator.py` — `--author` CLI flag or `CLI_PLUGINS_AUTHOR` env var; omit `author` field entirely when not specified; community generators must not carry hardcoded attribution *(FR-011; Blocker B6)*
- [ ] T040 [NEW] Implement progressive disclosure in `src/generator/plugin_generator.py` — SKILL.md compact view (≤800 tokens: top-level commands + global flags + 5 examples); `references/commands.md` (full flag tables, loaded on demand); `references/examples.md` (all examples, loaded on demand) *(FR-004; constitution §Auto-Geração e Otimização)*
- [ ] T041 [NEW] Improve Rich-Click parser in `src/crawler/parsers/` to correctly extract flags from box-drawing (`╭─╮│`) formatted output — currently extracts 7 flags from 51 commands (cli-claude-flow 2.55/5); target: >50% extraction rate for Rich-Click CLIs *(SC-003; evaluation-results I4; CRITICAL C2)*
- [ ] T042 [P] [NEW] Improve man page example extraction in `src/crawler/parsers/manpage.py` — fix zero-examples issue for npm-style man page CLIs; target: extract documented examples from `EXAMPLES` section *(SC-003; evaluation-results §1.4)*
- [ ] T043 [P] [NEW] Add thread-safety locks to `CrawlState` in `src/crawler/discovery.py` — `threading.Lock()` on `visited`, `errors`, `warnings` sets to prevent race conditions under `ThreadPoolExecutor` *(SC-008; evaluation-results R8)*
- [ ] T045 [P] [NEW] Fix error messages captured as descriptions — extend `_clean_description` in `src/crawler/parser.py` with patterns: runtime errors (`fatal:`, `error:`, `accepts N arg(s)`), circular names (description == command name), state messages (`already initialized`) *(Blocker B3; evaluation-results §8 B3)*
- [ ] T046 [P] [NEW] Fix git plugin code fence formatting in `src/generator/plugin_generator.py` — ensure description text does not leak outside fenced ` ``` ` blocks in `examples.md` output *(Blocker B4; evaluation-results §8 B4)*

**Checkpoint — Phase 2 AC**: All schema entities importable; subprocess utils pass security tests; Rich-Click flag extraction rate >50% for `claude-flow`; `plugin.json` has semantic keywords and no hardcoded author; SKILL.md + `references/` structure generated correctly for docker; zero error-message descriptions in regenerated git/gh plugins.

---

## Phase 3: User Story 1 — Obter Conhecimento Preciso de uma CLI (Priority: P1) 🎯 MVP

**Goal**: O assistente de IA pode dar comandos e flags precisos para qualquer CLI instalada, sem "alucinar" ou dar informações desatualizadas.

**Independent Test**: Instalar plugin `docker` gerado e usar Claude Code para perguntar sobre `docker run --gpus`. O assistente deve responder com a flag correcta.

### Tests for User Story 1 (write FIRST — ensure they FAIL before implementation)

- [ ] T009 [P] [US1] Unit test for initial CLI crawling (e.g., `git --help`) in `tests/unit/test_cli_crawler_basic.py`
- [ ] T010 [P] [US1] Unit test for basic flag extraction in `tests/unit/test_flag_parsing_basic.py`
- [ ] T011 [P] [US1] Unit test for basic command hierarchy parsing in `tests/unit/test_command_parsing_basic.py`
- [ ] T012 [P] [US1] Unit test for Rich-Click/man page parsing quality in `tests/unit/test_parsing_rich_man.py` — AC: Rich-Click extraction rate >50%; man page examples extracted for npm-equivalent fixture
- [ ] T047 [P] [NEW] [US1] Unit test for EC-01: CLI without standard `--help` → parser emits warning, returns partial CLIMap, does not crash; in `tests/unit/test_edge_case_no_help.py`
- [ ] T048 [P] [NEW] [US1] Unit test for EC-02: CLI requiring auth for `--help` (simulated via timeout/exit-code) → clear error message, no hang; in `tests/unit/test_edge_case_auth_help.py`
- [ ] T049 [P] [NEW] [US1] Unit test for EC-05: `--help` output >10 000 lines → progressive loading triggered, SKILL.md compact, references/ on-demand; in `tests/unit/test_edge_case_long_help.py`

### Implementation for User Story 1

- [ ] T013 [US1] Implement basic CLI crawling logic to execute `CLI --help` in `src/crawler/cli_crawler.py`
- [ ] T014 [US1] Implement core parsing logic for basic CLI formats (Go/Cobra, Python/Click) in `src/crawler/parser.py`
- [ ] T015 [US1] Implement pipeline orchestrator to manage crawl and parse steps in `src/crawler/pipeline.py`
- [ ] T016 [US1] Implement CLIMap-to-AI-Plugin conversion in `src/generator/plugin_generator.py` — delegates progressive disclosure to T040 implementation
- [ ] T050 [P] [NEW] [US1] Implement EC-01 handling: graceful degradation for non-standard `--help` (warnings emitted to logger, partial CLIMap returned, confidence_score penalised); in `src/crawler/cli_crawler.py`
- [ ] T051 [P] [NEW] [US1] Implement EC-02 handling: detect auth-required `--help` (exit-code, timeout, stderr patterns) → fail with structured error, no process hang; in `src/crawler/executor.py` / `subprocess_utils.py`
- [ ] T052 [P] [NEW] [US1] Implement EC-05 handling: when raw `--help` > configurable line threshold (default 10 000), activate chunked progressive loading in pipeline; store full detail in `references/` only; in `src/crawler/pipeline.py`
- [ ] T017 [P] [US1] Integration test for `CLI --help → CLIMap JSON` (docker) in `tests/integration/test_docker_climap_generation.py`
- [ ] T018 [P] [US1] E2E test for `CLI → CLIMap → Plugin` (mocking AI Assistant interaction) in `tests/end_to_end/test_docker_plugin_e2e.py`
- [ ] T053 [P] [NEW] Performance smoke test: `docker` crawl + generate completes in <30 s; parsing a 1 000-line help fixture in <5 s; in `tests/performance/test_smoke_perf.py` *(SC-004 early validation — prevents late discovery)*

**Checkpoint — US1 AC**: T009–T018, T047–T053 all pass; `pytest` exits 0; `docker` plugin generates with correct SKILL.md + `references/` structure; progressive disclosure active; Rich-Click extraction >50%; zero error-message descriptions; crawl+generate <30 s.

---

## Phase 4: User Story 2 — Manter Plugins de CLI Atualizados Automaticamente (Priority: P2)

**Goal**: Os plugins de CLI são automaticamente actualizados quando a CLI subjacente muda.

**Independent Test**: Alterar uma flag numa CLI de teste, re-executar crawler e gerador, verificar se o plugin reflecte a mudança.

### Tests for User Story 2

- [ ] T019 [P] [US2] Unit test for CLI version detection in `tests/unit/test_version_detection.py`
- [ ] T020 [P] [US2] Unit test for plugin outdated status logic in `tests/unit/test_plugin_status.py`

### Implementation for User Story 2

- [ ] T021 [US2] Implement CLI version detection in `src/crawler/cli_crawler.py`
- [ ] T022 [US2] Implement logic to signal/regenerate outdated plugins (based on version comparison) in `src/generator/plugin_generator.py`
- [ ] T023 [P] [US2] Integration test for `uv` CLI update and plugin regeneration in `tests/integration/test_uv_plugin_update.py`

**Checkpoint — US2 AC**: T019–T023 pass; US1 remains unbroken; version change in fixture CLI triggers regeneration.

---

## Phase 5: User Story 3 — Explorar CLIs Através de Interface Estruturada (Priority: P2)

**Goal**: Poder explorar qualquer CLI através de um formato estruturado e machine-readable (CLIMap JSON).

**Independent Test**: Gerar CLIMap JSON para `docker`, inspeccioná-lo com um JSON validator externo.

### Tests for User Story 3

- [ ] T024 [P] [US3] Unit test for CLIMap JSON schema validation in `tests/unit/test_climap_schema_validation.py` — validates against canonical schema from T044-reconciled `data-model.md`

### Implementation for User Story 3

- [ ] T025 [US3] Implement robust CLIMap JSON serialisation/deserialisation in `src/crawler/models.py`
- [ ] T026 [US3] Ensure CLIMap output adheres strictly to reconciled `data-model.md` schema (post-T044)
- [ ] T027 [P] [US3] Integration test for external tool (JSON validator / Python `jsonschema`) consumption of CLIMap in `tests/integration/test_climap_external_validation.py`

**Checkpoint — US3 AC**: T024–T027 pass; all US1–US3 independently functional and non-regressive.

---

## Phase 6: Polish, Cross-Cutting Concerns & Launch Readiness

**Purpose**: Improvements affecting multiple user stories, distribution, launch quality gates, and post-launch backlog. Constitution §TDD applies — tests for all Phase 6 features written FIRST.

### Tests for Phase 6 implementations (write FIRST)

- [ ] T054 [P] [NEW] Unit test for semantic keyword generation (T028) in `tests/unit/test_keyword_generation.py` — AC: keywords are domain-relevant, not first-word extractions; no stopwords
- [ ] T055 [P] [NEW] Unit test for author configuration (T029) in `tests/unit/test_author_config.py` — AC: `--author` flag sets author; omitting flag produces no `author` field in `plugin.json`
- [ ] T056 [P] [NEW] Unit test for observability/structured logging (T030) in `tests/unit/test_observability.py` — AC: pipeline emits structured log entries with level, stage, CLI name, duration
- [ ] T057 [P] [NEW] Unit test for confidence score calculation (T034) in `tests/unit/test_confidence_calculator.py` — AC: score in [0.0, 1.0]; known-good fixture produces score >0.8; ambiguous type fixture produces score <0.6
- [ ] T058 [P] [NEW] Unit test for token optimizer (T035) in `tests/unit/test_token_optimizer.py` — AC: SKILL.md output for docker is <800 tokens; references/commands.md is not loaded in compact path

### Implementations

- [ ] T030 Implement detailed observability in `src/lib/observability.py` — structured logging (stdlib only), per-stage metrics (crawl/parse/generate), basic tracing for bottleneck identification
- [ ] T031 Integrate logging, metrics, tracing across crawler and generator components
- [ ] T033 Code cleanup and refactoring across the codebase — fix `_separate_global_flags` no-op (both paths return same result); add `TypedDict` annotations to `src/crawler/formatter.py` serialisation shapes; add `py.typed` marker
- [ ] T034 [P] Implement confidence score calculation logic in `src/crawler/confidence_calculator.py` — per-flag score (FR-010); penalise ambiguous types, empty descriptions, runtime-error descriptions
- [ ] T035 [P] Benchmark and optimise token cost in `src/generator/token_optimizer.py` — validate SC-002 (≥5× reduction vs raw `--help`); document comparison table
- [ ] T036 [P] Benchmark and optimise crawl/parsing performance in `tests/performance/test_performance.py` — validate SC-004 (<30 s for docker), SC-009 (<5 s for 10 000-line fixture), SC-008 (50 CLIs in batches of 10 in parallel)
- [ ] T037 Update `README.md` — add demo GIF (`vhs`), "Why Not Just `--help`?" section, comparison table vs tldr/cheat.sh/man/jc, PyPI badges, shorten to <250 lines *(SC-007)*

### Distribution & Launch Readiness

- [ ] T059 [NEW] Verify pyproject.toml PyPI publish readiness (post-T038): `uv build && twine check dist/*` produces no errors; all metadata renders correctly on PyPI test server
- [ ] T060 [P] [NEW] Test clean install on fresh Python 3.11 venv: `pip install cli-plugins && cli-crawler docker -o docker.json && generate-plugin docker.json` succeeds end-to-end *(SC-005)*
- [ ] T061 [NEW] Publish to PyPI: `twine upload dist/*`; verify `pip install cli-plugins` works from PyPI *(SC-005)*

### CLI Coverage Expansion

- [ ] T062 [NEW] Crawl 13+ additional CLIs and fix parser issues found: `kubectl`, `terraform`, `aws`, `gcloud`, `az`, `cargo`, `go`, `rustup`, `helm`, `poetry`, `pdm`, `rye`, `mise`, `pnpm` — AC: each produces valid CLIMap JSON, no crashes *(SC-001; execution-plan A11)*

### Quality Validation Gates

- [ ] T063 [P] [NEW] SC-006 manual validation: test 10 representative CLI tasks with real Claude Code + generated plugin (docker, git, gh, uv); document results; AC: ≥90% correct answers without hallucination or unnecessary clarification *(SC-006)*
- [ ] T064 [P] [NEW] SC-010 reliability test: crawl 20 CLIs sequentially and in parallel batches; measure success rate; AC: >99% crawl success rate *(SC-010)*

### Documentation & Contracts

- [ ] T065 [P] [NEW] Update `specs/001-cli-plugins-base/contracts/plugin-contract.md` to reflect actual Markdown output format (SKILL.md + references/commands.md + references/examples.md + plugin.json) — remove YAML structural references which do not match the real generator output *(M4)*

### Future Backlog (DEFERRED — post-v1.0)

- [ ] T068 [DEFERRED] [NEW] co-author-injection: add `Co-Authored-By: <author>` trailer to generated `scripts/rescan.sh` commit template (Option A from `.ideas/co-author-injection.md`); low priority, implement after v1.0 stabilises *(L1)*

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup + Blockers)**: No dependencies — start immediately. CI/CD (T032) must be green before Phase 2 begins.
- **Phase 2 (Foundational)**: Depends on Phase 1 completion — BLOCKS all user stories. Includes parser quality gate (T041, T042) and progressive disclosure (T040).
- **User Stories (Phases 3–5)**: All depend on Phase 2 completion; can proceed in parallel if staffed. Priority order: US1 (P1) → US2/US3 (P2).
- **Polish (Phase 6)**: Depends on all desired user stories being complete. Tests for Phase 6 tasks written before their implementations.

### Task-Level Dependencies (key)

- T038 → T039 (entry points only after pyproject.toml is fixed)
- T006 + T044 → T025, T026 (schema reconciled before serialisation)
- T040 → T016 (progressive disclosure before plugin conversion)
- T041, T042 → T012 (parser improvements before parser quality test is meaningful)
- T043 → T036 (thread safety before parallel performance benchmark)
- T045, T046 → T049, T050, T051 (parser fixes before edge-case implementation)
- T028, T029 → T054, T055 (implementations before their unit tests — Phase 6 tests write after Phase 2 impl)
- T059 → T060 → T061 (PyPI readiness → clean install test → publish)

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
