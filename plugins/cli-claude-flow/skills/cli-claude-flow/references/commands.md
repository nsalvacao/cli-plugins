# claude-flow -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--config` | `-c` | string | Path to configuration file |
| `--format` | `-f` | bool | Output format (text, json, table) |
| `--help` | `-h` | bool | Show help information |
| `--interactive` | `-i` | bool | Enable interactive mode |
| `--no-color` | `` | bool | Disable colored output |
| `--quiet` | `-Q` | bool | Suppress non-essential output |
| `--verbose` | `-v` | bool | Enable verbose output |
| `--version` | `-V` | bool | Show version number |

## Commands

### `claude-flow agent`

Agent Management Commands

```
claude-flow agent <subcommand> [options]
```

### `claude-flow analyze`

Analyze Commands

### `claude-flow claims`

Claude Flow Claims System

### `claude-flow completions`

Shell Completions

### `claude-flow config`

Configuration Management

```
claude-flow config <subcommand> [options]
```

### `claude-flow daemon`

Worker Daemon - Background Task Management

### `claude-flow deployment`

Claude Flow Deployment

### `claude-flow doctor`

claude-flow doctor

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--component` | `-c` | bool | Check specific component (version, node, npm, config, daemon, memory, api, git, mcp, claude, disk, typescript) |
| `--fix` | `-f` | bool | Show fix commands for issues [default: false] (default: false) |
| `--install` | `-i` | bool | Auto-install missing dependencies (Claude Code CLI) [default: false] (default: false) |
| `--verbose` | `-v` | bool | Verbose output [default: false] (default: false) |

### `claude-flow embeddings`

Claude Flow Embeddings

### `claude-flow guidance`

Guidance Control Plane

### `claude-flow hive-mind`

Hive Mind - Consensus-Based Multi-Agent Coordination

```
claude-flow hive-mind <subcommand> [options]
```

### `claude-flow hooks`

Self-Learning Hooks System

```
claude-flow hooks <subcommand> [options]
```

### `claude-flow init`

Claude Flow appears to be already initialized

### `claude-flow issues`

Issue Claims (ADR-016)

### `claude-flow mcp`

MCP Server Management

```
claude-flow mcp <subcommand> [options]
```

### `claude-flow memory`

Memory Management Commands

```
claude-flow memory <subcommand> [options]
```

### `claude-flow migrate`

V2 to V3 Migration Tools

```
claude-flow migrate <subcommand> [options]
```

### `claude-flow neural`

Claude Flow Neural System

### `claude-flow performance`

Claude Flow Performance Suite

### `claude-flow plugins`

Claude Flow Plugin System

### `claude-flow progress`



### `claude-flow ruvector`

RuVector PostgreSQL Bridge

### `claude-flow security`

Claude Flow Security Suite

### `claude-flow session`

Session Management Commands

```
claude-flow session <subcommand> [options]
```

### `claude-flow start`

Starting Claude Flow V3

### `claude-flow status`



### `claude-flow swarm`

Swarm Coordination Commands

```
claude-flow swarm <subcommand> [options]
```

### `claude-flow task`

Task Management Commands

```
claude-flow task <subcommand> [options]
```

### `claude-flow update`

Update Command

### `claude-flow workflow`

Workflow Commands

```
claude-flow workflow <subcommand> [options]
```

## Command Groups

### `claude-flow process`

claude-flow process

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `-h` | bool | Show help for process command |

**Subcommands:**

#### `claude-flow process daemon`

Worker Daemon - Background Task Management

#### `claude-flow process logs`

View and manage process logs

#### `claude-flow process monitor`

Real-time process and resource monitoring

#### `claude-flow process signals`

Send signals to managed processes

#### `claude-flow process workers`

Manage background worker processes

### `claude-flow providers`

claude-flow providers

```
View provider usage and costs
```

**Subcommands:**

#### `claude-flow providers configure`

Configure provider settings and API keys

#### `claude-flow providers list`

List available AI providers and models

#### `claude-flow providers models`

List and manage available models

#### `claude-flow providers test`

Test provider connectivity and API access

#### `claude-flow providers usage`

View provider usage and costs

### `claude-flow route`

claude-flow route

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--agent` | `-a` | bool | Force specific agent |
| `--q-learning` | `-q` | bool | Use Q-Learning for agent selection [default: true] (default: true) |

**Subcommands:**

#### `claude-flow route coverage`

Route tasks based on test coverage analysis (ADR-017) (cov)

#### `claude-flow route export`

Export Q-table for persistence

#### `claude-flow route feedback`

Provide feedback on a routing decision

#### `claude-flow route import`

Import Q-table from file

#### `claude-flow route list-agents`

List all available agent types for routing (agents, ls)

#### `claude-flow route reset`

Reset the Q-Learning router state

#### `claude-flow route stats`

Show Q-Learning router statistics

#### `claude-flow route task`

Task Management Commands

