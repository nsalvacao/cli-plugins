---
name: cli-jq
description: >-
  This skill should be used when the user needs help with jq CLI commands, including . Covers flags, subcommands, usage patterns, and troubleshooting for all 0 jq commands.
---

# jq CLI Reference

Expert command reference for **jq** v.

- **0** commands (0 with subcommands)
- **0** command flags + **24** global flags
- **0** usage examples
- Max nesting depth: 0

## When to Use

This skill applies when:
- Constructing or validating `jq` commands
- Looking up flags, options, or subcommands
- Troubleshooting `jq` invocations or errors
- Needing correct syntax for `jq` operations

## Prerequisites

Ensure `jq` is installed and available on PATH.

## Quick Reference

| Command | Description |
| --- | --- |

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--args` | `` | bool | consume remaining arguments as positional |
| `--ascii-output` | `-a` | string | output strings by only ASCII characters |
| `--build-configuration` | `` | bool | show jq's build configuration; |
| `--color-output` | `-C` | bool | colorize JSON output; |
| `--compact-output` | `-c` | bool | compact instead of pretty-printed output; |
| `--exit-status` | `-e` | bool | set exit status code based on the output; |
| `--from-file` | `-f` | string | load filter from the file; |
| `--help` | `-h` | bool | show the help; |
| `--indent` | `` | string | use n spaces for indentation (max 7 spaces); |
| `--join-output` | `-j` | bool | implies -r and output without newline after |
| `--jsonargs` | `` | bool | consume remaining arguments as positional |
| `--monochrome-output` | `-M` | bool | disable colored output; |
| `--null-input` | `-n` | string | use `null` as the single input value; |
| `--raw-input` | `-R` | string | read each line as string instead of JSON; |
| `--raw-output` | `-r` | string | output strings without escapes and quotes; |
| `--raw-output0` | `` | bool | implies -r and output NUL after each output; |
| `--seq` | `` | bool | parse input/output as application/json-seq; |
| `--slurp` | `-s` | bool | read all inputs into an array and use it as |
| `--sort-keys` | `-S` | bool | sort keys of each object on output; |
| `--stream` | `` | string | parse the input value in streaming fashion; |
| `--stream-errors` | `` | bool | implies --stream and report parse error as |
| `--tab` | `` | bool | use tabs for indentation; |
| `--unbuffered` | `` | bool | flush output stream after each output; |
| `--version` | `-V` | bool | show the version; |

## Command Overview


## Common Usage Patterns


## Detailed References

For complete command documentation including all flags and subcommands:
- **Full command tree:** see `references/commands.md`
- **All usage examples:** see `references/examples.md`

## Troubleshooting

- Use `jq --help` or `jq <command> --help` for inline help
- Add `--verbose` for detailed output during debugging

## Re-scanning

To update this plugin after a CLI version change, run the `/scan-cli` command
or manually execute the crawler and generator.
