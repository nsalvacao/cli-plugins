# docker -- Complete Command Reference

## Global Flags

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

## Commands

### `docker attach`

Attach local standard input, output, and error streams to a running container

```
docker attach [OPTIONS] CONTAINER
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--no-stdin` | `` | bool | Do not attach STDIN |
| `--sig-proxy` | `` | bool | Proxy all received signals to the process |

### `docker bake`

Build from a file

```
docker buildx bake [OPTIONS] [TARGET...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow` | `` | string | Allow build to access specified resources |
| `--builder` | `` | string | Override the configured builder instance |
| `--call` | `` | string | Set method for evaluating build ("check", |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Build definition file |
| `--list` | `` | string | List targets or variables |
| `--load` | `` | bool | Shorthand for |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--print` | `` | bool | Print the options without building |
| `--progress` | `` | string | Set type of progress output ("auto", |
| `--provenance` | `` | string | Shorthand for "--set=*.attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all referenced images |
| `--push` | `` | bool | Shorthand for |
| `--sbom` | `` | string | Shorthand for "--set=*.attest=type=sbom" |
| `--set` | `` | string | Override target value (e.g., |
| `--var` | `` | string | Set a variable value (e.g., "name=value") |

### `docker build`

Start a build

```
docker buildx build [OPTIONS] PATH | URL | -
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--allow` | `` | string | Allow extra privileged entitlement |
| `--annotation` | `` | string | Add annotation to the image |
| `--attest` | `` | string | Attestation parameters (format: |
| `--build-arg` | `` | string | Set build-time variables |
| `--build-context` | `` | string | Additional build contexts (e.g., |
| `--builder` | `` | string | Override the configured builder |
| `--cache-from` | `` | string | External cache sources (e.g., |
| `--cache-to` | `` | string | Cache export destinations (e.g., |
| `--call` | `` | string | Set method for evaluating build |
| `--cgroup-parent` | `` | string | Set the parent cgroup for the "RUN" |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Name of the Dockerfile (default: |
| `--iidfile` | `` | string | Write the image ID to a file |
| `--label` | `` | string | Set metadata for an image |
| `--load` | `` | bool | Shorthand for "--output=type=docker" |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--network` | `` | string | Set the networking mode for the |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--no-cache-filter` | `` | string | Do not cache specified stages |
| `--output` | `-o` | string | Output destination (format: |
| `--platform` | `` | string | Set target platform for build |
| `--policy` | `` | string | Policy configuration (format: |
| `--progress` | `` | string | Set type of progress output |
| `--provenance` | `` | string | Shorthand for "--attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all |
| `--push` | `` | bool | Shorthand for |
| `--quiet` | `-q` | bool | Suppress the build output and print |
| `--sbom` | `` | string | Shorthand for "--attest=type=sbom" |
| `--secret` | `` | string | Secret to expose to the build |
| `--shm-size` | `` | string | Shared memory size for build containers |
| `--ssh` | `` | string | SSH agent socket or keys to expose |
| `--tag` | `-t` | string | Image identifier (format: |
| `--target` | `` | string | Set the target build stage to build |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |

### `docker commit`

Create a new image from a container's changes

```
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--author` | `-a` | string | Author (e.g., "John Hannibal Smith |
| `--change` | `-c` | string | Apply Dockerfile instruction to the created image |
| `--message` | `-m` | string | Commit message |
| `--no-pause` | `` | bool | Disable pausing container during commit |

### `docker cp`

docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

```
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--archive` | `-a` | bool | Archive mode (copy all uid/gid information) |
| `--follow-link` | `-L` | bool | Always follow symbol link in SRC_PATH |
| `--quiet` | `-q` | bool | Suppress progress output during copy. Progress |

### `docker create`

Create a new container

```
docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--annotation` | `` | string | Add an annotation to the |
| `--attach` | `-a` | string | Attach to STDIN, STDOUT or STDERR |
| `--blkio-weight` | `` | string | Block IO (relative weight), |
| `--blkio-weight-device` | `` | string | Block IO weight (relative device |
| `--cap-add` | `` | string | Add Linux capabilities |
| `--cap-drop` | `` | string | Drop Linux capabilities |
| `--cgroup-parent` | `` | string | Optional parent cgroup for the |
| `--cgroupns` | `` | string | Cgroup namespace to use |
| `--cidfile` | `` | string | Write the container ID to the file |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution |
| `--device` | `` | string | Add a host device to the container |
| `--device-cgroup-rule` | `` | string | Add a rule to the cgroup allowed |
| `--device-read-bps` | `` | string | Limit read rate (bytes per |
| `--device-read-iops` | `` | string | Limit read rate (IO per second) |
| `--device-write-bps` | `` | string | Limit write rate (bytes per |
| `--device-write-iops` | `` | string | Limit write rate (IO per second) |
| `--dns` | `` | string | Set custom DNS servers |
| `--dns-option` | `` | string | Set DNS options |
| `--dns-search` | `` | string | Set custom DNS search domains |
| `--domainname` | `` | string | Container NIS domain name |
| `--entrypoint` | `` | string | Overwrite the default ENTRYPOINT |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment |
| `--expose` | `` | string | Expose a port or a range of ports |
| `--gpus` | `` | string | GPU devices to add to the |
| `--group-add` | `` | string | Add additional groups to join |
| `--health-cmd` | `` | string | Command to run to check health |
| `--health-interval` | `` | string | Time between running the check |
| `--health-retries` | `` | string | Consecutive failures needed to |
| `--health-start-interval` | `` | string | Time between running the check |
| `--health-start-period` | `` | string | Start period for the container |
| `--health-timeout` | `` | string | Maximum time to allow one check |
| `--help` | `` | bool | Print usage |
| `--hostname` | `-h` | string | Container host name |
| `--init` | `` | bool | Run an init inside the container |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--ip` | `` | string | IPv4 address (e.g., 172.30.100.104) |
| `--ip6` | `` | string | IPv6 address (e.g., 2001:db8::33) |
| `--ipc` | `` | string | IPC mode to use |
| `--isolation` | `` | string | Container isolation technology |
| `--label` | `-l` | string | Set meta data on a container |
| `--label-file` | `` | string | Read in a line delimited file of |
| `--link` | `` | string | Add link to another container |
| `--link-local-ip` | `` | string | Container IPv4/IPv6 link-local |
| `--log-driver` | `` | string | Logging driver for the container |
| `--log-opt` | `` | string | Log driver options |
| `--mac-address` | `` | string | Container MAC address (e.g., |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus |
| `--memory-swappiness` | `` | string | Tune container memory swappiness |
| `--mount` | `` | string | Attach a filesystem mount to the |
| `--name` | `` | string | Assign a name to the container |
| `--network` | `` | string | Connect a container to a network |
| `--network-alias` | `` | string | Add network-scoped alias for the |
| `--no-healthcheck` | `` | bool | Disable any container-specified |
| `--oom-kill-disable` | `` | bool | Disable OOM Killer |
| `--oom-score-adj` | `` | string | Tune host's OOM preferences |
| `--pid` | `` | string | PID namespace to use |
| `--pids-limit` | `` | string | Tune container pids limit (set |
| `--platform` | `` | string | Set platform if server is |
| `--privileged` | `` | bool | Give extended privileges to this |
| `--publish` | `-p` | string | Publish a container's port(s) to |
| `--publish-all` | `-P` | bool | Publish all exposed ports to |
| `--pull` | `` | string | Pull image before creating |
| `--quiet` | `-q` | bool | Suppress the pull output |
| `--read-only` | `` | bool | Mount the container's root |
| `--restart` | `` | string | Restart policy to apply when a |
| `--rm` | `` | bool | Automatically remove the |
| `--runtime` | `` | string | Runtime to use for this container |
| `--security-opt` | `` | string | Security Options |
| `--shm-size` | `` | string | Size of /dev/shm |
| `--stop-signal` | `` | string | Signal to stop the container |
| `--stop-timeout` | `` | string | Timeout (in seconds) to stop a |
| `--storage-opt` | `` | string | Storage driver options for the |
| `--sysctl` | `` | string | Sysctl options (default map[]) (default: map[]) |
| `--tmpfs` | `` | string | Mount a tmpfs directory |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |
| `--use-api-socket` | `` | bool | Bind mount Docker API socket and |
| `--user` | `-u` | string | Username or UID (format: |
| `--userns` | `` | string | User namespace to use |
| `--uts` | `` | string | UTS namespace to use |
| `--volume` | `-v` | string | Bind mount a volume |
| `--volume-driver` | `` | string | Optional volume driver for the |
| `--volumes-from` | `` | string | Mount volumes from the specified |
| `--workdir` | `-w` | string | Working directory inside the |

### `docker diff`



```
docker diff CONTAINER
```

### `docker events`

Get real time events from the server

```
docker events [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--since` | `` | string | Show all events created since timestamp |
| `--until` | `` | string | Stream events until this timestamp |

### `docker exec`

Execute a command in a running container

```
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach` | `-d` | bool | Detached mode: run command in the background |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment variables |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--privileged` | `` | bool | Give extended privileges to the command |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--user` | `-u` | string | Username or UID (format: |
| `--workdir` | `-w` | string | Working directory inside the container |

### `docker export`

Export a container's filesystem as a tar archive

```
docker export [OPTIONS] CONTAINER
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--output` | `-o` | string | Write to a file, instead of STDOUT |

### `docker history`

Show the history of an image

```
docker history [OPTIONS] IMAGE
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Format output using a custom template: |
| `--human` | `-H` | bool | Print sizes and dates in human readable format |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--platform` | `` | string | Show history for the given platform. Formatted |
| `--quiet` | `-q` | bool | Only show image IDs |

### `docker images`

List images

```
docker images [OPTIONS] [REPOSITORY[:TAG]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all images (default hides intermediate and |
| `--digests` | `` | bool | Show digests |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--quiet` | `-q` | bool | Only show image IDs |
| `--tree` | `` | bool | List multi-platform images as a tree (EXPERIMENTAL) |

### `docker import`

Import the contents from a tarball to create a filesystem image

```
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--change` | `-c` | string | Apply Dockerfile instruction to the created image |
| `--message` | `-m` | string | Set commit message for imported image |
| `--platform` | `` | string | Set platform if server is multi-platform capable |

### `docker info`

Display system-wide information

```
docker info [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

### `docker inspect`

Return low-level information on Docker objects

```
docker inspect [OPTIONS] NAME|ID [NAME|ID...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |
| `--size` | `-s` | string | Display total file sizes if the type is container |
| `--type` | `` | string | Only inspect objects of the given type |

### `docker kill`

Kill one or more running containers

```
docker kill [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |

### `docker load`

Load an image from a tar archive or STDIN

```
docker load [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--input` | `-i` | string | Read from tar archive file, instead of STDIN |
| `--platform` | `` | string | Load only the given platform(s). Formatted as |
| `--quiet` | `-q` | bool | Suppress the load output |

### `docker login`

Authenticate to a registry.

```
docker login [OPTIONS] [SERVER]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--password` | `-p` | string | Password or Personal Access Token (PAT) |
| `--password-stdin` | `` | bool | Take the Password or Personal Access Token |
| `--username` | `-u` | string | Username |

### `docker logout`



```
docker logout [SERVER]
```

### `docker logs`

Fetch the logs of a container

```
docker logs [OPTIONS] CONTAINER
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--details` | `` | bool | Show extra details provided to logs |
| `--follow` | `-f` | bool | Follow log output |
| `--since` | `` | string | Show logs since timestamp (e.g. |
| `--tail` | `-n` | string | Number of lines to show from the end of the logs |
| `--timestamps` | `-t` | bool | Show timestamps |
| `--until` | `` | string | Show logs before a timestamp (e.g. |

### `docker pause`



```
docker pause CONTAINER [CONTAINER...]
```

### `docker port`



```
docker port CONTAINER [PRIVATE_PORT[/PROTO]]
```

### `docker ps`

List containers

```
docker ps [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all containers (default shows just running) |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--last` | `-n` | string | Show n last created containers (includes all |
| `--latest` | `-l` | bool | Show the latest created container (includes all |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--quiet` | `-q` | bool | Only display container IDs |
| `--size` | `-s` | string | Display total file sizes |

### `docker pull`

Download an image from a registry

```
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-tags` | `-a` | bool | Download all tagged images in the repository |
| `--platform` | `` | string | Set platform if server is multi-platform capable |
| `--quiet` | `-q` | bool | Suppress verbose output |

### `docker push`

Upload an image to a registry

```
docker push [OPTIONS] NAME[:TAG]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-tags` | `-a` | bool | Push all tags of an image to the repository |
| `--platform` | `` | string | Push a platform-specific manifest as a |
| `--quiet` | `-q` | bool | Suppress verbose output |

### `docker rename`



```
docker rename CONTAINER NEW_NAME
```

### `docker restart`

Restart one or more containers

```
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |
| `--timeout` | `-t` | string | Seconds to wait before killing the container |

### `docker rm`

Remove one or more containers

```
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the removal of a running container (uses SIGKILL) |
| `--link` | `-l` | bool | Remove the specified link |
| `--volumes` | `-v` | bool | Remove anonymous volumes associated with the container |

### `docker rmi`

Remove one or more images

```
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force removal of the image |
| `--no-prune` | `` | bool | Do not delete untagged parents |
| `--platform` | `` | string | Remove only the given platform variant. |

### `docker run`

Create and run a new container from an image

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--annotation` | `` | string | Add an annotation to the |
| `--attach` | `-a` | string | Attach to STDIN, STDOUT or STDERR |
| `--blkio-weight` | `` | string | Block IO (relative weight), |
| `--blkio-weight-device` | `` | string | Block IO weight (relative device |
| `--cap-add` | `` | string | Add Linux capabilities |
| `--cap-drop` | `` | string | Drop Linux capabilities |
| `--cgroup-parent` | `` | string | Optional parent cgroup for the |
| `--cgroupns` | `` | string | Cgroup namespace to use |
| `--cidfile` | `` | string | Write the container ID to the file |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution |
| `--detach` | `-d` | bool | Run container in background and |
| `--detach-keys` | `` | string | Override the key sequence for |
| `--device` | `` | string | Add a host device to the container |
| `--device-cgroup-rule` | `` | string | Add a rule to the cgroup allowed |
| `--device-read-bps` | `` | string | Limit read rate (bytes per |
| `--device-read-iops` | `` | string | Limit read rate (IO per second) |
| `--device-write-bps` | `` | string | Limit write rate (bytes per |
| `--device-write-iops` | `` | string | Limit write rate (IO per second) |
| `--dns` | `` | string | Set custom DNS servers |
| `--dns-option` | `` | string | Set DNS options |
| `--dns-search` | `` | string | Set custom DNS search domains |
| `--domainname` | `` | string | Container NIS domain name |
| `--entrypoint` | `` | string | Overwrite the default ENTRYPOINT |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment |
| `--expose` | `` | string | Expose a port or a range of ports |
| `--gpus` | `` | string | GPU devices to add to the |
| `--group-add` | `` | string | Add additional groups to join |
| `--health-cmd` | `` | string | Command to run to check health |
| `--health-interval` | `` | string | Time between running the check |
| `--health-retries` | `` | string | Consecutive failures needed to |
| `--health-start-interval` | `` | string | Time between running the check |
| `--health-start-period` | `` | string | Start period for the container |
| `--health-timeout` | `` | string | Maximum time to allow one check |
| `--help` | `` | bool | Print usage |
| `--hostname` | `-h` | string | Container host name |
| `--init` | `` | bool | Run an init inside the container |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--ip` | `` | string | IPv4 address (e.g., 172.30.100.104) |
| `--ip6` | `` | string | IPv6 address (e.g., 2001:db8::33) |
| `--ipc` | `` | string | IPC mode to use |
| `--isolation` | `` | string | Container isolation technology |
| `--label` | `-l` | string | Set meta data on a container |
| `--label-file` | `` | string | Read in a line delimited file of |
| `--link` | `` | string | Add link to another container |
| `--link-local-ip` | `` | string | Container IPv4/IPv6 link-local |
| `--log-driver` | `` | string | Logging driver for the container |
| `--log-opt` | `` | string | Log driver options |
| `--mac-address` | `` | string | Container MAC address (e.g., |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus |
| `--memory-swappiness` | `` | string | Tune container memory swappiness |
| `--mount` | `` | string | Attach a filesystem mount to the |
| `--name` | `` | string | Assign a name to the container |
| `--network` | `` | string | Connect a container to a network |
| `--network-alias` | `` | string | Add network-scoped alias for the |
| `--no-healthcheck` | `` | bool | Disable any container-specified |
| `--oom-kill-disable` | `` | bool | Disable OOM Killer |
| `--oom-score-adj` | `` | string | Tune host's OOM preferences |
| `--pid` | `` | string | PID namespace to use |
| `--pids-limit` | `` | string | Tune container pids limit (set |
| `--platform` | `` | string | Set platform if server is |
| `--privileged` | `` | bool | Give extended privileges to this |
| `--publish` | `-p` | string | Publish a container's port(s) to |
| `--publish-all` | `-P` | bool | Publish all exposed ports to |
| `--pull` | `` | string | Pull image before running |
| `--quiet` | `-q` | bool | Suppress the pull output |
| `--read-only` | `` | bool | Mount the container's root |
| `--restart` | `` | string | Restart policy to apply when a |
| `--rm` | `` | bool | Automatically remove the |
| `--runtime` | `` | string | Runtime to use for this container |
| `--security-opt` | `` | string | Security Options |
| `--shm-size` | `` | string | Size of /dev/shm |
| `--sig-proxy` | `` | bool | Proxy received signals to the |
| `--stop-signal` | `` | string | Signal to stop the container |
| `--stop-timeout` | `` | string | Timeout (in seconds) to stop a |
| `--storage-opt` | `` | string | Storage driver options for the |
| `--sysctl` | `` | string | Sysctl options (default map[]) (default: map[]) |
| `--tmpfs` | `` | string | Mount a tmpfs directory |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |
| `--use-api-socket` | `` | bool | Bind mount Docker API socket and |
| `--user` | `-u` | string | Username or UID (format: |
| `--userns` | `` | string | User namespace to use |
| `--uts` | `` | string | UTS namespace to use |
| `--volume` | `-v` | string | Bind mount a volume |
| `--volume-driver` | `` | string | Optional volume driver for the |
| `--volumes-from` | `` | string | Mount volumes from the specified |
| `--workdir` | `-w` | string | Working directory inside the |

### `docker save`

Save one or more images to a tar archive (streamed to STDOUT by default)

```
docker save [OPTIONS] IMAGE [IMAGE...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--output` | `-o` | string | Write to a file, instead of STDOUT |
| `--platform` | `` | string | Save only the given platform(s). Formatted as |

### `docker search`

Search Docker Hub for images

```
docker search [OPTIONS] TERM
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Pretty-print search using a Go template |
| `--limit` | `` | string | Max number of search results |
| `--no-trunc` | `` | bool | Don't truncate output |

### `docker start`

Start one or more stopped containers

```
docker start [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--attach` | `-a` | bool | Attach STDOUT/STDERR and forward signals |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--interactive` | `-i` | bool | Attach container's STDIN |

### `docker stats`

Display a live stream of container(s) resource usage statistics

```
docker stats [OPTIONS] [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all containers (default shows just running) |
| `--format` | `` | string | Format output using a custom template: |
| `--no-stream` | `` | bool | Disable streaming stats and only pull the first result |
| `--no-trunc` | `` | bool | Do not truncate output |

### `docker stop`

Stop one or more running containers

```
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |
| `--timeout` | `-t` | string | Seconds to wait before killing the container |

### `docker tag`



```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

### `docker top`

Display the running processes of a container

```
docker top CONTAINER [ps OPTIONS]
```

### `docker unpause`



```
docker unpause CONTAINER [CONTAINER...]
```

### `docker update`

Update configuration of one or more containers

```
docker update [OPTIONS] CONTAINER [CONTAINER...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--blkio-weight` | `` | string | Block IO (relative weight), between 10 |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit the CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit the CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution (0-3, 0,1) |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution (0-3, 0,1) |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus swap: |
| `--pids-limit` | `` | string | Tune container pids limit (set -1 for |
| `--restart` | `` | string | Restart policy to apply when a |

### `docker version`

Show the Docker version information

```
docker version [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

### `docker wait`



```
docker wait CONTAINER [CONTAINER...]
```

## Command Groups

### `docker builder`

Extended build capabilities with BuildKit

```
docker buildx [OPTIONS] COMMAND
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

**Subcommands:**

#### `docker builder bake`

Build from a file

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow` | `` | string | Allow build to access specified resources |
| `--builder` | `` | string | Override the configured builder instance |
| `--call` | `` | string | Set method for evaluating build ("check", |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Build definition file |
| `--list` | `` | string | List targets or variables |
| `--load` | `` | bool | Shorthand for |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--print` | `` | bool | Print the options without building |
| `--progress` | `` | string | Set type of progress output ("auto", |
| `--provenance` | `` | string | Shorthand for "--set=*.attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all referenced images |
| `--push` | `` | bool | Shorthand for |
| `--sbom` | `` | string | Shorthand for "--set=*.attest=type=sbom" |
| `--set` | `` | string | Override target value (e.g., |
| `--var` | `` | string | Set a variable value (e.g., "name=value") |

#### `docker builder build`

Start a build

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--allow` | `` | string | Allow extra privileged entitlement |
| `--annotation` | `` | string | Add annotation to the image |
| `--attest` | `` | string | Attestation parameters (format: |
| `--build-arg` | `` | string | Set build-time variables |
| `--build-context` | `` | string | Additional build contexts (e.g., |
| `--builder` | `` | string | Override the configured builder |
| `--cache-from` | `` | string | External cache sources (e.g., |
| `--cache-to` | `` | string | Cache export destinations (e.g., |
| `--call` | `` | string | Set method for evaluating build |
| `--cgroup-parent` | `` | string | Set the parent cgroup for the "RUN" |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Name of the Dockerfile (default: |
| `--iidfile` | `` | string | Write the image ID to a file |
| `--label` | `` | string | Set metadata for an image |
| `--load` | `` | bool | Shorthand for "--output=type=docker" |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--network` | `` | string | Set the networking mode for the |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--no-cache-filter` | `` | string | Do not cache specified stages |
| `--output` | `-o` | string | Output destination (format: |
| `--platform` | `` | string | Set target platform for build |
| `--policy` | `` | string | Policy configuration (format: |
| `--progress` | `` | string | Set type of progress output |
| `--provenance` | `` | string | Shorthand for "--attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all |
| `--push` | `` | bool | Shorthand for |
| `--quiet` | `-q` | bool | Suppress the build output and print |
| `--sbom` | `` | string | Shorthand for "--attest=type=sbom" |
| `--secret` | `` | string | Secret to expose to the build |
| `--shm-size` | `` | string | Shared memory size for build containers |
| `--ssh` | `` | string | SSH agent socket or keys to expose |
| `--tag` | `-t` | string | Image identifier (format: |
| `--target` | `` | string | Set the target build stage to build |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |

#### `docker builder create`

Create a new builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--append` | `` | bool | Append a node to builder instead of |
| `--bootstrap` | `` | bool | Boot builder after creation |
| `--buildkitd-config` | `` | string | BuildKit daemon config file |
| `--buildkitd-flags` | `` | string | BuildKit daemon flags |
| `--debug` | `-D` | bool | Enable debug logging |
| `--driver` | `` | string | Driver to use (available: |
| `--driver-opt` | `` | string | Options for the driver |
| `--leave` | `` | bool | Remove a node from builder instead of |
| `--name` | `` | string | Builder instance name |
| `--node` | `` | string | Create/modify node with given name |
| `--platform` | `` | string | Fixed platforms for current node |
| `--use` | `` | bool | Set the current builder instance |

#### `docker builder dial-stdio`

Proxy current stdio streams to builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--platform` | `` | string | Target platform: this is used for node selection |
| `--progress` | `` | string | Set type of progress output ("auto", "plain", |

#### `docker builder du`

Disk usage

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--filter` | `` | string | Provide filter values |
| `--format` | `` | string | Format the output |
| `--verbose` | `` | bool | Shorthand for "--format=pretty" |

#### `docker builder history`

Commands to work on build records

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker builder history export`

Export build records into Docker Desktop bundle

##### `docker builder history import`

Import build records into Docker Desktop

##### `docker builder history inspect`

Inspect a build record

##### `docker builder history logs`

Print the logs of a build record

##### `docker builder history ls`

List build records

##### `docker builder history open`

Open a build record in Docker Desktop

##### `docker builder history rm`

Remove build records

##### `docker builder history trace`

Show the OpenTelemetry trace of a build record

#### `docker builder imagetools`

Commands to work on images in registry

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker builder imagetools create`

Create a new image based on source images

##### `docker builder imagetools inspect`

Show details of an image in the registry

#### `docker builder inspect`

Inspect current builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bootstrap` | `` | bool | Ensure builder has booted before inspecting |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

#### `docker builder ls`

List builder instances

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `-D` | bool | Enable debug logging |
| `--format` | `` | string | Format the output (default "table") (default: table) |
| `--no-trunc` | `` | bool | Don't truncate output |

#### `docker builder policy`

Commands for working with build policies

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker builder policy eval`

Evaluate policy for a source

##### `docker builder policy test`

Run policy tests

#### `docker builder prune`

Remove build cache

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Include internal/frontend images |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--filter` | `` | string | Provide filter values |
| `--force` | `-f` | bool | Do not prompt for confirmation |
| `--max-used-space` | `` | string | Maximum amount of disk space allowed to |
| `--min-free-space` | `` | string | Target amount of free disk space after pruning |
| `--reserved-space` | `` | string | Amount of disk space always allowed to |
| `--verbose` | `` | bool | Provide a more verbose output |

#### `docker builder rm`

Remove one or more builder instances

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-inactive` | `` | bool | Remove all inactive builders |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--force` | `-f` | bool | Do not prompt for confirmation |
| `--keep-daemon` | `` | bool | Keep the BuildKit daemon running |
| `--keep-state` | `` | bool | Keep BuildKit state |

#### `docker builder stop`

Stop builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

#### `docker builder version`

Show buildx version information

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `-D` | bool | Enable debug logging |

### `docker buildx`

Extended build capabilities with BuildKit

```
docker buildx [OPTIONS] COMMAND
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

**Subcommands:**

#### `docker buildx bake`

Build from a file

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow` | `` | string | Allow build to access specified resources |
| `--builder` | `` | string | Override the configured builder instance |
| `--call` | `` | string | Set method for evaluating build ("check", |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Build definition file |
| `--list` | `` | string | List targets or variables |
| `--load` | `` | bool | Shorthand for |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--print` | `` | bool | Print the options without building |
| `--progress` | `` | string | Set type of progress output ("auto", |
| `--provenance` | `` | string | Shorthand for "--set=*.attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all referenced images |
| `--push` | `` | bool | Shorthand for |
| `--sbom` | `` | string | Shorthand for "--set=*.attest=type=sbom" |
| `--set` | `` | string | Override target value (e.g., |
| `--var` | `` | string | Set a variable value (e.g., "name=value") |

#### `docker buildx build`

Start a build

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--allow` | `` | string | Allow extra privileged entitlement |
| `--annotation` | `` | string | Add annotation to the image |
| `--attest` | `` | string | Attestation parameters (format: |
| `--build-arg` | `` | string | Set build-time variables |
| `--build-context` | `` | string | Additional build contexts (e.g., |
| `--builder` | `` | string | Override the configured builder instance |
| `--cache-from` | `` | string | External cache sources (e.g., |
| `--cache-to` | `` | string | Cache export destinations (e.g., |
| `--call` | `` | string | Set method for evaluating build |
| `--cgroup-parent` | `` | string | Set the parent cgroup for the "RUN" |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Name of the Dockerfile (default: |
| `--iidfile` | `` | string | Write the image ID to a file |
| `--label` | `` | string | Set metadata for an image |
| `--load` | `` | bool | Shorthand for "--output=type=docker" |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--network` | `` | string | Set the networking mode for the |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--no-cache-filter` | `` | string | Do not cache specified stages |
| `--output` | `-o` | string | Output destination (format: |
| `--platform` | `` | string | Set target platform for build |
| `--policy` | `` | string | Policy configuration (format: |
| `--progress` | `` | string | Set type of progress output |
| `--provenance` | `` | string | Shorthand for "--attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all |
| `--push` | `` | bool | Shorthand for |
| `--quiet` | `-q` | bool | Suppress the build output and print |
| `--sbom` | `` | string | Shorthand for "--attest=type=sbom" |
| `--secret` | `` | string | Secret to expose to the build |
| `--shm-size` | `` | string | Shared memory size for build containers |
| `--ssh` | `` | string | SSH agent socket or keys to expose |
| `--tag` | `-t` | string | Image identifier (format: |
| `--target` | `` | string | Set the target build stage to build |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |

#### `docker buildx create`

Create a new builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--append` | `` | bool | Append a node to builder instead of |
| `--bootstrap` | `` | bool | Boot builder after creation |
| `--buildkitd-config` | `` | string | BuildKit daemon config file |
| `--buildkitd-flags` | `` | string | BuildKit daemon flags |
| `--debug` | `-D` | bool | Enable debug logging |
| `--driver` | `` | string | Driver to use (available: |
| `--driver-opt` | `` | string | Options for the driver |
| `--leave` | `` | bool | Remove a node from builder instead of |
| `--name` | `` | string | Builder instance name |
| `--node` | `` | string | Create/modify node with given name |
| `--platform` | `` | string | Fixed platforms for current node |
| `--use` | `` | bool | Set the current builder instance |

#### `docker buildx dial-stdio`

Proxy current stdio streams to builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--platform` | `` | string | Target platform: this is used for node selection |
| `--progress` | `` | string | Set type of progress output ("auto", "plain", |

#### `docker buildx du`

Disk usage

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--filter` | `` | string | Provide filter values |
| `--format` | `` | string | Format the output |
| `--verbose` | `` | bool | Shorthand for "--format=pretty" |

#### `docker buildx history`

Commands to work on build records

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker buildx history export`

Export build records into Docker Desktop bundle

##### `docker buildx history import`

Import build records into Docker Desktop

##### `docker buildx history inspect`

Inspect a build record

##### `docker buildx history logs`

Print the logs of a build record

##### `docker buildx history ls`

List build records

##### `docker buildx history open`

Open a build record in Docker Desktop

##### `docker buildx history rm`

Remove build records

##### `docker buildx history trace`

Show the OpenTelemetry trace of a build record

#### `docker buildx imagetools`

Commands to work on images in registry

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker buildx imagetools create`

Create a new image based on source images

##### `docker buildx imagetools inspect`

Show details of an image in the registry

#### `docker buildx inspect`

Inspect current builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bootstrap` | `` | bool | Ensure builder has booted before inspecting |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

#### `docker buildx ls`

List builder instances

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `-D` | bool | Enable debug logging |
| `--format` | `` | string | Format the output (default "table") (default: table) |
| `--no-trunc` | `` | bool | Don't truncate output |

#### `docker buildx policy`

Commands for working with build policies

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

##### `docker buildx policy eval`

Evaluate policy for a source

##### `docker buildx policy test`

Run policy tests

#### `docker buildx prune`

Remove build cache

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Include internal/frontend images |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--filter` | `` | string | Provide filter values |
| `--force` | `-f` | bool | Do not prompt for confirmation |
| `--max-used-space` | `` | string | Maximum amount of disk space allowed to |
| `--min-free-space` | `` | string | Target amount of free disk space after pruning |
| `--reserved-space` | `` | string | Amount of disk space always allowed to |
| `--verbose` | `` | bool | Provide a more verbose output |

#### `docker buildx rm`

Remove one or more builder instances

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-inactive` | `` | bool | Remove all inactive builders |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |
| `--force` | `-f` | bool | Do not prompt for confirmation |
| `--keep-daemon` | `` | bool | Keep the BuildKit daemon running |
| `--keep-state` | `` | bool | Keep BuildKit state |

#### `docker buildx stop`

Stop builder instance

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--builder` | `` | string | Override the configured builder instance |
| `--debug` | `-D` | bool | Enable debug logging |

#### `docker buildx version`

Show buildx version information

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--debug` | `-D` | bool | Enable debug logging |

### `docker compose`

Define and run multi-container applications with Docker

```
docker compose [OPTIONS] COMMAND
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-resources` | `` | bool | Include all resources, even those not |
| `--ansi` | `` | string | Control when to print ANSI control |
| `--compatibility` | `` | bool | Run compose in backward compatibility mode |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--env-file` | `` | string | Specify an alternate environment file |
| `--file` | `-f` | string | Compose configuration files |
| `--parallel` | `` | string | Control max parallelism, -1 for |
| `--profile` | `` | string | Specify a profile to enable |
| `--progress` | `` | string | Set type of progress output (auto, |
| `--project-directory` | `` | string | Specify an alternate working directory |
| `--project-name` | `-p` | string | Project name |

**Subcommands:**

#### `docker compose attach`

Attach local standard input, output, and error streams to a service's running container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach-keys` | `` | string | Override the key sequence for detaching from |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--index` | `` | string | index of the container if service has |
| `--no-stdin` | `` | bool | Do not attach STDIN |
| `--sig-proxy` | `` | bool | Proxy all received signals to the process |

#### `docker compose bridge`

Convert compose files into another model

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |

##### `docker compose bridge convert`

Convert compose files to Kubernetes manifests, Helm charts, or another model

#### `docker compose build`

Build or rebuild services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--build-arg` | `` | string | Set build-time variables for services |
| `--builder` | `` | string | Set builder to use |
| `--check` | `` | bool | Check build configuration |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--memory` | `-m` | string | Set memory limit for the build container. |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--print` | `` | string | Print equivalent bake file |
| `--provenance` | `` | string | Add a provenance attestation |
| `--pull` | `` | bool | Always attempt to pull a newer version of |
| `--push` | `` | bool | Push service images |
| `--quiet` | `-q` | bool | Suppress the build output |
| `--sbom` | `` | string | Add a SBOM attestation |
| `--ssh` | `` | string | Set SSH authentications used when |
| `--with-dependencies` | `` | bool | Also build dependencies (transitively) |

#### `docker compose commit`

Create a new image from a service container's changes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--author` | `-a` | string | Author (e.g., "John Hannibal Smith |
| `--change` | `-c` | string | Apply Dockerfile instruction to the created image |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--index` | `` | string | index of the container if service has multiple |
| `--message` | `-m` | string | Commit message |
| `--pause` | `-p` | bool | Pause container during commit (default true) (default: true) |

#### `docker compose config`

Parse, resolve and render compose file in canonical format

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--environment` | `` | bool | Print environment used for interpolation. |
| `--format` | `` | string | Format the output. Values: [yaml | json] |
| `--hash` | `` | string | Print the service config hash, one per line. |
| `--images` | `` | bool | Print the image names, one per line. |
| `--lock-image-digests` | `` | string | Produces an override file with image digests |
| `--models` | `` | bool | Print the model names, one per line. |
| `--networks` | `` | bool | Print the network names, one per line. |
| `--no-consistency` | `` | bool | Don't check model consistency - warning: |
| `--no-env-resolution` | `` | string | Don't resolve service env files |
| `--no-interpolate` | `` | bool | Don't interpolate environment variables |
| `--no-normalize` | `` | bool | Don't normalize compose model |
| `--no-path-resolution` | `` | string | Don't resolve file paths |
| `--output` | `-o` | string | Save to file (default to stdout) |
| `--profiles` | `` | string | Print the profile names, one per line. |
| `--quiet` | `-q` | bool | Only validate the configuration, don't |
| `--resolve-image-digests` | `` | bool | Pin image tags to digests |
| `--services` | `` | bool | Print the service names, one per line. |
| `--variables` | `` | string | Print model variables and default values. |
| `--volumes` | `` | bool | Print the volume names, one per line. |

#### `docker compose cp`

docker compose cp [OPTIONS] SRC_PATH|- SERVICE:DEST_PATH

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Include containers created by the run command |
| `--archive` | `-a` | bool | Archive mode (copy all uid/gid information) |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--follow-link` | `-L` | bool | Always follow symbol link in SRC_PATH |
| `--index` | `` | string | Index of the container if service has multiple replicas |

#### `docker compose create`

Creates containers for a service

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--build` | `` | bool | Build images before starting containers |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--force-recreate` | `` | bool | Recreate containers even if their configuration |
| `--no-build` | `` | bool | Don't build an image, even if it's policy |
| `--no-recreate` | `` | bool | If containers already exist, don't recreate |
| `--pull` | `` | string | Pull image before running |
| `--quiet-pull` | `` | bool | Pull without printing progress information |
| `--remove-orphans` | `` | bool | Remove containers for services not defined in |
| `--scale` | `` | string | Scale SERVICE to NUM instances. Overrides the |
| `--yes` | `-y` | bool | Assume "yes" as answer to all prompts and run |

#### `docker compose down`

Stop and remove containers, networks

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--remove-orphans` | `` | bool | Remove containers for services not defined in |
| `--rmi` | `` | string | Remove images used by services. "local" remove |
| `--timeout` | `-t` | string | Specify a shutdown timeout in seconds |
| `--volumes` | `-v` | bool | Remove named volumes declared in the "volumes" |

#### `docker compose events`

Receive real time events from containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--json` | `` | bool | Output events as a stream of json objects |
| `--since` | `` | string | Show all events created since timestamp |
| `--until` | `` | string | Stream events until this timestamp |

#### `docker compose exec`

Execute a command in a running container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach` | `-d` | bool | Detached mode: Run command in the background |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--env` | `-e` | string | Set environment variables |
| `--index` | `` | string | Index of the container if service has multiple |
| `--no-tty` | `-T` | bool | Disable pseudo-TTY allocation. By default |
| `--privileged` | `` | bool | Give extended privileges to the process |
| `--user` | `-u` | string | Run the command as this user |
| `--workdir` | `-w` | string | Path to workdir directory for this command |

#### `docker compose export`

Export a service container's filesystem as a tar archive

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--index` | `` | string | index of the container if service has multiple |
| `--output` | `-o` | string | Write to a file, instead of STDOUT |

#### `docker compose images`

List images used by the created containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--format` | `` | string | Format the output. Values: [table | json] |
| `--quiet` | `-q` | bool | Only display IDs |

#### `docker compose kill`

Force stop service containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--remove-orphans` | `` | bool | Remove containers for services not defined in |
| `--signal` | `-s` | string | SIGNAL to send to the container (default "SIGKILL") (default: SIGKILL) |

#### `docker compose logs`

View output from containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--follow` | `-f` | bool | Follow log output |
| `--index` | `` | string | index of the container if service has multiple |
| `--no-color` | `` | bool | Produce monochrome output |
| `--no-log-prefix` | `` | bool | Don't print prefix in logs |
| `--since` | `` | string | Show logs since timestamp (e.g. |
| `--tail` | `-n` | string | Number of lines to show from the end of the logs |
| `--timestamps` | `-t` | bool | Show timestamps |
| `--until` | `` | string | Show logs before a timestamp (e.g. |

#### `docker compose ls`

List running compose projects

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all stopped Compose projects |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--filter` | `` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format the output. Values: [table | json] |
| `--quiet` | `-q` | bool | Only display project names |

#### `docker compose pause`

Pause services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |

#### `docker compose port`

Print the public port for a port binding

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--index` | `` | string | Index of the container if service has multiple |
| `--protocol` | `` | string | tcp or udp (default "tcp") (default: tcp) |

#### `docker compose ps`

List containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all stopped containers (including those |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--filter` | `` | string | Filter services by a property (supported |
| `--format` | `` | string | Format output using a custom template: |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--orphans` | `` | bool | Include orphaned services (not declared by |
| `--quiet` | `-q` | bool | Only display IDs |
| `--services` | `` | bool | Display services |
| `--status` | `` | string | Filter services by status. Values: [paused | |

#### `docker compose publish`

Publish compose application

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | bool | Published compose application (includes |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--oci-version` | `` | string | OCI image/artifact specification version |
| `--resolve-image-digests` | `` | bool | Pin image tags to digests |
| `--with-env` | `` | bool | Include environment variables in the |
| `--yes` | `-y` | bool | Assume "yes" as answer to all prompts |

#### `docker compose pull`

Pull service images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--ignore-buildable` | `` | bool | Ignore images that can be built |
| `--ignore-pull-failures` | `` | bool | Pull what it can and ignores images with |
| `--include-deps` | `` | bool | Also pull services declared as dependencies |
| `--policy` | `` | string | Apply pull policy ("missing"|"always") |
| `--quiet` | `-q` | bool | Pull without printing progress information |

#### `docker compose push`

Push service images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--ignore-push-failures` | `` | bool | Push what it can and ignores images with |
| `--include-deps` | `` | bool | Also push images of services declared as |
| `--quiet` | `-q` | bool | Push without printing progress information |

#### `docker compose restart`

Restart service containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--no-deps` | `` | bool | Don't restart dependent services |
| `--timeout` | `-t` | string | Specify a shutdown timeout in seconds |

#### `docker compose rm`

Removes stopped service containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--force` | `-f` | bool | Don't ask to confirm removal |
| `--stop` | `-s` | bool | Stop the containers, if required, before removing |
| `--volumes` | `-v` | bool | Remove any anonymous volumes attached to containers |

#### `docker compose run`

Run a one-off command on a service

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--build` | `` | bool | Build image before starting container |
| `--cap-add` | `` | string | Add Linux capabilities |
| `--cap-drop` | `` | string | Drop Linux capabilities |
| `--detach` | `-d` | bool | Run container in background and print |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--entrypoint` | `` | string | Override the entrypoint of the image |
| `--env` | `-e` | string | Set environment variables |
| `--env-from-file` | `` | string | Set environment variables from file |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--label` | `-l` | string | Add or override a label |
| `--name` | `` | string | Assign a name to the container |
| `--no-TTY` | `-T` | bool | Disable pseudo-TTY allocation |
| `--no-deps` | `` | bool | Don't start linked services |
| `--publish` | `-p` | string | Publish a container's port(s) to the host |
| `--pull` | `` | string | Pull image before running |
| `--quiet` | `-q` | bool | Don't print anything to STDOUT |
| `--quiet-build` | `` | bool | Suppress progress output from the |
| `--quiet-pull` | `` | bool | Pull without printing progress information |
| `--remove-orphans` | `` | bool | Remove containers for services not |
| `--rm` | `` | bool | Automatically remove the container |
| `--service-ports` | `-P` | bool | Run command with all service's ports |
| `--use-aliases` | `` | bool | Use the service's network useAliases |
| `--user` | `-u` | string | Run as specified username or uid |
| `--volume` | `-v` | string | Bind mount a volume |
| `--workdir` | `-w` | string | Working directory inside the container |

#### `docker compose scale`

Scale services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--no-deps` | `` | bool | Don't start linked services |

#### `docker compose start`

Start services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--wait` | `` | bool | Wait for services to be running|healthy. |
| `--wait-timeout` | `` | string | Maximum duration in seconds to wait for the |

#### `docker compose stats`

Display a live stream of container(s) resource usage statistics

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all containers (default shows just running) |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--format` | `` | string | Format output using a custom template: |
| `--no-stream` | `` | bool | Disable streaming stats and only pull the first result |
| `--no-trunc` | `` | bool | Do not truncate output |

#### `docker compose stop`

Stop services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--timeout` | `-t` | string | Specify a shutdown timeout in seconds |

#### `docker compose top`

Display the running processes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |

#### `docker compose unpause`

Unpause services

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |

#### `docker compose up`

Create and start containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abort-on-container-exit` | `` | bool | Stops all containers if any |
| `--abort-on-container-exit` | `` | bool |  |
| `--abort-on-container-failure` | `` | bool | Stops all containers if any |
| `--always-recreate-deps` | `` | bool | Recreate dependent containers. |
| `--attach` | `` | string | Restrict attaching to the specified |
| `--attach-dependencies` | `` | bool | Automatically attach to log output |
| `--build` | `` | bool | Build images before starting containers |
| `--detach` | `-d` | bool | Detached mode: Run containers in the |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--exit-code-from` | `` | string | Return the exit code of the selected |
| `--force-recreate` | `` | bool | Recreate containers even if their |
| `--menu` | `` | bool | Enable interactive shortcuts when |
| `--no-attach` | `` | string | Do not attach (stream logs) to the |
| `--no-build` | `` | bool | Don't build an image, even if it's policy |
| `--no-color` | `` | bool | Produce monochrome output |
| `--no-deps` | `` | bool | Don't start linked services |
| `--no-log-prefix` | `` | bool | Don't print prefix in logs |
| `--no-recreate` | `` | bool | If containers already exist, don't |
| `--no-start` | `` | bool | Don't start the services after |
| `--pull` | `` | string | Pull image before running |
| `--quiet-build` | `` | bool | Suppress the build output |
| `--quiet-pull` | `` | bool | Pull without printing progress |
| `--remove-orphans` | `` | bool | Remove containers for services not |
| `--renew-anon-volumes` | `-V` | bool | Recreate anonymous volumes instead |
| `--scale` | `` | string | Scale SERVICE to NUM instances. |
| `--timeout` | `-t` | string | Use this timeout in seconds for |
| `--timestamps` | `` | bool | Show timestamps |
| `--wait` | `` | bool | Wait for services to be |
| `--wait-timeout` | `` | string | Maximum duration in seconds to wait |
| `--watch` | `-w` | bool | Watch source code and |
| `--yes` | `-y` | bool | Assume "yes" as answer to all |

#### `docker compose version`

Show the Docker Compose version information

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--format` | `-f` | string | Format the output. Values: [pretty | json]. |
| `--short` | `` | bool | Shows only Compose's version number |

#### `docker compose volumes`

List volumes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--format` | `` | string | Format output using a custom template: |
| `--quiet` | `-q` | bool | Only display volume names |

#### `docker compose wait`

Block until containers of all (or specified) services stop.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--down-project` | `` | bool | Drops project when the first container stops |
| `--dry-run` | `` | bool | Execute command in dry run mode |

#### `docker compose watch`

Watch build context for service and rebuild/refresh containers when files are updated

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `` | bool | Execute command in dry run mode |
| `--no-up` | `` | bool | Do not build & start services before watching |
| `--prune` | `` | bool | Prune dangling images on rebuild (default true) (default: true) |
| `--quiet` | `` | bool | hide build output |

### `docker container`

Manage containers

```
docker container COMMAND
```

**Subcommands:**

#### `docker container attach`

Attach local standard input, output, and error streams to a running container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--no-stdin` | `` | bool | Do not attach STDIN |
| `--sig-proxy` | `` | bool | Proxy all received signals to the process |

#### `docker container commit`

Create a new image from a container's changes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--author` | `-a` | string | Author (e.g., "John Hannibal Smith |
| `--change` | `-c` | string | Apply Dockerfile instruction to the created image |
| `--message` | `-m` | string | Commit message |
| `--no-pause` | `` | bool | Disable pausing container during commit |

#### `docker container cp`

docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--archive` | `-a` | bool | Archive mode (copy all uid/gid information) |
| `--follow-link` | `-L` | bool | Always follow symbol link in SRC_PATH |
| `--quiet` | `-q` | bool | Suppress progress output during copy. Progress |

#### `docker container create`

Create a new container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--annotation` | `` | string | Add an annotation to the |
| `--attach` | `-a` | string | Attach to STDIN, STDOUT or STDERR |
| `--blkio-weight` | `` | string | Block IO (relative weight), |
| `--blkio-weight-device` | `` | string | Block IO weight (relative device |
| `--cap-add` | `` | string | Add Linux capabilities |
| `--cap-drop` | `` | string | Drop Linux capabilities |
| `--cgroup-parent` | `` | string | Optional parent cgroup for the |
| `--cgroupns` | `` | string | Cgroup namespace to use |
| `--cidfile` | `` | string | Write the container ID to the file |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution |
| `--device` | `` | string | Add a host device to the container |
| `--device-cgroup-rule` | `` | string | Add a rule to the cgroup allowed |
| `--device-read-bps` | `` | string | Limit read rate (bytes per |
| `--device-read-iops` | `` | string | Limit read rate (IO per second) |
| `--device-write-bps` | `` | string | Limit write rate (bytes per |
| `--device-write-iops` | `` | string | Limit write rate (IO per second) |
| `--dns` | `` | string | Set custom DNS servers |
| `--dns-option` | `` | string | Set DNS options |
| `--dns-search` | `` | string | Set custom DNS search domains |
| `--domainname` | `` | string | Container NIS domain name |
| `--entrypoint` | `` | string | Overwrite the default ENTRYPOINT |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment |
| `--expose` | `` | string | Expose a port or a range of ports |
| `--gpus` | `` | string | GPU devices to add to the |
| `--group-add` | `` | string | Add additional groups to join |
| `--health-cmd` | `` | string | Command to run to check health |
| `--health-interval` | `` | string | Time between running the check |
| `--health-retries` | `` | string | Consecutive failures needed to |
| `--health-start-interval` | `` | string | Time between running the check |
| `--health-start-period` | `` | string | Start period for the container |
| `--health-timeout` | `` | string | Maximum time to allow one check |
| `--help` | `` | bool | Print usage |
| `--hostname` | `-h` | string | Container host name |
| `--init` | `` | bool | Run an init inside the container |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--ip` | `` | string | IPv4 address (e.g., 172.30.100.104) |
| `--ip6` | `` | string | IPv6 address (e.g., 2001:db8::33) |
| `--ipc` | `` | string | IPC mode to use |
| `--isolation` | `` | string | Container isolation technology |
| `--label` | `-l` | string | Set meta data on a container |
| `--label-file` | `` | string | Read in a line delimited file of |
| `--link` | `` | string | Add link to another container |
| `--link-local-ip` | `` | string | Container IPv4/IPv6 link-local |
| `--log-driver` | `` | string | Logging driver for the container |
| `--log-opt` | `` | string | Log driver options |
| `--mac-address` | `` | string | Container MAC address (e.g., |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus |
| `--memory-swappiness` | `` | string | Tune container memory swappiness |
| `--mount` | `` | string | Attach a filesystem mount to the |
| `--name` | `` | string | Assign a name to the container |
| `--network` | `` | string | Connect a container to a network |
| `--network-alias` | `` | string | Add network-scoped alias for the |
| `--no-healthcheck` | `` | bool | Disable any container-specified |
| `--oom-kill-disable` | `` | bool | Disable OOM Killer |
| `--oom-score-adj` | `` | string | Tune host's OOM preferences |
| `--pid` | `` | string | PID namespace to use |
| `--pids-limit` | `` | string | Tune container pids limit (set |
| `--platform` | `` | string | Set platform if server is |
| `--privileged` | `` | bool | Give extended privileges to this |
| `--publish` | `-p` | string | Publish a container's port(s) to |
| `--publish-all` | `-P` | bool | Publish all exposed ports to |
| `--pull` | `` | string | Pull image before creating |
| `--quiet` | `-q` | bool | Suppress the pull output |
| `--read-only` | `` | bool | Mount the container's root |
| `--restart` | `` | string | Restart policy to apply when a |
| `--rm` | `` | bool | Automatically remove the |
| `--runtime` | `` | string | Runtime to use for this container |
| `--security-opt` | `` | string | Security Options |
| `--shm-size` | `` | string | Size of /dev/shm |
| `--stop-signal` | `` | string | Signal to stop the container |
| `--stop-timeout` | `` | string | Timeout (in seconds) to stop a |
| `--storage-opt` | `` | string | Storage driver options for the |
| `--sysctl` | `` | string | Sysctl options (default map[]) (default: map[]) |
| `--tmpfs` | `` | string | Mount a tmpfs directory |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |
| `--use-api-socket` | `` | bool | Bind mount Docker API socket and |
| `--user` | `-u` | string | Username or UID (format: |
| `--userns` | `` | string | User namespace to use |
| `--uts` | `` | string | UTS namespace to use |
| `--volume` | `-v` | string | Bind mount a volume |
| `--volume-driver` | `` | string | Optional volume driver for the |
| `--volumes-from` | `` | string | Mount volumes from the specified |
| `--workdir` | `-w` | string | Working directory inside the |

#### `docker container diff`



#### `docker container exec`

Execute a command in a running container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--detach` | `-d` | bool | Detached mode: run command in the background |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment variables |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--privileged` | `` | bool | Give extended privileges to the command |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--user` | `-u` | string | Username or UID (format: |
| `--workdir` | `-w` | string | Working directory inside the container |

#### `docker container export`

Export a container's filesystem as a tar archive

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--output` | `-o` | string | Write to a file, instead of STDOUT |

#### `docker container inspect`

Display detailed information on one or more containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |
| `--size` | `-s` | string | Display total file sizes |

#### `docker container kill`

Kill one or more running containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |

#### `docker container logs`

Fetch the logs of a container

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--details` | `` | bool | Show extra details provided to logs |
| `--follow` | `-f` | bool | Follow log output |
| `--since` | `` | string | Show logs since timestamp (e.g. |
| `--tail` | `-n` | string | Number of lines to show from the end of the logs |
| `--timestamps` | `-t` | bool | Show timestamps |
| `--until` | `` | string | Show logs before a timestamp (e.g. |

#### `docker container ls`

List containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all containers (default shows just running) |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--last` | `-n` | string | Show n last created containers (includes all |
| `--latest` | `-l` | bool | Show the latest created container (includes all |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--quiet` | `-q` | bool | Only display container IDs |
| `--size` | `-s` | string | Display total file sizes |

#### `docker container pause`



#### `docker container port`



#### `docker container prune`

Remove all stopped containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `` | string | Provide filter values (e.g. "until=<timestamp>") |
| `--force` | `-f` | bool | Do not prompt for confirmation |

#### `docker container rename`



#### `docker container restart`

Restart one or more containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |
| `--timeout` | `-t` | string | Seconds to wait before killing the container |

#### `docker container rm`

Remove one or more containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the removal of a running container (uses SIGKILL) |
| `--link` | `-l` | bool | Remove the specified link |
| `--volumes` | `-v` | bool | Remove anonymous volumes associated with the container |

#### `docker container run`

Create and run a new container from an image

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--annotation` | `` | string | Add an annotation to the |
| `--attach` | `-a` | string | Attach to STDIN, STDOUT or STDERR |
| `--blkio-weight` | `` | string | Block IO (relative weight), |
| `--blkio-weight-device` | `` | string | Block IO weight (relative device |
| `--cap-add` | `` | string | Add Linux capabilities |
| `--cap-drop` | `` | string | Drop Linux capabilities |
| `--cgroup-parent` | `` | string | Optional parent cgroup for the |
| `--cgroupns` | `` | string | Cgroup namespace to use |
| `--cidfile` | `` | string | Write the container ID to the file |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution |
| `--detach` | `-d` | bool | Run container in background and |
| `--detach-keys` | `` | string | Override the key sequence for |
| `--device` | `` | string | Add a host device to the container |
| `--device-cgroup-rule` | `` | string | Add a rule to the cgroup allowed |
| `--device-read-bps` | `` | string | Limit read rate (bytes per |
| `--device-read-iops` | `` | string | Limit read rate (IO per second) |
| `--device-write-bps` | `` | string | Limit write rate (bytes per |
| `--device-write-iops` | `` | string | Limit write rate (IO per second) |
| `--dns` | `` | string | Set custom DNS servers |
| `--dns-option` | `` | string | Set DNS options |
| `--dns-search` | `` | string | Set custom DNS search domains |
| `--domainname` | `` | string | Container NIS domain name |
| `--entrypoint` | `` | string | Overwrite the default ENTRYPOINT |
| `--env` | `-e` | string | Set environment variables |
| `--env-file` | `` | string | Read in a file of environment |
| `--expose` | `` | string | Expose a port or a range of ports |
| `--gpus` | `` | string | GPU devices to add to the |
| `--group-add` | `` | string | Add additional groups to join |
| `--health-cmd` | `` | string | Command to run to check health |
| `--health-interval` | `` | string | Time between running the check |
| `--health-retries` | `` | string | Consecutive failures needed to |
| `--health-start-interval` | `` | string | Time between running the check |
| `--health-start-period` | `` | string | Start period for the container |
| `--health-timeout` | `` | string | Maximum time to allow one check |
| `--help` | `` | bool | Print usage |
| `--hostname` | `-h` | string | Container host name |
| `--init` | `` | bool | Run an init inside the container |
| `--interactive` | `-i` | bool | Keep STDIN open even if not attached |
| `--ip` | `` | string | IPv4 address (e.g., 172.30.100.104) |
| `--ip6` | `` | string | IPv6 address (e.g., 2001:db8::33) |
| `--ipc` | `` | string | IPC mode to use |
| `--isolation` | `` | string | Container isolation technology |
| `--label` | `-l` | string | Set meta data on a container |
| `--label-file` | `` | string | Read in a line delimited file of |
| `--link` | `` | string | Add link to another container |
| `--link-local-ip` | `` | string | Container IPv4/IPv6 link-local |
| `--log-driver` | `` | string | Logging driver for the container |
| `--log-opt` | `` | string | Log driver options |
| `--mac-address` | `` | string | Container MAC address (e.g., |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus |
| `--memory-swappiness` | `` | string | Tune container memory swappiness |
| `--mount` | `` | string | Attach a filesystem mount to the |
| `--name` | `` | string | Assign a name to the container |
| `--network` | `` | string | Connect a container to a network |
| `--network-alias` | `` | string | Add network-scoped alias for the |
| `--no-healthcheck` | `` | bool | Disable any container-specified |
| `--oom-kill-disable` | `` | bool | Disable OOM Killer |
| `--oom-score-adj` | `` | string | Tune host's OOM preferences |
| `--pid` | `` | string | PID namespace to use |
| `--pids-limit` | `` | string | Tune container pids limit (set |
| `--platform` | `` | string | Set platform if server is |
| `--privileged` | `` | bool | Give extended privileges to this |
| `--publish` | `-p` | string | Publish a container's port(s) to |
| `--publish-all` | `-P` | bool | Publish all exposed ports to |
| `--pull` | `` | string | Pull image before running |
| `--quiet` | `-q` | bool | Suppress the pull output |
| `--read-only` | `` | bool | Mount the container's root |
| `--restart` | `` | string | Restart policy to apply when a |
| `--rm` | `` | bool | Automatically remove the |
| `--runtime` | `` | string | Runtime to use for this container |
| `--security-opt` | `` | string | Security Options |
| `--shm-size` | `` | string | Size of /dev/shm |
| `--sig-proxy` | `` | bool | Proxy received signals to the |
| `--stop-signal` | `` | string | Signal to stop the container |
| `--stop-timeout` | `` | string | Timeout (in seconds) to stop a |
| `--storage-opt` | `` | string | Storage driver options for the |
| `--sysctl` | `` | string | Sysctl options (default map[]) (default: map[]) |
| `--tmpfs` | `` | string | Mount a tmpfs directory |
| `--tty` | `-t` | bool | Allocate a pseudo-TTY |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |
| `--use-api-socket` | `` | bool | Bind mount Docker API socket and |
| `--user` | `-u` | string | Username or UID (format: |
| `--userns` | `` | string | User namespace to use |
| `--uts` | `` | string | UTS namespace to use |
| `--volume` | `-v` | string | Bind mount a volume |
| `--volume-driver` | `` | string | Optional volume driver for the |
| `--volumes-from` | `` | string | Mount volumes from the specified |
| `--workdir` | `-w` | string | Working directory inside the |

#### `docker container start`

Start one or more stopped containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--attach` | `-a` | bool | Attach STDOUT/STDERR and forward signals |
| `--detach-keys` | `` | string | Override the key sequence for detaching a |
| `--interactive` | `-i` | bool | Attach container's STDIN |

#### `docker container stats`

Display a live stream of container(s) resource usage statistics

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all containers (default shows just running) |
| `--format` | `` | string | Format output using a custom template: |
| `--no-stream` | `` | bool | Disable streaming stats and only pull the first result |
| `--no-trunc` | `` | bool | Do not truncate output |

#### `docker container stop`

Stop one or more running containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--signal` | `-s` | string | Signal to send to the container |
| `--timeout` | `-t` | string | Seconds to wait before killing the container |

#### `docker container top`

Display the running processes of a container

#### `docker container unpause`



#### `docker container update`

Update configuration of one or more containers

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--blkio-weight` | `` | string | Block IO (relative weight), between 10 |
| `--cpu-period` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-quota` | `` | string | Limit CPU CFS (Completely Fair |
| `--cpu-rt-period` | `` | string | Limit the CPU real-time period in |
| `--cpu-rt-runtime` | `` | string | Limit the CPU real-time runtime in |
| `--cpu-shares` | `-c` | string | CPU shares (relative weight) |
| `--cpus` | `` | string | Number of CPUs |
| `--cpuset-cpus` | `` | string | CPUs in which to allow execution (0-3, 0,1) |
| `--cpuset-mems` | `` | string | MEMs in which to allow execution (0-3, 0,1) |
| `--memory` | `-m` | string | Memory limit |
| `--memory-reservation` | `` | string | Memory soft limit |
| `--memory-swap` | `` | string | Swap limit equal to memory plus swap: |
| `--pids-limit` | `` | string | Tune container pids limit (set -1 for |
| `--restart` | `` | string | Restart policy to apply when a |

#### `docker container wait`



### `docker context`

Manage contexts

```
docker context COMMAND
```

**Subcommands:**

#### `docker context create`

Create a context

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--description` | `` | string | Description of the context |
| `--docker` | `` | string | set the docker endpoint (default []) (default: []) |
| `--from` | `` | string | create context from a named context |

#### `docker context export`

Export a context to a tar archive FILE or a tar stream on STDOUT.

#### `docker context import`



#### `docker context inspect`

Display detailed information on one or more contexts

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

#### `docker context ls`

List contexts

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Format output using a custom template: |
| `--quiet` | `-q` | bool | Only show context names |

#### `docker context rm`

Remove one or more contexts

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the removal of a context in use |

#### `docker context show`



#### `docker context update`

Update a context

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--description` | `` | string | Description of the context |
| `--docker` | `` | string | set the docker endpoint (default []) (default: []) |

### `docker image`

Manage images

```
docker image COMMAND
```

**Subcommands:**

#### `docker image build`

Start a build

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--add-host` | `` | string | Add a custom host-to-IP mapping |
| `--allow` | `` | string | Allow extra privileged entitlement |
| `--annotation` | `` | string | Add annotation to the image |
| `--attest` | `` | string | Attestation parameters (format: |
| `--build-arg` | `` | string | Set build-time variables |
| `--build-context` | `` | string | Additional build contexts (e.g., |
| `--builder` | `` | string | Override the configured builder |
| `--cache-from` | `` | string | External cache sources (e.g., |
| `--cache-to` | `` | string | Cache export destinations (e.g., |
| `--call` | `` | string | Set method for evaluating build |
| `--cgroup-parent` | `` | string | Set the parent cgroup for the "RUN" |
| `--check` | `` | bool | Shorthand for "--call=check" |
| `--debug` | `-D` | bool | Enable debug logging |
| `--file` | `-f` | string | Name of the Dockerfile (default: |
| `--iidfile` | `` | string | Write the image ID to a file |
| `--label` | `` | string | Set metadata for an image |
| `--load` | `` | bool | Shorthand for "--output=type=docker" |
| `--metadata-file` | `` | string | Write build result metadata to a file |
| `--network` | `` | string | Set the networking mode for the |
| `--no-cache` | `` | bool | Do not use cache when building the image |
| `--no-cache-filter` | `` | string | Do not cache specified stages |
| `--output` | `-o` | string | Output destination (format: |
| `--platform` | `` | string | Set target platform for build |
| `--policy` | `` | string | Policy configuration (format: |
| `--progress` | `` | string | Set type of progress output |
| `--provenance` | `` | string | Shorthand for "--attest=type=provenance" |
| `--pull` | `` | bool | Always attempt to pull all |
| `--push` | `` | bool | Shorthand for |
| `--quiet` | `-q` | bool | Suppress the build output and print |
| `--sbom` | `` | string | Shorthand for "--attest=type=sbom" |
| `--secret` | `` | string | Secret to expose to the build |
| `--shm-size` | `` | string | Shared memory size for build containers |
| `--ssh` | `` | string | SSH agent socket or keys to expose |
| `--tag` | `-t` | string | Image identifier (format: |
| `--target` | `` | string | Set the target build stage to build |
| `--ulimit` | `` | string | Ulimit options (default []) (default: []) |

#### `docker image history`

Show the history of an image

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Format output using a custom template: |
| `--human` | `-H` | bool | Print sizes and dates in human readable format |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--platform` | `` | string | Show history for the given platform. Formatted |
| `--quiet` | `-q` | bool | Only show image IDs |

#### `docker image import`

Import the contents from a tarball to create a filesystem image

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--change` | `-c` | string | Apply Dockerfile instruction to the created image |
| `--message` | `-m` | string | Set commit message for imported image |
| `--platform` | `` | string | Set platform if server is multi-platform capable |

#### `docker image inspect`

Display detailed information on one or more images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |
| `--platform` | `` | string | Inspect a specific platform of the |

#### `docker image load`

Load an image from a tar archive or STDIN

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--input` | `-i` | string | Read from tar archive file, instead of STDIN |
| `--platform` | `` | string | Load only the given platform(s). Formatted as |
| `--quiet` | `-q` | bool | Suppress the load output |

#### `docker image ls`

List images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Show all images (default hides intermediate and |
| `--digests` | `` | bool | Show digests |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--quiet` | `-q` | bool | Only show image IDs |
| `--tree` | `` | bool | List multi-platform images as a tree (EXPERIMENTAL) |

#### `docker image prune`

Remove unused images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Remove all unused images, not just dangling ones |
| `--filter` | `` | string | Provide filter values (e.g. "until=<timestamp>") |
| `--force` | `-f` | bool | Do not prompt for confirmation |

#### `docker image pull`

Download an image from a registry

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-tags` | `-a` | bool | Download all tagged images in the repository |
| `--platform` | `` | string | Set platform if server is multi-platform capable |
| `--quiet` | `-q` | bool | Suppress verbose output |

#### `docker image push`

Upload an image to a registry

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-tags` | `-a` | bool | Push all tags of an image to the repository |
| `--platform` | `` | string | Push a platform-specific manifest as a |
| `--quiet` | `-q` | bool | Suppress verbose output |

#### `docker image rm`

Remove one or more images

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force removal of the image |
| `--no-prune` | `` | bool | Do not delete untagged parents |
| `--platform` | `` | string | Remove only the given platform variant. |

#### `docker image save`

Save one or more images to a tar archive (streamed to STDOUT by default)

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--output` | `-o` | string | Write to a file, instead of STDOUT |
| `--platform` | `` | string | Save only the given platform(s). Formatted as |

#### `docker image tag`



### `docker manifest`

The **docker manifest** command has subcommands for managing image manifests and

```
docker manifest COMMAND
```

**Subcommands:**

#### `docker manifest annotate`

Add additional information to a local image manifest

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--arch` | `` | string | Set architecture |
| `--os` | `` | string | Set operating system |
| `--os-features` | `` | string | Set operating system feature |
| `--os-version` | `` | string | Set operating system version |
| `--variant` | `` | string | Set architecture variant |

#### `docker manifest create`

Create a local manifest list for annotating and pushing to a registry

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--amend` | `-a` | bool | Amend an existing manifest list |
| `--insecure` | `` | bool | Allow communication with an insecure registry |

#### `docker manifest inspect`

Display an image manifest, or manifest list

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--insecure` | `` | bool | Allow communication with an insecure registry |
| `--verbose` | `-v` | bool | Output additional info including layers and platform |

#### `docker manifest push`

Push a manifest list to a repository

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--insecure` | `` | bool | Allow push to an insecure registry |
| `--purge` | `-p` | bool | Remove the local manifest list after push |

#### `docker manifest rm`



### `docker mcp`

Docker MCP Toolkit's CLI - Manage your MCP servers and clients.

```
docker mcp [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--version` | `-v` | bool | Print version information and quit |

**Subcommands:**

#### `docker mcp catalog`

Manage MCP server catalogs

##### `docker mcp catalog add`

Add a server to a catalog

##### `docker mcp catalog bootstrap`



##### `docker mcp catalog create`



##### `docker mcp catalog export`



##### `docker mcp catalog fork`



##### `docker mcp catalog import`

Import a catalog from URL or file

##### `docker mcp catalog init`



##### `docker mcp catalog ls`

List all configured catalogs

##### `docker mcp catalog reset`



##### `docker mcp catalog rm`



##### `docker mcp catalog show`

Display catalog contents

##### `docker mcp catalog update`



#### `docker mcp client`

Manage MCP clients

##### `docker mcp client connect`

Connect the Docker MCP Toolkit to a client. Supported clients: claude-code claude-desktop cline codex continue cursor gemini goose gordon kiro lmstudio opencode sema4 vscode zed

##### `docker mcp client disconnect`

Disconnect the Docker MCP Toolkit from a client. Supported clients: claude-code claude-desktop cline codex continue cursor gemini goose gordon kiro lmstudio opencode sema4 vscode zed

##### `docker mcp client ls`

List client configurations

#### `docker mcp config`

Manage the configuration

##### `docker mcp config read`



##### `docker mcp config reset`



##### `docker mcp config write`



#### `docker mcp feature`

Manage experimental features

##### `docker mcp feature disable`



##### `docker mcp feature enable`



##### `docker mcp feature ls`



#### `docker mcp gateway`

Manage the MCP Server gateway

##### `docker mcp gateway run`

Run the gateway

#### `docker mcp policy`

Manage secret policies

##### `docker mcp policy dump`



##### `docker mcp policy set`



#### `docker mcp secret`

Manage secrets

##### `docker mcp secret ls`

List all secret names in Docker Desktop's secret store

##### `docker mcp secret rm`

Remove secrets from Docker Desktop's secret store

##### `docker mcp secret set`

Set a secret in Docker Desktop's secret store

#### `docker mcp server`

Manage servers

##### `docker mcp server disable`



##### `docker mcp server enable`



##### `docker mcp server init`

Initialize a new MCP server project

##### `docker mcp server inspect`



##### `docker mcp server ls`

List enabled servers

##### `docker mcp server reset`



#### `docker mcp tools`

Manage tools

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Output format (json|list) (default "list") (default: list) |
| `--gateway-arg` | `` | string | Additional arguments passed to the gateway |
| `--verbose` | `` | bool | Verbose output |
| `--version` | `` | string | Version of the gateway (default "2") (default: 2) |

##### `docker mcp tools call`



##### `docker mcp tools count`



##### `docker mcp tools disable`

disable one or more tools

##### `docker mcp tools enable`

enable one or more tools

##### `docker mcp tools inspect`



##### `docker mcp tools ls`



#### `docker mcp version`



### `docker network`

Manage networks

```
docker network COMMAND
```

**Subcommands:**

#### `docker network connect`

Connect a container to a network

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--alias` | `` | string | Add network-scoped alias for the container |
| `--driver-opt` | `` | string | driver options for the network |
| `--gw-priority` | `` | string | Highest gw-priority provides the default |
| `--ip` | `` | string | IPv4 address (e.g., "172.30.100.104") |
| `--ip6` | `` | string | IPv6 address (e.g., "2001:db8::33") |
| `--link` | `` | string | Add link to another container |
| `--link-local-ip` | `` | string | Add a link-local address for the |

#### `docker network create`

Create a network

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--attachable` | `` | bool | Enable manual container attachment |
| `--aux-address` | `` | string | Auxiliary IPv4 or IPv6 addresses used by |
| `--config-from` | `` | string | The network from which to copy the configuration |
| `--config-only` | `` | bool | Create a configuration only network |
| `--driver` | `-d` | string | Driver to manage the Network (default "bridge") (default: bridge) |
| `--gateway` | `` | string | IPv4 or IPv6 Gateway for the master subnet |
| `--ingress` | `` | bool | Create swarm routing-mesh network |
| `--internal` | `` | bool | Restrict external access to the network |
| `--ip-range` | `` | string | Allocate container ip from a sub-range |
| `--ipam-driver` | `` | string | IP Address Management Driver (default "default") (default: default) |
| `--ipam-opt` | `` | string | Set IPAM driver specific options (default map[]) (default: map[]) |
| `--ipv4` | `` | bool | Enable or disable IPv4 address assignment |
| `--ipv6` | `` | bool | Enable or disable IPv6 address assignment |
| `--label` | `` | string | Set metadata on a network |
| `--opt` | `-o` | string | Set driver specific options (default map[]) (default: map[]) |
| `--scope` | `` | string | Control the network's scope |
| `--subnet` | `` | string | Subnet in CIDR format that represents a |

#### `docker network disconnect`

Disconnect a container from a network

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the container to disconnect from a network |

#### `docker network inspect`

Display detailed information on one or more networks

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |
| `--verbose` | `-v` | bool | Verbose output for diagnostics |

#### `docker network ls`

List networks

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Provide filter values (e.g. "driver=bridge") |
| `--format` | `` | string | Format output using a custom template: |
| `--no-trunc` | `` | bool | Do not truncate the output |
| `--quiet` | `-q` | bool | Only display network IDs |

#### `docker network prune`

Remove all unused networks

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `` | string | Provide filter values (e.g. "until=<timestamp>") |
| `--force` | `-f` | bool | Do not prompt for confirmation |

#### `docker network rm`

Remove one or more networks

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Do not error if the network does not exist |

### `docker plugin`

Manage plugins

```
docker plugin COMMAND
```

**Subcommands:**

#### `docker plugin create`

Create a plugin from a rootfs and configuration. Plugin data directory must contain config.json and rootfs directory.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--compress` | `` | bool | Compress the context using gzip |

#### `docker plugin disable`

Disable a plugin

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the disable of an active plugin |

#### `docker plugin enable`

Enable a plugin

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--timeout` | `` | string | HTTP client timeout (in seconds) (default 30) (default: 30) |

#### `docker plugin inspect`

Display detailed information on one or more plugins

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

#### `docker plugin install`

Install a plugin

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--alias` | `` | string | Local name for plugin |
| `--disable` | `` | bool | Do not enable the plugin on install |
| `--grant-all-permissions` | `` | bool | Grant all permissions necessary to run |

#### `docker plugin ls`

List plugins

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Provide filter values (e.g. "enabled=true") |
| `--format` | `` | string | Format output using a custom template: |
| `--no-trunc` | `` | bool | Don't truncate output |
| `--quiet` | `-q` | bool | Only display plugin IDs |

#### `docker plugin push`

Push a plugin to a registry

#### `docker plugin rm`

Remove one or more plugins

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the removal of an active plugin |

#### `docker plugin set`



#### `docker plugin upgrade`

Upgrade an existing plugin

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--grant-all-permissions` | `` | bool | Grant all permissions necessary to run |
| `--skip-remote-check` | `` | bool | Do not check if specified remote plugin |

### `docker swarm`

Manage Swarm

```
docker swarm COMMAND
```

**Subcommands:**

#### `docker swarm init`

Initialize a swarm

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--advertise-addr` | `` | string | Advertised address |
| `--autolock` | `` | bool | Enable manager autolocking |
| `--availability` | `` | string | Availability of the node |
| `--cert-expiry` | `` | string | Validity period for node |
| `--data-path-addr` | `` | string | Address or interface to |
| `--data-path-port` | `` | string | Port number to use for |
| `--default-addr-pool` | `` | string | default address pool in |
| `--default-addr-pool-mask-length` | `` | string | default address pool |
| `--dispatcher-heartbeat` | `` | string | Dispatcher heartbeat |
| `--external-ca` | `` | string | Specifications of one or |
| `--force-new-cluster` | `` | bool | Force create a new cluster |
| `--listen-addr` | `` | string | Listen address (format: |
| `--max-snapshots` | `` | string | Number of additional Raft |
| `--snapshot-interval` | `` | string | Number of log entries |
| `--task-history-limit` | `` | string | Task history retention |

#### `docker swarm join`

Join a swarm as a node and/or manager

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--advertise-addr` | `` | string | Advertised address (format: |
| `--availability` | `` | string | Availability of the node ("active", |
| `--data-path-addr` | `` | string | Address or interface to use for data path |
| `--listen-addr` | `` | string | Listen address (format: |
| `--token` | `` | string | Token for entry into the swarm |

### `docker system`

Manage Docker

```
docker system COMMAND
```

**Subcommands:**

#### `docker system df`

Show docker disk usage

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `` | string | Format output using a custom template: |
| `--verbose` | `-v` | bool | Show detailed information on space usage |

#### `docker system events`

Get real time events from the server

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Filter output based on conditions provided |
| `--format` | `` | string | Format output using a custom template: |
| `--since` | `` | string | Show all events created since timestamp |
| `--until` | `` | string | Stream events until this timestamp |

#### `docker system info`

Display system-wide information

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

#### `docker system prune`

Remove unused data

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Remove all unused images not just dangling ones |
| `--filter` | `` | string | Provide filter values (e.g. "label=<key>=<value>") |
| `--force` | `-f` | bool | Do not prompt for confirmation |
| `--volumes` | `` | bool | Prune anonymous volumes |

### `docker volume`

Manage volumes

```
docker volume COMMAND
```

**Subcommands:**

#### `docker volume create`

Create a volume

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--driver` | `-d` | string | Specify volume driver name (default "local") (default: local) |
| `--label` | `` | string | Set metadata for a volume |
| `--opt` | `-o` | string | Set driver specific options (default map[]) (default: map[]) |

#### `docker volume inspect`

Display detailed information on one or more volumes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--format` | `-f` | string | Format output using a custom template: |

#### `docker volume ls`

List volumes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--filter` | `-f` | string | Provide filter values (e.g. "dangling=true") |
| `--format` | `` | string | Format output using a custom template: |
| `--quiet` | `-q` | bool | Only display volume names |

#### `docker volume prune`

Remove unused local volumes

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | bool | Remove all unused volumes, not just anonymous ones |
| `--filter` | `` | string | Provide filter values (e.g. "label=<label>") |
| `--force` | `-f` | bool | Do not prompt for confirmation |

#### `docker volume rm`

Remove one or more volumes. You cannot remove a volume that is in use by a container.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--force` | `-f` | bool | Force the removal of one or more volumes |

