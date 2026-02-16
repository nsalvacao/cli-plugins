# pip -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

## Commands

### `pip cache`

Inspect and manage pip's wheel cache.

```
pip cache dir
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--format` | `` | string | Select the output format among: human (default) or abspath |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip check`

Verify installed packages have compatible dependencies.

```
pip check [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip completion`

A helper command to be used for command completion.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bash` | `-b` | bool | Emit completion code for bash |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--fish` | `-f` | bool | Emit completion code for fish |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--powershell` | `-p` | bool | Emit completion code for powershell |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |
| `--zsh` | `-z` | bool | Emit completion code for zsh |

### `pip config`

Manage local and global configuration.

```
pip config [<file-option>] list
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--editor` | `` | string | Editor to use to edit the file. Uses VISUAL or EDITOR environment variables if not |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--global` | `` | string | Use the system-wide configuration file only |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--site` | `` | string | Use the current environment configuration file only |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--user` | `` | string | Use the user configuration file only |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip debug`

Display debug information.

```
pip debug <options>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abi` | `` | string | Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--implementation` | `` | string | Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified, then the current interpreter implementation is used. Use 'py' to force implementation-agnostic wheels. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--platform` | `` | string | Only use wheels compatible with <platform>. Defaults to the platform of the running |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--python-version` | `` | string | The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0). |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip download`

Download packages from:

```
pip download [options] <requirement specifier> [package-index-options] ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abi` | `` | string | Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--check-build-dependencies` | `` | bool | Check the build dependencies when PEP517 is used. |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--constraint` | `-c` | string | Constrain versions using the given constraints file. This option can be used multiple |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--dest` | `-d` | string | Download packages into <dir>. |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--extra-index-url` | `` | string | Extra URLs of package indexes to use in addition to --index-url. Should follow the same |
| `--find-links` | `-f` | string | If a URL or path to an html file, then parse for links to archives such as sdist |
| `--global-option` | `` | string | Extra global options to be supplied to the setup.py call before the install or |
| `--help` | `-h` | bool | Show help. |
| `--ignore-requires-python` | `` | bool | Ignore the Requires-Python information. |
| `--implementation` | `` | string | Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified, then the current interpreter implementation is used. Use 'py' to force implementation-agnostic wheels. |
| `--index-url` | `-i` | string | Base URL of the Python Package Index (default https://pypi.org/simple). This should (default: https://pypi.org/simple) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-binary` | `` | string | Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on them. |
| `--no-build-isolation` | `` | bool | Disable isolation when building a modern source distribution. Build dependencies |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-clean` | `` | bool | Don't clean up build directories. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-deps` | `` | bool | Don't install package dependencies. |
| `--no-index` | `` | string | Ignore package index (only looking at --find-links URLs instead). |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--only-binary` | `` | string | Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option is used on them. |
| `--platform` | `` | string | Only use wheels compatible with <platform>. Defaults to the platform of the running |
| `--pre` | `` | bool | Include pre-release and development versions. By default, pip only finds stable |
| `--prefer-binary` | `` | bool | Prefer binary packages over source packages, even if the source packages are newer. |
| `--progress-bar` | `` | string | Specify whether the progress bar should be used [on, off] (default: on) (default: on) |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--python-version` | `` | string | The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0). |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-hashes` | `` | bool | Require a hash to check each requirement against, for repeatable installs. This option |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--requirement` | `-r` | string | Install from the given requirements file. This option can be used multiple times. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--src` | `` | string | Directory to check out editable projects into. The default in a virtualenv is "<venv |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--use-pep517` | `` | bool | Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip freeze`

Output installed packages in requirements format.

```
pip freeze [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Do not skip these packages in the output: pip |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exclude` | `` | string | Exclude specified package from the output |
| `--exclude-editable` | `` | bool | Exclude editable package from output. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--local` | `-l` | bool | If in a virtualenv that has global access, do not output globally-installed packages. |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--path` | `` | string | Restrict to the specified installation path for listing packages (can be used multiple |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--requirement` | `-r` | string | Use the order in the given requirements file and its comments when generating output. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--user` | `` | bool | Only output packages installed in user-site. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip hash`

Compute a hash of a local package archive.

```
pip hash [options] <file> ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--algorithm` | `-a` | string | The hash algorithm to use: one of sha256, sha384, sha512 |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip help`

Show help for commands

```
pip help <command>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip index`

Inspect information available from package indexes.

```
pip index versions <package>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abi` | `` | string | Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--extra-index-url` | `` | string | Extra URLs of package indexes to use in addition to --index-url. Should follow the same |
| `--find-links` | `-f` | string | If a URL or path to an html file, then parse for links to archives such as sdist |
| `--help` | `-h` | bool | Show help. |
| `--ignore-requires-python` | `` | bool | Ignore the Requires-Python information. |
| `--implementation` | `` | string | Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified, then the current interpreter implementation is used. Use 'py' to force implementation-agnostic wheels. |
| `--index-url` | `-i` | string | Base URL of the Python Package Index (default https://pypi.org/simple). This should (default: https://pypi.org/simple) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-binary` | `` | string | Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on them. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-index` | `` | string | Ignore package index (only looking at --find-links URLs instead). |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--only-binary` | `` | string | Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option is used on them. |
| `--platform` | `` | string | Only use wheels compatible with <platform>. Defaults to the platform of the running |
| `--pre` | `` | bool | Include pre-release and development versions. By default, pip only finds stable |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--python-version` | `` | string | The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0). |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip inspect`

Inspect the content of a Python environment and produce a report in JSON format.

```
pip inspect [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--local` | `` | bool | If in a virtualenv that has global access, do not list globally-installed packages. |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--path` | `` | string | Restrict to the specified installation path for listing packages (can be used multiple |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--user` | `` | bool | Only output packages installed in user-site. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip install`

Install packages from:

```
pip install [options] <requirement specifier> [package-index-options] ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abi` | `` | string | Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then |
| `--break-system-packages` | `` | bool | Allow pip to modify an EXTERNALLY-MANAGED Python installation |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--check-build-dependencies` | `` | bool | Check the build dependencies when PEP517 is used. |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--compile` | `` | string | Compile Python source files to bytecode |
| `--config-settings` | `-C` | string | Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-settings options to pass multiple keys to the backend. |
| `--constraint` | `-c` | string | Constrain versions using the given constraints file. This option can be used multiple |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--dry-run` | `` | bool | Don't actually install anything, just print what would be. Can be used in combination |
| `--editable` | `-e` | string | Install a project in editable mode (i.e. setuptools "develop mode") from a local project |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--extra-index-url` | `` | string | Extra URLs of package indexes to use in addition to --index-url. Should follow the same |
| `--find-links` | `-f` | string | If a URL or path to an html file, then parse for links to archives such as sdist |
| `--force-reinstall` | `` | bool | Reinstall all packages even if they are already up-to-date. |
| `--global-option` | `` | string | Extra global options to be supplied to the setup.py call before the install or |
| `--help` | `-h` | bool | Show help. |
| `--ignore-installed` | `-I` | bool | Ignore the installed packages, overwriting them. This can break your system if the |
| `--ignore-requires-python` | `` | bool | Ignore the Requires-Python information. |
| `--implementation` | `` | string | Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified, then the current interpreter implementation is used. Use 'py' to force implementation-agnostic wheels. |
| `--index-url` | `-i` | string | Base URL of the Python Package Index (default https://pypi.org/simple). This should (default: https://pypi.org/simple) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-binary` | `` | string | Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on them. |
| `--no-build-isolation` | `` | bool | Disable isolation when building a modern source distribution. Build dependencies |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-clean` | `` | bool | Don't clean up build directories. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-compile` | `` | string | Do not compile Python source files to bytecode |
| `--no-deps` | `` | bool | Don't install package dependencies. |
| `--no-index` | `` | string | Ignore package index (only looking at --find-links URLs instead). |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--no-warn-conflicts` | `` | bool | Do not warn about broken dependencies |
| `--no-warn-script-location` | `` | bool | Do not warn when installing scripts outside PATH |
| `--only-binary` | `` | string | Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option is used on them. |
| `--platform` | `` | string | Only use wheels compatible with <platform>. Defaults to the platform of the running |
| `--pre` | `` | bool | Include pre-release and development versions. By default, pip only finds stable |
| `--prefer-binary` | `` | bool | Prefer binary packages over source packages, even if the source packages are newer. |
| `--prefix` | `` | string | Installation prefix where lib, bin and other top-level folders are placed. Note that the |
| `--progress-bar` | `` | string | Specify whether the progress bar should be used [on, off] (default: on) (default: on) |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--python-version` | `` | string | The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0). |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--report` | `` | string | Generate a JSON file describing what pip did to install the provided requirements. Can |
| `--require-hashes` | `` | bool | Require a hash to check each requirement against, for repeatable installs. This option |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--requirement` | `-r` | string | Install from the given requirements file. This option can be used multiple times. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--root` | `` | string | Install everything relative to this alternate root directory. |
| `--root-user-action` | `` | string | Action if pip is run as a root user. By default, a warning message is shown. |
| `--src` | `` | string | Directory to check out editable projects into. The default in a virtualenv is "<venv |
| `--target` | `-t` | string | Install packages into <dir>. By default this will not replace existing files/folders in |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--upgrade` | `-U` | bool | Upgrade all specified packages to the newest available version. The handling of |
| `--upgrade-strategy` | `` | string | Determines how dependency upgrading should be handled [default: only-if-needed]. "eager" (default: only-if-needed) |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--use-pep517` | `` | bool | Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy |
| `--user` | `` | string | Install to the Python user install directory for your platform. Typically ~/.local/, or |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip list`

List installed packages, including editables.

```
pip list [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--editable` | `-e` | bool | List editable projects. |
| `--exclude` | `` | string | Exclude specified package from the output |
| `--exclude-editable` | `` | bool | Exclude editable package from output. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--extra-index-url` | `` | string | Extra URLs of package indexes to use in addition to --index-url. Should follow the same |
| `--find-links` | `-f` | string | If a URL or path to an html file, then parse for links to archives such as sdist |
| `--format` | `` | string | Select the output format among: columns (default), freeze, or json. The 'freeze' format |
| `--help` | `-h` | bool | Show help. |
| `--include-editable` | `` | bool | Include editable package from output. |
| `--index-url` | `-i` | string | Base URL of the Python Package Index (default https://pypi.org/simple). This should (default: https://pypi.org/simple) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--local` | `-l` | bool | If in a virtualenv that has global access, do not list globally-installed packages. |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-index` | `` | string | Ignore package index (only looking at --find-links URLs instead). |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--not-required` | `` | bool | List packages that are not dependencies of installed packages. |
| `--outdated` | `-o` | bool | List outdated packages |
| `--path` | `` | string | Restrict to the specified installation path for listing packages (can be used multiple |
| `--pre` | `` | bool | Include pre-release and development versions. By default, pip only finds stable |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--uptodate` | `-u` | bool | List uptodate packages |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--user` | `` | bool | Only output packages installed in user-site. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip search`

Search for PyPI packages whose name or summary contains <query>.

```
pip search [options] <query>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--index` | `-i` | string | Base URL of Python Package Index (default https://pypi.org/pypi) (default: https://pypi.org/pypi) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip show`

Show information about one or more installed packages.

```
pip show [options] <package> ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--files` | `-f` | string | Show the full list of installed files for each package. |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |

### `pip uninstall`

Uninstall packages.

```
pip uninstall [options] <package> ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--break-system-packages` | `` | bool | Allow pip to modify an EXTERNALLY-MANAGED Python installation |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--help` | `-h` | bool | Show help. |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--requirement` | `-r` | string | Uninstall all the packages listed in the given requirements file.  This option can be |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--root-user-action` | `` | string | Action if pip is run as a root user. By default, a warning message is shown. |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |
| `--yes` | `-y` | bool | Don't ask for confirmation of uninstall deletions. |

### `pip wheel`

Build Wheel archives for your requirements and dependencies.

```
pip wheel [options] <requirement specifier> ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--build-option` | `` | string | Extra arguments to be supplied to 'setup.py bdist_wheel'. |
| `--cache-dir` | `` | string | Store the cache data in <dir>. |
| `--cert` | `` | string | Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL |
| `--check-build-dependencies` | `` | bool | Check the build dependencies when PEP517 is used. |
| `--client-cert` | `` | string | Path to SSL client certificate, a single file containing the private key and the |
| `--config-settings` | `-C` | string | Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-settings options to pass multiple keys to the backend. |
| `--constraint` | `-c` | string | Constrain versions using the given constraints file. This option can be used multiple |
| `--debug` | `` | bool | Let unhandled exceptions propagate outside the main subroutine, instead of logging them |
| `--disable-pip-version-check` | `` | bool | Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index. |
| `--editable` | `-e` | string | Install a project in editable mode (i.e. setuptools "develop mode") from a local project |
| `--exists-action` | `` | string | Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, |
| `--extra-index-url` | `` | string | Extra URLs of package indexes to use in addition to --index-url. Should follow the same |
| `--find-links` | `-f` | string | If a URL or path to an html file, then parse for links to archives such as sdist |
| `--global-option` | `` | string | Extra global options to be supplied to the setup.py call before the install or |
| `--help` | `-h` | bool | Show help. |
| `--ignore-requires-python` | `` | bool | Ignore the Requires-Python information. |
| `--index-url` | `-i` | string | Base URL of the Python Package Index (default https://pypi.org/simple). This should (default: https://pypi.org/simple) |
| `--isolated` | `` | bool | Run pip in an isolated mode, ignoring environment variables and user configuration. |
| `--keyring-provider` | `` | string | Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled) (default: disabled) |
| `--log` | `` | string | Path to a verbose appending log. |
| `--no-binary` | `` | string | Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on them. |
| `--no-build-isolation` | `` | bool | Disable isolation when building a modern source distribution. Build dependencies |
| `--no-cache-dir` | `` | bool | Disable the cache. |
| `--no-clean` | `` | bool | Don't clean up build directories. |
| `--no-color` | `` | bool | Suppress colored output. |
| `--no-deps` | `` | bool | Don't install package dependencies. |
| `--no-index` | `` | string | Ignore package index (only looking at --find-links URLs instead). |
| `--no-input` | `` | bool | Disable prompting for input. |
| `--no-python-version-warning` | `` | bool | Silence deprecation warnings for upcoming unsupported Pythons. |
| `--no-verify` | `` | bool | Don't verify if built wheel is valid. |
| `--only-binary` | `` | string | Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:" to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option is used on them. |
| `--pre` | `` | bool | Include pre-release and development versions. By default, pip only finds stable |
| `--prefer-binary` | `` | bool | Prefer binary packages over source packages, even if the source packages are newer. |
| `--progress-bar` | `` | string | Specify whether the progress bar should be used [on, off] (default: on) (default: on) |
| `--proxy` | `` | string | Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. |
| `--python` | `` | string | Run pip with the specified Python interpreter. |
| `--quiet` | `-q` | bool | Give less output. Option is additive, and can be used up to 3 times (corresponding to |
| `--require-hashes` | `` | bool | Require a hash to check each requirement against, for repeatable installs. This option |
| `--require-virtualenv` | `` | bool | Allow pip to only run in a virtual environment; exit with an error otherwise. |
| `--requirement` | `-r` | string | Install from the given requirements file. This option can be used multiple times. |
| `--retries` | `` | string | Maximum number of retries each connection should attempt (default 5 times). |
| `--src` | `` | string | Directory to check out editable projects into. The default in a virtualenv is "<venv |
| `--timeout` | `` | string | Set the socket timeout (default 15 seconds). |
| `--trusted-host` | `` | string | Mark this host or host:port pair as trusted, even though it does not have valid or any |
| `--use-deprecated` | `` | string | Enable deprecated functionality, that will be removed in the future. |
| `--use-feature` | `` | string | Enable new functionality, that may be backward incompatible. |
| `--use-pep517` | `` | bool | Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy |
| `--verbose` | `-v` | bool | Give more output. Option is additive, and can be used up to 3 times. |
| `--version` | `-V` | bool | Show version and exit. |
| `--wheel-dir` | `-w` | string | Build wheels into <dir>, where the default is the current working directory. |

