# langchain -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |
| `--version` | `-v` | bool | Print the current CLI version. |

## Command Groups

### `langchain app`

Manage LangChain apps.

```
langchain app [OPTIONS] COMMAND [ARGS]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |

**Subcommands:**

#### `langchain app add`

Add the specified template to the current LangServe app.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--api-path` | `` | string | API paths to add |
| `--branch` | `` | string | Install templates from a specific branch |
| `--help` | `` | bool | Show this message and exit. |
| `--project-dir` | `` | string | The project directory |
| `--repo` | `` | string | Install templates from a specific github repo instead |

#### `langchain app new`

Create a new LangServe application.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |
| `--non-interactive` | `` | bool | Don't prompt for any input [default: interactive] |
| `--package` | `` | string | Packages to seed the project with |
| `--pip` | `` | bool | Pip install the template(s) as editable dependencies |

#### `langchain app remove`

Remove the specified package from the current LangServe app.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |
| `--project-dir` | `` | string | The project directory |

#### `langchain app serve`

Start the LangServe app.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--app` | `` | string | The app to run, e.g. `app.server:app` |
| `--help` | `` | bool | Show this message and exit. |
| `--host` | `` | string | The host to run the server on |
| `--port` | `` | string | The port to run the server on |

### `langchain integration`

Develop integration packages for LangChain.

```
langchain integration [OPTIONS] COMMAND [ARGS]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |

**Subcommands:**

#### `langchain integration create-doc`

Create a new integration doc.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--component-type` | `` | string | The type of component. Currently supported: `ChatModel`, `DocumentLoader`, `Tool`, `VectorStore`, `Embeddings`, `ByteStore`, `LLM`, `Provider`, `Toolkit`, `Retriever`. [default: ChatModel] (default: ChatModel) |
| `--destination-dir` | `` | string | The relative path to the docs directory to place the new file in. [default: docs/docs/integrations/chat/] (default: docs/docs/integrations/chat/) |
| `--help` | `` | bool | Show this message and exit. |
| `--name-class` | `` | string | The PascalCase name of the integration (e.g. `OpenAI`, `VertexAI`). Do not include a 'Chat', 'VectorStore', etc. prefix/suffix. |

#### `langchain integration new`

Create a new integration package.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dst` | `` | string | The relative path to the integration package to place the new file in. e.g. `my-integration/my_integration.py` |
| `--help` | `` | bool | Show this message and exit. |
| `--name-class` | `` | string | The name of the integration in PascalCase. e.g. `MyIntegration`. This is used to name classes like `MyIntegrationVectorStore` |
| `--src` | `` | string | The name of the single template file to copy. e.g. `--src integration_template/chat_models.py --dst my_integration/chat_models.py`. Can be used multiple times. |

### `langchain template`

Develop installable templates.

```
langchain template [OPTIONS] COMMAND [ARGS]...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |

**Subcommands:**

#### `langchain template list`

List all or search for available templates.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |

#### `langchain template new`

Create a new template package.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |
| `--with-poetry` | `` | bool | Don't run poetry install [default: no-poetry] |

#### `langchain template serve`

Start a demo app for this template.

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--chat-playground` | `` | bool | Whether to include a chat playground route [default: no-chat-playground] |
| `--configurable` | `` | bool | Whether to include a configurable route |
| `--help` | `` | bool | Show this message and exit. |
| `--host` | `` | string | The host to run the server on |
| `--port` | `` | string | The port to run the server on |

## Commands

### `langchain migrate`

Migrate langchain to the most recent version.

```
langchain migrate [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--diff` | `` | bool | Show the changes that would be made without applying them. |
| `--help` | `` | bool | Show this message and exit. |
| `--interactive` | `` | bool | Prompt for confirmation before making each change |

### `langchain serve`

Start the LangServe app, whether it's a template or an app.

```
langchain serve [OPTIONS]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--help` | `` | bool | Show this message and exit. |
| `--host` | `` | string | The host to run the server on |
| `--port` | `` | string | The port to run the server on |

