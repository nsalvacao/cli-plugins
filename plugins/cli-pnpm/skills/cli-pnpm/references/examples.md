# pnpm -- Usage Examples

_No explicit examples found in CLI help; generated from usage patterns._

## `pnpm add`

```bash
pnpm add <name>
```
Installs a package and any packages that it depends on. By default, any new package is installed as a prod dependency

## `pnpm audit`

```bash
pnpm audit [options]
```
Checks for known security issues with the installed packages

## `pnpm config`

```bash
pnpm config set <key> <value>
```
Manage the pnpm configuration files

### `pnpm config delete`

```bash
pnpm config delete
```
Remove the config key from the config file

### `pnpm config get`

```bash
pnpm config get
```
Print the config value for the provided key

### `pnpm config list`

```bash
pnpm config list
```
Show all the config settings

### `pnpm config set`

```bash
pnpm config set
```
Set the config key to the value provided

## `pnpm create`

```bash
pnpm create <name>
```
pnpm create <name-without-create>

## `pnpm dlx`

```bash
pnpm dlx <command> [args...]
```
Fetches a package from the registry without installing it as a dependency, hot loads it, and runs whatever default command binary it exposes

## `pnpm exec`

```bash
pnpm [-r] [-c] exec <command> [args...]
```
Executes a shell command in scope of a project

## `pnpm init`

```bash
pnpm init
```
Create a package.json file

## `pnpm install`

```bash
pnpm install [options]
```
Install all dependencies for a project

## `pnpm link`

```bash
pnpm link <dir|pkg name>
```
Connect the local project to another one

## `pnpm list`

```bash
pnpm ls [<pkg> ...]
```
Print all the versions of packages that are installed, as well as their dependencies, in a tree-structure

## `pnpm outdated`

```bash
pnpm outdated [<pkg> ...]
```
Check for outdated packages

## `pnpm publish`

```bash
pnpm publish [<tarball>|<dir>] [--tag <tag>] [--access <public|restricted>] [options]
```
Publishes a package to the registry

## `pnpm remove`

```bash
pnpm remove <pkg>[@<version>]...
```
Removes packages from node_modules and from the project's package.json

## `pnpm run`

```bash
pnpm run <command> [<args>...]
```
Runs a defined package script

## `pnpm self-update`

```bash
pnpm self-update
```
Nothing to stop. No server is running for the store at /mnt/d/.pnpm-store/v10

## `pnpm unlink`

```bash
pnpm unlink (in package dir)
```
Unlinks a package. Like yarn unlink but pnpm re-installs the dependency after removing the external link

## `pnpm update`

```bash
pnpm update [-g] [<pkg>...]
```
Updates packages to their latest version based on the specified range

## `pnpm why`

```bash
pnpm why <pkg> ...
```
Shows all packages that depend on the specified package

