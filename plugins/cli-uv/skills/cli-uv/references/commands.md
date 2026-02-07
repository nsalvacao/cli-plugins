# uv -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--version` | `-V` | bool | Display the uv version |

## Commands

### `uv add`

Add dependencies to the project

```
uv add [OPTIONS] <PACKAGES|--requirements <REQUIREMENTS>>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `` | bool | Prefer the active virtual environment over the project's virtual environment |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--bounds` | `` | string | The kind of version specifier to use when adding dependencies [possible values: lower, major, minor, exact] |
| `--branch` | `` | string | Branch to use when adding a dependency from Git |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: UV_CONSTRAINT=] |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--dev` | `` | bool | Add the requirements to the development dependency group [env: UV_DEV=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--editable` | `` | bool | Add the requirements as editable |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra` | `` | string | Extras to enable for the dependency |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--frozen` | `` | bool | Add dependencies without re-locking the project [env: UV_FROZEN=] |
| `--group` | `` | string | Add the requirements to the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--lfs` | `` | bool | Whether to use Git LFS when adding a dependency from Git |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--marker` | `-m` | string | Apply this marker to all added packages |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-install-local` | `` | bool | Do not install local path dependencies |
| `--no-install-package` | `` | string | Do not install the given package(s) |
| `--no-install-project` | `` | bool | Do not install the current project |
| `--no-install-workspace` | `` | bool | Do not install any workspace members, including the current project |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-sync` | `` | bool | Avoid syncing the virtual environment [env: UV_NO_SYNC=] |
| `--no-workspace` | `` | bool | Don't add the dependency as a workspace member |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--optional` | `` | string | Add the requirements to the package's optional dependencies for the specified extra |
| `--package` | `` | string | Add the dependency to a specific package in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for resolving and syncing. [env: UV_PYTHON=] |
| `--raw` | `` | bool | Add a dependency as provided |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--requirements` | `-r` | string | Add the packages listed in the given files |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--rev` | `` | string | Commit to use when adding a dependency from Git |
| `--script` | `` | string | Add the dependency to the specified Python script, rather than to a project |
| `--tag` | `` | string | Tag to use when adding a dependency from Git |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--workspace` | `` | bool | Add the dependency as a workspace member |

### `uv build`

Build Python packages into source distributions and wheels

```
uv build [OPTIONS] [SRC]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-packages` | `` | bool | Builds all packages in the workspace |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--clear` | `` | string | Clear the output directory before the build, removing stale artifacts |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--force-pep517` | `` | bool | Always build through PEP 517, don't use the fast path for the uv build |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-logs` | `` | bool | Hide logs from the build backend |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-create-gitignore` | `` | string | Do not create a `.gitignore` file in the output directory |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-verify-hashes` | `` | string | Disable validation of hashes in the requirements file [env: |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--out-dir` | `-o` | string | The output directory to which distributions should be written |
| `--package` | `` | string | Build a specific package in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for the build environment. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--require-hashes` | `` | bool | Require a matching hash for each requirement [env: UV_REQUIRE_HASHES=] |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--sdist` | `` | string | Build a source distribution ("sdist") from the given directory |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--wheel` | `` | string | Build a binary distribution ("wheel") from the given directory |

### `uv export`

Export the project's lockfile to an alternate format

```
uv export [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--all-groups` | `` | bool | Include dependencies from all dependency groups |
| `--all-packages` | `` | bool | Export the entire workspace |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra` | `` | string | Include optional dependencies from the specified extra name |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--format` | `` | string | The format to which `uv.lock` should be exported [possible values: |
| `--frozen` | `` | bool | Do not update the `uv.lock` before exporting [env: UV_FROZEN=] |
| `--group` | `` | string | Include dependencies from the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-annotate` | `` | bool | Exclude comment annotations indicating the source of each package |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-default-groups` | `` | bool | Ignore the default dependency groups [env: UV_NO_DEFAULT_GROUPS=] |
| `--no-dev` | `` | bool | Disable the development dependency group [env: UV_NO_DEV=] |
| `--no-editable` | `` | bool | Export any editable dependencies, including the project and any workspace |
| `--no-emit-local` | `` | bool | Do not include local path dependencies in the exported requirements |
| `--no-emit-package` | `` | string | Do not emit the given package(s) |
| `--no-emit-project` | `` | bool | Do not emit the current project |
| `--no-emit-workspace` | `` | bool | Do not emit any workspace members, including the root project |
| `--no-extra` | `` | string | Exclude the specified optional dependencies, if `--all-extras` is supplied |
| `--no-group` | `` | string | Disable the specified dependency group [env: UV_NO_GROUP=] |
| `--no-hashes` | `` | bool | Omit hashes in the generated output |
| `--no-header` | `` | string | Exclude the comment header at the top of the generated output file |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-dev` | `` | bool | Only include the development dependency group |
| `--only-group` | `` | string | Only include dependencies from the specified dependency group |
| `--output-file` | `-o` | string | Write the exported requirements to the given file |
| `--package` | `` | string | Export the dependencies for specific packages in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--prune` | `` | string | Prune the given package from the dependency tree |
| `--python` | `-p` | string | The Python interpreter to use during resolution. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--script` | `` | string | Export the dependencies for the specified PEP 723 Python script, rather than |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

### `uv format`

Format Python code in the project

```
uv format [OPTIONS] [-- <EXTRA_ARGS>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--check` | `` | string | Check if files are formatted without applying changes |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--diff` | `` | bool | Show a diff of formatting changes without applying them |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-project` | `` | bool | Avoid discovering a project or workspace |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--version` | `` | string | The version of Ruff to use for formatting |

### `uv help`

Display documentation for a command

```
uv help [OPTIONS] [COMMAND]...
```

### `uv init`

Create a new project

```
uv init [OPTIONS] [PATH]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--app` | `` | bool | Create a project for an application |
| `--author-from` | `` | string | Fill in the `authors` field in the `pyproject.toml` [possible values: auto, git, |
| `--bare` | `` | bool | Only create a `pyproject.toml` |
| `--build-backend` | `` | string | Initialize a build-backend of choice for the project [env: |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--description` | `` | string | Set the project description |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--lib` | `` | bool | Create a project for a library |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--name` | `` | string | The name of the project |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-description` | `` | bool | Disable the description for the project |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-package` | `` | bool | Do not set up the project to be built as a Python package |
| `--no-pin-python` | `` | string | Do not create a `.python-version` file for the project |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-readme` | `` | string | Do not create a `README.md` file |
| `--no-workspace` | `` | bool | Avoid discovering a workspace and create a standalone project |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--package` | `` | bool | Set up the project to be built as a Python package |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use to determine the minimum supported Python version. [env: |
| `--script` | `` | bool | Create a script |
| `--vcs` | `` | string | Initialize a version control system for the project [possible values: git, none] |

### `uv lock`

Update the project's lockfile

```
uv lock [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--check` | `` | string | Check if the lockfile is up-to-date |
| `--check-exists` | `` | bool | Assert that a `uv.lock` exists without checking if it is up-to-date [env: UV_FROZEN=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | string | Perform a dry run, without writing the lockfile |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use during resolution. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--script` | `` | string | Lock the specified Python script, rather than the current project |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

### `uv publish`

Upload distributions to an index

```
uv publish [OPTIONS] [FILES]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--check-url` | `` | string | Check an index URL for existing files to skip duplicate uploads [env: UV_PUBLISH_CHECK_URL=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | string | Perform a dry run without uploading files |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The name of an index in the configuration to use for publishing. [env: UV_PUBLISH_INDEX=] |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for remote requirements files [env: UV_KEYRING_PROVIDER=] [possible values: disabled, subprocess] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-attestations` | `` | string | Do not upload attestations for the published files [env: UV_PUBLISH_NO_ATTESTATIONS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--password` | `-p` | string | The password for the upload [env: UV_PUBLISH_PASSWORD=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--publish-url` | `` | string | The URL of the upload endpoint (not the index URL) [env: UV_PUBLISH_URL=] |
| `--token` | `-t` | string | The token for the upload [env: UV_PUBLISH_TOKEN=] |
| `--trusted-publishing` | `` | string | Configure trusted publishing [possible values: automatic, always, never] |
| `--username` | `-u` | string | The username for the upload [env: UV_PUBLISH_USERNAME=] |

### `uv remove`

Remove dependencies from the project

```
uv remove [OPTIONS] <PACKAGES>...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `` | bool | Prefer the active virtual environment over the project's virtual environment |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--dev` | `` | bool | Remove the packages from the development dependency group [env: UV_DEV=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--frozen` | `` | bool | Remove dependencies without re-locking the project [env: UV_FROZEN=] |
| `--group` | `` | string | Remove the packages from the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-sync` | `` | bool | Avoid syncing the virtual environment after re-locking the project [env: UV_NO_SYNC=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--optional` | `` | string | Remove the packages from the project's optional dependencies for the specified extra |
| `--package` | `` | string | Remove the dependencies from a specific package in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for resolving and syncing. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--script` | `` | string | Remove the dependency from the specified Python script, rather than from a project |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

### `uv run`

Run a command or script

```
uv run [OPTIONS] [COMMAND]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `` | bool | Prefer the active virtual environment over the project's virtual |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--all-groups` | `` | bool | Include dependencies from all dependency groups |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--env-file` | `` | string | Load environment variables from a `.env` file [env: UV_ENV_FILE=] |
| `--exact` | `` | bool | Perform an exact sync, removing extraneous packages |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra` | `` | string | Include optional dependencies from the specified extra name |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--group` | `` | string | Include dependencies from the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--isolated` | `` | bool | Run the command in an isolated virtual environment [env: UV_ISOLATED=] |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--module` | `-m` | bool | Run a Python module |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-default-groups` | `` | bool | Ignore the default dependency groups [env: UV_NO_DEFAULT_GROUPS=] |
| `--no-dev` | `` | bool | Disable the development dependency group [env: UV_NO_DEV=] |
| `--no-editable` | `` | bool | Install any editable dependencies, including the project and any |
| `--no-env-file` | `` | string | Avoid reading environment variables from a `.env` file [env: |
| `--no-extra` | `` | string | Exclude the specified optional dependencies, if `--all-extras` is |
| `--no-group` | `` | string | Disable the specified dependency group [env: UV_NO_GROUP=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-dev` | `` | bool | Only include the development dependency group |
| `--only-group` | `` | string | Only include dependencies from the specified dependency group |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for the run environment. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--with` | `-w` | string | Run with the given packages installed |
| `--with-editable` | `` | string | Run with the given packages installed in editable mode |
| `--with-requirements` | `` | string | Run with the packages listed in the given files |

### `uv sync`

Update the project's environment

```
uv sync [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `` | bool | Sync dependencies to the active virtual environment |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--all-groups` | `` | bool | Include dependencies from all dependency groups |
| `--all-packages` | `` | bool | Sync all packages in the workspace |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--check` | `` | bool | Check if the Python environment is synchronized with the project |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | string | Perform a dry run, without writing the lockfile or modifying the project environment |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra` | `` | string | Include optional dependencies from the specified extra name |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--frozen` | `` | string | Sync without updating the `uv.lock` file [env: UV_FROZEN=] |
| `--group` | `` | string | Include dependencies from the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--inexact` | `` | bool | Do not remove extraneous packages present in the environment |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-default-groups` | `` | bool | Ignore the default dependency groups [env: UV_NO_DEFAULT_GROUPS=] |
| `--no-dev` | `` | bool | Disable the development dependency group [env: UV_NO_DEV=] |
| `--no-editable` | `` | bool | Install any editable dependencies, including the project and any workspace members, as non-editable [env: UV_NO_EDITABLE=] |
| `--no-extra` | `` | string | Exclude the specified optional dependencies, if `--all-extras` is supplied |
| `--no-group` | `` | string | Disable the specified dependency group [env: UV_NO_GROUP=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-install-local` | `` | bool | Do not install local path dependencies |
| `--no-install-package` | `` | string | Do not install the given package(s) |
| `--no-install-project` | `` | bool | Do not install the current project |
| `--no-install-workspace` | `` | bool | Do not install any workspace members, including the root project |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-dev` | `` | bool | Only include the development dependency group |
| `--only-group` | `` | string | Only include dependencies from the specified dependency group |
| `--output-format` | `` | string | Select the output format [default: text] [possible values: text, json] (default: text) |
| `--package` | `` | string | Sync for specific packages in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for the project environment. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: windows, linux, macos, x86_64-pc-windows-msvc, aarch64-pc-windows-msvc, i686-pc-windows-msvc, x86_64-unknown-linux-gnu, aarch64-apple-darwin, x86_64-apple-darwin, aarch64-unknown-linux-gnu, aarch64-unknown-linux-musl, x86_64-unknown-linux-musl, riscv64-unknown-linux, x86_64-manylinux2014, x86_64-manylinux_2_17, x86_64-manylinux_2_28, x86_64-manylinux_2_31, x86_64-manylinux_2_32, x86_64-manylinux_2_33, x86_64-manylinux_2_34, x86_64-manylinux_2_35, x86_64-manylinux_2_36, x86_64-manylinux_2_37, x86_64-manylinux_2_38, x86_64-manylinux_2_39, x86_64-manylinux_2_40, aarch64-manylinux2014, aarch64-manylinux_2_17, aarch64-manylinux_2_28, aarch64-manylinux_2_31, aarch64-manylinux_2_32, aarch64-manylinux_2_33, aarch64-manylinux_2_34, aarch64-manylinux_2_35, aarch64-manylinux_2_36, aarch64-manylinux_2_37, aarch64-manylinux_2_38, aarch64-manylinux_2_39, aarch64-manylinux_2_40, aarch64-linux-android, x86_64-linux-android, wasm32-pyodide2024, arm64-apple-ios, arm64-apple-ios-simulator, x86_64-apple-ios-simulator] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--script` | `` | string | Sync the environment for a Python script, rather than the current project |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

### `uv tree`

Display the project's dependency tree

```
uv tree [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-groups` | `` | bool | Include dependencies from all dependency groups |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--depth` | `-d` | string | Maximum display depth of the dependency tree [default: 255] (default: 255) |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--frozen` | `` | bool | Display the requirements without locking the project [env: UV_FROZEN=] |
| `--group` | `` | string | Include dependencies from the specified dependency group |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--invert` | `` | bool | Show the reverse dependencies for the given package. This flag will invert |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-dedupe` | `` | bool | Do not de-duplicate repeated dependencies. Usually, when a package has |
| `--no-default-groups` | `` | bool | Ignore the default dependency groups [env: UV_NO_DEFAULT_GROUPS=] |
| `--no-dev` | `` | bool | Disable the development dependency group [env: UV_NO_DEV=] |
| `--no-group` | `` | string | Disable the specified dependency group [env: UV_NO_GROUP=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-dev` | `` | bool | Only include the development dependency group |
| `--only-group` | `` | string | Only include dependencies from the specified dependency group |
| `--outdated` | `` | bool | Show the latest available version of each package in the tree |
| `--package` | `` | string | Display only the specified packages |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--prune` | `` | string | Prune the given package from the display of the dependency tree |
| `--python` | `-p` | string | The Python interpreter to use for locking and filtering. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform to use when filtering the tree [possible values: windows, linux, |
| `--python-version` | `` | string | The Python version to use when filtering the tree |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--script` | `` | string | Show the dependency tree the specified PEP 723 Python script, rather than the |
| `--show-sizes` | `` | bool | Show compressed wheel sizes for packages in the tree |
| `--universal` | `` | bool | Show a platform-independent dependency tree |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

### `uv venv`

Create a virtual environment

```
uv venv [OPTIONS] [PATH]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-existing` | `` | string | Preserve any existing files or directories at the target path |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--clear` | `-c` | string | Remove any existing files or directories at the target path [env: UV_VENV_CLEAR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--default-index` | `` | string | The URL of the default package index (by default: <https://pypi.org/simple>) |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for a specific package to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, in |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default index |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: UV_INDEX_STRATEGY=] [possible values: first-index, unsafe-first-match, unsafe-best-match] |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: UV_KEYRING_PROVIDER=] [possible values: disabled, subprocess] |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] [possible values: clone, copy, hardlink, symlink] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-project` | `` | bool | Avoid discovering a project or workspace |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--prompt` | `` | string | Provide an alternative prompt prefix for the virtual environment. |
| `--python` | `-p` | string | The Python interpreter to use for the virtual environment. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--relocatable` | `` | bool | Make the virtual environment relocatable |
| `--seed` | `` | bool | Install seed packages (one or more of: `pip`, `setuptools`, and `wheel`) into the virtual environment [env: UV_VENV_SEED=] |
| `--system-site-packages` | `` | string | Give the virtual environment access to the system site packages directory |

### `uv version`

Read or update the project's version

```
uv version [OPTIONS] [VALUE]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `` | bool | Prefer the active virtual environment over the project's virtual environment |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | bool | Don't write a new version to the `pyproject.toml` |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--frozen` | `` | bool | Update the version without re-locking the project [env: UV_FROZEN=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--locked` | `` | bool | Assert that the `uv.lock` will remain unchanged [env: UV_LOCKED=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-sync` | `` | bool | Avoid syncing the virtual environment after re-locking the project [env: |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--output-format` | `` | string | The format of the output [default: text] [possible values: text, json] (default: text) |
| `--package` | `` | string | Update the version of a specific package in the workspace |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use for resolving and syncing. [env: UV_PYTHON=] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--short` | `` | bool | Only show the version |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

## Command Groups

### `uv auth`

Manage authentication

```
uv auth [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv auth dir`

Show the path to the uv credentials directory

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv auth login`

Login to a service

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--keyring-provider` | `` | string | The keyring provider to use for storage of credentials [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--password` | `` | string | The password to use for the service |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--token` | `-t` | string | The token to use for the service |
| `--username` | `-u` | string | The username to use for the service |

#### `uv auth logout`

Logout of a service

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--keyring-provider` | `` | string | The keyring provider to use for storage of credentials [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--username` | `-u` | string | The username to logout |

#### `uv auth token`

Show the authentication token for a service

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--keyring-provider` | `` | string | The keyring provider to use for reading credentials [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--username` | `-u` | string | The username to lookup |

### `uv cache`

Manage uv's cache

```
uv cache [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv cache clean`

Clear the cache, removing all entries or those linked to specific packages

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--force` | `` | bool | Force removal of the cache, ignoring in-use checks |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv cache dir`

Show the cache directory

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv cache prune`

Prune all unreachable objects from the cache

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--ci` | `` | bool | Optimize the cache for persistence in a continuous integration environment, like GitHub Actions |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--force` | `` | bool | Force removal of the cache, ignoring in-use checks |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv cache size`

Show the cache size

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--human` | `-H` | bool | Display the cache size in human-readable format (e.g., `1.2 GiB` instead of raw bytes) |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

### `uv pip`

Manage Python packages with a pip-compatible interface

```
uv pip [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv pip check`

Verify installed packages have compatible dependencies

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter for which packages should be checked. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which packages should be checked [possible values: windows, |
| `--python-version` | `` | string | The Python version against which packages should be checked |
| `--system` | `` | bool | Check packages in the system Python environment [env: UV_SYSTEM_PYTHON=] |

#### `uv pip compile`

Compile a `requirements.in` file to a `requirements.txt` or `pylock.toml` file

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--annotation-style` | `` | string | The style of the annotation comments included in the output file, used to indicate the source of each package [possible values: line, split] |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when building source distributions [env: UV_BUILD_CONSTRAINT=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: UV_CONSTRAINT=] |
| `--custom-compile-command` | `` | string | The header comment to include at the top of the output file generated by `uv pip compile` [env: UV_CUSTOM_COMPILE_COMMAND=] |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--emit-build-options` | `` | string | Include `--no-binary` and `--only-binary` entries in the generated output file |
| `--emit-find-links` | `` | string | Include `--find-links` entries in the generated output file |
| `--emit-index-annotation` | `` | bool | Include comment annotations indicating the index used to resolve each package (e.g., `# from https://pypi.org/simple`) |
| `--emit-index-url` | `` | string | Include `--index-url` and `--extra-index-url` entries in the generated output file |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--excludes` | `` | string | Exclude packages from resolution using the given requirements files [env: UV_EXCLUDE=] |
| `--extra` | `` | string | Include optional dependencies from the specified extra name; may be provided more than once |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--format` | `` | string | The format in which the resolution should be output [possible values: requirements.txt, pylock.toml] |
| `--generate-hashes` | `` | string | Include distribution hashes in the output file |
| `--group` | `` | string | Install the specified dependency group from a `pyproject.toml` |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: UV_LINK_MODE=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-annotate` | `` | bool | Exclude comment annotations indicating the source of each package |
| `--no-binary` | `` | string | Don't install pre-built wheels |
| `--no-build` | `` | bool | Don't build source distributions |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-deps` | `` | string | Ignore package dependencies, instead only add those packages explicitly listed on the command line to the resulting requirements file |
| `--no-emit-package` | `` | string | Specify a package to omit from the output resolution. Its dependencies will still be included in the resolution. Equivalent to pip-compile's `--unsafe-package` option |
| `--no-header` | `` | string | Exclude the comment header at the top of the generated output file |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-strip-extras` | `` | string | Include extras in the output file |
| `--no-strip-markers` | `` | string | Include environment markers in the output file |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-binary` | `` | string | Only use pre-built wheels; don't build source distributions |
| `--output-file` | `-o` | string | Write the compiled requirements to the given `requirements.txt` or `pylock.toml` file |
| `--overrides` | `` | string | Override versions using the given requirements files [env: UV_OVERRIDE=] |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use during resolution. |
| `--python-platform` | `` | string | The platform for which requirements should be resolved [possible values: windows, linux, macos, x86_64-pc-windows-msvc, aarch64-pc-windows-msvc, i686-pc-windows-msvc, x86_64-unknown-linux-gnu, aarch64-apple-darwin, x86_64-apple-darwin, aarch64-unknown-linux-gnu, aarch64-unknown-linux-musl, x86_64-unknown-linux-musl, riscv64-unknown-linux, x86_64-manylinux2014, x86_64-manylinux_2_17, x86_64-manylinux_2_28, x86_64-manylinux_2_31, x86_64-manylinux_2_32, x86_64-manylinux_2_33, x86_64-manylinux_2_34, x86_64-manylinux_2_35, x86_64-manylinux_2_36, x86_64-manylinux_2_37, x86_64-manylinux_2_38, x86_64-manylinux_2_39, x86_64-manylinux_2_40, aarch64-manylinux2014, aarch64-manylinux_2_17, aarch64-manylinux_2_28, aarch64-manylinux_2_31, aarch64-manylinux_2_32, aarch64-manylinux_2_33, aarch64-manylinux_2_34, aarch64-manylinux_2_35, aarch64-manylinux_2_36, aarch64-manylinux_2_37, aarch64-manylinux_2_38, aarch64-manylinux_2_39, aarch64-manylinux_2_40, aarch64-linux-android, x86_64-linux-android, wasm32-pyodide2024, arm64-apple-ios, arm64-apple-ios-simulator, x86_64-apple-ios-simulator] |
| `--python-version` | `` | string | The Python version to use for resolution |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--system` | `` | bool | Install packages into the system Python environment [env: UV_SYSTEM_PYTHON=] |
| `--torch-backend` | `` | string | The backend to use when fetching packages in the PyTorch ecosystem (e.g., `cpu`, `cu126`, or `auto`) [env: UV_TORCH_BACKEND=] [possible values: auto, cpu, cu130, cu129, cu128, cu126, cu125, cu124, cu123, cu122, cu121, cu120, cu118, cu117, cu116, cu115, cu114, cu113, cu112, cu111, cu110, cu102, cu101, cu100, cu92, cu91, cu90, cu80, rocm7.1, rocm7.0, rocm6.4, rocm6.3, rocm6.2.4, rocm6.2, rocm6.1, rocm6.0, rocm5.7, rocm5.6, rocm5.5, rocm5.4.2, rocm5.4, rocm5.3, rocm5.2, rocm5.1.1, rocm4.2, rocm4.1, rocm4.0.1, xpu] |
| `--universal` | `` | string | Perform a universal resolution, attempting to generate a single `requirements.txt` output file that is compatible with all operating systems, architectures, and Python implementations |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |

#### `uv pip freeze`

List, in requirements format, packages installed in an environment

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude` | `` | string | Exclude the specified package(s) from the output |
| `--exclude-editable` | `` | bool | Exclude any editable packages from output |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--path` | `` | string | Restrict to the specified installation path for listing packages (can be used multiple times) |
| `--prefix` | `` | string | List packages from the specified `--prefix` directory |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter for which packages should be listed. [env: UV_PYTHON=] |
| `--strict` | `` | bool | Validate the Python environment, to detect packages with missing dependencies and other |
| `--system` | `` | bool | List packages in the system Python environment [env: UV_SYSTEM_PYTHON=] |
| `--target` | `-t` | string | List packages from the specified `--target` directory |

#### `uv pip install`

Install packages into an environment

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--break-system-packages` | `` | bool | Allow uv to modify an `EXTERNALLY-MANAGED` Python installation [env: |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | bool | Perform a dry run, i.e., don't actually install anything but resolve the |
| `--editable` | `-e` | string | Install the editable package based on the provided local file path |
| `--exact` | `` | bool | Perform an exact sync, removing extraneous packages |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--excludes` | `` | string | Exclude packages from resolution using the given requirements files [env: |
| `--extra` | `` | string | Include optional dependencies from the specified extra name; may be |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--group` | `` | string | Install the specified dependency group from a `pylock.toml` or |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | string | Don't install pre-built wheels |
| `--no-break-system-packages` | `` | bool |  |
| `--no-build` | `` | bool | Don't build source distributions |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-deps` | `` | bool | Ignore package dependencies, instead only installing those packages |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-verify-hashes` | `` | string | Disable validation of hashes in the requirements file [env: |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-binary` | `` | string | Only use pre-built wheels; don't build source distributions |
| `--overrides` | `` | string | Override versions using the given requirements files [env: UV_OVERRIDE=] |
| `--prefix` | `` | string | Install packages into `lib`, `bin`, and other top-level folders under the |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter into which packages should be installed. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: |
| `--python-version` | `` | string | The minimum Python version that should be supported by the requirements |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--require-hashes` | `` | bool | Require a matching hash for each requirement [env: UV_REQUIRE_HASHES=] |
| `--requirements` | `-r` | string | Install the packages listed in the given files |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--strict` | `` | bool | Validate the Python environment after completing the installation, to |
| `--system` | `` | bool | Install packages into the system Python environment [env: |
| `--target` | `-t` | string | Install packages into the specified directory, rather than into the |
| `--torch-backend` | `` | string | The backend to use when fetching packages in the PyTorch ecosystem (e.g., |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--user` | `` | bool |  |

#### `uv pip list`

List, in tabular format, packages installed in an environment

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--editable` | `-e` | bool | Only include editable projects |
| `--exclude` | `` | string | Exclude the specified package(s) from the output |
| `--exclude-editable` | `` | bool | Exclude any editable packages from output |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--format` | `` | string | Select the output format [default: columns] [possible values: columns, freeze, json] (default: columns) |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--outdated` | `` | bool | List outdated packages |
| `--prefix` | `` | string | List packages from the specified `--prefix` directory |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter for which packages should be listed. [env: UV_PYTHON=] |
| `--strict` | `` | bool | Validate the Python environment, to detect packages with missing dependencies and other |
| `--system` | `` | bool | List packages in the system Python environment [env: UV_SYSTEM_PYTHON=] |
| `--target` | `-t` | string | List packages from the specified `--target` directory |

#### `uv pip show`

Show information about one or more installed packages

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--files` | `-f` | string | Show the full list of installed files for each package |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--prefix` | `` | string | Show a package from the specified `--prefix` directory |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to find the package in. [env: UV_PYTHON=] |
| `--strict` | `` | bool | Validate the Python environment, to detect packages with missing dependencies and other issues |
| `--system` | `` | bool | Show a package in the system Python environment [env: UV_SYSTEM_PYTHON=] |
| `--target` | `-t` | string | Show a package from the specified `--target` directory |

#### `uv pip sync`

Sync an environment with a `requirements.txt` or `pylock.toml` file

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-extras` | `` | bool | Include all optional dependencies |
| `--allow-empty-requirements` | `` | bool | Allow sync of empty requirements, which will clear the environment of all |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--break-system-packages` | `` | bool | Allow uv to modify an `EXTERNALLY-MANAGED` Python installation [env: |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | bool | Perform a dry run, i.e., don't actually install anything but resolve the |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra` | `` | string | Include optional dependencies from the specified extra name; may be |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--group` | `` | string | Install the specified dependency group from a `pylock.toml` or |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-allow-empty-requirements` | `` | bool |  |
| `--no-binary` | `` | string | Don't install pre-built wheels |
| `--no-break-system-packages` | `` | bool |  |
| `--no-build` | `` | bool | Don't build source distributions |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--no-verify-hashes` | `` | string | Disable validation of hashes in the requirements file [env: |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-binary` | `` | string | Only use pre-built wheels; don't build source distributions |
| `--prefix` | `` | string | Install packages into `lib`, `bin`, and other top-level folders under the |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter into which packages should be installed. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: |
| `--python-version` | `` | string | The minimum Python version that should be supported by the requirements |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--require-hashes` | `` | bool | Require a matching hash for each requirement [env: UV_REQUIRE_HASHES=] |
| `--strict` | `` | bool | Validate the Python environment after completing the installation, to |
| `--system` | `` | bool | Install packages into the system Python environment [env: |
| `--target` | `-t` | string | Install packages into the specified directory, rather than into the |
| `--torch-backend` | `` | string | The backend to use when fetching packages in the PyTorch ecosystem (e.g., |

#### `uv pip tree`

Display the dependency tree for an environment

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--depth` | `-d` | string | Maximum display depth of the dependency tree [default: 255] (default: 255) |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--invert` | `` | bool | Show the reverse dependencies for the given package. This flag will invert the tree and |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-dedupe` | `` | bool | Do not de-duplicate repeated dependencies. Usually, when a package has already |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--outdated` | `` | bool | Show the latest available version of each package in the tree |
| `--package` | `` | string | Display only the specified packages |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--prune` | `` | string | Prune the given package from the display of the dependency tree |
| `--python` | `-p` | string | The Python interpreter for which packages should be listed. [env: UV_PYTHON=] |
| `--show-sizes` | `` | bool | Show compressed wheel sizes for packages in the tree |
| `--show-version-specifiers` | `` | bool | Show the version constraint(s) imposed on each package |
| `--strict` | `` | bool | Validate the Python environment, to detect packages with missing dependencies and other |
| `--system` | `` | bool | List packages in the system Python environment [env: UV_SYSTEM_PYTHON=] |

#### `uv pip uninstall`

Uninstall packages from an environment

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--break-system-packages` | `` | bool | Allow uv to modify an `EXTERNALLY-MANAGED` Python installation [env: |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | bool | Perform a dry run, i.e., don't actually uninstall anything but print the |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for remote requirements files |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-break-system-packages` | `` | bool |  |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--prefix` | `` | string | Uninstall packages from the specified `--prefix` directory |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter from which packages should be uninstalled. [env: UV_PYTHON=] |
| `--requirements` | `-r` | string | Uninstall the packages listed in the given files |
| `--system` | `` | bool | Use the system Python to uninstall packages [env: UV_SYSTEM_PYTHON=] |
| `--target` | `-t` | string | Uninstall packages from the specified `--target` directory |

### `uv python`

Manage Python versions and installations

```
uv python [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv python dir`

Show the uv Python installation directory

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--bin` | `` | string | Show the directory into which `uv python` will install Python executables. |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv python find`

Search for a Python installation

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-project` | `` | bool | Avoid discovering a project or workspace |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python-downloads-json-url` | `` | string | URL pointing to JSON of custom Python installations |
| `--script` | `` | string | Find the environment for a Python script, rather than the current project |
| `--show-version` | `` | string | Show the Python version that would be used instead of the path to the interpreter |
| `--system` | `` | bool | Only find system Python interpreters [env: UV_SYSTEM_PYTHON=] |

#### `uv python install`

Download and install Python versions

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | bool | Compile Python's standard library to bytecode after installation [env: UV_COMPILE_BYTECODE=] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--default` | `` | bool | Use as the default Python version |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--force` | `-f` | bool | Replace existing Python executables during installation |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--install-dir` | `-i` | string | The directory to store the Python installation in [env: UV_PYTHON_INSTALL_DIR=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--mirror` | `` | string | Set the URL to use as the source for downloading Python installations |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-bin` | `` | string | Do not install a Python executable into the `bin` directory |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-registry` | `` | bool | Do not register the Python installation in the Windows registry |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--pypy-mirror` | `` | string | Set the URL to use as the source for downloading PyPy installations |
| `--python-downloads-json-url` | `` | string | URL pointing to JSON of custom Python installations |
| `--reinstall` | `-r` | bool | Reinstall the requested Python version, if it's already installed |
| `--upgrade` | `-U` | bool | Upgrade existing Python installations to the latest patch version |

#### `uv python list`

List the available Python installations

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-arches` | `` | bool | List Python downloads for all architectures |
| `--all-platforms` | `` | bool | List Python downloads for all platforms |
| `--all-versions` | `` | bool | List all Python versions, including old patch versions |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--only-downloads` | `` | bool | Only show available Python downloads |
| `--only-installed` | `` | bool | Only show installed Python versions |
| `--output-format` | `` | string | Select the output format [default: text] [possible values: text, json] (default: text) |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python-downloads-json-url` | `` | string | URL pointing to JSON of custom Python installations |
| `--show-urls` | `` | string | Show the URLs of available Python downloads |

#### `uv python pin`

Pin to a specific Python version

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--global` | `` | bool | Update the global Python version pin |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-project` | `` | bool | Avoid validating the Python pin is compatible with the project or workspace |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--resolved` | `` | bool | Write the resolved Python interpreter path instead of the request |
| `--rm` | `` | bool | Remove the Python version pin |

#### `uv python uninstall`

Uninstall Python versions

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Uninstall all managed Python versions |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--install-dir` | `-i` | string | The directory where the Python was installed [env: UV_PYTHON_INSTALL_DIR=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv python update-shell`

Ensure that the Python executable directory is on the `PATH`

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv python upgrade`

Upgrade installed Python versions

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | bool | Compile Python's standard library to bytecode after installation [env: UV_COMPILE_BYTECODE=] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--install-dir` | `-i` | string | The directory Python installations are stored in [env: UV_PYTHON_INSTALL_DIR=] |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--mirror` | `` | string | Set the URL to use as the source for downloading Python installations |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--pypy-mirror` | `` | string | Set the URL to use as the source for downloading PyPy installations |
| `--python-downloads-json-url` | `` | string | URL pointing to JSON of custom Python installations |
| `--reinstall` | `-r` | bool | Reinstall the latest Python patch, if it's already installed |

### `uv self`

Manage the uv executable

```
uv self [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv self update`

Update uv

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--dry-run` | `` | bool | Run without performing the update |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--token` | `` | string | A GitHub token for authentication. A token is not required but can be used to reduce the chance |

#### `uv self version`

Display uv's version

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--output-format` | `` | string | [default: text] [possible values: text, json] (default: text) |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--short` | `` | bool | Only print the version |

### `uv tool`

Run and install commands provided by Python packages

```
uv tool [OPTIONS] <COMMAND>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

**Subcommands:**

#### `uv tool dir`

Show the path to the uv tools directory

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--bin` | `` | string | Show the directory into which `uv tool` will install executables. |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv tool install`

Install commands provided by a Python package

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when building source distributions [env: UV_BUILD_CONSTRAINT=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: UV_CONSTRAINT=] |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--editable` | `-e` | string | Install the target package in editable mode, such that changes in the package's source directory are reflected without reinstallation |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--excludes` | `` | string | Exclude packages from resolution using the given requirements files [env: UV_EXCLUDE=] |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--force` | `` | bool | Force installation of the tool |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--lfs` | `` | bool | Whether to use Git LFS when adding a dependency from Git |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--overrides` | `` | string | Override versions using the given requirements files [env: UV_OVERRIDE=] |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use to build the tool environment. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: windows, linux, macos, x86_64-pc-windows-msvc, aarch64-pc-windows-msvc, i686-pc-windows-msvc, x86_64-unknown-linux-gnu, aarch64-apple-darwin, x86_64-apple-darwin, aarch64-unknown-linux-gnu, aarch64-unknown-linux-musl, x86_64-unknown-linux-musl, riscv64-unknown-linux, x86_64-manylinux2014, x86_64-manylinux_2_17, x86_64-manylinux_2_28, x86_64-manylinux_2_31, x86_64-manylinux_2_32, x86_64-manylinux_2_33, x86_64-manylinux_2_34, x86_64-manylinux_2_35, x86_64-manylinux_2_36, x86_64-manylinux_2_37, x86_64-manylinux_2_38, x86_64-manylinux_2_39, x86_64-manylinux_2_40, aarch64-manylinux2014, aarch64-manylinux_2_17, aarch64-manylinux_2_28, aarch64-manylinux_2_31, aarch64-manylinux_2_32, aarch64-manylinux_2_33, aarch64-manylinux_2_34, aarch64-manylinux_2_35, aarch64-manylinux_2_36, aarch64-manylinux_2_37, aarch64-manylinux_2_38, aarch64-manylinux_2_39, aarch64-manylinux_2_40, aarch64-linux-android, x86_64-linux-android, wasm32-pyodide2024, arm64-apple-ios, arm64-apple-ios-simulator, x86_64-apple-ios-simulator] |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--torch-backend` | `` | string | The backend to use when fetching packages in the PyTorch ecosystem (e.g., `cpu`, `cu126`, or `auto`) [env: UV_TORCH_BACKEND=] [possible values: auto, cpu, cu130, cu129, cu128, cu126, cu125, cu124, cu123, cu122, cu121, cu120, cu118, cu117, cu116, cu115, cu114, cu113, cu112, cu111, cu110, cu102, cu101, cu100, cu92, cu91, cu90, cu80, rocm7.1, rocm7.0, rocm6.4, rocm6.3, rocm6.2.4, rocm6.2, rocm6.1, rocm6.0, rocm5.7, rocm5.6, rocm5.5, rocm5.4.2, rocm5.4, rocm5.3, rocm5.2, rocm5.1.1, rocm4.2, rocm4.1, rocm4.0.1, xpu] |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--with` | `-w` | string | Include the following additional requirements |
| `--with-editable` | `` | string | Include the given packages in editable mode |
| `--with-executables-from` | `` | string | Install executables from the following packages |
| `--with-requirements` | `` | string | Run with the packages listed in the given files |

#### `uv tool list`

List installed tools

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--show-extras` | `` | bool | Whether to display the extra requirements installed with each tool |
| `--show-paths` | `` | string | Whether to display the path to each tool environment and installed executable |
| `--show-python` | `` | bool | Whether to display the Python version associated with each tool |
| `--show-version-specifiers` | `` | bool | Whether to display the version specifier(s) used to install each tool |
| `--show-with` | `` | bool | Whether to display the additional requirements installed with each tool |

#### `uv tool run`

Run a command provided by a Python package

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--build-constraints` | `-b` | string | Constrain build dependencies using the given requirements files when |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-settings-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--constraints` | `-c` | string | Constrain versions using the given requirements files [env: |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--env-file` | `` | string | Load environment variables from a `.env` file [env: UV_ENV_FILE=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--from` | `` | string | Use the given package to provide the command |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--isolated` | `` | bool | Run the tool in an isolated virtual environment, ignoring any |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--lfs` | `` | bool | Whether to use Git LFS when adding a dependency from Git |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | bool | Avoid reading from or writing to the cache, instead using a temporary |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-env-file` | `` | string | Avoid reading environment variables from a `.env` file [env: |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--overrides` | `` | string | Override versions using the given requirements files [env: UV_OVERRIDE=] |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | The Python interpreter to use to build the run environment. [env: UV_PYTHON=] |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: |
| `--refresh` | `` | bool | Refresh all cached data |
| `--refresh-package` | `` | string | Refresh cached data for a specific package |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |
| `--torch-backend` | `` | string | The backend to use when fetching packages in the PyTorch ecosystem (e.g., |
| `--upgrade` | `-U` | string | Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh` |
| `--upgrade-package` | `-P` | string | Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package` |
| `--with` | `-w` | string | Run with the given packages installed |
| `--with-editable` | `` | string | Run with the given packages installed in editable mode |
| `--with-requirements` | `` | string | Run with the packages listed in the given files |

#### `uv tool uninstall`

Uninstall a tool

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Uninstall all tools |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv tool update-shell`

Ensure that the tool executable directory is on the `PATH`

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |

#### `uv tool upgrade`

Upgrade installed tools

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Upgrade all tools |
| `--allow-insecure-host` | `` | string | Allow insecure connections to a host [env: UV_INSECURE_HOST=] |
| `--cache-dir` | `` | string | Path to the cache directory [env: UV_CACHE_DIR=] |
| `--color` | `` | string | Control the use of color in output [possible values: auto, always, never] |
| `--compile-bytecode` | `` | string | Compile Python files to bytecode after installation [env: |
| `--config-file` | `` | string | The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=] |
| `--config-setting` | `-C` | string | Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs |
| `--config-setting-package` | `` | string | Settings to pass to the PEP 517 build backend for a specific package, specified as `PACKAGE:KEY=VALUE` pairs |
| `--default-index` | `` | string | The URL of the default package index (by default: |
| `--directory` | `` | string | Change to the given directory prior to running the command [env: UV_WORKING_DIR=] |
| `--exclude-newer` | `` | string | Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=] |
| `--exclude-newer-package` | `` | string | Limit candidate packages for specific packages to those that were uploaded prior to the given date |
| `--extra-index-url` | `` | string | (Deprecated: use `--index` instead) Extra URLs of package indexes to use, |
| `--find-links` | `-f` | string | Locations to search for candidate distributions, in addition to those found |
| `--fork-strategy` | `` | string | The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values: fewest, requires-python] |
| `--help` | `-h` | bool | Display the concise help for this command |
| `--index` | `` | string | The URLs to use when resolving dependencies, in addition to the default |
| `--index-strategy` | `` | string | The strategy to use when resolving against multiple index URLs [env: |
| `--index-url` | `-i` | string | (Deprecated: use `--default-index` instead) The URL of the Python package |
| `--keyring-provider` | `` | string | Attempt to use `keyring` for authentication for index URLs [env: |
| `--link-mode` | `` | string | The method to use when installing packages from the global cache [env: |
| `--managed-python` | `` | bool | Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=] |
| `--native-tls` | `` | bool | Whether to load TLS certificates from the platform's native store [env: UV_NATIVE_TLS=] |
| `--no-binary` | `` | bool | Don't install pre-built wheels [env: UV_NO_BINARY=] |
| `--no-binary-package` | `` | string | Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=] |
| `--no-build` | `` | bool | Don't build source distributions [env: UV_NO_BUILD=] |
| `--no-build-isolation` | `` | bool | Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=] |
| `--no-build-isolation-package` | `` | string | Disable isolation when building source distributions for a specific package |
| `--no-build-package` | `` | string | Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=] |
| `--no-cache` | `-n` | string | Avoid reading from or writing to the cache, instead using a temporary directory for the |
| `--no-config` | `` | string | Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=] |
| `--no-index` | `` | string | Ignore the registry index (e.g., PyPI), instead relying on direct URL |
| `--no-managed-python` | `` | bool | Disable use of uv-managed Python versions [env: UV_NO_MANAGED_PYTHON=] |
| `--no-progress` | `` | bool | Hide all progress outputs [env: UV_NO_PROGRESS=] |
| `--no-python-downloads` | `` | bool | Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"] |
| `--no-sources` | `` | string | Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any workspace, Git, URL, or local path sources [env: UV_NO_SOURCES=] |
| `--no-sources-package` | `` | string | Don't use sources from the `tool.uv.sources` table for the specified packages [env: UV_NO_SOURCES_PACKAGE=] |
| `--offline` | `` | bool | Disable network access [env: UV_OFFLINE=] |
| `--prerelease` | `` | string | The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit, if-necessary-or-explicit] |
| `--project` | `` | string | Discover a project in the given directory [env: UV_PROJECT=] |
| `--python` | `-p` | string | Upgrade a tool, and specify it to use the given Python interpreter to build its |
| `--python-platform` | `` | string | The platform for which requirements should be installed [possible values: |
| `--reinstall` | `` | bool | Reinstall all packages, regardless of whether they're already installed. |
| `--reinstall-package` | `` | string | Reinstall a specific package, regardless of whether it's already |
| `--resolution` | `` | string | The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest, lowest, lowest-direct] |

