---
description: Run a real-world end-to-end smoke test — crawl a CLI and generate its plugin
---

# Real-World Smoke Test — Crawl + Generate

This workflow crawls a CLI's `--help` output and generates a complete plugin from it,
validating the full pipeline end-to-end.

## Steps

1. **Check already-tested CLIs** — list files in `output/` and `plugins/` to see what's been done:
// turbo
```
Get-ChildItem "D:\GitHub\cli-plugins\output" -Filter "*.json" -Name | Where-Object { $_ -notlike "*.raw.json" }; Write-Host "---PLUGINS---"; Get-ChildItem "D:\GitHub\cli-plugins\plugins" -Name -Directory
```

2. **Find an untested CLI on the system** — scan for installed CLIs not yet in output/:
// turbo
```
foreach ($cmd in @("python","pip","cargo","rustup","go","kubectl","terraform","az","gcloud","helm","poetry","pdm","rye","mise","pnpm","node","dotnet","winget","scoop","choco","ffmpeg","curl","wget","ruff","pytest","conda","bun","deno","yarn","gradle","mvn","ant","cmake","make","ninja","clang","gcc","java","javac","ruby","perl","php","lua","R")) { if (Get-Command $cmd -ErrorAction SilentlyContinue) { $existing = Test-Path "D:\GitHub\cli-plugins\output\$cmd.json"; if (-not $existing) { Write-Host "AVAILABLE: $cmd" } } }
```

3. **Pick one CLI** from the AVAILABLE list (prefer one with rich subcommands).
   If no CLI is available, report this and stop.

4. **Activate the venv and crawl the chosen CLI**:
```
.venv\Scripts\cli-crawler.exe <CLI_NAME> -o output
```
   - Verify the output reports commands and flags found.
   - Check `output/<CLI_NAME>.json` was created.

5. **Generate the plugin from the crawl output**:
```
.venv\Scripts\generate-plugin.exe output/<CLI_NAME>.json -o plugins
```
   - Verify `plugins/cli-<CLI_NAME>/` directory was created.
   - Check it contains: `.claude-plugin/plugin.json`, `skills/cli-<CLI_NAME>/SKILL.md`,
     `skills/cli-<CLI_NAME>/references/commands.md`, `skills/cli-<CLI_NAME>/references/examples.md`,
     `commands/scan-cli.md`, `scripts/rescan.sh`.

6. **Validate the generated plugin JSON**:
// turbo
```
.venv\Scripts\python.exe -c "import json; d=json.load(open('plugins/cli-<CLI_NAME>/.claude-plugin/plugin.json',encoding='utf-8')); assert d['name']=='cli-<CLI_NAME>'; print(f'OK: {d[\"name\"]} v{d[\"version\"]}')"
```

7. **Run the full test suite** to make sure nothing broke:
// turbo
```
.venv\Scripts\pytest.exe tests/ -q
```

8. **Report results**:
   - CLI crawled: name, number of commands, number of flags, duration
   - Plugin generated: directory path, file count
   - Tests: pass/fail count
