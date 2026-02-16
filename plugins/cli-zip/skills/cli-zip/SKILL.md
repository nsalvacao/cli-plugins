---
name: cli-zip
description: >-
  This skill should be used when the user needs help with zip CLI commands, flags, and troubleshooting.
---

# zip CLI Reference

Compact command reference for **zip** v2.91.

- **0** total commands
- **0** command flags + **14** global flags
- **0** extracted usage examples
- Max nesting depth: 0

## When to Use

- Constructing or validating `zip` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Command format examples: 

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `-0` | `-0` | bool | store only -l convert LF to CR LF (-ll CR LF to LF) |
| `-1` | `-1` | bool | compress faster -9 compress better |
| `-A` | `-A` | bool | adjust self-extracting exe -J junk zipfile prefix (unzipsfx) |
| `-F` | `-F` | bool | fix zipfile (-FF try harder) -D do not add directory entries |
| `-T` | `-T` | bool | test zipfile integrity -X eXclude eXtra file attributes |
| `-c` | `-c` | bool | add one-line comments -z add zipfile comment |
| `-d` | `-d` | bool | delete entries in zipfile -m move into zipfile (delete OS files) |
| `-e` | `-e` | bool | encrypt -n don't compress these suffixes |
| `-f` | `-f` | bool | freshen: only changed files -u update: only changed or new files |
| `-h` | `-h` | string | show more help |
| `-q` | `-q` | bool | quiet operation -v verbose operation/print version info |
| `-r` | `-r` | bool | recurse into directories -j junk (don't record) directory names |
| `-x` | `-x` | bool | exclude the following names -i include only the following names |
| `-y` | `-y` | bool | store symbolic links as the link instead of the referenced file |

## Common Usage Patterns (Compact)

_No examples extracted._
## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
