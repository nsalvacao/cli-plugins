# docker -- Usage Examples

### `docker mcp catalog add`

```bash
docker mcp catalog add my-catalog github-server ./github-catalog.yaml
```
docker mcp catalog add my-catalog slack-bot ./team-catalog.yaml --force

### `docker mcp catalog create`

```bash
docker mcp catalog create dev-servers
```
docker mcp catalog create prod-monitoring

### `docker mcp catalog fork`

```bash
docker mcp catalog fork docker-mcp my-custom-docker
```
docker mcp catalog fork team-servers my-servers

### `docker mcp catalog import`

```bash
docker mcp catalog import https://example.com/my-catalog.yaml
```
docker mcp catalog import ./shared-catalog.yaml

### `docker mcp catalog ls`

```bash
docker mcp catalog ls
```
docker mcp catalog ls --format=json

### `docker mcp catalog show`

```bash
docker mcp catalog show
```
docker mcp catalog show my-catalog --format=json

### `docker mcp catalog update`

```bash
docker mcp catalog update
```
docker mcp catalog update team-servers

