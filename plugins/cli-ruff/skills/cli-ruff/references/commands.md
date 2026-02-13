# ruff -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |
| `--version` | `-V` | bool | Print version |

## Command Groups

### `ruff analyze`

Run analysis over Python source code

```
ruff analyze [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

**Subcommands:**

#### `ruff analyze graph`

Generate a map of Python file dependencies or dependents

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML `<KEY> = <VALUE>` pair (such as you might find in a `ruff.toml` configuration file) overriding a specific configuration option. Overrides of individual settings using this option always take precedence over all configuration files, including configuration files that were also specified using `--config` |
| `--detect-string-imports` | `` | string | Attempt to detect imports from string literals |
| `--direction` | `` | string | The direction of the import map. By default, generates a dependency map, i.e., a map from file to files that it depends on. Use `--direction dependents` to generate a map from file to files that depend on it |
| `--help` | `-h` | bool | Print help (see a summary with '-h') |
| `--isolated` | `` | string | Ignore all configuration files |
| `--min-dots` | `` | string | The minimum number of dots in a string import to consider it a valid import |
| `--preview` | `` | bool | Enable preview mode. Use `--no-preview` to disable |
| `--python` | `` | string | Path to a virtual environment to use for resolving additional dependencies |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--target-version` | `` | string | The minimum Python version that should be supported |
| `--type-checking-imports` | `` | bool | Include imports that are only used for type checking (i.e., imports within `if TYPE_CHECKING:` blocks). Use `--no-type-checking-imports` to exclude imports that are only used for type checking |
| `--verbose` | `-v` | bool | Enable verbose logging |

#### `ruff analyze help`

error: unrecognized subcommand '--help'

## Commands

### `ruff check`

Run Ruff on the given files or directories

```
ruff check [OPTIONS] [FILES]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Path to the cache directory [env: RUFF_CACHE_DIR=] |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--diff` | `` | string | Avoid writing any fixed files back; instead, output a diff for each changed |
| `--exclude` | `` | string | List of paths, used to omit files and/or directories from analysis |
| `--exit-non-zero-on-fix` | `` | string | Exit with a non-zero status code if any files were modified via fix, even if no |
| `--exit-zero` | `-e` | bool | Exit with status code "0", even upon detecting lint violations |
| `--extend-exclude` | `` | string | Like --exclude, but adds additional files and directories on top of those already |
| `--extend-fixable` | `` | string | Like --fixable, but adds additional rule codes on top of those already specified |
| `--extend-per-file-ignores` | `` | string | Like `--per-file-ignores`, but adds additional ignores on top of those already specified |
| `--extend-select` | `` | string | Like --select, but adds additional rule codes on top of those already specified |
| `--extension` | `` | string | List of mappings from file extension to language (one of `python`, `ipynb`, |
| `--fix` | `` | bool | Apply fixes to resolve lint violations. Use `--no-fix` to disable or |
| `--fix-only` | `` | bool | Apply fixes to resolve lint violations, but don't report on, or exit non-zero |
| `--fixable` | `` | string | List of rule codes to treat as eligible for fix. Only applicable when fix itself is enabled (e.g., via `--fix`) |
| `--force-exclude` | `` | bool | Enforce exclusions, even for paths passed to Ruff directly on the command-line. |
| `--help` | `-h` | bool | Print help |
| `--ignore` | `` | string | Comma-separated list of rule codes to disable |
| `--ignore-noqa` | `` | bool | Ignore any `# noqa` comments |
| `--isolated` | `` | string | Ignore all configuration files |
| `--no-cache` | `-n` | bool | Disable cache reads [env: RUFF_NO_CACHE=] |
| `--output-file` | `-o` | string | Specify file to write the linter output to (default: stdout) [env: (default: stdout) |
| `--output-format` | `` | string | Output serialization format for violations. The default serialization format is |
| `--per-file-ignores` | `` | string | List of mappings from file pattern to code to exclude |
| `--preview` | `` | bool | Enable preview mode; checks will include unstable rules and fixes. Use |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--respect-gitignore` | `` | string | Respect file exclusions via `.gitignore` and other standard ignore files. Use |
| `--select` | `` | string | Comma-separated list of rule codes to enable (or ALL, to enable all rules) |
| `--show-files` | `` | string | See the files Ruff will be run against with the current settings |
| `--show-fixes` | `` | bool | Show an enumeration of all fixed lint violations. Use `--no-show-fixes` to |
| `--show-settings` | `` | string | See the settings Ruff will use to lint a given Python file |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--statistics` | `` | bool | Show counts for every rule with at least one violation |
| `--stdin-filename` | `` | string | The name of the file when passing it through stdin |
| `--target-version` | `` | string | The minimum Python version that should be supported [possible values: py37, |
| `--unfixable` | `` | string | List of rule codes to treat as ineligible for fix. Only applicable when fix itself is enabled (e.g., via `--fix`) |
| `--unsafe-fixes` | `` | bool | Include fixes that may not retain the original intent of the code. Use |
| `--verbose` | `-v` | bool | Enable verbose logging |
| `--watch` | `-w` | string | Run in watch mode by re-running whenever files change |

### `ruff clean`

Clear any caches in the current directory and any subdirectories

```
ruff clean [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff config`

List or describe the available configuration options

```
ruff config [OPTIONS] [OPTION]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--output-format` | `` | string | Output format [default: text] [possible values: text, json] (default: text) |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff format`

Run the Ruff formatter on the given files or directories

```
ruff format [OPTIONS] [FILES]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Path to the cache directory |
| `--check` | `` | string | Avoid writing any formatted files back; instead, exit with a non-zero status code if any files would have been modified, and zero otherwise |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML `<KEY> = <VALUE>` pair (such as you might find in a `ruff.toml` configuration file) overriding a specific configuration option. Overrides of individual settings using this option always take precedence over all configuration files, including configuration files that were also specified using `--config` |
| `--diff` | `` | string | Avoid writing any formatted files back; instead, exit with a non-zero status code and the difference between the current file and how the formatted file would look like |
| `--exclude` | `` | string | List of paths, used to omit files and/or directories from analysis |
| `--exit-non-zero-on-format` | `` | string | Exit with a non-zero status code if any files were modified via format, even if all files were formatted successfully |
| `--extension` | `` | string | List of mappings from file extension to language (one of `python`, `ipynb`, `pyi`). For example, to treat `.ipy` files as IPython notebooks, use `--extension ipy:ipynb` |
| `--force-exclude` | `` | bool | Enforce exclusions, even for paths passed to Ruff directly on the command-line. Use `--no-force-exclude` to disable |
| `--help` | `-h` | bool | Print help (see a summary with '-h') |
| `--isolated` | `` | string | Ignore all configuration files |
| `--line-length` | `` | string | Set the line-length |
| `--no-cache` | `-n` | bool | Disable cache reads |
| `--output-format` | `` | string | Output serialization format for violations, when used with `--check`. The default serialization format is "full". |
| `--preview` | `` | bool | Enable preview mode; enables unstable formatting. Use `--no-preview` to disable |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--range` | `` | string | When specified, Ruff will try to only format the code in the given range. It might be necessary to extend the start backwards or the end forwards, to fully enclose a logical line. The `<RANGE>` uses the format `<start_line>:<start_column>-<end_line>:<end_column>`. |
| `--respect-gitignore` | `` | string | Respect file exclusions via `.gitignore` and other standard ignore files. Use `--no-respect-gitignore` to disable |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--stdin-filename` | `` | string | The name of the file when passing it through stdin |
| `--target-version` | `` | string | The minimum Python version that should be supported |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff help`

error: unrecognized subcommand '--help'

```
ruff [OPTIONS] <COMMAND>
```

### `ruff linter`

List all supported upstream linters

```
ruff linter [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--output-format` | `` | string | Output format [default: text] [possible values: text, json] (default: text) |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff rule`

Explain a rule (or all rules)

```
ruff rule [OPTIONS] <RULE|--all>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Explain all rules |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--output-format` | `` | string | Output format [default: text] [possible values: text, json] (default: text) |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff server`

Run the language server

```
ruff server [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML `<KEY> = <VALUE>` pair (such as you might find in a `ruff.toml` configuration file) overriding a specific configuration option. Overrides of individual settings using this option always take precedence over all configuration files, including configuration files that were also specified using `--config` |
| `--help` | `-h` | bool | Print help (see a summary with '-h') |
| `--isolated` | `` | string | Ignore all configuration files |
| `--preview` | `` | bool | Enable preview mode. Use `--no-preview` to disable. |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

### `ruff version`

Display Ruff's version

```
ruff version [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Either a path to a TOML configuration file (`pyproject.toml` or `ruff.toml`), or a TOML |
| `--help` | `-h` | bool | Print help |
| `--isolated` | `` | string | Ignore all configuration files |
| `--output-format` | `` | string | [default: text] [possible values: text, json] (default: text) |
| `--quiet` | `-q` | bool | Print diagnostics, but nothing else |
| `--silent` | `-s` | bool | Disable all logging (but still exit with status code "1" upon detecting diagnostics) |
| `--verbose` | `-v` | bool | Enable verbose logging |

