# Contributing

Contributions are welcome. This guide covers the development workflow.

## Setup

```bash
git clone https://github.com/nsalvacao/cli-plugins.git
cd cli-plugins
uv sync
```

## Development Workflow

1. **Make changes** to crawler (`crawler/`) or generator (`scripts/generate_plugin.py`)
2. **Run tests**: `uv run python -m pytest tests/ -v`
3. **Test with a real CLI**: `uv run python cli_crawler.py <cli> -o output/<cli>.json -v`
4. **Generate a plugin**: `uv run python scripts/generate_plugin.py output/<cli>.json`
5. **Verify the plugin**: inspect generated files in `plugins/cli-<cli>/`

## Adding a New CLI Configuration

Edit `config.yaml`:

```yaml
clis:
  new-tool:
    max_depth: 5
    group: category-name
```

Then crawl: `uv run python cli_crawler.py new-tool -o output/new-tool.json -v`

## Adding Test Fixtures

1. Capture raw help text: `new-tool --help > tests/fixtures/new-tool-root.txt`
2. Add parse tests in `tests/test_pipeline_integration.py`
3. Add section tests in `tests/test_parser_sections.py` if the format is new

## Code Style

- Python 3.11+ with type hints
- No external dependencies for crawler or generator (stdlib only)
- Keep files under 500 lines
- Tests go in `tests/`, never in root

## Pull Requests

- One feature per PR
- All tests must pass: `uv run python -m pytest tests/ -v`
- Include test fixtures for new CLI formats
- Update `config.yaml` if adding a new CLI
