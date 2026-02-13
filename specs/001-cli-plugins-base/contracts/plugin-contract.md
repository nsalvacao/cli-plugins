# Plugin Contract: CLI Plugins Core Project

**Branch**: `001-cli-plugins-base` | **Date**: 2026-02-12 | **Spec**: [specs/001-cli-plugins-base/spec.md](specs/001-cli-plugins-base/spec.md)
**Input**: Functional Requirements from `/specs/001-cli-plugins-base/spec.md` and CLIMap schema from `/specs/001-cli-plugins-base/data-model.md`

## Summary of Plugin Contract

Este documento define o contrato para a geração de plugins para assistentes de IA a partir do CLIMap. Dada a natureza do projeto, o "contrato de API" não é uma interface REST/GraphQL tradicional para o `cli-plugins` em si, mas sim o formato e a interação dos plugins gerados com os assistentes de IA externos.

## Plugin Format and Structure

Os plugins serão gerados no formato YAML ou Markdown (`.claude/commands/*.md` e ficheiros associados) conforme a especificação do assistente de IA alvo (e.g., Claude Code, GitHub Copilot). A estrutura será uma transpilação otimizada do CLIMap JSON, focando na "progressive disclosure" para eficiência de tokens.

### Estrutura Base (Exemplo para Claude Code)

```yaml
name: "[CLI_NAME]"
description: "Plugin for [CLI_NAME] CLI. Generated from CLIMap."
version: "[CLI_VERSION]"
commands:
  - name: "[COMMAND_NAME]"
    description: "[COMMAND_DESCRIPTION]"
    usage: "[COMMAND_USAGE]"
    parameters:
      - name: "[FLAG_NAME]"
        type: "[FLAG_TYPE]"
        description: "[FLAG_DESCRIPTION]"
        required: [BOOLEAN]
        default: "[DEFAULT_VALUE]"
      # ... outros parâmetros (flags, argumentos posicionais)
    subcommands:
      # ... subcomandos aninhados
semantic_keywords:
  - "[KEYWORD1]"
  - "[KEYWORD2]"
# ... outros metadados do plugin
```

## Interaction Patterns with AI Assistants

Os plugins serão consumidos pelos assistentes de IA para fornecer conhecimento sobre CLIs. A interação primária será:

1.  **Consulta de Comandos/Flags**: O assistente de IA interpreta a pergunta do utilizador sobre uma CLI.
2.  **Uso do Plugin**: O assistente de IA invoca o plugin gerado, que expõe o conhecimento estruturado do CLIMap.
3.  **Progressive Disclosure**: Se o CLIMap for muito extenso, o plugin deve fornecer apenas a informação relevante para a consulta inicial, permitindo que o assistente de IA solicite mais detalhes conforme necessário para economizar tokens.
4.  **Geração de Comandos**: O assistente de IA usa a informação do plugin para construir e sugerir comandos precisos ao utilizador.

## Error Handling and Limitations (Integração com AI Assistants)

Conforme clarificado na especificação:

-   A abordagem para lidar com a integração e possíveis falhas/limitações de API ao gerar e interagir com plugins para múltiplos assistentes de IA externos será **deferida para uma fase posterior**. No entanto, a intenção é implementar adaptadores por assistente, com lógica de retry, circuit breaker e cache.
-   O sistema `cli-plugins` será responsável por gerar o CLIMap correto e um plugin válido. Quaisquer erros de interpretação ou "alucinações" por parte do assistente de IA, após o plugin ser fornecido corretamente, estão fora do escopo direto de `cli-plugins`, embora o `confidence_score` no CLIMap possa ajudar a mitigar estes problemas.

## Versioning

O versionamento dos plugins deve seguir a versão da CLI de origem e incluir a versão do schema CLIMap utilizado. Mecanismos de deteção de desatualização baseados na versão da CLI de origem serão implementados.
