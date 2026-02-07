# npm -- Complete Command Reference

## Commands

### `npm access`

Set access level on published packages

```
npm access list packages [<user>|<scope>|<scope:team>] [<package>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |

### `npm adduser`

Add a registry user account

```
npm adduser
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--auth-type` | `` | string |  |
| `--registry` | `` | string |  |
| `--scope` | `` | string |  |

### `npm audit`

Run a security audit

```
npm audit [fix|signatures]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--audit-level` | `` | string |  |
| `--dry-run` | `` | bool |  |
| `--force` | `-f` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--json` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--package-lock-only` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm bugs`

Report bugs for a package in a web browser

```
npm bugs [<pkgname> [<pkgname> ...]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--browser` | `` | string |  |
| `--include-workspace-root` | `` | bool |  |
| `--no-browser` | `` | string |  |
| `--registry` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm cache`

Manipulates packages and npx cache

```
npm cache add <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cache` | `` | string |  |

### `npm ci`

Clean install a project

```
npm ci
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm completion`

Tab Completion for npm

```
npm completion
```

### `npm config`

Manage the npm configuration files

```
npm config set <key>=<value> [<key>=<value> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--editor` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--json` | `` | bool |  |
| `--location` | `-L` | string |  |
| `--long` | `-l` | bool |  |

### `npm dedupe`

Reduce duplication in the package tree

```
npm dedupe
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm deprecate`

Deprecate a version of a package

```
npm deprecate <package-spec> <message>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |

### `npm diff`

The registry diff command

```
npm diff [...<paths>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--diff-dst-prefix` | `` | string |  |
| `--diff-ignore-all-space` | `` | bool |  |
| `--diff-name-only` | `` | bool |  |
| `--diff-no-prefix` | `` | bool |  |
| `--diff-src-prefix` | `` | string |  |
| `--diff-text` | `` | bool |  |
| `--diff-unified` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--tag` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm dist-tag`

Modify package distribution tags

```
npm dist-tag add <package-spec (with version)> [<tag>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--include-workspace-root` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm docs`

Open documentation for a package in a web browser

```
npm docs [<pkgname> [<pkgname> ...]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--browser` | `` | string |  |
| `--include-workspace-root` | `` | bool |  |
| `--no-browser` | `` | string |  |
| `--registry` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm doctor`

Check the health of your npm environment

```
npm doctor [connection] [registry] [versions] [environment] [permissions] [cache]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--registry` | `` | string |  |

### `npm edit`

Edit an installed package

```
npm edit <pkg>[/<subpkg>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--editor` | `` | string |  |

### `npm exec`

Run a command from a local or remote npm package

```
npm exec -- <pkg>[@<version>] [args...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--call` | `-c` | string |  |
| `--include-workspace-root` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm explain`

Explain installed packages

```
npm explain <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |

### `npm explore`

Browse an installed package

```
npm explore <pkg> [ -- <command>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--shell` | `` | string |  |

### `npm find-dupes`

Find duplication in the package tree

```
npm find-dupes
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm fund`

Retrieve funding information

```
npm fund [<package-spec>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--browser` | `` | string |  |
| `--json` | `` | bool |  |
| `--no-browser` | `` | string |  |
| `--unicode` | `` | bool |  |
| `--which` | `` | string |  |

### `npm get`

Get a value from the npm configuration

```
npm get [<key> ...] (See `npm config`)
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--long` | `-l` | bool |  |

### `npm help`

Get help on npm

```
npm help <term> [<terms..>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--viewer` | `` | string |  |

### `npm help-search`

Search npm help documentation

```
npm help-search <text>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--long` | `-l` | bool |  |

### `npm init`

Create a package.json file

```
npm init <package-spec> (same as `npx create-<package-spec>`)
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--init-author-name` | `` | string |  |
| `--init-author-url` | `` | string |  |
| `--init-license` | `` | string |  |
| `--init-module` | `` | string |  |
| `--init-private` | `` | bool |  |
| `--init-type` | `` | string |  |
| `--init-version` | `` | string |  |
| `--no-workspaces-update` | `` | bool |  |
| `--scope` | `` | string |  |
| `--workspaces` | `` | bool |  |
| `--yes` | `-y` | bool |  |

### `npm install`

Install a package

```
npm install [<package-spec> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--before` | `` | string |  |
| `--cpu` | `` | string |  |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--global` | `-g` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--libc` | `` | string |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--os` | `` | string |  |
| `--package-lock-only` | `` | bool |  |
| `--prefer-dedupe` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-exact` | `-E` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm install-ci-test`

Install a project with a clean slate and run tests

```
npm install-ci-test
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm install-test`

Install package(s) and run tests

```
npm install-test [<package-spec> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--before` | `` | string |  |
| `--cpu` | `` | string |  |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--global` | `-g` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--libc` | `` | string |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--os` | `` | string |  |
| `--package-lock-only` | `` | bool |  |
| `--prefer-dedupe` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-exact` | `-E` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm link`

Symlink a package folder

```
npm link [<package-spec>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--global` | `-g` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-exact` | `-E` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm ll`

List installed packages

```
npm ll [[<@scope>/]<pkg> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool |  |
| `--depth` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--json` | `` | bool |  |
| `--link` | `` | bool |  |
| `--long` | `-l` | bool |  |
| `--package-lock-only` | `` | bool |  |
| `--parseable` | `-p` | bool |  |
| `--unicode` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm login`

Login to a registry user account

```
npm login
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--auth-type` | `` | string |  |
| `--registry` | `` | string |  |
| `--scope` | `` | string |  |

### `npm logout`

Log out of the registry

```
npm logout
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--registry` | `` | string |  |
| `--scope` | `` | string |  |

### `npm ls`

List installed packages

```
npm ls <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool |  |
| `--depth` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--json` | `` | bool |  |
| `--link` | `` | bool |  |
| `--long` | `-l` | bool |  |
| `--package-lock-only` | `` | bool |  |
| `--parseable` | `-p` | bool |  |
| `--unicode` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm org`

Manage orgs

```
npm org set orgname username [developer | admin | owner]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |
| `--otp` | `` | string |  |
| `--parseable` | `-p` | bool |  |
| `--registry` | `` | string |  |

### `npm outdated`

Check for outdated packages

```
npm outdated [<package-spec> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool |  |
| `--before` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--json` | `` | bool |  |
| `--long` | `-l` | bool |  |
| `--parseable` | `-p` | bool |  |

### `npm owner`

Manage package owners

```
npm owner add <user> <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm pack`

Create a tarball from a package

```
npm pack <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--json` | `` | bool |  |
| `--pack-destination` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm ping`

Ping npm registry

```
npm ping
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--registry` | `` | string |  |

### `npm pkg`

Manages your package.json

```
npm pkg set <key>=<value> [<key>=<value> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool |  |
| `--json` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm prefix`

Display prefix

```
npm prefix
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global` | `-g` | bool |  |

### `npm profile`

Change settings on your registry profile

```
npm profile enable-2fa [auth-only|auth-and-writes]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |
| `--otp` | `` | string |  |
| `--parseable` | `-p` | bool |  |
| `--registry` | `` | string |  |

### `npm prune`

Remove extraneous packages

```
npm prune [[<@scope>/]<pkg>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--json` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm publish`

Publish a package

```
npm publish <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--access` | `` | string |  |
| `--dry-run` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--otp` | `` | string |  |
| `--provenance` | `` | string |  |
| `--provenance-file` | `` | string |  |
| `--tag` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm query`

Retrieve a filtered list of packages

```
npm query <selector>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--expect-result-count` | `` | string |  |
| `--expect-results` | `` | string |  |
| `--global` | `-g` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--package-lock-only` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm rebuild`

Rebuild a package

```
npm rebuild [<package-spec>] ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--foreground-scripts` | `` | bool |  |
| `--global` | `-g` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm repo`

Open package repository page in the browser

```
npm repo [<pkgname> [<pkgname> ...]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--browser` | `` | string |  |
| `--include-workspace-root` | `` | bool |  |
| `--no-browser` | `` | string |  |
| `--registry` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm restart`

Restart a package

```
npm restart [-- <args>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--ignore-scripts` | `` | bool |  |
| `--script-shell` | `` | string |  |

### `npm root`

Display npm root

```
npm root
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global` | `-g` | bool |  |

### `npm run`

Run arbitrary package scripts

```
npm run <command> [-- <args>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--foreground-scripts` | `` | bool |  |
| `--if-present` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--script-shell` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm sbom`

Generate a Software Bill of Materials (SBOM)

```
npm sbom
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--package-lock-only` | `` | bool |  |
| `--sbom-format` | `` | string |  |
| `--sbom-type` | `` | string |  |
| `--workspaces` | `` | bool |  |

### `npm search`

Search for packages

```
npm search <search term> [<search term> ...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |
| `--no-description` | `` | bool |  |
| `--offline` | `` | bool |  |
| `--parseable` | `-p` | bool |  |
| `--prefer-offline` | `` | bool |  |
| `--prefer-online` | `` | bool |  |
| `--registry` | `` | string |  |
| `--searchexclude` | `` | string |  |
| `--searchlimit` | `` | string |  |
| `--searchopts` | `` | string |  |

### `npm set`

Set a value in the npm configuration

```
npm set <key>=<value> [<key>=<value> ...] (See `npm config`)
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global` | `-g` | bool |  |
| `--location` | `-L` | string |  |

### `npm shrinkwrap`

Lock down dependency versions for publication

```
npm shrinkwrap
```

### `npm star`

Mark your favorite packages

```
npm star [<package-spec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |
| `--unicode` | `` | bool |  |

### `npm stars`

View packages marked as favorites

```
npm stars [<user>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--registry` | `` | string |  |

### `npm start`

Start a package

```
npm start [-- <args>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--ignore-scripts` | `` | bool |  |
| `--script-shell` | `` | string |  |

### `npm stop`

Stop a package

```
npm stop [-- <args>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--ignore-scripts` | `` | bool |  |
| `--script-shell` | `` | string |  |

### `npm team`

Manage organization teams and team memberships

```
npm team create <scope:team> [--otp <otpcode>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--json` | `` | bool |  |
| `--otp` | `` | string |  |
| `--parseable` | `-p` | bool |  |
| `--registry` | `` | string |  |

### `npm test`

Test a package

```
npm test [-- <args>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--ignore-scripts` | `` | bool |  |
| `--script-shell` | `` | string |  |

### `npm token`

Manage your authentication tokens

```
npm token list
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bypass-2fa` | `` | bool |  |
| `--expires` | `` | string |  |
| `--name` | `` | string |  |
| `--orgs-permission` | `` | string |  |
| `--otp` | `` | string |  |
| `--packages-all` | `` | bool |  |
| `--packages-and-scopes-permission` | `` | string |  |
| `--password` | `` | string |  |
| `--read-only` | `` | bool |  |
| `--registry` | `` | string |  |
| `--token-description` | `` | string |  |

### `npm undeprecate`

Undeprecate a version of a package

```
npm undeprecate <package-spec>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |

### `npm uninstall`

Remove a package

```
npm uninstall [<@scope>/]<pkg>...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--global` | `-g` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm unpublish`

Remove a package from the registry

```
npm unpublish [<package-spec>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool |  |
| `--force` | `-f` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm unstar`

Remove an item from your favorite packages

```
npm unstar [<package-spec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--otp` | `` | string |  |
| `--registry` | `` | string |  |
| `--unicode` | `` | bool |  |

### `npm update`

Update packages

```
npm update [<pkg>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--before` | `` | string |  |
| `--dry-run` | `` | bool |  |
| `--foreground-scripts` | `` | bool |  |
| `--global` | `-g` | bool |  |
| `--global-style` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--install-links` | `` | bool |  |
| `--install-strategy` | `` | string |  |
| `--legacy-bundling` | `` | bool |  |
| `--no-audit` | `` | bool |  |
| `--no-bin-links` | `` | bool |  |
| `--no-fund` | `` | bool |  |
| `--no-package-lock` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--strict-peer-deps` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm version`

Bump a package version

```
npm version [<newversion> | major | minor | patch | premajor | preminor | prepatch | prerelease | from-git]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-same-version` | `` | bool |  |
| `--ignore-scripts` | `` | bool |  |
| `--include-workspace-root` | `` | bool |  |
| `--json` | `` | bool |  |
| `--no-commit-hooks` | `` | bool |  |
| `--no-git-tag-version` | `` | bool |  |
| `--no-save` | `` | bool |  |
| `--no-workspaces-update` | `` | bool |  |
| `--save` | `-S` | bool |  |
| `--save-bundle` | `` | bool |  |
| `--save-dev` | `` | bool |  |
| `--save-optional` | `` | bool |  |
| `--save-peer` | `` | bool |  |
| `--save-prod` | `` | bool |  |
| `--sign-git-tag` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm view`

View registry info

```
npm view [<package-spec>] [<field>[.subfield]...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--include-workspace-root` | `` | bool |  |
| `--json` | `` | bool |  |
| `--workspaces` | `` | bool |  |

### `npm whoami`

Display npm username

```
npm whoami
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--registry` | `` | string |  |

