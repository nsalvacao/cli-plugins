---
name: cli-pnpm
description: >-
  This skill should be used when the user needs help with pnpm CLI commands, flags, and troubleshooting.
---

# pnpm CLI Reference

Compact command reference for **pnpm** v10.29.3.

- **22** total commands
- **361** command flags + **1** global flags
- **0** extracted usage examples
- Max nesting depth: 1

## When to Use

- Constructing or validating `pnpm` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Command Groups:
`config`
Standalone Commands:
`add`, `audit`, `create`, `dlx`, `exec`, `init`, `install`, `link`, `list`, `outdated`, `publish`, `remove`, `run`, `self-update`, `unlink`, `update`, `why`
Command format examples: `pnpm add`, `pnpm audit`, `pnpm config`

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--recursive` | `-r` | bool | Run the command for each project in the workspace. |

## Common Usage Patterns (Compact)

```bash
pnpm add <name>
```
Installs a package and any packages that it depends on. By default, any new package is installed as a prod dependency

```bash
pnpm audit [options]
```
Checks for known security issues with the installed packages

```bash
pnpm config set <key> <value>
```
Manage the pnpm configuration files

```bash
pnpm config delete
```
Remove the config key from the config file

```bash
pnpm config get
```
Print the config value for the provided key

## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
