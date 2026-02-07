---
name: cli-gh
description: >-
  This skill should be used when the user needs help with gh CLI commands, including agent-task, alias, attestation (download and verify artifact attestations), auth (authenticate gh and git with github), cache (work with github actions caches), codespace (connect to and manage codespaces), config (display or change configuration settings for gh), extension, gist (work with github gists), gpg-key, issue (work with github issues), label (work with github labels), org (work with github organizations), pr (work with github pull requests), preview (preview commands are for testing), project (work with github projects), release (manage releases), repo (work with github repositories), ruleset, run (list), search (search across all of github), secret (secrets can be set at the repository), ssh-key, variable (variables can be set at the repository), workflow (list), api, browse, completion, copilot, status. Covers flags, subcommands, usage patterns, and troubleshooting for all 30 gh commands.
---

# gh CLI Reference

Expert command reference for **gh** v2.86.0.

- **212** commands (30 with subcommands)
- **1095** command flags + **2** global flags
- **166** usage examples
- Max nesting depth: 2

## When to Use

This skill applies when:
- Constructing or validating `gh` commands
- Looking up flags, options, or subcommands
- Troubleshooting `gh` invocations or errors
- Needing correct syntax for `gh` operations

## Prerequisites

Ensure `gh` is installed and available on PATH.

## Quick Reference

| Command | Description |
| --- | --- |
| `gh agent-task` | Working with agent tasks in the GitHub CLI is in preview and |
| `gh alias` | Aliases can be used to make shortcuts for gh commands or to compose multiple commands. |
| `gh api` | accepts 1 arg(s), received 0 |
| `gh attestation` | Download and verify artifact attestations. |
| `gh auth` | Authenticate gh and git with GitHub |
| `gh browse` | Transition from the terminal to the web browser to view and interact with: |
| `gh cache` | Work with GitHub Actions caches. |
| `gh codespace` | Connect to and manage codespaces |
| `gh completion` | Generate shell completion scripts for GitHub CLI commands. |
| `gh config` | Display or change configuration settings for gh. |
| `gh copilot` | Runs the GitHub Copilot CLI. |
| `gh extension` | GitHub CLI extensions are repositories that provide additional gh commands. |
| `gh gist` | Work with GitHub gists. |
| `gh gpg-key` | Manage GPG keys registered with your GitHub account. |
| `gh issue` | Work with GitHub issues. |
| `gh label` | Work with GitHub labels. |
| `gh org` | Work with GitHub organizations. |
| `gh pr` | Work with GitHub pull requests. |
| `gh preview` | Preview commands are for testing, demonstrative, and development purposes only. |
| `gh project` | Work with GitHub Projects. |
| `gh release` | Manage releases |
| `gh repo` | Work with GitHub repositories. |
| `gh ruleset` | Repository rulesets are a way to define a set of rules that apply to a repository. |
| `gh run` | List, view, and watch recent workflow runs from GitHub Actions. |
| `gh search` | Search across all of GitHub. |
| `gh secret` | Secrets can be set at the repository, or organization level for use in |
| `gh ssh-key` | Manage SSH keys registered with your GitHub account. |
| `gh status` | The status command prints information about your work on GitHub across all the repositories you're subscribed to, including: |
| `gh variable` | Variables can be set at the repository, environment or organization level for use in |
| `gh workflow` | List, view, and run workflows in GitHub Actions. |

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--version` | `` | bool | Show gh version |

## Command Overview


### Command Groups

`agent-task`, `alias`, `attestation`, `auth`, `cache`, `codespace`, `config`, `extension`, `gist`, `gpg-key`, `issue`, `label`, `org`, `pr`, `preview`, `project`, `release`, `repo`, `ruleset`, `run`, `search`, `secret`, `ssh-key`, `variable`, `workflow`

### Commands

`api`, `browse`, `completion`, `copilot`, `status`

## Common Usage Patterns

```bash
gh agent-task list
```
gh agent-task create "Improve the performance of the data processing pipeline"

```bash
gh agent-task view 123
```
gh agent-task view 12345abc-12345-12345-12345-12345abc

```bash
gh agent-task create "build me a new app"
```
gh agent-task create "build me a new app" --follow

```bash
gh agent-task create -F task-desc.md
```
echo "build me a new app" | gh agent-task create -F -

```bash
gh agent-task create
```
gh agent-task create -F task-desc.md

```bash
gh agent-task create "fix errors" --base branch
```
gh agent-task create "build me a new app" --custom-agent my-agent

```bash
gh agent-task view e2fa49d2-f164-4a56-ab99-498090b8fcdf
```
gh agent-task view 12345

```bash
gh agent-task view --repo OWNER/REPO 12345
```
gh agent-task view OWNER/REPO#12345

## Detailed References

For complete command documentation including all flags and subcommands:
- **Full command tree:** see `references/commands.md`
- **All usage examples:** see `references/examples.md`

## Troubleshooting

- Use `gh --help` or `gh <command> --help` for inline help
- Add `--verbose` for detailed output during debugging

## Re-scanning

To update this plugin after a CLI version change, run the `/scan-cli` command
or manually execute the crawler and generator.
