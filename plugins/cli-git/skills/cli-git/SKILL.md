---
name: cli-git
description: >-
  This skill should be used when the user needs help with git CLI commands, including add, bisect, branch, clone, commit, diff, fetch, grep, init, log, merge, mv, pull, push, rebase, reset, restore, rm, show, status, switch, tag. Covers flags, subcommands, usage patterns, and troubleshooting for all 22 git commands.
---

# git CLI Reference

Expert command reference for **git** v2.43.0.

- **22** commands (0 with subcommands)
- **441** command flags + **0** global flags
- **126** usage examples
- Max nesting depth: 0

## When to Use

This skill applies when:
- Constructing or validating `git` commands
- Looking up flags, options, or subcommands
- Troubleshooting `git` invocations or errors
- Needing correct syntax for `git` operations

## Prerequisites

Ensure `git` is installed and available on PATH.

## Quick Reference

| Command | Description |
| --- | --- |
| `git add` | Add file contents to the index |
| `git bisect` | Use binary search to find the commit that introduced a bug |
| `git branch` | List, create, or delete branches |
| `git clone` | Clone a repository into a new directory |
| `git commit` | Record changes to the repository |
| `git diff` | Show changes between commits, commit and working tree, etc |
| `git fetch` | Download objects and refs from another repository |
| `git grep` | Print lines matching a pattern |
| `git init` | Create an empty Git repository or reinitialize an existing one |
| `git log` | Show commit logs |
| `git merge` | or: git merge --abort |
| `git mv` | Move or rename a file, a directory, or a symlink |
| `git pull` | Fetch from and integrate with another repository or a local branch |
| `git push` | Update remote refs along with associated objects |
| `git rebase` | Reapply commits on top of another base tip |
| `git reset` | fatal: not a git repository (or any parent up to mount point /mnt) |
| `git restore` | Restore working tree files |
| `git rm` | Remove files from the working tree and from the index |
| `git show` | Show various types of objects |
| `git status` | Show the working tree status |
| `git switch` | Switch branches |
| `git tag` | Create, list, delete or verify a tag object signed with GPG |

### Global Flags



## Command Overview


### Commands

`add`, `bisect`, `branch`, `clone`, `commit`, `diff`, `fetch`, `grep`, `init`, `log`, `merge`, `mv`, `pull`, `push`, `rebase`, `reset`, `restore`, `rm`, `show`, `status`, `switch`, `tag`

## Common Usage Patterns

```bash
git add Documentation/\*.txt
```
Note that the asterisk * is quoted from the shell in this example; this lets the command include the files

```bash
from subdirectories of Documentation/ directory.
```
git add git-*.sh

```bash
Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it
```
does not consider subdir/git-foo.sh.

```bash
git bisect start HEAD v1.2 --      # HEAD is bad, v1.2 is good
```
git bisect run make                # "make" builds the app

```bash
git bisect reset                   # quit the bisect session
```
git bisect start HEAD origin --    # HEAD is bad, origin is good

```bash
git bisect run make test           # "make test" builds and tests
```
git bisect reset                   # quit the bisect session

```bash
cat ~/test.sh
```
make || exit 125                     # this skips broken builds

```bash
git bisect start HEAD HEAD~10 --   # culprit is among the last 10
```
git bisect run ~/test.sh

## Detailed References

For complete command documentation including all flags and subcommands:
- **Full command tree:** see `references/commands.md`
- **All usage examples:** see `references/examples.md`

## Troubleshooting

- Use `git --help` or `git <command> --help` for inline help
- Add `--verbose` for detailed output during debugging

## Re-scanning

To update this plugin after a CLI version change, run the `/scan-cli` command
or manually execute the crawler and generator.
