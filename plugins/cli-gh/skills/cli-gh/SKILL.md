---
name: cli-gh
description: >-
  This skill should be used when the user needs help with gh CLI commands, flags, and troubleshooting.
---

# gh CLI Reference

Compact command reference for **gh** v2.86.0.

- **212** total commands
- **1095** command flags + **2** global flags
- **166** extracted usage examples
- Max nesting depth: 2

## When to Use

- Constructing or validating `gh` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Command Groups:
`agent-task`, `alias`, `attestation`, `auth`, `cache`, `codespace`, `config`, `extension`, `gist`, `gpg-key`, `issue`, `label`, `org`, `pr`, `preview`, `project`, `release`, `repo`, `ruleset`, `run`, `search`, `secret`, `ssh-key`, `variable`, `workflow`
Standalone Commands:
`api`, `browse`, `completion`, `copilot`, `status`
Command format examples: `gh agent-task`, `gh alias`, `gh api`

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--version` | `` | bool | Show gh version |

## Common Usage Patterns (Compact)

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

## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
