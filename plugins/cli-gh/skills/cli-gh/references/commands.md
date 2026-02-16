# gh -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--version` | `` | bool | Show gh version |

## Command Groups

### `gh agent-task`

Working with agent tasks in the GitHub CLI is in preview and

```
gh agent-task <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh agent-task create`

Create an agent task (preview)

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--base` | `-b` | string | Base branch for the pull request (use default branch if not provided) |
| `--custom-agent` | `-a` | string | Use a custom agent for the task. e.g., use 'my-agent' for the 'my-agent.md' agent |
| `--follow` | `` | bool | Follow agent session logs |
| `--from-file` | `-F` | string | Read task description from file (use "-" to read from standard input) |
| `--help` | `` | bool | Show help for command |

#### `gh agent-task list`

List agent tasks (preview)

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--limit` | `-L` | string | Maximum number of agent tasks to fetch (default 30) (default: 30) |
| `--web` | `-w` | bool | Open agent tasks in the browser |

#### `gh agent-task view`

View an agent task session.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--follow` | `` | bool | Follow agent session logs |
| `--help` | `` | bool | Show help for command |
| `--log` | `` | bool | Show agent session logs |
| `--web` | `-w` | bool | Open agent task in the browser |

### `gh alias`

Aliases can be used to make shortcuts for gh commands or to compose multiple commands.

```
gh alias <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh alias delete`

Delete set aliases

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Delete all aliases |
| `--help` | `` | bool | Show help for command |

#### `gh alias import`

Import aliases from the contents of a YAML file.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clobber` | `` | bool | Overwrite existing aliases of the same name |
| `--help` | `` | bool | Show help for command |

#### `gh alias list`

This command prints out all of the aliases gh is configured to use.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh alias set`

Define a word that will expand to a full gh command when invoked.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clobber` | `` | bool | Overwrite existing aliases of the same name |
| `--help` | `` | bool | Show help for command |
| `--shell` | `-s` | bool | Declare an alias to be passed through a shell interpreter |

### `gh attestation`

Download and verify artifact attestations.

```
gh attestation [subcommand] [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh attestation download`

### NOTE: This feature is currently in public preview, and subject to change.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--digest-alg` | `-d` | string | The algorithm used to compute a digest of the artifact: {sha256|sha512} (default "sha256") (default: sha256) |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `` | string | Configure host to use |
| `--limit` | `-L` | string | Maximum number of attestations to fetch (default 30) (default: 30) |
| `--owner` | `-o` | string | GitHub organization to scope attestation lookup by |
| `--predicate-type` | `` | string | Filter attestations by provided predicate type |
| `--repo` | `-R` | string | Repository name in the format <owner>/<repo> |

#### `gh attestation trusted-root`

Output contents for a trusted_root.jsonl file, likely for offline verification.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `` | string | Configure host to use |
| `--tuf-root` | `` | string | Path to the TUF root.json file on disk |
| `--tuf-url` | `` | string | URL to the TUF repository mirror |
| `--verify-only` | `` | bool | Don't output trusted_root.jsonl contents |

#### `gh attestation verify`

Verify the integrity and provenance of an artifact using its associated

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bundle` | `-b` | string | Path to bundle on disk, either a single bundle in a JSON file or a JSON lines file with multiple bundles |
| `--bundle-from-oci` | `` | bool | When verifying an OCI image, fetch the attestation bundle from the OCI registry instead of from GitHub |
| `--cert-identity` | `` | string | Enforce that the certificate's SubjectAlternativeName matches the provided value exactly |
| `--cert-identity-regex` | `-i` | string | Enforce that the certificate's SubjectAlternativeName matches the provided regex |
| `--cert-oidc-issuer` | `` | string | Enforce that the issuer of the OIDC token matches the provided value (default "https://token.actions.githubusercontent.com") (default: https://token.actions.githubusercontent.com) |
| `--custom-trusted-root` | `` | string | Path to a trusted_root.jsonl file; likely for offline verification |
| `--deny-self-hosted-runners` | `` | bool | Fail verification for attestations generated on self-hosted runners |
| `--digest-alg` | `-d` | string | The algorithm used to compute a digest of the artifact: {sha256|sha512} (default "sha256") (default: sha256) |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `` | string | Configure host to use |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--limit` | `-L` | string | Maximum number of attestations to fetch (default 30) (default: 30) |
| `--no-public-good` | `` | bool | Do not verify attestations signed with Sigstore public good instance |
| `--owner` | `-o` | string | GitHub organization to scope attestation lookup by |
| `--predicate-type` | `` | string | Enforce that verified attestations' predicate type matches the provided value (default "https://slsa.dev/provenance/v1") (default: https://slsa.dev/provenance/v1) |
| `--repo` | `-R` | string | Repository name in the format <owner>/<repo> |
| `--signer-digest` | `` | string | Enforce that the digest associated with the signer workflow matches the provided value |
| `--signer-repo` | `` | string | Enforce that the workflow that signed the attestation's repository matches the provided value (<owner>/<repo>) |
| `--signer-workflow` | `` | string | Enforce that the workflow that signed the attestation matches the provided value ([host/]<owner>/<repo>/<path>/<to>/<workflow>) |
| `--source-digest` | `` | string | Enforce that the digest associated with the source repository matches the provided value |
| `--source-ref` | `` | string | Enforce that the git ref associated with the source repository matches the provided value |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

### `gh auth`

Authenticate gh and git with GitHub

```
gh auth <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh auth login`

Authenticate with a GitHub host.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clipboard` | `-c` | bool | Copy one-time OAuth device code to clipboard |
| `--git-protocol` | `-p` | string | The protocol to use for git operations on this host: {ssh|https} |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The hostname of the GitHub instance to authenticate with |
| `--insecure-storage` | `` | bool | Save authentication credentials in plain text instead of credential store |
| `--scopes` | `-s` | string | Additional authentication scopes to request |
| `--skip-ssh-key` | `` | bool | Skip generate/upload SSH key prompt |
| `--web` | `-w` | bool | Open a browser to authenticate |
| `--with-token` | `` | bool | Read token from standard input |

#### `gh auth logout`

Remove authentication for a GitHub account.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The hostname of the GitHub instance to log out of |
| `--user` | `-u` | string | The account to log out of |

#### `gh auth refresh`

Expand or fix the permission scopes for stored credentials for active account.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clipboard` | `-c` | bool | Copy one-time OAuth device code to clipboard |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The GitHub host to use for authentication |
| `--insecure-storage` | `` | bool | Save authentication credentials in plain text instead of credential store |
| `--remove-scopes` | `-r` | string | Authentication scopes to remove from gh |
| `--reset-scopes` | `` | bool | Reset authentication scopes to the default minimum set of scopes |
| `--scopes` | `-s` | string | Additional authentication scopes for gh to have |

#### `gh auth setup-git`

This command configures `git` to use GitHub CLI as a credential helper.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | string | Force setup even if the host is not known. Must be used in conjunction with --hostname |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The hostname to configure git for |

#### `gh auth status`

Display active account and authentication state on each known GitHub host.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--active` | `-a` | bool | Display the active account only |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | Check only a specific hostname's auth status |
| `--jq` | `` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--show-token` | `-t` | bool | Display the auth token |
| `--template` | `` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh auth switch`

Switch the active account for a GitHub host.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The hostname of the GitHub instance to switch account for |
| `--user` | `-u` | string | The account to switch to |

#### `gh auth token`

This command outputs the authentication token for an account on a given GitHub host.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--hostname` | `-h` | string | The hostname of the GitHub instance authenticated with |
| `--user` | `-u` | string | The account to output the token for |

### `gh cache`

Work with GitHub Actions caches.

```
gh cache <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh cache delete`

Delete GitHub Actions caches.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Delete all caches, can be used with --ref to delete all caches for a specific ref |
| `--help` | `` | bool | Show help for command |
| `--ref` | `-r` | string | Delete by cache key and ref, formatted as refs/heads/<branch name> or refs/pull/<number>/merge |
| `--succeed-on-no-caches` | `` | string | Return exit code 0 if no caches found. Must be used in conjunction with --all |

#### `gh cache list`

List GitHub Actions caches

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--key` | `-k` | string | Filter by cache key prefix |
| `--limit` | `-L` | string | Maximum number of caches to fetch (default 30) (default: 30) |
| `--order` | `-O` | string | Order of caches returned: {asc|desc} (default "desc") (default: desc) |
| `--ref` | `-r` | string | Filter by ref, formatted as refs/heads/<branch name> or refs/pull/<number>/merge |
| `--sort` | `-S` | string | Sort fetched caches: {created_at|last_accessed_at|size_in_bytes} (default "last_accessed_at") (default: last_accessed_at) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

### `gh codespace`

Connect to and manage codespaces

```
gh codespace [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh codespace code`

Open a codespace in Visual Studio Code

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--help` | `` | bool | Show help for command |
| `--insiders` | `` | bool | Use the insiders version of Visual Studio Code |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--web` | `-w` | bool | Use the web version of Visual Studio Code |

#### `gh codespace cp`

The `cp` command copies files between the local and remote file systems.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--expand` | `-e` | string | Expand remote file names on remote shell |
| `--help` | `` | bool | Show help for command |
| `--profile` | `-p` | string | Name of the SSH profile to use |
| `--recursive` | `-r` | bool | Recursively copy directories |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |

#### `gh codespace create`

Create a codespace

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--branch` | `-b` | string | Repository branch |
| `--default-permissions` | `` | bool | Do not prompt to accept additional permissions requested by the codespace |
| `--devcontainer-path` | `` | string | Path to the devcontainer.json file to use when creating codespace |
| `--display-name` | `-d` | string | Display name for the codespace (48 characters or less) |
| `--help` | `` | bool | Show help for command |
| `--idle-timeout` | `` | string | Allowed inactivity before codespace is stopped, e.g. "10m", "1h" |
| `--location` | `-l` | string | Location: {EastUs|SouthEastAsia|WestEurope|WestUs2} (determined automatically if not provided) |
| `--machine` | `-m` | string | Hardware specifications for the VM |
| `--repo` | `-R` | string | Repository name with owner: user/repo |
| `--retention-period` | `` | string | Allowed time after shutting down before the codespace is automatically deleted (maximum 30 days), e.g. "1h", "72h" |
| `--status` | `-s` | string | Show status of post-create command and dotfiles |
| `--web` | `-w` | bool | Create codespace from browser, cannot be used with --display-name, --idle-timeout, or --retention-period |

#### `gh codespace delete`

Delete codespaces based on selection criteria.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Delete all codespaces |
| `--codespace` | `-c` | string | Name of the codespace |
| `--days` | `` | string | Delete codespaces older than N days |
| `--force` | `-f` | bool | Skip confirmation for codespaces that contain unsaved changes |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | The login handle of the organization (admin-only) |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--user` | `-u` | string | The username to delete codespaces for (used with --org) |

#### `gh codespace edit`

Edit a codespace

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--display-name` | `-d` | string | Set the display name |
| `--help` | `` | bool | Show help for command |
| `--machine` | `-m` | string | Set hardware specifications for the VM |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |

#### `gh codespace jupyter`

Open a codespace in JupyterLab

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--help` | `` | bool | Show help for command |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |

#### `gh codespace list`

List codespaces of the authenticated user.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of codespaces to list (default 30) (default: 30) |
| `--org` | `-o` | string | The login handle of the organization to list codespaces for (admin-only) |
| `--repo` | `-R` | string | Repository name with owner: user/repo |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--user` | `-u` | string | The username to list codespaces for (used with --org) |
| `--web` | `-w` | bool | List codespaces in the web browser, cannot be used with --user or --org |

#### `gh codespace logs`

Access codespace logs

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--follow` | `-f` | bool | Tail and follow the logs |
| `--help` | `` | bool | Show help for command |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |

#### `gh codespace ports`

List ports in a codespace

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

##### `gh codespace ports forward`

Forward ports

##### `gh codespace ports visibility`

Change the visibility of the forwarded port

#### `gh codespace rebuild`

Rebuilding recreates your codespace.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--full` | `` | bool | Perform a full rebuild |
| `--help` | `` | bool | Show help for command |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |

#### `gh codespace ssh`

The `ssh` command is used to SSH into a codespace. In its simplest form, you can

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--config` | `` | bool | Write OpenSSH configuration to stdout |
| `--debug` | `-d` | string | Log debug data to a file |
| `--debug-file` | `` | string | Path of the file log to |
| `--help` | `` | bool | Show help for command |
| `--profile` | `` | string | Name of the SSH profile to use |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--server-port` | `` | string | SSH server port number (0 => pick unused) |

#### `gh codespace stop`

Stop a running codespace

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | The login handle of the organization (admin-only) |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--user` | `-u` | string | The username to stop codespace for (used with --org) |

#### `gh codespace view`

View details about a codespace

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--codespace` | `-c` | string | Name of the codespace |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--repo` | `-R` | string | Filter codespace selection by repository name (user/repo) |
| `--repo-owner` | `` | string | Filter codespace selection by repository owner (username or org) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

### `gh config`

Display or change configuration settings for gh.

```
gh config <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh config clear-cache`

Clear the cli cache

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh config get`

Print the value of a given configuration key

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--host` | `-h` | string | Get per-host setting |

#### `gh config list`

Print a list of configuration keys and values

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--host` | `-h` | string | Get per-host configuration |

#### `gh config set`

Update configuration with a value for the given key

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--host` | `-h` | string | Set per-host setting |

### `gh extension`

GitHub CLI extensions are repositories that provide additional gh commands.

```
gh extension [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh extension browse`

This command will take over your terminal and run a fully interactive

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `` | bool | Log to /tmp/extBrowse-* |
| `--help` | `` | bool | Show help for command |
| `--single-column` | `-s` | bool | Render TUI with only one column of text |

#### `gh extension create`

Create a new extension

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--precompiled` | `` | string | Create a precompiled extension. Possible values: go, other |

#### `gh extension exec`

Execute an extension using the short name. For example, if the extension repository is

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh extension install`

Install a GitHub CLI extension from a GitHub or local repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `` | bool | Force upgrade extension, or ignore if latest already installed |
| `--help` | `` | bool | Show help for command |
| `--pin` | `` | string | Pin extension to a release tag or commit ref |

#### `gh extension list`

List installed extension commands

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh extension remove`

Remove an installed extension

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh extension search`

Search for gh extensions.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--license` | `` | string | Filter based on license type |
| `--limit` | `-L` | string | Maximum number of extensions to fetch (default 30) (default: 30) |
| `--order` | `` | string | Order of repositories returned, ignored unless '--sort' flag is specified: {asc|desc} (default "desc") (default: desc) |
| `--owner` | `` | string | Filter on owner |
| `--sort` | `` | string | Sort fetched repositories: {forks|help-wanted-issues|stars|updated} (default "best-match") (default: best-match) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open the search query in the web browser |

#### `gh extension upgrade`

Upgrade installed extensions

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Upgrade all extensions |
| `--dry-run` | `` | bool | Only display upgrades |
| `--force` | `` | bool | Force upgrade extension |
| `--help` | `` | bool | Show help for command |

### `gh gist`

Work with GitHub gists.

```
gh gist <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh gist clone`

Clone a GitHub gist locally.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh gist create`

Create a new GitHub gist with given contents.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--desc` | `-d` | string | A description for this gist |
| `--filename` | `-f` | string | Provide a filename to be used when reading from standard input |
| `--help` | `` | bool | Show help for command |
| `--public` | `-p` | bool | List the gist publicly (default "secret") (default: secret) |
| `--web` | `-w` | bool | Open the web browser with created gist |

#### `gh gist delete`

Delete a GitHub gist.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `` | bool | Confirm deletion without prompting |

#### `gh gist edit`

Edit one of your gists

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add` | `-a` | string | Add a new file to the gist |
| `--desc` | `-d` | string | New description for the gist |
| `--filename` | `-f` | string | Select a file to edit |
| `--help` | `` | bool | Show help for command |
| `--remove` | `-r` | string | Remove a file from the gist |

#### `gh gist list`

List gists from your user account.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `` | string | Filter gists using a regular expression |
| `--help` | `` | bool | Show help for command |
| `--include-content` | `` | string | Include gists' file content when filtering |
| `--limit` | `-L` | string | Maximum number of gists to fetch (default 10) (default: 10) |
| `--public` | `` | bool | Show only public gists |
| `--secret` | `` | bool | Show only secret gists |

#### `gh gist rename`

Rename a file in the given gist ID / URL.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh gist view`

View the given gist or select from recent gists.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filename` | `-f` | string | Display a single file from the gist |
| `--files` | `` | string | List file names from the gist |
| `--help` | `` | bool | Show help for command |
| `--raw` | `-r` | bool | Print raw instead of rendered gist contents |
| `--web` | `-w` | bool | Open gist in the browser |

### `gh gpg-key`

Manage GPG keys registered with your GitHub account.

```
gh gpg-key <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh gpg-key add`

Add a GPG key to your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--title` | `-t` | string | Title for the new key |

#### `gh gpg-key delete`

Delete a GPG key from your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh gpg-key list`

Lists GPG keys in your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

### `gh issue`

Work with GitHub issues.

```
gh issue <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh issue close`

Close issue

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comment` | `-c` | string | Leave a closing comment |
| `--help` | `` | bool | Show help for command |
| `--reason` | `-r` | string | Reason for closing: {completed|not planned} |

#### `gh issue comment`

Add a comment to a GitHub issue.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `-b` | string | The comment body text |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--create-if-none` | `` | bool | Create a new comment if no comments are found. Can be used only with --edit-last |
| `--delete-last` | `` | bool | Delete the last comment of the current user |
| `--edit-last` | `` | bool | Edit the last comment of the current user |
| `--editor` | `-e` | bool | Skip prompts and open the text editor to write the body in |
| `--help` | `` | bool | Show help for command |
| `--web` | `-w` | bool | Open the web browser to write the comment |
| `--yes` | `` | bool | Skip the delete confirmation prompt when --delete-last is provided |

#### `gh issue create`

Create an issue on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--assignee` | `-a` | string | Assign people by their login. Use "@me" to self-assign. |
| `--body` | `-b` | string | Supply a body. Will prompt for one otherwise. |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--editor` | `-e` | bool | Skip prompts and open the text editor to write the title and body in. The first line is the title and the remaining text is the body. |
| `--help` | `` | bool | Show help for command |
| `--label` | `-l` | string | Add labels by name |
| `--milestone` | `-m` | string | Add the issue to a milestone by name |
| `--project` | `-p` | string | Add the issue to projects by title |
| `--recover` | `` | string | Recover input from a failed run of create |
| `--template` | `-T` | string | Template name to use as starting body text |
| `--title` | `-t` | string | Supply a title. Will prompt for one otherwise. |
| `--web` | `-w` | bool | Open the browser to create an issue |

#### `gh issue delete`

Delete issue

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `` | bool | Confirm deletion without prompting |

#### `gh issue develop`

Manage linked branches for an issue.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--base` | `-b` | string | Name of the remote branch you want to make your new branch from |
| `--branch-repo` | `` | string | Name or URL of the repository where you want to create your new branch |
| `--checkout` | `-c` | bool | Checkout the branch after creating it |
| `--help` | `` | bool | Show help for command |
| `--list` | `-l` | bool | List linked branches for the issue |
| `--name` | `-n` | string | Name of the branch to create |

#### `gh issue edit`

Edit one or more issues within the same repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-assignee` | `` | string | Add assigned users by their login. Use "@me" to assign yourself, or "@copilot" to assign Copilot. |
| `--add-label` | `` | string | Add labels by name |
| `--add-project` | `` | string | Add the issue to projects by title |
| `--body` | `-b` | string | Set the new body. |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--help` | `` | bool | Show help for command |
| `--milestone` | `-m` | string | Edit the milestone the issue belongs to by name |
| `--remove-assignee` | `` | string | Remove assigned users by their login. Use "@me" to unassign yourself, or "@copilot" to unassign Copilot. |
| `--remove-label` | `` | string | Remove labels by name |
| `--remove-milestone` | `` | bool | Remove the milestone association from the issue |
| `--remove-project` | `` | string | Remove the issue from projects by title |
| `--title` | `-t` | string | Set the new title. |

#### `gh issue list`

List issues in a GitHub repository. By default, this only lists open issues.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | string | Filter by GitHub App author |
| `--assignee` | `-a` | string | Filter by assignee |
| `--author` | `-A` | string | Filter by author |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--label` | `-l` | string | Filter by label |
| `--limit` | `-L` | string | Maximum number of issues to fetch (default 30) (default: 30) |
| `--mention` | `` | string | Filter by mention |
| `--milestone` | `-m` | string | Filter by milestone number or title |
| `--search` | `-S` | string | Search issues with query |
| `--state` | `-s` | string | Filter by state: {open|closed|all} (default "open") (default: open) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | List issues in the web browser |

#### `gh issue lock`

Lock issue conversation

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--reason` | `-r` | string | Optional reason for locking conversation (off_topic, resolved, spam, too_heated). |

#### `gh issue pin`

Pin an issue to a repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh issue reopen`

Reopen issue

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comment` | `-c` | string | Add a reopening comment |
| `--help` | `` | bool | Show help for command |

#### `gh issue status`

Show status of relevant issues

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh issue transfer`

Transfer issue to another repository

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh issue unlock`

Unlock issue conversation

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh issue unpin`

Unpin an issue from a repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh issue view`

Display the title, body, and other information about an issue.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comments` | `-c` | bool | View issue comments |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open an issue in the browser |

### `gh label`

Work with GitHub labels.

```
gh label <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh label clone`

Clones labels from a source repository to a destination repository on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Overwrite labels in the destination repository |
| `--help` | `` | bool | Show help for command |

#### `gh label create`

Create a new label on GitHub, or update an existing one with `--force`.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--color` | `-c` | string | Color of the label |
| `--description` | `-d` | string | Description of the label |
| `--force` | `-f` | bool | Update the label color and description if label already exists |
| `--help` | `` | bool | Show help for command |

#### `gh label delete`

Delete a label from a repository

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `` | bool | Confirm deletion without prompting |

#### `gh label edit`

Update a label on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--color` | `-c` | string | Color of the label |
| `--description` | `-d` | string | Description of the label |
| `--help` | `` | bool | Show help for command |
| `--name` | `-n` | string | New name of the label |

#### `gh label list`

Display labels in a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of labels to fetch (default 30) (default: 30) |
| `--order` | `` | string | Order of labels returned: {asc|desc} (default "asc") (default: asc) |
| `--search` | `-S` | string | Search label names and descriptions |
| `--sort` | `` | string | Sort fetched labels: {created|name} (default "created") (default: created) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | List labels in the web browser |

### `gh org`

Work with GitHub organizations.

```
gh org <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh org list`

List organizations for the authenticated user.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--limit` | `-L` | string | Maximum number of organizations to list (default 30) (default: 30) |

### `gh pr`

Work with GitHub pull requests.

```
gh pr <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh pr checkout`

Check out a pull request in git

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--branch` | `-b` | string | Local branch name to use (default [the name of the head branch]) |
| `--detach` | `` | bool | Checkout PR with a detached HEAD |
| `--force` | `-f` | bool | Reset the existing local branch to the latest state of the pull request |
| `--help` | `` | bool | Show help for command |
| `--recurse-submodules` | `` | bool | Update all submodules after checkout |

#### `gh pr checks`

Show CI status for a single pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--fail-fast` | `` | bool | Exit watch mode on first check failure |
| `--help` | `` | bool | Show help for command |
| `--interval` | `-i` | string | Refresh interval in seconds in watch mode (default 10) (default: 10) |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--required` | `` | bool | Only show checks that are required |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--watch` | `` | bool | Watch checks until they finish |
| `--web` | `-w` | bool | Open the web browser to show details about checks |

#### `gh pr close`

Close a pull request

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comment` | `-c` | string | Leave a closing comment |
| `--delete-branch` | `-d` | bool | Delete the local and remote branch after close |
| `--help` | `` | bool | Show help for command |

#### `gh pr comment`

Add a comment to a GitHub pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `-b` | string | The comment body text |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--create-if-none` | `` | bool | Create a new comment if no comments are found. Can be used only with --edit-last |
| `--delete-last` | `` | bool | Delete the last comment of the current user |
| `--edit-last` | `` | bool | Edit the last comment of the current user |
| `--editor` | `-e` | bool | Skip prompts and open the text editor to write the body in |
| `--help` | `` | bool | Show help for command |
| `--web` | `-w` | bool | Open the web browser to write the comment |
| `--yes` | `` | bool | Skip the delete confirmation prompt when --delete-last is provided |

#### `gh pr create`

Create a pull request on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--assignee` | `-a` | string | Assign people by their login. Use "@me" to self-assign. |
| `--base` | `-B` | string | The branch into which you want your code merged |
| `--body` | `-b` | string | Body for the pull request |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--draft` | `-d` | bool | Mark pull request as a draft |
| `--dry-run` | `` | bool | Print details instead of creating the PR. May still push git changes. |
| `--editor` | `-e` | bool | Skip prompts and open the text editor to write the title and body in. The first line is the title and the remaining text is the body. |
| `--fill` | `-f` | bool | Use commit info for title and body |
| `--fill-first` | `` | bool | Use first commit info for title and body |
| `--fill-verbose` | `` | bool | Use commits msg+body for description |
| `--head` | `-H` | string | The branch that contains commits for your pull request (default [current branch]) |
| `--help` | `` | bool | Show help for command |
| `--label` | `-l` | string | Add labels by name |
| `--milestone` | `-m` | string | Add the pull request to a milestone by name |
| `--no-maintainer-edit` | `` | bool | Disable maintainer's ability to modify pull request |
| `--project` | `-p` | string | Add the pull request to projects by title |
| `--recover` | `` | string | Recover input from a failed run of create |
| `--reviewer` | `-r` | string | Request reviews from people or teams by their handle |
| `--template` | `-T` | string | Template file to use as starting body text |
| `--title` | `-t` | string | Title for the pull request |
| `--web` | `-w` | bool | Open the web browser to create a pull request |

#### `gh pr diff`

View changes in a pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--color` | `` | string | Use color in diff output: {always|never|auto} (default "auto") (default: auto) |
| `--help` | `` | bool | Show help for command |
| `--name-only` | `` | string | Display only names of changed files |
| `--patch` | `` | bool | Display diff in patch format |
| `--web` | `-w` | bool | Open the pull request diff in the browser |

#### `gh pr edit`

Edit a pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-assignee` | `` | string | Add assigned users by their login. Use "@me" to assign yourself, or "@copilot" to assign Copilot. |
| `--add-label` | `` | string | Add labels by name |
| `--add-project` | `` | string | Add the pull request to projects by title |
| `--add-reviewer` | `` | string | Add reviewers by their login. |
| `--base` | `-B` | string | Change the base branch for this pull request |
| `--body` | `-b` | string | Set the new body. |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--help` | `` | bool | Show help for command |
| `--milestone` | `-m` | string | Edit the milestone the pull request belongs to by name |
| `--remove-assignee` | `` | string | Remove assigned users by their login. Use "@me" to unassign yourself, or "@copilot" to unassign Copilot. |
| `--remove-label` | `` | string | Remove labels by name |
| `--remove-milestone` | `` | bool | Remove the milestone association from the pull request |
| `--remove-project` | `` | string | Remove the pull request from projects by title |
| `--remove-reviewer` | `` | string | Remove reviewers by their login. |
| `--title` | `-t` | string | Set the new title. |

#### `gh pr list`

List pull requests in a GitHub repository. By default, this only lists open PRs.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | string | Filter by GitHub App author |
| `--assignee` | `-a` | string | Filter by assignee |
| `--author` | `-A` | string | Filter by author |
| `--base` | `-B` | string | Filter by base branch |
| `--draft` | `-d` | bool | Filter by draft state |
| `--head` | `-H` | string | Filter by head branch ("<owner>:<branch>" syntax not supported) |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--label` | `-l` | string | Filter by label |
| `--limit` | `-L` | string | Maximum number of items to fetch (default 30) (default: 30) |
| `--search` | `-S` | string | Search pull requests with query |
| `--state` | `-s` | string | Filter by state: {open|closed|merged|all} (default "open") (default: open) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | List pull requests in the web browser |

#### `gh pr lock`

Lock pull request conversation

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--reason` | `-r` | string | Optional reason for locking conversation (off_topic, resolved, spam, too_heated). |

#### `gh pr merge`

Merge a pull request on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--admin` | `` | bool | Use administrator privileges to merge a pull request that does not meet requirements |
| `--author-email` | `-A` | string | Email text for merge commit author |
| `--auto` | `` | bool | Automatically merge only after necessary requirements are met |
| `--body` | `-b` | string | Body text for the merge commit |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--delete-branch` | `-d` | bool | Delete the local and remote branch after merge |
| `--disable-auto` | `` | bool | Disable auto-merge for this pull request |
| `--help` | `` | bool | Show help for command |
| `--match-head-commit` | `` | string | Commit SHA that the pull request head must match to allow merge |
| `--merge` | `-m` | bool | Merge the commits with the base branch |
| `--rebase` | `-r` | bool | Rebase the commits onto the base branch |
| `--squash` | `-s` | bool | Squash the commits into one commit and merge it into the base branch |
| `--subject` | `-t` | string | Subject text for the merge commit |

#### `gh pr ready`

Mark a pull request as ready for review.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--undo` | `` | bool | Convert a pull request to "draft" |

#### `gh pr reopen`

Reopen a pull request

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comment` | `-c` | string | Add a reopening comment |
| `--help` | `` | bool | Show help for command |

#### `gh pr revert`

Revert a pull request

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `-b` | string | Body for the revert pull request |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--draft` | `-d` | bool | Mark revert pull request as a draft |
| `--help` | `` | bool | Show help for command |
| `--title` | `-t` | string | Title for the revert pull request |

#### `gh pr review`

Add a review to a pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--approve` | `-a` | bool | Approve pull request |
| `--body` | `-b` | string | Specify the body of a review |
| `--body-file` | `-F` | string | Read body text from file (use "-" to read from standard input) |
| `--comment` | `-c` | bool | Comment on a pull request |
| `--help` | `` | bool | Show help for command |
| `--request-changes` | `-r` | bool | Request changes on a pull request |

#### `gh pr status`

Show status of relevant pull requests.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--conflict-status` | `-c` | bool | Display the merge conflict status of each pull request |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh pr unlock`

Unlock pull request conversation

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh pr update-branch`

Update a pull request branch with latest changes of the base branch.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--rebase` | `` | bool | Update PR branch by rebasing on top of latest base branch |

#### `gh pr view`

Display the title, body, and other information about a pull request.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--comments` | `-c` | bool | View pull request comments |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open a pull request in the browser |

### `gh preview`

Preview commands are for testing, demonstrative, and development purposes only.

```
gh preview <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh preview prompter`

Execute a test program to preview the prompter.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

### `gh project`

Work with GitHub Projects.

```
gh project <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh project close`

Close a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--undo` | `` | bool | Reopen a closed project |

#### `gh project copy`

Copy a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--drafts` | `` | bool | Include draft issues when copying |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--source-owner` | `` | string | Login of the source owner. Use "@me" for the current user. |
| `--target-owner` | `` | string | Login of the target owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--title` | `` | string | Title for the new project |

#### `gh project create`

Create a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--title` | `` | string | Title for the project |

#### `gh project delete`

Delete a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project edit`

Edit a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--description` | `-d` | string | New description of the project |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--readme` | `` | string | New readme for the project |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--title` | `` | string | New title for the project |
| `--visibility` | `` | string | Change project visibility: {PUBLIC|PRIVATE} |

#### `gh project field-create`

Create a field in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--data-type` | `` | string | DataType of the new field.: {TEXT|SINGLE_SELECT|DATE|NUMBER} |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--name` | `` | string | Name of the new field |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--single-select-options` | `` | string | Options for SINGLE_SELECT data type |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project field-delete`

Delete a field in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--id` | `` | string | ID of the field to delete |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project field-list`

List the fields in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--limit` | `-L` | string | Maximum number of fields to fetch (default 30) (default: 30) |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project item-add`

Add a pull request or an issue to a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--url` | `` | string | URL of the issue or pull request to add to the project |

#### `gh project item-archive`

Archive an item in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--id` | `` | string | ID of the item to archive |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--undo` | `` | bool | Unarchive an item |

#### `gh project item-create`

Create a draft issue item in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `` | string | Body for the draft issue |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--title` | `` | string | Title for the draft issue |

#### `gh project item-delete`

Delete an item from a project by ID

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--id` | `` | string | ID of the item to delete |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project item-edit`

Edit either a draft issue or a project item. Both usages require the ID of the item to edit.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `` | string | Body of the draft issue item |
| `--clear` | `` | string | Remove field value |
| `--date` | `` | string | Date value for the field (YYYY-MM-DD) |
| `--field-id` | `` | string | ID of the field to update |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--id` | `` | string | ID of the item to edit |
| `--iteration-id` | `` | string | ID of the iteration value to set on the field |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--number` | `` | string | Number value for the field |
| `--project-id` | `` | string | ID of the project to which the field belongs to |
| `--single-select-option-id` | `` | string | ID of the single select option value to set on the field |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--text` | `` | string | Text value for the field |
| `--title` | `` | string | Title of the draft issue item |

#### `gh project item-list`

List the items in a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--limit` | `-L` | string | Maximum number of items to fetch (default 30) (default: 30) |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh project link`

Link a project to a repository or a team

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--repo` | `-R` | string | The repository to be linked to this project |
| `--team` | `-T` | string | The team to be linked to this project |

#### `gh project list`

List the projects for an owner

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--closed` | `` | bool | Include closed projects |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--limit` | `-L` | string | Maximum number of projects to fetch (default 30) (default: 30) |
| `--owner` | `` | string | Login of the owner |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open projects list in the browser |

#### `gh project mark-template`

Mark a project as a template

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the org owner. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--undo` | `` | bool | Unmark the project as a template. |

#### `gh project unlink`

Unlink a project from a repository or a team

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--repo` | `-R` | string | The repository to be unlinked from this project |
| `--team` | `-T` | string | The team to be unlinked from this project |

#### `gh project view`

View a project

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--owner` | `` | string | Login of the owner. Use "@me" for the current user. |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open a project in the browser |

### `gh release`

Manage releases

```
gh release <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh release create`

tag required when not running interactively

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--discussion-category` | `` | string | Start a discussion in the specified category |
| `--draft` | `-d` | bool | Save the release as a draft instead of publishing it |
| `--fail-on-no-commits` | `` | bool | Fail if there are no commits since the last release (no impact on the first release) |
| `--generate-notes` | `` | bool | Automatically generate title and notes for the release via GitHub Release Notes API |
| `--latest` | `` | bool | Mark this release as "Latest" (default [automatic based on date and version]). --latest=false to explicitly NOT set as latest |
| `--notes` | `-n` | string | Release notes |
| `--notes-file` | `-F` | string | Read release notes from file (use "-" to read from standard input) |
| `--notes-from-tag` | `` | bool | Fetch notes from the tag annotation or message of commit associated with tag |
| `--notes-start-tag` | `` | string | Tag to use as the starting point for generating release notes |
| `--prerelease` | `-p` | bool | Mark the release as a prerelease |
| `--target` | `` | string | Target branch or full commit SHA (default [main branch]) |
| `--title` | `-t` | string | Release title |
| `--verify-tag` | `` | bool | Abort in case the git tag doesn't already exist in the remote repository |

#### `gh release delete`

Delete a release

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cleanup-tag` | `` | bool | Delete the specified tag in addition to its release |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh release delete-asset`

Delete an asset from a release

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh release download`

Download assets from a GitHub release.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--archive` | `-A` | string | Download the source code archive in the specified format (zip or tar.gz) |
| `--clobber` | `` | string | Overwrite existing files of the same name |
| `--dir` | `-D` | string | The directory to download files into (default ".") (default: .) |
| `--help` | `` | bool | Show help for command |
| `--output` | `-O` | string | The file to write a single asset to (use "-" to write to standard output) |
| `--pattern` | `-p` | string | Download only assets that match a glob pattern |
| `--skip-existing` | `` | string | Skip downloading when files of the same name exist |

#### `gh release edit`

Edit a release

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--discussion-category` | `` | string | Start a discussion in the specified category when publishing a draft |
| `--draft` | `` | bool | Save the release as a draft instead of publishing it |
| `--help` | `` | bool | Show help for command |
| `--latest` | `` | bool | Explicitly mark the release as "Latest" |
| `--notes` | `-n` | string | Release notes |
| `--notes-file` | `-F` | string | Read release notes from file (use "-" to read from standard input) |
| `--prerelease` | `` | bool | Mark the release as a prerelease |
| `--tag` | `` | string | The name of the tag |
| `--target` | `` | string | Target branch or full commit SHA (default [main branch]) |
| `--title` | `-t` | string | Release title |
| `--verify-tag` | `` | bool | Abort in case the git tag doesn't already exist in the remote repository |

#### `gh release list`

List releases in a repository

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--exclude-drafts` | `` | bool | Exclude draft releases |
| `--exclude-pre-releases` | `` | bool | Exclude pre-releases |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of items to fetch (default 30) (default: 30) |
| `--order` | `-O` | string | Order of releases returned: {asc|desc} (default "desc") (default: desc) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh release upload`

Upload asset files to a GitHub Release.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clobber` | `` | bool | Overwrite existing assets of the same name |
| `--help` | `` | bool | Show help for command |

#### `gh release verify`

Verify that a GitHub Release is accompanied by a valid cryptographically signed attestation.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh release verify-asset`

Verify that a given asset file originated from a specific GitHub Release using cryptographically signed attestations.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format: {json} |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh release view`

View information about a GitHub Release.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open the release in the browser |

### `gh repo`

Work with GitHub repositories.

```
gh repo <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh repo archive`

Archive a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh repo autolink`

Autolinks link issues, pull requests, commit messages, and release descriptions to external third-party services.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

##### `gh repo autolink create`

Create a new autolink reference for a repository.

##### `gh repo autolink delete`

Delete an autolink reference for a repository.

##### `gh repo autolink list`

Gets all autolink references that are configured for a repository.

##### `gh repo autolink view`

View an autolink reference for a repository.

#### `gh repo clone`

Clone a GitHub repository locally. Pass additional `git clone` flags by listing

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--upstream-remote-name` | `-u` | string | Upstream remote name when cloning a fork (default "upstream") (default: upstream) |

#### `gh repo create`

Create a new GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-readme` | `` | string | Add a README file to the new repository |
| `--clone` | `-c` | string | Clone the new repository to the current directory |
| `--description` | `-d` | string | Description of the repository |
| `--disable-issues` | `` | bool | Disable issues in the new repository |
| `--disable-wiki` | `` | bool | Disable wiki in the new repository |
| `--gitignore` | `-g` | string | Specify a gitignore template for the repository |
| `--help` | `` | bool | Show help for command |
| `--homepage` | `-h` | string | Repository home page URL |
| `--include-all-branches` | `` | bool | Include all branches from template repository |
| `--internal` | `` | bool | Make the new repository internal |
| `--license` | `-l` | string | Specify an Open Source License for the repository |
| `--private` | `` | bool | Make the new repository private |
| `--public` | `` | bool | Make the new repository public |
| `--push` | `` | bool | Push local commits to the new repository |
| `--remote` | `-r` | string | Specify remote name for the new repository |
| `--source` | `-s` | string | Specify path to local repository to use as source |
| `--team` | `-t` | string | The name of the organization team to be granted access |
| `--template` | `-p` | string | Make the new repository based on a template repository |

#### `gh repo delete`

Delete a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `` | bool | Confirm deletion without prompting |

#### `gh repo deploy-key`

Manage deploy keys in a repository

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

##### `gh repo deploy-key add`

Add a deploy key to a GitHub repository.

##### `gh repo deploy-key delete`

Delete a deploy key from a GitHub repository

##### `gh repo deploy-key list`

List deploy keys in a GitHub repository

#### `gh repo edit`

Edit repository settings.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--accept-visibility-change-consequences` | `` | bool | Accept the consequences of changing the repository visibility |
| `--add-topic` | `` | string | Add repository topic |
| `--allow-forking` | `` | bool | Allow forking of an organization repository |
| `--allow-update-branch` | `` | bool | Allow a pull request head branch that is behind its base branch to be updated |
| `--default-branch` | `` | string | Set the default branch name for the repository |
| `--delete-branch-on-merge` | `` | bool | Delete head branch when pull requests are merged |
| `--description` | `-d` | string | Description of the repository |
| `--enable-advanced-security` | `` | bool | Enable advanced security in the repository |
| `--enable-auto-merge` | `` | bool | Enable auto-merge functionality |
| `--enable-discussions` | `` | bool | Enable discussions in the repository |
| `--enable-issues` | `` | bool | Enable issues in the repository |
| `--enable-merge-commit` | `` | bool | Enable merging pull requests via merge commit |
| `--enable-projects` | `` | bool | Enable projects in the repository |
| `--enable-rebase-merge` | `` | bool | Enable merging pull requests via rebase |
| `--enable-secret-scanning` | `` | bool | Enable secret scanning in the repository |
| `--enable-secret-scanning-push-protection` | `` | bool | Enable secret scanning push protection in the repository. Secret scanning must be enabled first |
| `--enable-squash-merge` | `` | bool | Enable merging pull requests via squashed commit |
| `--enable-wiki` | `` | bool | Enable wiki in the repository |
| `--help` | `` | bool | Show help for command |
| `--homepage` | `-h` | string | Repository home page URL |
| `--remove-topic` | `` | string | Remove repository topic |
| `--template` | `` | bool | Make the repository available as a template repository |
| `--visibility` | `` | string | Change the visibility of the repository to {public,private,internal} |

#### `gh repo fork`

Create a fork of a repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--clone` | `` | bool | Clone the fork |
| `--default-branch-only` | `` | bool | Only include the default branch in the fork |
| `--fork-name` | `` | string | Rename the forked repository |
| `--help` | `` | bool | Show help for command |
| `--org` | `` | string | Create the fork in an organization |
| `--remote` | `` | bool | Add a git remote for the fork |
| `--remote-name` | `` | string | Specify the name for the new remote (default "origin") (default: origin) |

#### `gh repo gitignore`

List and view available repository gitignore templates

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

##### `gh repo gitignore list`

List available repository gitignore templates

##### `gh repo gitignore view`

View an available repository `.gitignore` template.

#### `gh repo license`

Explore repository licenses

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

##### `gh repo license list`

List common repository licenses.

##### `gh repo license view`

View a specific repository license by license key or SPDX ID.

#### `gh repo list`

List repositories owned by a user or organization.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--archived` | `` | bool | Show only archived repositories |
| `--fork` | `` | bool | Show only forks |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--language` | `-l` | string | Filter by primary coding language |
| `--limit` | `-L` | string | Maximum number of repositories to list (default 30) (default: 30) |
| `--no-archived` | `` | bool | Omit archived repositories |
| `--source` | `` | bool | Show only non-forks |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--topic` | `` | string | Filter by topic |
| `--visibility` | `` | string | Filter by repository visibility: {public|private|internal} |

#### `gh repo rename`

Rename a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh repo set-default`

This command sets the default remote repository to use when querying the

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--unset` | `-u` | bool | Unset the current default repository |
| `--view` | `-v` | bool | View the current default repository |

#### `gh repo sync`

Sync destination repository from source repository. Syncing uses the default branch

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--branch` | `-b` | string | Branch to sync (default [default branch]) |
| `--force` | `` | bool | Hard reset the branch of the destination repository to match the source repository |
| `--help` | `` | bool | Show help for command |
| `--source` | `-s` | string | Source repository |

#### `gh repo unarchive`

Unarchive a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh repo view`

Display the description and the README of a GitHub repository.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--branch` | `-b` | string | View a specific branch of the repository |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open a repository in the browser |

### `gh ruleset`

Repository rulesets are a way to define a set of rules that apply to a repository.

```
gh ruleset <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh ruleset check`

View information about GitHub rules that apply to a given branch.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--default` | `` | bool | Check rules on default branch |
| `--help` | `` | bool | Show help for command |
| `--web` | `-w` | bool | Open the branch rules page in a web browser |

#### `gh ruleset list`

List GitHub rulesets for a repository or organization.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--limit` | `-L` | string | Maximum number of rulesets to list (default 30) (default: 30) |
| `--org` | `-o` | string | List organization-wide rulesets for the provided organization |
| `--parents` | `-p` | bool | Whether to include rulesets configured at higher levels that also apply (default true) (default: true) |
| `--web` | `-w` | bool | Open the list of rulesets in the web browser |

#### `gh ruleset view`

View information about a GitHub ruleset.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | Organization name if the provided ID is an organization-level ruleset |
| `--parents` | `-p` | bool | Whether to include rulesets configured at higher levels that also apply (default true) (default: true) |
| `--web` | `-w` | bool | Open the ruleset in the browser |

### `gh run`

List, view, and watch recent workflow runs from GitHub Actions.

```
gh run <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh run cancel`

Cancel a workflow run

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `` | bool | Force cancel a workflow run |
| `--help` | `` | bool | Show help for command |

#### `gh run delete`

Delete a workflow run

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh run download`

Download artifacts generated by a GitHub Actions workflow run.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dir` | `-D` | string | The directory to download artifacts into (default ".") (default: .) |
| `--help` | `` | bool | Show help for command |
| `--name` | `-n` | string | Download artifacts that match any of the given names |
| `--pattern` | `-p` | string | Download artifacts that match a glob pattern |

#### `gh run list`

List recent workflow runs.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Include disabled workflows |
| `--branch` | `-b` | string | Filter runs by branch |
| `--commit` | `-c` | string | Filter runs by the SHA of the commit |
| `--created` | `` | string | Filter runs by the date it was created |
| `--event` | `-e` | string | Filter runs by which event triggered the run |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of runs to fetch (default 20) (default: 20) |
| `--status` | `-s` | string | Filter runs by status: {queued|completed|in_progress|requested|waiting|pending|action_required|cancelled|failure|neutral|skipped|stale|startup_failure|success|timed_out} |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--user` | `-u` | string | Filter runs by user who triggered the run |
| `--workflow` | `-w` | string | Filter runs by workflow |

#### `gh run rerun`

Rerun an entire run, only failed jobs, or a specific job from a run.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `-d` | bool | Rerun with debug logging |
| `--failed` | `` | bool | Rerun only failed jobs, including dependencies |
| `--help` | `` | bool | Show help for command |
| `--job` | `-j` | string | Rerun a specific job ID from a run, including dependencies |

#### `gh run view`

View a summary of a workflow run.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--attempt` | `-a` | string | The attempt number of the workflow run |
| `--exit-status` | `` | bool | Exit with non-zero status if run failed |
| `--help` | `` | bool | Show help for command |
| `--job` | `-j` | string | View a specific job ID from a run |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--log` | `` | bool | View full log for either a run or specific job |
| `--log-failed` | `` | bool | View the log for any failed steps in a run or specific job |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--verbose` | `-v` | bool | Show job steps |
| `--web` | `-w` | bool | Open run in the browser |

#### `gh run watch`

Watch a run until it completes, showing its progress.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--compact` | `` | bool | Show only relevant/failed steps |
| `--exit-status` | `` | bool | Exit with non-zero status if run fails |
| `--help` | `` | bool | Show help for command |
| `--interval` | `-i` | string | Refresh interval in seconds (default 3) (default: 3) |

### `gh search`

Search across all of GitHub.

```
gh search <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh search code`

Search within code in GitHub repositories.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--extension` | `` | string | Filter on file extension |
| `--filename` | `` | string | Filter on filename |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--language` | `` | string | Filter results by language |
| `--limit` | `-L` | string | Maximum number of code results to fetch (default 30) (default: 30) |
| `--match` | `` | string | Restrict search to file contents or file path: {file|path} |
| `--owner` | `` | string | Filter on owner |
| `--repo` | `-R` | string | Filter on repository |
| `--size` | `` | string | Filter on size range, in kilobytes |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--web` | `-w` | bool | Open the search query in the web browser |

#### `gh search commits`

Search for commits on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--author` | `` | string | Filter by author |
| `--author-date` | `` | string | Filter based on authored date |
| `--author-email` | `` | string | Filter on author email |
| `--author-name` | `` | string | Filter on author name |
| `--committer` | `` | string | Filter by committer |
| `--committer-date` | `` | string | Filter based on committed date |
| `--committer-email` | `` | string | Filter on committer email |
| `--committer-name` | `` | string | Filter on committer name |
| `--hash` | `` | string | Filter by commit hash |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of commits to fetch (default 30) (default: 30) |
| `--merge` | `` | bool | Filter on merge commits |
| `--order` | `` | string | Order of commits returned, ignored unless '--sort' flag is specified: {asc|desc} (default "desc") (default: desc) |
| `--owner` | `` | string | Filter on repository owner |
| `--parent` | `` | string | Filter by parent hash |
| `--repo` | `-R` | string | Filter on repository |
| `--sort` | `` | string | Sort fetched commits: {author-date|committer-date} (default "best-match") (default: best-match) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--tree` | `` | string | Filter by tree hash |
| `--visibility` | `` | string | Filter based on repository visibility: {public|private|internal} |
| `--web` | `-w` | bool | Open the search query in the web browser |

#### `gh search issues`

Search for issues on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | string | Filter by GitHub App author |
| `--archived` | `` | bool | Filter based on the repository archived state {true|false} |
| `--assignee` | `` | string | Filter by assignee |
| `--author` | `` | string | Filter by author |
| `--closed` | `` | string | Filter on closed at date |
| `--commenter` | `` | string | Filter based on comments by user |
| `--comments` | `` | string | Filter on number of comments |
| `--created` | `` | string | Filter based on created at date |
| `--help` | `` | bool | Show help for command |
| `--include-prs` | `` | bool | Include pull requests in results |
| `--interactions` | `` | string | Filter on number of reactions and comments |
| `--involves` | `` | string | Filter based on involvement of user |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--label` | `` | string | Filter on label |
| `--language` | `` | string | Filter based on the coding language |
| `--limit` | `-L` | string | Maximum number of results to fetch (default 30) (default: 30) |
| `--locked` | `` | bool | Filter on locked conversation status |
| `--match` | `` | string | Restrict search to specific field of issue: {title|body|comments} |
| `--mentions` | `` | string | Filter based on user mentions |
| `--milestone` | `` | string | Filter by milestone title |
| `--no-assignee` | `` | bool | Filter on missing assignee |
| `--no-label` | `` | bool | Filter on missing label |
| `--no-milestone` | `` | bool | Filter on missing milestone |
| `--no-project` | `` | bool | Filter on missing project |
| `--order` | `` | string | Order of results returned, ignored unless '--sort' flag is specified: {asc|desc} (default "desc") (default: desc) |
| `--owner` | `` | string | Filter on repository owner |
| `--project` | `` | string | Filter on project board owner/number |
| `--reactions` | `` | string | Filter on number of reactions |
| `--repo` | `-R` | string | Filter on repository |
| `--sort` | `` | string | Sort fetched results: {comments|created|interactions|reactions|reactions-+1|reactions--1|reactions-heart|reactions-smile|reactions-tada|reactions-thinking_face|updated} (default "best-match") (default: best-match) |
| `--state` | `` | string | Filter based on state: {open|closed} |
| `--team-mentions` | `` | string | Filter based on team mentions |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--updated` | `` | string | Filter on last updated at date |
| `--visibility` | `` | string | Filter based on repository visibility: {public|private|internal} |
| `--web` | `-w` | bool | Open the search query in the web browser |

#### `gh search prs`

Search for pull requests on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | string | Filter by GitHub App author |
| `--archived` | `` | bool | Filter based on the repository archived state {true|false} |
| `--assignee` | `` | string | Filter by assignee |
| `--author` | `` | string | Filter by author |
| `--base` | `-B` | string | Filter on base branch name |
| `--checks` | `` | string | Filter based on status of the checks: {pending|success|failure} |
| `--closed` | `` | string | Filter on closed at date |
| `--commenter` | `` | string | Filter based on comments by user |
| `--comments` | `` | string | Filter on number of comments |
| `--created` | `` | string | Filter based on created at date |
| `--draft` | `` | bool | Filter based on draft state |
| `--head` | `-H` | string | Filter on head branch name |
| `--help` | `` | bool | Show help for command |
| `--interactions` | `` | string | Filter on number of reactions and comments |
| `--involves` | `` | string | Filter based on involvement of user |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--label` | `` | string | Filter on label |
| `--language` | `` | string | Filter based on the coding language |
| `--limit` | `-L` | string | Maximum number of results to fetch (default 30) (default: 30) |
| `--locked` | `` | bool | Filter on locked conversation status |
| `--match` | `` | string | Restrict search to specific field of issue: {title|body|comments} |
| `--mentions` | `` | string | Filter based on user mentions |
| `--merged` | `` | bool | Filter based on merged state |
| `--merged-at` | `` | string | Filter on merged at date |
| `--milestone` | `` | string | Filter by milestone title |
| `--no-assignee` | `` | bool | Filter on missing assignee |
| `--no-label` | `` | bool | Filter on missing label |
| `--no-milestone` | `` | bool | Filter on missing milestone |
| `--no-project` | `` | bool | Filter on missing project |
| `--order` | `` | string | Order of results returned, ignored unless '--sort' flag is specified: {asc|desc} (default "desc") (default: desc) |
| `--owner` | `` | string | Filter on repository owner |
| `--project` | `` | string | Filter on project board owner/number |
| `--reactions` | `` | string | Filter on number of reactions |
| `--repo` | `-R` | string | Filter on repository |
| `--review` | `` | string | Filter based on review status: {none|required|approved|changes_requested} |
| `--review-requested` | `` | string | Filter on user or team requested to review |
| `--reviewed-by` | `` | string | Filter on user who reviewed |
| `--sort` | `` | string | Sort fetched results: {comments|reactions|reactions-+1|reactions--1|reactions-smile|reactions-thinking_face|reactions-heart|reactions-tada|interactions|created|updated} (default "best-match") (default: best-match) |
| `--state` | `` | string | Filter based on state: {open|closed} |
| `--team-mentions` | `` | string | Filter based on team mentions |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--updated` | `` | string | Filter on last updated at date |
| `--visibility` | `` | string | Filter based on repository visibility: {public|private|internal} |
| `--web` | `-w` | bool | Open the search query in the web browser |

#### `gh search repos`

Search for repositories on GitHub.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--archived` | `` | bool | Filter based on the repository archived state {true|false} |
| `--created` | `` | string | Filter based on created at date |
| `--followers` | `` | string | Filter based on number of followers |
| `--forks` | `` | string | Filter on number of forks |
| `--good-first-issues` | `` | string | Filter on number of issues with the 'good first issue' label |
| `--help` | `` | bool | Show help for command |
| `--help-wanted-issues` | `` | string | Filter on number of issues with the 'help wanted' label |
| `--include-forks` | `` | string | Include forks in fetched repositories: {false|true|only} |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--language` | `` | string | Filter based on the coding language |
| `--license` | `` | string | Filter based on license type |
| `--limit` | `-L` | string | Maximum number of repositories to fetch (default 30) (default: 30) |
| `--match` | `` | string | Restrict search to specific field of repository: {name|description|readme} |
| `--number-topics` | `` | string | Filter on number of topics |
| `--order` | `` | string | Order of repositories returned, ignored unless '--sort' flag is specified: {asc|desc} (default "desc") (default: desc) |
| `--owner` | `` | string | Filter on owner |
| `--size` | `` | string | Filter on a size range, in kilobytes |
| `--sort` | `` | string | Sort fetched repositories: {forks|help-wanted-issues|stars|updated} (default "best-match") (default: best-match) |
| `--stars` | `` | string | Filter on number of stars |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--topic` | `` | string | Filter on topic |
| `--updated` | `` | string | Filter on last updated at date |
| `--visibility` | `` | string | Filter based on visibility: {public|private|internal} |
| `--web` | `-w` | bool | Open the search query in the web browser |

### `gh secret`

Secrets can be set at the repository, or organization level for use in

```
gh secret <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh secret delete`

Delete a secret on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `-a` | string | Delete a secret for a specific application: {actions|codespaces|dependabot} |
| `--env` | `-e` | string | Delete a secret for an environment |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | Delete a secret for an organization |
| `--user` | `-u` | bool | Delete a secret for your user |

#### `gh secret list`

List secrets on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `-a` | string | List secrets for a specific application: {actions|codespaces|dependabot} |
| `--env` | `-e` | string | List secrets for an environment |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--org` | `-o` | string | List secrets for an organization |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |
| `--user` | `-u` | bool | List a secret for your user |

#### `gh secret set`

Set a value for a secret on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `-a` | string | Set the application for a secret: {actions|codespaces|dependabot} |
| `--body` | `-b` | string | The value for the secret (reads from standard input if not specified) |
| `--env` | `-e` | string | Set deployment environment secret |
| `--env-file` | `-f` | string | Load secret names and values from a dotenv-formatted file |
| `--help` | `` | bool | Show help for command |
| `--no-repos-selected` | `` | bool | No repositories can access the organization secret |
| `--no-store` | `` | string | Print the encrypted, base64-encoded value instead of storing it on GitHub |
| `--org` | `-o` | string | Set organization secret |
| `--repos` | `-r` | string | List of repositories that can access an organization or user secret |
| `--user` | `-u` | bool | Set a secret for your user |
| `--visibility` | `-v` | string | Set visibility for an organization secret: {all|private|selected} (default "private") (default: private) |

### `gh ssh-key`

Manage SSH keys registered with your GitHub account.

```
gh ssh-key <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh ssh-key add`

Add an SSH key to your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--title` | `-t` | string | Title for the new key |
| `--type` | `` | string | Type of the ssh key: {authentication|signing} (default "authentication") (default: authentication) |

#### `gh ssh-key delete`

Delete an SSH key from your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--yes` | `-y` | bool | Skip the confirmation prompt |

#### `gh ssh-key list`

Lists SSH keys in your GitHub account

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

### `gh variable`

Variables can be set at the repository, environment or organization level for use in

```
gh variable <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh variable delete`

Delete a variable on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--env` | `-e` | string | Delete a variable for an environment |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | Delete a variable for an organization |

#### `gh variable get`

Get a variable on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--env` | `-e` | string | Get a variable for an environment |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--org` | `-o` | string | Get a variable for an organization |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh variable list`

List variables on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--env` | `-e` | string | List variables for an environment |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--org` | `-o` | string | List variables for an organization |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh variable set`

Set a value for a variable on one of the following levels:

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--body` | `-b` | string | The value for the variable (reads from standard input if not specified) |
| `--env` | `-e` | string | Set deployment environment variable |
| `--env-file` | `-f` | string | Load variable names and values from a dotenv-formatted file |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | Set organization variable |
| `--repos` | `-r` | string | List of repositories that can access an organization variable |
| `--visibility` | `-v` | string | Set visibility for an organization variable: {all|private|selected} (default "private") (default: private) |

### `gh workflow`

List, view, and run workflows in GitHub Actions.

```
gh workflow <command> [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

**Subcommands:**

#### `gh workflow disable`

Disable a workflow, preventing it from running or showing up when listing workflows.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh workflow enable`

Enable a workflow, allowing it to be run and show up when listing workflows.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |

#### `gh workflow list`

List workflow files, hiding disabled workflows by default.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Include disabled workflows |
| `--help` | `` | bool | Show help for command |
| `--jq` | `-q` | string | Filter JSON output using a jq expression |
| `--json` | `` | string | Output JSON with the specified fields |
| `--limit` | `-L` | string | Maximum number of workflows to fetch (default 50) (default: 50) |
| `--template` | `-t` | string | Format JSON output using a Go template; see "gh help formatting" |

#### `gh workflow run`

Create a `workflow_dispatch` event for a given workflow.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--field` | `-F` | string | Add a string parameter in key=value format, respecting @ syntax (see "gh help api"). |
| `--help` | `` | bool | Show help for command |
| `--json` | `` | bool | Read workflow inputs as JSON via STDIN |
| `--raw-field` | `-f` | string | Add a string parameter in key=value format |
| `--ref` | `-r` | string | Branch or tag name which contains the version of the workflow file you'd like to run |

#### `gh workflow view`

View the summary of a workflow

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--ref` | `-r` | string | The branch or tag name which contains the version of the workflow file you'd like to view |
| `--web` | `-w` | bool | Open workflow in the browser |
| `--yaml` | `-y` | string | View the workflow yaml file |

## Commands

### `gh api`



### `gh browse`

Transition from the terminal to the web browser to view and interact with:

```
gh browse [<number> | <path> | <commit-sha>] [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--actions` | `-a` | bool | Open repository actions |
| `--branch` | `-b` | string | Select another branch by passing in the branch name |
| `--commit` | `-c` | string | Select another commit by passing in the commit SHA, default is the last commit |
| `--help` | `` | bool | Show help for command |
| `--no-browser` | `-n` | string | Print destination URL instead of opening the browser |
| `--projects` | `-p` | bool | Open repository projects |
| `--releases` | `-r` | bool | Open repository releases |
| `--settings` | `-s` | bool | Open repository settings |
| `--wiki` | `-w` | bool | Open repository wiki |

### `gh completion`

Generate shell completion scripts for GitHub CLI commands.

```
gh completion -s <shell>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--shell` | `-s` | string | Shell type: {bash|zsh|fish|powershell} |

### `gh copilot`

Runs the GitHub Copilot CLI.

```
gh copilot [flags] [args]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show help for command |
| `--remove` | `` | bool | Remove the downloaded Copilot CLI |

### `gh status`

The status command prints information about your work on GitHub across all the repositories you're subscribed to, including:

```
gh status [flags]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--exclude` | `-e` | string | Comma separated list of repos to exclude in owner/name format |
| `--help` | `` | bool | Show help for command |
| `--org` | `-o` | string | Report status within an organization |

