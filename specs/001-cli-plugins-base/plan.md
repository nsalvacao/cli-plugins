# Implementation Plan: CLI Plugins Core Project

**Branch**: `001-cli-plugins-base` | **Date**: 2026-02-12 | **Spec**: [specs/001-cli-plugins-base/spec.md](specs/001-cli-plugins-base/spec.md)
**Input**: Feature specification from `/specs/001-cli-plugins-base/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

O projeto cli-plugins tem como objetivo ser o 'OpenAPI for CLIs', auto-gerando plugins estruturados para assistentes de IA a partir da saída `--help` de CLIs, fornecendo conhecimento preciso e atualizado sobre ferramentas de linha de comando. Inclui um crawler universal, um gerador de plugins multi-agente, e visa a criação de uma especificação OCS. O plano de implementação focará na construção de um crawler robusto, um gerador de CLIMap e plugins, garantindo segurança e testabilidade.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Standard library only (core crawler and generator)
**Storage**: Filesystem (for CLIMap JSON and generated plugins)
**Testing**: Pytest
**Target Platform**: Linux (WSL), macOS, Windows (for CLI execution and crawling)
**Project Type**: CLI Tool (single project: crawler, parser, generator)
**Performance Goals**:
- Crawler processa 50 CLIs (lotes de 10 em paralelo) e `--help` de até 10000 linhas, com tempo médio consistente com SC-004 (<30 segundos).
- Parsing de `--help` de 10000 linhas para CLIMap JSON em memória concluído em menos de 5 segundos.
**Constraints**:
- Proteção contra injeção de comandos e utilização de sandbox de execução (`subprocess.run` com argumentos tokenizados e sem `shell=True`).
- Core do crawler e gerador sem dependências externas (stdlib only).
- Geração de keywords semanticamente relevantes para plugins.
- Configuração do autor do plugin permitida.
**Scale/Scope**:
- Extração de 90% das flags e comandos principais de 20 CLIs populares com >95% de precisão no CLIMap JSON.
- Qualidade de parsing de flags e exemplos superior a 80% para Rich-Click e man page CLIs.
- Taxa de sucesso de crawling > 99%, Disponibilidade do serviço > 99.5% para atualização de plugins.
- O `cli-plugins` será apenas o produtor do CLIMap e não terá responsabilidade direta pelo desenvolvimento ou manutenção de um linter de design de CLI (projeto externo).
- Priorização: Precisão e segurança do parsing > Tempo de processamento inicial (dentro dos SCs) > Universalidade e economia de tokens.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Open CLI Specification (OCS)**: O CLIMap JSON deve ser a descrição padrão e machine-readable para interfaces CLI.
- [x] **Auto-Geração e Otimização para IA**: Todo o conhecimento da CLI deve ser auto-gerado e otimizado para consumo por agentes de IA.
- [x] **Universalidade e Multi-Agente**: A solução deve ser universal, funcionando com qualquer CLI e gerando output para múltiplos agentes de IA.
- [x] **Qualidade, Testabilidade e Confiança**: O sistema deve garantir a qualidade do output, ser testável e fornecer níveis de confiança.
- [x] **Foco no Ecossistema e Comunidade**: Promover um ecossistema auto-sustentável e impulsionado pela comunidade.
- [x] **Zero Dependencies (Core)**: O core do crawler e gerador deve ter zero dependências externas.
- [x] **Segurança Robusta**: Todas as operações de subprocessos devem ser realizadas de forma segura.
- [x] **Test-Driven Development (TDD)**: Seguir um ciclo `Red-Green-Refactor` rigoroso.
- [x] **Micro-Commits e Validação Contínua**: Fazer commits pequenos e frequentes.
- [x] **CI/CD Automatizado**: Manter um pipeline de CI/CD para automatizar testes.
- [x] **Spec-Driven Development**: Utilizar especificações como o driver primário para o desenvolvimento.

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-plugins-base/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── crawler/             # Lógica de crawling e parsing
│   ├── cli_crawler.py   # Ponto de entrada do crawler
│   ├── pipeline.py      # Orquestrador do pipeline de crawling
│   └── models.py        # Definição do schema CLIMap (Key Entity)
├── generator/           # Lógica de geração de plugins
│   └── plugin_generator.py
├── config/              # Ficheiros de configuração (config.yaml)
└── lib/                 # Utilitários partilhados (e.g., helpers de subprocessos seguros)

tests/
├── unit/                # Testes unitários para crawler, parser, generator
├── integration/         # Testes de integração (e.g., CLI real -> CLIMap)
└── end_to_end/          # Testes E2E (e.g., CLI real -> CLIMap -> Plugin -> AI Assistant)
```

**Structure Decision**: A estrutura `Single project (DEFAULT)` será utilizada, com a divisão lógica em `src/crawler`, `src/generator`, `src/config` e `src/lib` para modularidade e conformidade com o princípio de "Zero Dependencies (Core)" para o core. Os testes serão organizados em `tests/unit`, `tests/integration` e `tests/end_to_end` para garantir 100% de cobertura de testes.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
