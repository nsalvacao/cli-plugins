# Data Model: CLI Plugins Core Project

**Branch**: `001-cli-plugins-base` | **Date**: 2026-02-12 | **Spec**: [specs/001-cli-plugins-base/spec.md](specs/001-cli-plugins-base/spec.md)
**Input**: Key Entities from `/specs/001-cli-plugins-base/spec.md`

## Summary of Data Model

Este modelo de dados descreve as entidades centrais do projeto `cli-plugins`, que são fundamentais para representar o conhecimento de CLIs de forma estruturada e gerar plugins para assistentes de IA.

## Entities

### 1. CLI (Command Line Interface)
- **Descrição**: A ferramenta de linha de comando a ser rastreada.
- **Atributos**:
    - `name` (string): Nome da CLI (e.g., `docker`, `git`, `uv`).
    - `version` (string): Versão da CLI.
    - `help_patterns` (array of string): Padrões ou formatos de saída `--help` esperados.
    - `command_hierarchy` (reference to Command tree): Estrutura hierárquica de comandos.

### 2. CLIMap
- **Descrição**: A representação JSON estruturada e machine-readable do conhecimento de uma CLI. Este é o ativo estratégico do projeto.
- **Atributos**:
    - `cli_name` (string): Nome da CLI a que este CLIMap se refere.
    - `cli_version` (string): Versão da CLI.
    - `metadata` (object): Metadados adicionais (e.g., autor do plugin, data de geração).
    - `global_flags` (array of Flag): Flags globais aplicáveis a todos os comandos da CLI.
    - `environment_variables` (array of object): Variáveis de ambiente que a CLI consome.
    - `commands` (array of Command): Uma árvore ou lista hierárquica de comandos disponíveis na CLI.
    - `confidence_score` (float): Score de confiança global do parsing.

### 3. Command
- **Descrição**: Um comando específico dentro de uma CLI.
- **Atributos**:
    - `path` (string): Caminho completo do comando (e.g., `docker run`, `git commit`).
    - `name` (string): Nome do comando (e.g., `run`, `commit`).
    - `description` (string): Descrição do comando.
    - `usage` (string): Exemplo de uso do comando.
    - `aliases` (array of string): Nomes alternativos para o comando.
    - `flags` (array of Flag): Flags específicas para este comando.
    - `positional_arguments` (array of object): Argumentos posicionais.
    - `environment_variables` (array of object): Variáveis de ambiente específicas do comando.
    - `subcommands` (array of Command): Subcomandos aninhados, formando uma árvore de comandos.

### 4. Flag
- **Descrição**: Uma opção ou argumento para um comando.
- **Atributos**:
    - `name` (string): Nome da flag (e.g., `--help`, `-v`, `--config`).
    - `long_name` (string, optional): Nome longo da flag (e.g., `--version`).
    - `short_name` (string, optional): Nome curto da flag (e.g., `-v`).
    - `type` (string): Tipo do valor da flag (e.g., `bool`, `string`, `int`, `enum`).
    - `description` (string): Descrição da flag.
    - `default_value` (string, optional): Valor padrão, se houver.
    - `required` (boolean): Indica se a flag é obrigatória.
    - `choices` (array of string, optional): Opções de valores permitidos para a flag.
    - `confidence_score` (float): Score de confiança da extração desta flag.

### 5. Plugin (AI Agent Plugin)
- **Descrição**: O formato de output para um assistente de IA que consome o CLIMap.
- **Atributos**:
    - `agent_id` (string): Identificador do assistente de IA para o qual o plugin é gerado.
    - `format_version` (string): Versão do formato do plugin (específico do assistente de IA).
    - `generated_from_climap` (reference to CLIMap): Referência ao CLIMap de origem.
    - `exposed_commands` (array of object): Comandos e flags do CLIMap adaptados para a interface do assistente de IA.
    - `semantic_keywords` (array of string): Palavras-chave semanticamente relevantes para o plugin.

## Relationships

- Uma `CLI` possui um `CLIMap`.
- Um `CLIMap` contém uma coleção de `Command`s.
- Um `Command` pode ter `subcommands` e `flags`.
- Um `Flag` pertence a um `Command` ou é global ao `CLIMap`.
- Um `Plugin` é gerado a partir de um `CLIMap`.

## Validation Rules (derived from requirements)

- Todos os campos obrigatórios nas entidades `CLIMap`, `Command` e `Flag` devem estar presentes.
- `confidence_score` (em `CLIMap` e `Flag`) deve ser um float entre 0.0 e 1.0.
- Proteção contra injeção de comandos na execução de CLIs.
- O core do crawler e gerador não deve ter dependências externas.
- `cli_name` e `cli_version` no `CLIMap` devem corresponder aos da `CLI` de origem.

