---
name: scan-cli
description: Re-scan the ls CLI and regenerate plugin reference files
allowed-tools: ["Bash"]
---

# Re-scan ls CLI

Run the rescan script to crawl the CLI and regenerate this plugin:

```bash
bash $CLAUDE_PLUGIN_ROOT/scripts/rescan.sh
```

Add `--dry-run` to preview without writing files:

```bash
bash $CLAUDE_PLUGIN_ROOT/scripts/rescan.sh --dry-run
```

## Notes

- Requires `ls` installed and on PATH
- Idempotent -- re-running overwrites existing files cleanly
