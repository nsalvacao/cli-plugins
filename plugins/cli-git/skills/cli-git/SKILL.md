---
name: cli-git
description: >-
  This skill should be used when the user needs help with git CLI commands, flags, and troubleshooting.
---

# git CLI Reference

Compact command reference for **git** v2.43.0.

- **22** total commands
- **441** command flags + **0** global flags
- **31** extracted usage examples
- Max nesting depth: 0

## When to Use

- Constructing or validating `git` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Standalone Commands:
`add`, `bisect`, `branch`, `clone`, `commit`, `diff`, `fetch`, `grep`, `init`, `log`, `merge`, `mv`, `pull`, `push`, `rebase`, `reset`, `restore`, `rm`, `show`, `status`, `switch`, `tag`
Command format examples: `git add`, `git bisect`, `git branch`

### Global Flags

_No global flags detected._

## Common Usage Patterns (Compact)

```bash
o   Adds content from all *.txt files under Documentation directory and its subdirectories:
```
o   Considers adding content from all git-*.sh scripts:

```bash
o   Clone from upstream:
```
o   Make a local clone that borrows from the current directory, without checking things out:

```bash
o   Clone from upstream while borrowing from an existing local directory:
```
o   Create a bare repository to publish your changes to the public:

```bash
staging area called the "index" with git add. A file can be reverted back, only in the index but not in the
```
working tree, to that of the last commit with git restore --staged <file>, which effectively reverts git add

```bash
and prevents the changes to this file from participating in the next commit. After building the state to be
```
committed incrementally with these commands, git commit (without any pathname parameter) is used to record

## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
