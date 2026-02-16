#!/usr/bin/env bash
# Re-scan ls CLI and regenerate this plugin.
# Usage: bash scripts/rescan.sh [--dry-run]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

CLI_NAME="ls"
JSON_PATH="$PROJECT_ROOT/output/$CLI_NAME.json"
PLUGIN_DIR="$PROJECT_ROOT/plugins/cli-ls"

# Check CLI is available
if ! command -v "$CLI_NAME" &>/dev/null; then
    echo "ERROR: $CLI_NAME not found on PATH. Install it first." >&2
    exit 1
fi

PYTHONPATH_FALLBACK="$PROJECT_ROOT/src${PYTHONPATH:+:$PYTHONPATH}"

echo "==> Crawling $CLI_NAME..."
if command -v cli-crawler &>/dev/null; then
    cli-crawler "$CLI_NAME" -o "$JSON_PATH"
else
    PYTHONPATH="$PYTHONPATH_FALLBACK" python3 -m crawler.pipeline "$CLI_NAME" -o "$JSON_PATH"
fi

echo "==> Generating plugin..."
if command -v generate-plugin &>/dev/null; then
    generate-plugin "$JSON_PATH" -o "$PROJECT_ROOT/plugins" "$@"
else
    PYTHONPATH="$PYTHONPATH_FALLBACK" \
        python3 -m generator.plugin_generator "$JSON_PATH" -o "$PROJECT_ROOT/plugins" "$@"
fi

echo "==> Done. Plugin at: $PLUGIN_DIR"
ls -la "$PLUGIN_DIR"
