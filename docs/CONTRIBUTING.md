# Contributing to cli-plugins

We welcome and appreciate all contributions to the `cli-plugins` project! By participating, you agree to uphold our [Code of Conduct](../CODE_OF_CONDUCT.md).

This guide outlines the development workflow and how you can get involved.

## Table of Contents

- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Contributing Code](#contributing-code)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Community & Ecosystem](#community--ecosystem)

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on our [GitHub Issues page](https://github.com/nsalvacao/cli-plugins/issues) and include:

- A clear and concise description of the bug.
- Steps to reproduce the behavior.
- Expected behavior.
- Actual behavior.
- Screenshots or error messages if applicable.
- Your environment (OS, Python version, `uv` version).

### Suggesting Features

We love new ideas! If you have a feature request, please open an issue on our [GitHub Issues page](https://github.com/nsalvacao/cli-plugins/issues) and include:

- A clear and concise description of the feature.
- The problem it solves.
- Any alternative solutions you've considered.

### Contributing Code

1.  **Fork** the repository on GitHub.
2.  **Clone** your forked repository to your local machine.
    ```bash
    git clone https://github.com/YOUR_USERNAME/cli-plugins.git
    cd cli-plugins
    ```
3.  **Setup your development environment** as described in [Development Setup](#development-setup).
4.  **Create a new branch** for your feature or bug fix.
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/fix-bug-description
    ```
5.  **Make your changes**. Ensure your code adheres to our [Code Style Guidelines](#code-style-guidelines).
    - For changes to the crawler (`crawler/`) or generator (`scripts/generate_plugin.py`)
    - For adding a new CLI configuration, edit `config.yaml` as described in the existing documentation.
6.  **Run tests**: `uv run python -m pytest tests/ -v` to ensure everything is working as expected and all tests pass.
7.  **Test with a real CLI**: `uv run python cli_crawler.py <cli> -o output/<cli>.json -v` to verify your changes.
8.  **Generate a plugin**: `uv run python scripts/generate_plugin.py output/<cli>.json` and verify the output.
9.  **Commit your changes** using our [Commit Message Guidelines](#commit-message-guidelines).
    ```bash
    git commit -m "feat: Add new feature"
    ```
10. **Push** your branch to your forked repository.
    ```bash
    git push origin feature/your-feature-name
    ```
11. **Open a Pull Request** against the `main` branch of the original repository. Provide a clear description of your changes, reference any related issues, and ensure all tests pass.

## Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/nsalvacao/cli-plugins.git
    cd cli-plugins
    ```
2.  **Install dependencies** using `uv`:
    ```bash
    uv sync
    ```

## Code Style Guidelines

We adhere to the following code style and quality standards:

- Python 3.11+ with type hints
- No external dependencies for crawler or generator (stdlib only)
- Keep files under 500 lines
- Tests go in `tests/`, never in root
- We use linters and formatters to maintain code consistency. Ensure your code passes all checks before submitting a PR.
    - Run `uv run python -m ruff check .` for linting.
    - Run `uv run python -m black .` for formatting.

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This helps us maintain a clear commit history and automate releases.

Examples:

- `feat: Add new CLI configuration for new-tool`
- `fix: Correct parsing of --help output for tool-x`
- `docs: Update contributing guidelines with community focus`
- `refactor: Improve crawler performance`

## Community & Ecosystem

We are committed to building a friendly and inclusive community around `cli-plugins`.

- **Be Respectful**: Always adhere to our [Code of Conduct](../CODE_OF_CONDUCT.md).
- **Engage**: Participate in discussions, provide feedback on issues and pull requests, and help others.
- **Share**: If you build something cool with `cli-plugins` (e.g., a new plugin, a useful script, or an integration), share it with the community!
- **Support**: Help us improve by reporting bugs, suggesting features, and contributing code.


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
