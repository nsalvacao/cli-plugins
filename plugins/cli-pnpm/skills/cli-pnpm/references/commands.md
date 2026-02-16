# pnpm -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--recursive` | `-r` | bool | Run the command for each project in the workspace. |

## Commands

### `pnpm add`

Installs a package and any packages that it depends on. By default, any new package is installed as a prod dependency

```
pnpm add <name>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, |
| `--[no-]save-exact` | `-E` | bool | Install exact version |
| `--[no-]save-workspace-protocol` | `` | bool | Save packages from the workspace with a |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that |
| `--allow-build` | `` | bool | A list of package names that are allowed |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--config` | `` | bool | Save the dependency to configurational |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--global` | `-g` | bool | Install as a global package |
| `--global-dir` | `` | string | Specify a custom directory to store global |
| `--help` | `-h` | bool | Output usage information |
| `--ignore-scripts` | `` | bool | Don't run lifecycle scripts |
| `--loglevel` | `` | string | What level of logs to report. Any logs at |
| `--offline` | `` | bool | Trigger an error if any required |
| `--prefer-offline` | `` | bool | Skip staleness checks for cached data, but |
| `--recursive` | `-r` | bool | Run installation recursively in every |
| `--save-catalog` | `` | bool | Save package to the default catalog |
| `--save-catalog-name` | `` | string | Save package to the specified catalog |
| `--save-dev` | `-D` | bool | Save package to your `devDependencies` |
| `--save-optional` | `-O` | bool | Save package to your |
| `--save-peer` | `` | bool | Save package to your `peerDependencies` |
| `--save-prod` | `-P` | bool | Save package to your `dependencies`. The |
| `--store-dir` | `` | string | The directory in which all the packages |
| `--stream` | `` | bool | Stream output from child processes |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--virtual-store-dir` | `` | string | The directory with links to the store |
| `--workspace` | `` | bool | Only adds the new dependency if it is |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace |

### `pnpm audit`

Checks for known security issues with the installed packages

```
pnpm audit [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--audit-level` | `` | string | Only print advisories with severity greater than |
| `--dev` | `-D` | bool | Only audit "devDependencies" |
| `--fix` | `` | string | Add overrides to the package.json file in order |
| `--ignore` | `` | string | Ignore a vulnerability by CVE |
| `--ignore-registry-errors` | `` | bool | Use exit code 0 if the registry responds with an |
| `--ignore-unfixable` | `` | bool | Ignore all CVEs with no resolution |
| `--json` | `` | bool | Output audit report in JSON format |
| `--no-optional` | `` | bool | Don't audit "optionalDependencies" |
| `--prod` | `-P` | bool | Only audit "dependencies" and |

### `pnpm create`

pnpm create <name-without-create>

```
pnpm create <name>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-build` | `` | bool | A list of package names that are allowed to run |

### `pnpm dlx`

Fetches a package from the registry without installing it as a dependency, hot loads it, and runs whatever default command binary it exposes

```
pnpm dlx <command> [args...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-build` | `` | bool | A list of package names that are allowed to run |
| `--package` | `` | bool | The package to install before running the command |
| `--reporter` | `` | string | The output is always appended to the end. No |
| `--reporter` | `` | string | The default reporter when the stdout is TTY |
| `--reporter` | `` | string | The most verbose reporter. Prints all logs in |
| `--shell-mode` | `-c` | bool | Runs the script inside of a shell. Uses /bin/sh on |

### `pnpm exec`

Executes a shell command in scope of a project

```
pnpm [-r] [-c] exec <command> [args...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--help` | `-h` | bool | Output usage information |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or |
| `--no-reporter-hide-prefix` | `` | bool | Do not hide project name prefix from output of |
| `--parallel` | `` | bool | Completely disregard concurrency and |
| `--recursive` | `-r` | bool | Run the shell command in every package found in |
| `--report-summary` | `` | bool | Save the execution results of every package to |
| `--resume-from` | `` | bool | Command executed from given package |
| `--shell-mode` | `-c` | string | If exist, runs file inside of a shell. Uses |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm init`

Create a package.json file

```
pnpm init
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bare` | `` | string | Create a package.json file with the bare |
| `--init-package-manager` | `` | bool | Pin the project to the current pnpm version |
| `--init-type` | `` | string | Set the module system for the package. |

### `pnpm install`

Install all dependencies for a project

```
pnpm install [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By |
| `--[no-]frozen-lockfile` | `` | string | Don't generate a lockfile and fail |
| `--[no-]verify-store-integrity` | `` | bool | If false, doesn't check whether |
| `--aggregate-output` | `` | bool | Aggregate output from child |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--child-concurrency` | `` | string | Controls the number of child |
| `--dev` | `-D` | bool | Only `devDependencies` are |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--fix-lockfile` | `` | string | Fix broken lockfile entries |
| `--force` | `` | bool | Force reinstall dependencies: |
| `--global-dir` | `` | string | Specify a custom directory to store |
| `--help` | `-h` | bool | Output usage information |
| `--hoist-pattern` | `` | string | Hoist all dependencies matching the |
| `--ignore-pnpmfile` | `` | bool | Disable pnpm hooks defined in |
| `--ignore-scripts` | `` | bool | Don't run lifecycle scripts |
| `--ignore-workspace` | `` | bool | Ignore pnpm-workspace.yaml if |
| `--lockfile-dir` | `` | string | The directory in which the |
| `--lockfile-only` | `` | bool | Dependencies are not downloaded. |
| `--loglevel` | `` | string | What level of logs to report. Any |
| `--merge-git-branch-lockfiles` | `` | string | Merge lockfiles were generated on |
| `--modules-dir` | `` | string | The directory in which dependencies |
| `--network-concurrency` | `` | string | Maximum number of concurrent |
| `--no-hoist` | `` | bool | Dependencies inside the modules |
| `--no-lockfile` | `` | bool | Don't read or generate a |
| `--no-optional` | `` | bool | `optionalDependencies` are not |
| `--offline` | `` | bool | Trigger an error if any required |
| `--optimistic-repeat-install` | `` | bool | Skip reinstall if the workspace |
| `--package-import-method` | `` | string | Clones/hardlinks or copies |
| `--package-import-method` | `` | string | Clone (aka copy-on-write) packages |
| `--package-import-method` | `` | string | Copy packages from the store |
| `--package-import-method` | `` | string | Hardlink packages from the store |
| `--prefer-frozen-lockfile` | `` | bool | If the available `pnpm-lock.yaml` |
| `--prefer-offline` | `` | bool | Skip staleness checks for cached |
| `--prod` | `-P` | bool | Packages in `devDependencies` won't |
| `--public-hoist-pattern` | `` | string | Hoist all dependencies matching the |
| `--recursive` | `-r` | bool | Run installation recursively in |
| `--reporter` | `` | string | The output is always appended to the end. No |
| `--reporter` | `` | string | The default reporter when the stdout is TTY |
| `--reporter` | `` | string | The most verbose reporter. Prints all logs in |
| `--resolution-only` | `` | bool | Re-runs resolution: useful for |
| `--shamefully-hoist` | `` | bool | All the subdeps will be hoisted |
| `--side-effects-cache` | `` | bool | Use or cache the results of |
| `--side-effects-cache-readonly` | `` | bool | Only use the side effects cache if |
| `--store-dir` | `` | string | The directory in which all the |
| `--stream` | `` | bool | Stream output from child processes |
| `--strict-peer-dependencies` | `` | bool | Fail on missing or invalid peer |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--trust-policy` | `` | string | Fail when a package's trust level |
| `--trust-policy-exclude` | `` | string | Exclude specific packages from |
| `--trust-policy-ignore-after` | `` | string | Ignore trust downgrades for |
| `--use-running-store-server` | `` | bool | Only allows installation with a |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--use-store-server` | `` | bool | Starts a store server in the |
| `--virtual-store-dir` | `` | string | The directory with links to the |
| `--workspace-root` | `-w` | bool | Run the command on the root |

### `pnpm link`

Connect the local project to another one

```
pnpm link <dir|pkg name>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--help` | `-h` | bool | Output usage information |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm list`

Print all the versions of packages that are installed, as well as their dependencies, in a tree-structure

```
pnpm ls [<pkg> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--depth` | `-1` | bool | Display only projects. Useful in a monorepo. `pnpm ls |
| `--depth` | `` | string | Max display depth of the dependency tree |
| `--depth` | `` | string | Display only direct dependencies |
| `--dev` | `-D` | bool | Display only the dependency graph for packages in |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--exclude-peers` | `` | bool | Exclude peer dependencies |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--global` | `-g` | bool | List packages in the global install prefix instead of |
| `--global-dir` | `` | string | Specify a custom directory to store global packages |
| `--help` | `-h` | bool | Output usage information |
| `--json` | `` | bool | Show information in JSON format |
| `--lockfile-only` | `` | string | List packages from the lockfile only, without |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--long` | `` | bool | Show extended information |
| `--no-optional` | `` | bool | Don't display packages from `optionalDependencies` |
| `--only-projects` | `` | bool | Display only dependencies that are also projects |
| `--parseable` | `` | bool | Show parseable output instead of tree view |
| `--prod` | `-P` | bool | Display only the dependency graph for packages in |
| `--recursive` | `-r` | bool | Perform command on every package in subdirectories or |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm outdated`

Check for outdated packages

```
pnpm outdated [<pkg> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--compatible` | `` | bool | Print only versions that satisfy specs in |
| `--dev` | `-D` | bool | Check only "devDependencies" |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--format` | `` | string | Prints the outdated dependencies in the given format. |
| `--global-dir` | `` | string | Specify a custom directory to store global packages |
| `--help` | `-h` | bool | Output usage information |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--long` | `` | bool | By default, details about the outdated packages (such |
| `--no-optional` | `` | bool | Don't check "optionalDependencies" |
| `--no-table` | `` | bool | Prints the outdated packages in a list. Good for |
| `--prod` | `-P` | bool | Check only "dependencies" and "optionalDependencies" |
| `--recursive` | `-r` | bool | Check for outdated dependencies in every package |
| `--sort-by` | `` | string | Specify the sorting method. Currently only `name` is |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm publish`

Publishes a package to the registry

```
pnpm publish [<tarball>|<dir>] [--tag <tag>] [--access <public|restricted>] [options]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--access` | `` | string | Tells the registry whether this package |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--dry-run` | `` | bool | Does everything a publish would do except |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--force` | `` | bool | Packages are proceeded to be published even |
| `--ignore-scripts` | `` | bool | Ignores any publish related lifecycle |
| `--json` | `` | bool | Show information in JSON format |
| `--no-git-checks` | `` | bool | Don't check if current branch is your |
| `--otp` | `` | bool | When publishing packages that require |
| `--publish-branch` | `` | bool | Sets branch name to publish. Default is |
| `--recursive` | `-r` | bool | Publish all packages from the workspace |
| `--report-summary` | `` | bool | Save the list of the newly published |
| `--tag` | `` | string | Registers the published package with the |
| `--test-pattern` | `` | string | Defines files related to tests. |

### `pnpm remove`

Removes packages from node_modules and from the project's package.json

```
pnpm remove <pkg>[@<version>]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--global-dir` | `` | string | Specify a custom directory to store global packages |
| `--help` | `-h` | bool | Output usage information |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--recursive` | `-r` | bool | Remove from every package found in subdirectories or |
| `--save-dev` | `-D` | bool | Remove the dependency only from "devDependencies" |
| `--save-optional` | `-O` | bool | Remove the dependency only from |
| `--save-prod` | `-P` | bool | Remove the dependency only from "dependencies" |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm run`

Runs a defined package script

```
pnpm run <command> [<args>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--help` | `-h` | bool | Output usage information |
| `--if-present` | `` | bool | Avoid exiting with a non-zero exit code when the |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or |
| `--no-bail` | `` | bool | The command will exit with a 0 exit code even if |
| `--parallel` | `` | bool | Completely disregard concurrency and topological |
| `--recursive` | `-r` | bool | Run the defined package script in every package |
| `--report-summary` | `` | bool | Save the execution results of every package to |
| `--reporter-hide-prefix` | `` | bool | Hide project name prefix from output of running |
| `--resume-from` | `` | bool | Command executed from given package |
| `--sequential` | `` | bool | Run the specified scripts one by one |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm self-update`

Nothing to stop. No server is running for the store at /mnt/d/.pnpm-store/v10

### `pnpm unlink`

Unlinks a package. Like yarn unlink but pnpm re-installs the dependency after removing the external link

```
pnpm unlink (in package dir)
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--help` | `-h` | bool | Output usage information |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--recursive` | `-r` | bool | Unlink in every package found in subdirectories or in |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm update`

Updates packages to their latest version based on the specified range

```
pnpm update [-g] [<pkg>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--depth` | `` | string | How deep should levels of dependencies be inspected. |
| `--dev` | `-D` | bool | Update packages only in "devDependencies" |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--global` | `-g` | bool | Update globally installed packages |
| `--global-dir` | `` | string | Specify a custom directory to store global packages |
| `--help` | `-h` | bool | Output usage information |
| `--interactive` | `-i` | bool | Show outdated dependencies and select which ones to |
| `--latest` | `-L` | bool | Ignore version ranges in package.json |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--no-optional` | `` | bool | Don't update packages in "optionalDependencies" |
| `--prod` | `-P` | bool | Update packages only in "dependencies" and |
| `--recursive` | `-r` | bool | Update in every package found in subdirectories or |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace` | `` | bool | Tries to link all packages from the workspace. |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

### `pnpm why`

Shows all packages that depend on the specified package

```
pnpm why <pkg> ...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--[no-]color` | `` | bool | Controls colors in the output. By default, output is |
| `--aggregate-output` | `` | bool | Aggregate output from child processes that are run in |
| `--changed-files-ignore-` | `` | bool |  |
| `--changed-files-ignore-pattern` | `` | string | Defines files to ignore when |
| `--depth` | `` | string | Max display depth of the dependency graph |
| `--dev` | `-D` | bool | Display only the dependency graph for packages in |
| `--dir` | `-C` | string | Change to directory <dir> (default: |
| `--exclude-peers` | `` | bool | Exclude peer dependencies |
| `--fail-if-no-match` | `` | bool | If no projects are matched by |
| `--filter` | `` | string | If a selector starts with ! (or |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Includes only the direct and |
| `--filter` | `` | string | Includes all direct and indirect |
| `--filter` | `` | string | Includes all packages that are |
| `--filter` | `` | string | Restricts the scope to package |
| `--filter-prod` | `` | string | Restricts the scope to package |
| `--global` | `-g` | bool | List packages in the global install prefix instead of |
| `--global-dir` | `` | string | Specify a custom directory to store global packages |
| `--help` | `-h` | bool | Output usage information |
| `--json` | `` | bool | Show information in JSON format |
| `--loglevel` | `` | string | What level of logs to report. Any logs at or higher |
| `--long` | `` | bool | Show extended information |
| `--no-optional` | `` | bool | Don't display packages from `optionalDependencies` |
| `--parseable` | `` | bool | Show parseable output instead of tree view |
| `--prod` | `-P` | bool | Display only the dependency graph for packages in |
| `--recursive` | `-r` | bool | Perform command on every package in subdirectories or |
| `--stream` | `` | bool | Stream output from child processes immediately, |
| `--test-pattern` | `` | string | Defines files related to tests. |
| `--use-stderr` | `` | bool | Divert all output to stderr |
| `--workspace-root` | `-w` | bool | Run the command on the root workspace project |

## Command Groups

### `pnpm config`

Manage the pnpm configuration files

```
pnpm config set <key> <value>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global` | `-g` | bool | Sets the configuration in the global config |
| `--json` | `` | bool | Show all the config settings in JSON format |
| `--location` | `` | string | When set to "project", the |

**Subcommands:**

#### `pnpm config delete`

Remove the config key from the config file

#### `pnpm config get`

Print the config value for the provided key

#### `pnpm config list`

Show all the config settings

#### `pnpm config set`

Set the config key to the value provided

