# make -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--always-make` | `-B` | bool | Unconditionally make all targets. |
| `--check-symlink-times` | `-L` | bool | Use the latest mtime between symlinks and target. |
| `--environment-overrides` | `-e` | string | Environment variables override makefiles. |
| `--help` | `-h` | bool | Print this message and exit. |
| `--ignore-errors` | `-i` | bool | Ignore errors from recipes. |
| `--keep-going` | `-k` | bool | Keep going when some targets can't be made. |
| `--no-builtin-rules` | `-r` | bool | Disable the built-in implicit rules. |
| `--no-builtin-variables` | `-R` | bool | Disable the built-in variable settings. |
| `--no-print-directory` | `` | bool | Turn off -w, even if it was turned on implicitly. |
| `--no-silent` | `` | bool | Echo recipes (disable --silent mode). |
| `--print-data-base` | `-p` | bool | Print make's internal database. |
| `--print-directory` | `-w` | string | Print the current directory. |
| `--question` | `-q` | bool | Run no recipe; exit status says if up to date. |
| `--touch` | `-t` | bool | Touch targets instead of remaking them. |
| `--trace` | `` | bool | Print tracing information. |
| `--version` | `-v` | string | Print the version number of make and exit. |
| `--warn-undefined-variables` | `` | bool | Warn when an undefined variable is referenced. |
| `-d` | `-d` | bool | Print lots of debugging information. |

