#!/usr/bin/env bash
# Re-scan gh CLI and regenerate this plugin.
# Usage: bash scripts/rescan.sh [--dry-run]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

CLI_NAME="gh"
JSON_PATH="$PROJECT_ROOT/output/$CLI_NAME.json"
PLUGIN_DIR="$PROJECT_ROOT/plugins/cli-$CLI_NAME"

# Check CLI is available
if ! command -v "$CLI_NAME" &>/dev/null; then
    echo "ERROR: $CLI_NAME not found on PATH. Install it first." >&2
    exit 1
fi

echo "==> Crawling $CLI_NAME..."
python3 "$PROJECT_ROOT/cli_crawler.py" "$CLI_NAME"

echo "==> Generating plugin..."
python3 "$PROJECT_ROOT/scripts/generate_plugin.py" "$JSON_PATH" "$@"

echo "==> Done. Plugin at: $PLUGIN_DIR"
ls -la "$PLUGIN_DIR"
