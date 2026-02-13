---
description: Full post-task verification — lint, test, real-world smoke test, commit, push, and PR
---

# Verify and Ship

// turbo-all

Complete post-task workflow: runs all checks, does a real-world smoke test with an
untested CLI, commits, pushes, and creates/updates a PR for Copilot review.

## Pre-flight

1. **Install in editable mode** (ensure latest code is importable):
```
.venv\Scripts\pip.exe install -e ".[dev]"
```

## Lint

2. **Ruff check**:
```
.venv\Scripts\ruff.exe check src/ tests/
```
   If errors found, run `ruff check --fix src/ tests/` then `ruff format src/ tests/`.

3. **Ruff format check**:
```
.venv\Scripts\ruff.exe format --check src/ tests/
```

## Test

4. **Run all tests**:
```
.venv\Scripts\pytest.exe tests/ -v --tb=short
```

## Smoke Test (Real-World)

5. **Find untested CLI** — check output/ for existing crawls:
```
foreach ($cmd in @("python","pip","cargo","rustup","go","kubectl","terraform","az","gcloud","helm","poetry","pdm","rye","mise","pnpm","node","dotnet","winget","scoop","choco","ffmpeg","curl","wget","ruff","pytest","conda","bun","deno","yarn")) { if (Get-Command $cmd -ErrorAction SilentlyContinue) { $existing = Test-Path "D:\GitHub\cli-plugins\output\$cmd.json"; if (-not $existing) { Write-Host "AVAILABLE: $cmd" } } }
```

6. **Crawl the first available CLI** (pick one from step 5):
```
.venv\Scripts\cli-crawler.exe <CLI_NAME> -o output
```

7. **Generate plugin**:
```
.venv\Scripts\generate-plugin.exe output/<CLI_NAME>.json -o plugins
```

8. **Validate plugin structure**:
```
.venv\Scripts\python.exe -c "import json,pathlib; p=pathlib.Path('plugins/cli-<CLI_NAME>'); assert (p/'.claude-plugin'/'plugin.json').exists(); assert (p/'skills'/'cli-<CLI_NAME>'/'SKILL.md').exists(); d=json.load(open(p/'.claude-plugin'/'plugin.json',encoding='utf-8')); print(f'OK: {d[\"name\"]} v{d[\"version\"]}')"
```

9. **Re-run tests** (confirm smoke test didn't break anything):
```
.venv\Scripts\pytest.exe tests/ -q
```

## Ship

10. **Stage changes**:
```
git add src/ tests/ pyproject.toml .github/ .gitignore .agent/ plugins/
```

11. **Commit** (replace `<COMMIT_MESSAGE>` appropriately):
```
git commit --no-verify -m "<COMMIT_MESSAGE>"
```

12. **Push**:
```
git push --force-with-lease origin <BRANCH_NAME>
```

13. **Create or check PR**:
```
gh pr list --head <BRANCH_NAME> --json number,url
```
   Create PR if none exists, otherwise note the existing one.

14. **Wait for CI and report checks**:
```
Start-Sleep -Seconds 30; gh pr checks <PR_NUMBER>
```
