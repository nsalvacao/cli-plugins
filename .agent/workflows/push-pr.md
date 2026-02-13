---
description: Commit, push, and create a PR via gh CLI for Copilot review
---

# Commit, Push, and PR

// turbo-all

This workflow commits all staged changes, pushes the current branch, and creates
a PR for Copilot review. It uses `--no-verify` for commits to avoid hanging hooks.

## Steps

1. **Check status** — review what's changed:
```
git status --short
```

2. **Stage all relevant changes** (exclude common junk):
```
git add src/ tests/ pyproject.toml .github/ .gitignore .agent/ plugins/
```

3. **Commit with --no-verify** to avoid hook hangs:
```
git commit --no-verify -m "<COMMIT_MESSAGE>"
```
   Replace `<COMMIT_MESSAGE>` with a descriptive conventional commit message.

4. **Push the branch** (force-with-lease if amended):
```
git push --force-with-lease origin <BRANCH_NAME>
```

5. **Check if PR exists**:
```
gh pr list --head <BRANCH_NAME> --json number,title,url
```

6. **Create PR if none exists** (or skip if already open):
```
gh pr create --base main --head <BRANCH_NAME> --title "<PR_TITLE>" --body "<PR_BODY>"
```

7. **Wait for CI and verify checks**:
```
Start-Sleep -Seconds 30; gh pr checks <PR_NUMBER>
```

8. **Report** — PR URL and CI status.
