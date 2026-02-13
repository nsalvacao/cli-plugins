# Quickstart Guide: CLI Plugins Core Project

**Branch**: `001-cli-plugins-base` | **Date**: 2026-02-12 | **Plan**: [specs/001-cli-plugins-base/plan.md](specs/001-cli-plugins-base/plan.md)
**Input**: `plan.md`, `spec.md`, `data-model.md`

## Summary

Este guia rápido oferece uma visão geral do setup inicial, execução e testes para o projeto `cli-plugins`. Ele assume que o ambiente Python 3.11+ está configurado.

## 1. Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga estes passos:

1.  **Criar e ativar um ambiente virtual (recomendado)**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Instalar dependências (apenas para desenvolvimento/testes)**:
    O core do crawler e gerador tem zero dependências externas. No entanto, para testes e linting (Pytest, Black, Flake8, Radon), você precisará instalar as dependências de desenvolvimento.
    ```bash
    pip install -e '.[dev]'
    ```

## 2. Estrutura do Projeto

O projeto segue a seguinte estrutura:

```text
cli-plugins/
├── src/
│   ├── crawler/             # Lógica de crawling e parsing (cli_crawler.py, pipeline.py, models.py)
│   ├── generator/           # Lógica de geração de plugins (plugin_generator.py)
│   ├── config/              # Ficheiros de configuração (config.yaml)
│   └── lib/                 # Utilitários partilhados (subprocess_utils.py, logger.py, observability.py)
│
├── tests/
│   ├── unit/                # Testes unitários
│   ├── integration/         # Testes de integração
│   ├── end_to_end/          # Testes E2E
│   └── performance/         # Testes de performance/benchmarking
│
├── .github/                 # Workflows de GitHub Actions (CI, CodeQL)
├── CODE_OF_CONDUCT.md       # Código de Conduta
├── docs/CONTRIBUTING.md     # Guia de Contribuição
├── pyproject.toml           # Configuração do projeto Python
├── config.yaml              # Configuração básica do projeto
├── .repo-audit-2026-02-12.md # Último relatório de auditoria do repositório
└── specs/001-cli-plugins-base/
    ├── plan.md
    ├── spec.md
    ├── research.md
    ├── data-model.md
    ├── contracts/
    └── tasks.md
```

## 3. Comandos Essenciais

### Construir e Instalar (apenas para desenvolvimento)

Como o core tem zero dependências, a instalação é principalmente para ferramentas de desenvolvimento.

```bash
# Instalar o projeto em modo editável com dependências de desenvolvimento
pip install -e '.[dev]'
```

### Testes

Execute todos os testes com `pytest`.

```bash
pytest
```

Para executar testes específicos:

```bash
pytest tests/unit/test_cli_crawler_basic.py
```

### Linting e Formatação

Execute as ferramentas de linting e formatação configuradas no `pyproject.toml` (e.g., Black, Ruff).

```bash
# Exemplo: Verificar formatação com Black
black --check src/ tests/

# Exemplo: Executar linting com Ruff
ruff check src/ tests/
```

### Executar o Crawler/Gerador (Exemplo)

Um exemplo de como invocar o crawler e gerador após a implementação. (Este comando será mais detalhado após a implementação inicial).

```bash
# Exemplo de uso (assumindo um CLI principal)
python3 src/cli_main.py crawl --cli docker --output-path output/docker_climap.json
python3 src/cli_main.py generate --climap-path output/docker_climap.json --output-plugin-path .claude/commands/docker.md
```

## 4. Workflows de CI/CD (GitHub Actions)

Os workflows de CI/CD estão configurados no diretório `.github/workflows/`:

-   `ci.yml`: Pipeline de CI para linting, formatação, testes e análise de complexidade de código.
-   `codeql-analysis.yml`: Análise de segurança contínua com CodeQL.

Monitorize a execução destes workflows no GitHub Actions para garantir a qualidade e segurança do código.

## 5. Contribuições

Consulte o `docs/CONTRIBUTING.md` para diretrizes detalhadas sobre como contribuir para o projeto.

## 6. Código de Conduta

Consulte o `CODE_OF_CONDUCT.md` para as expectativas de comportamento na comunidade.

