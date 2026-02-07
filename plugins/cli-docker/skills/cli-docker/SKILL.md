---
name: cli-docker
description: >-
  This skill should be used when the user needs help with docker CLI commands, including builder (extended build capabilities with buildkit), buildx (extended build capabilities with buildkit), compose, container (manage containers), context (manage contexts), image (manage images), manifest, mcp, network (manage networks), plugin (manage plugins), swarm (manage swarm), system (manage docker), volume (manage volumes), attach, bake, build, commit, cp, create, diff, events, exec, export, history, images, import, info, inspect, kill, load, login, logout, logs, pause, port, ps, pull, push, rename, restart, rm, rmi, run, save, search, start, stats, stop, tag, top, unpause, update, version, wait. Covers flags, subcommands, usage patterns, and troubleshooting for all 54 docker commands.
---

# docker CLI Reference

Expert command reference for **docker** v29.2.0.

- **271** commands (31 with subcommands)
- **1408** command flags + **11** global flags
- **7** usage examples
- Max nesting depth: 3

## When to Use

This skill applies when:
- Constructing or validating `docker` commands
- Looking up flags, options, or subcommands
- Troubleshooting `docker` invocations or errors
- Needing correct syntax for `docker` operations

## Prerequisites

Ensure `docker` is installed and available on PATH.

## Quick Reference

| Command | Description |
| --- | --- |
| `docker attach` | Attach local standard input, output, and error streams to a running container |
| `docker bake` | Build from a file |
| `docker build` | Start a build |
| `docker builder` | Extended build capabilities with BuildKit |
| `docker buildx` | Extended build capabilities with BuildKit |
| `docker commit` | Create a new image from a container's changes |
| `docker compose` | Define and run multi-container applications with Docker |
| `docker container` | Manage containers |
| `docker context` | Manage contexts |
| `docker cp` | docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH |
| `docker create` | Create a new container |
| `docker diff` |  |
| `docker events` | Get real time events from the server |
| `docker exec` | Execute a command in a running container |
| `docker export` | Export a container's filesystem as a tar archive |
| `docker history` | Show the history of an image |
| `docker image` | Manage images |
| `docker images` | List images |
| `docker import` | Import the contents from a tarball to create a filesystem image |
| `docker info` | Display system-wide information |
| `docker inspect` | Return low-level information on Docker objects |
| `docker kill` | Kill one or more running containers |
| `docker load` | Load an image from a tar archive or STDIN |
| `docker login` | Authenticate to a registry. |
| `docker logout` |  |
| `docker logs` | Fetch the logs of a container |
| `docker manifest` | The **docker manifest** command has subcommands for managing image manifests and |
| `docker mcp` | Docker MCP Toolkit's CLI - Manage your MCP servers and clients. |
| `docker network` | Manage networks |
| `docker pause` |  |
| `docker plugin` | Manage plugins |
| `docker port` |  |
| `docker ps` | List containers |
| `docker pull` | Download an image from a registry |
| `docker push` | Upload an image to a registry |
| `docker rename` |  |
| `docker restart` | Restart one or more containers |
| `docker rm` | Remove one or more containers |
| `docker rmi` | Remove one or more images |
| `docker run` | Create and run a new container from an image |
| `docker save` | Save one or more images to a tar archive (streamed to STDOUT by default) |
| `docker search` | Search Docker Hub for images |
| `docker start` | Start one or more stopped containers |
| `docker stats` | Display a live stream of container(s) resource usage statistics |
| `docker stop` | Stop one or more running containers |
| `docker swarm` | Manage Swarm |
| `docker system` | Manage Docker |
| `docker tag` |  |
| `docker top` | Display the running processes of a container |
| `docker unpause` |  |
| `docker update` | Update configuration of one or more containers |
| `docker version` | Show the Docker version information |
| `docker volume` | Manage volumes |
| `docker wait` |  |

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `` | string | Location of client config files (default |
| `--context` | `-c` | string | Name of the context to use to connect to the |
| `--debug` | `-D` | bool | Enable debug mode |
| `--host` | `-H` | string | Daemon socket to connect to |
| `--log-level` | `-l` | string | Set the logging level ("debug", "info", |
| `--tls` | `` | bool | Use TLS; implied by --tlsverify |
| `--tlscacert` | `` | string | Trust certs signed only by this CA (default |
| `--tlscert` | `` | string | Path to TLS certificate file (default |
| `--tlskey` | `` | string | Path to TLS key file (default |
| `--tlsverify` | `` | bool | Use TLS and verify the remote |
| `--version` | `-v` | bool | Print version information and quit |

## Command Overview


### Commands

`attach`, `bake`, `build`, `commit`, `cp`, `create`, `diff`, `events`, `exec`, `export`, `history`, `images`, `import`, `info`, `inspect`, `kill`, `load`, `login`, `logout`, `logs`, `pause`, `port`, `ps`, `pull`, `push`, `rename`, `restart`, `rm`, `rmi`, `run`, `save`, `search`, `start`, `stats`, `stop`, `tag`, `top`, `unpause`, `update`, `version`, `wait`

### Command Groups

`builder`, `buildx`, `compose`, `container`, `context`, `image`, `manifest`, `mcp`, `network`, `plugin`, `swarm`, `system`, `volume`

## Common Usage Patterns

```bash
docker mcp catalog add my-catalog github-server ./github-catalog.yaml
```
docker mcp catalog add my-catalog slack-bot ./team-catalog.yaml --force

```bash
docker mcp catalog create dev-servers
```
docker mcp catalog create prod-monitoring

```bash
docker mcp catalog fork docker-mcp my-custom-docker
```
docker mcp catalog fork team-servers my-servers

```bash
docker mcp catalog import https://example.com/my-catalog.yaml
```
docker mcp catalog import ./shared-catalog.yaml

```bash
docker mcp catalog ls
```
docker mcp catalog ls --format=json

```bash
docker mcp catalog show
```
docker mcp catalog show my-catalog --format=json

```bash
docker mcp catalog update
```
docker mcp catalog update team-servers

## Detailed References

For complete command documentation including all flags and subcommands:
- **Full command tree:** see `references/commands.md`
- **All usage examples:** see `references/examples.md`

## Troubleshooting

- Use `docker --help` or `docker <command> --help` for inline help
- Add `--verbose` for detailed output during debugging

## Re-scanning

To update this plugin after a CLI version change, run the `/scan-cli` command
or manually execute the crawler and generator.
