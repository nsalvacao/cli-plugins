# claude-flow -- Usage Examples

## `claude-flow doctor`

```bash
claude-flow doctor
```
Run full health check

```bash
claude-flow doctor --fix
```
Show fixes for issues

```bash
claude-flow doctor --install
```
Auto-install missing dependencies

```bash
claude-flow doctor -c version
```
Check for stale npx cache

```bash
claude-flow doctor -c claude
```
Check Claude Code CLI only

## `claude-flow process`

```bash
claude-flow process daemon --action start
```
Start daemon

```bash
claude-flow process monitor --watch
```
Watch processes

```bash
claude-flow process workers --action list
```
List workers

```bash
claude-flow process logs --follow
```
Follow logs

## `claude-flow providers`

```bash
claude-flow providers list
```
List all providers

```bash
claude-flow providers configure -p openai
```
Configure OpenAI

```bash
claude-flow providers test --all
```
Test all providers

## `claude-flow route`

```bash
claude-flow route "implement feature"
```
Route task to best agent

```bash
claude-flow route "write tests" --q-learning
```
Use Q-Learning routing

```bash
claude-flow route --agent coder "fix bug"
```
Force specific agent

```bash
claude-flow route list-agents
```
List available agents

```bash
claude-flow route stats
```
Show routing statistics

