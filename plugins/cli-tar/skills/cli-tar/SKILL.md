---
name: cli-tar
description: >-
  This skill should be used when the user needs help with tar CLI commands, flags, and troubleshooting.
---

# tar CLI Reference

Compact command reference for **tar** v.

- **0** total commands
- **0** command flags + **33** global flags
- **0** extracted usage examples
- Max nesting depth: 0

## When to Use

- Constructing or validating `tar` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Command format examples: 

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--absolute-names` | `-P` | string | don't strip leading '/'s from file names |
| `--auto-compress` | `-a` | bool | use archive suffix to determine the compression |
| `--block-number` | `-R` | bool | show block number within archive with each message |
| `--bzip2` | `-j` | bool | filter the archive through bzip2 |
| `--check-links` | `-l` | bool | print a message if not all links are dumped |
| `--checkpoint-action` | `` | string | execute ACTION on each checkpoint |
| `--dereference` | `-h` | string | follow symlinks; archive and dump the files they |
| `--full-time` | `` | string | print file time to its full resolution |
| `--hard-dereference` | `` | string | follow hard links; archive and dump the files they |
| `--index-file` | `` | string | send verbose output to FILE |
| `--lzip` | `` | bool | filter the archive through lzip |
| `--lzma` | `` | bool | filter the archive through xz |
| `--lzop` | `` | bool | filter the archive through lzop |
| `--newer-mtime` | `` | string | compare date and time when data changed only |
| `--no-auto-compress` | `` | bool | do not use archive suffix to determine the |
| `--no-quote-chars` | `` | string | disable quoting for characters from STRING |
| `--one-file-system` | `` | string | stay in local file system when creating archive |
| `--quote-chars` | `` | string | additionally quote characters from STRING |
| `--quoting-style` | `` | string | set name quoting style; see below for valid STYLE |
| `--restrict` | `` | bool | disable use of some potentially harmful options |
| `--show-defaults` | `` | bool | show tar defaults |
| `--show-omitted-dirs` | `` | string | when listing or extracting, list each directory |
| `--show-snapshot-field-ranges` | `` | string | show valid ranges for snapshot-file fields |
| `--strip-components` | `` | string | strip NUMBER leading components from file |
| `--suffix` | `` | string | backup before removal, override usual suffix ('~' |
| `--usage` | `` | bool | give a short usage message |
| `--utc` | `` | string | print file modification times in UTC |
| `--verbose` | `-v` | string | verbosely list files processed |
| `--version` | `` | bool | print program version |
| `--warning` | `` | string | warning control |
| `--xz` | `-J` | bool | filter the archive through xz |
| `--zstd` | `` | bool | filter the archive through zstd |
| `-o` | `-o` | bool | when creating, same as --old-archive; when |

## Common Usage Patterns (Compact)

_No examples extracted._
## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
