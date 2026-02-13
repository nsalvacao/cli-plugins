# Feature Specification: CLI Plugins Core Project

**Feature Branch**: `001-cli-plugins-base`
**Created**: 2026-02-12
**Status**: Draft
**Input**: User description: "O projeto cli-plugins tem como objetivo ser o 'OpenAPI for CLIs', auto-gerando plugins estruturados para assistentes de IA a partir da saída --help de CLIs, fornecendo conhecimento preciso e atualizado sobre ferramentas de linha de comando. Inclui um crawler universal, um gerador de plugins multi-agente, e visa a criação de uma especificação OCS."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Obter Conhecimento Preciso de uma CLI (Priority: P1)

Como um desenvolvedor que usa um assistente de IA, eu quero que o assistente seja capaz de me dar comandos e flags precisos para qualquer CLI que eu tenha instalada, sem "alucinar" ou dar informações desatualizadas.

**Why this priority**: Esta é a proposta de valor central do projeto. Resolve o problema primário da ineficácia dos assistentes de IA com CLIs, aumentando a confiança e a produtividade do utilizador.

**Independent Test**: Pode ser totalmente testado ao instalar um plugin gerado para uma CLI popular (e.g., `docker`), e depois usar um assistente de IA (e.g., Claude Code) para perguntar sobre os comandos e flags dessa CLI. O assistente deve fornecer respostas corretas e detalhadas.

**Acceptance Scenarios**:

1.  **Given** que o plugin `docker` foi gerado e está ativo no assistente de IA, **When** eu pergunto ao assistente "como faço `docker run` com uma flag para GPU?", **Then** o assistente deve responder com a flag correta (`--gpus`) e uma descrição precisa.
2.  **Given** que o plugin `git` foi gerado e está ativo, **When** eu pergunto ao assistente "quais são as opções de `git commit`?", **Then** o assistente deve listar as flags de `git commit` com descrições corretas e sem mensagens de erro de runtime.
3.  **Given** que o plugin `npm` foi gerado e está ativo, **When** eu pergunto ao assistente "como publico um pacote npm?", **Then** o assistente deve fornecer o comando `npm publish` com flags relevantes e um exemplo de uso.

---

### User Story 2 - Manter Plugins de CLI Atualizados Automaticamente (Priority: P2)

Como um utilizador de assistentes de IA, eu quero que os plugins de CLI sejam automaticamente atualizados quando a CLI subjacente muda, para garantir que o assistente de IA usa sempre o conhecimento mais recente.

**Why this priority**: A frescura dos dados é um problema crítico para o conhecimento de CLIs. A automação reduz a carga de manutenção e garante a relevância contínua dos plugins.

**Independent Test**: Pode ser testado ao alterar uma flag numa CLI (num ambiente de teste), re-executar o crawler e o gerador, e verificar se o plugin gerado reflete a mudança.

**Acceptance Scenarios**:

1.  **Given** que a versão da CLI `uv` foi atualizada e uma flag foi adicionada, **When** o crawler é executado para `uv` e o plugin é regenerado, **Then** o assistente de IA deve ser capaz de usar a nova flag sem qualquer configuração manual adicional.
2.  **Given** que um plugin foi gerado e está ativo, **When** uma nova versão da CLI é lançada e o crawler deteta que o plugin está desatualizado, **Then** o sistema deve sinalizar a necessidade de atualização ou regenerar o plugin automaticamente.

---

### User Story 3 - Explorar CLIs Através de uma Interface Estruturada (Priority: P2)

Como um desenvolvedor, eu quero poder explorar a funcionalidade de qualquer CLI através de um formato estruturado e machine-readable (CLIMap), que posso usar para automação, linting ou outras ferramentas. O linter de design de CLI será uma ferramenta externa que consome o CLIMap existente, sem modificações no schema CLIMap nesta fase.

**Why this priority**: Este cenário valida o CLIMap como uma especificação e abre caminho para um ecossistema de ferramentas que consomem o CLIMap, indo além da simples geração de plugins para IA.

**Independent Test**: Pode ser testado ao gerar o CLIMap JSON para uma CLI e depois usar uma ferramenta externa (e.g., um JSON validator ou um script Python) para inspecionar a estrutura, flags, subcomandos e outros metadados.

**Acceptance Scenarios**:

1.  **Given** que um CLIMap JSON foi gerado para a CLI `docker`, **When** eu inspeciono o ficheiro JSON, **Then** devo encontrar uma representação precisa de todos os comandos, flags (globais e específicos do comando), argumentos posicionais, variáveis de ambiente e exemplos, seguindo o schema CLIMap.
2.  **Given** um CLIMap JSON, **When** eu o submeto a um linter de design de CLI (futuro), **Then** ele deve ser capaz de identificar inconsistências ou violações de boas práticas de design de CLI.

---

### Edge Cases

-   O que acontece quando uma CLI não tem um `--help` padrão ou tem um output formatado de forma muito exótica? (O parser deve tentar a melhor correspondência e emitir avisos, não falhar abruptamente).
-   Como o sistema lida com CLIs que exigem autenticação para `--help`? (Atualmente, assume-se que `--help` é sempre acessível sem auth; se não, deve falhar graciosamente com um erro).
-   O que acontece se uma CLI muda de forma não retrocompatível (e.g., remove uma flag principal)? (O sistema deve detetar a mudança e o plugin deve ser regenerado; um futuro diff engine pode gerar um guia de migração).
-   Como o sistema lida com flags com tipos ambíguos (e.g., `-f` que pode ser `bool` ou `string` dependendo do contexto)? (O parser deve fazer a melhor inferência e emitir um `confidence score` mais baixo se houver ambiguidade).
-   O que acontece quando o output `--help` é muito longo e excede os limites de tokens de um LLM? (Progressive disclosure deve ser ativada, carregando apenas a informação relevante).

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: O sistema MUST ser capaz de rastrear (`crawl`) a saída `--help` de CLIs em diferentes famílias de formatos (Go/Cobra, Python/Click, Rich-Click, man pages, etc.).
-   **FR-002**: O sistema MUST ser capaz de extrair flags (short, long, type, required, default, choices), argumentos posicionais, descrições, exemplos e variáveis de ambiente das CLIs rastreadas.
-   **FR-003**: O sistema MUST gerar um CLIMap JSON estruturado, conforme o schema definido em `crawler/models.py`.
-   **FR-004**: O sistema MUST ser capaz de converter o CLIMap JSON numa estrutura de plugin para assistentes de IA (Claude Code) que suporta "progressive disclosure".
-   **FR-005**: O sistema MUST permitir a configuração de CLIs a serem rastreadas via `config.yaml`.
-   **FR-006**: O sistema MUST suportar a atualização e regeneração de plugins, detetando desatualizações através da comparação da versão da CLI de origem.
-   **FR-007**: O sistema MUST ter 100% de cobertura de testes para o crawler e gerador.
-   **FR-008**: O sistema MUST garantir que o core do crawler e gerador não tenha dependências externas (stdlib only).
-   **FR-009**: O sistema MUST lidar com a execução de subprocessos de forma segura, incluindo a proteção contra injeção de comandos e a utilização de sandbox de execução (e.g., `subprocess.run` com argumentos tokenizados e sem `shell=True`).
-   **FR-010**: O sistema SHOULD fornecer um `confidence score` para os dados extraídos, indicando a probabilidade de precisão do parsing.
-   **FR-011**: O sistema MUST permitir a configuração do autor do plugin e não o hardcodificar no output gerado.
-   **FR-012**: O sistema MUST gerar keywords semanticamente relevantes para os plugins, em vez de palavras aleatórias.

### Key Entities

-   **CLI (Command Line Interface)**: A ferramenta de linha de comando a ser rastreada (e.g., `docker`, `git`, `uv`). Possui nome, versão, padrões de ajuda e uma hierarquia de comandos.
-   **CLIMap**: A representação JSON estruturada do conhecimento de uma CLI, incluindo metadados, flags globais, variáveis de ambiente e uma árvore de comandos. Este é o ativo estratégico do projeto.
-   **Command**: Um comando específico dentro de uma CLI (e.g., `docker run`, `git commit`). Possui path, descrição, uso, aliases, flags, argumentos posicionais, variáveis de ambiente e subcomandos.
-   **Flag**: Uma opção ou argumento para um comando (e.g., `--help`, `-v`, `--config string`). Possui nome, tipo, descrição, valor default, se é obrigatório, e score de confiança.
-   **Plugin (AI Agent Plugin)**: O formato de output para um assistente de IA (e.g., `.claude/commands/docker.md` e ficheiros associados) que consome o CLIMap para fornecer conhecimento de CLI.

---

## Success Criteria *(mandatory)*

---

## Clarifications

### Session 2026-02-12

- Q: Quais são os objetivos de segurança de alto nível para o projeto `cli-plugins`? → A: Proteção contra injeção de comandos e sandbox de execução
- Q: Quais são os objetivos de fiabilidade (e.g., taxa de sucesso de crawling) e disponibilidade (e.g., tempo de atividade do serviço) para o sistema `cli-plugins`? → A: Taxa de sucesso de crawling > 99%, Disponibilidade do serviço > 99.5%
- Q: Como o sistema `cli-plugins` gerará logs, métricas e sinais de tracing para garantir a observabilidade das suas operações (e.g., crawling, parsing, geração de plugins)? → A: Implementar logging estruturado com níveis configuráveis, métricas de sucesso/falha/desempenho para cada etapa do pipeline (crawl, parse, generate) e tracing básico para identificar gargalos. A clarificação dos prós e contras de abordagens como dashboard próprio ou Prometheus/Grafana, e a importância do UI/UX, serão detalhadas posteriormente.
- Q: Como o sistema `cli-plugins` vai lidar com a integração e possíveis falhas/limitações de API ao gerar e interagir com plugins para múltiplos assistentes de IA externos (e.g., Claude Code, GitHub Copilot, Gemini)? → A: Implementar um adaptador por assistente de IA, cada um com lógica de retry, circuit breaker e tratamento de erros específicos da API. Usar um sistema de cache para minimizar chamadas redundantes e respeitar limites de rate limiting. (Esta abordagem será deferida para uma fase posterior)
- Q: O projeto `cli-plugins` terá alguma responsabilidade pela criação ou manutenção do "linter de design de CLI", ou a sua interação com o linter é estritamente a de um consumidor do CLIMap? → A: O `cli-plugins` será apenas o produtor do CLIMap e não terá responsabilidade direta pelo desenvolvimento ou manutenção do linter de design de CLI. O linter será um projeto externo que consome o CLIMap.
- Q: Quais são os principais tradeoffs que o projeto `cli-plugins` enfrentará, e como devem ser priorizados (e.g., performance sobre custo, segurança sobre conveniência)? → A: Priorizar a precisão e a segurança do parsing acima de tudo, aceitando potenciais tradeoffs em termos de tempo de processamento inicial (mas ainda dentro dos SCs definidos). A universalidade e a economia de tokens (Progressive Disclosure) vêm em segundo lugar.

### Measurable Outcomes

-   **SC-001**: Pelo menos **90%** das flags e comandos principais de 20 CLIs populares (incluindo as 7 CLIs testadas) são extraídos com **mais de 95% de precisão** no CLIMap JSON.
-   **SC-002**: O custo de tokens por consulta de CLI num assistente de IA, usando o plugin `SKILL.md`, é **reduzido em pelo menos 5x** em comparação com a colagem do `raw --help` completo.
-   **SC-003**: Os plugins gerados para `Rich-Click` e `man page` CLIs atingem uma **qualidade de parsing de flags e exemplos superior a 80%**, conforme avaliado pelo skill de `evaluation`.
-   **SC-004**: O processo de crawl e geração de um plugin para uma CLI de tamanho médio (e.g., `docker`) é concluído em **menos de 30 segundos** numa máquina de desenvolvimento padrão.
-   **SC-005**: Após o lançamento no PyPI, **99%** das instalações via `pip install cli-plugins` em ambientes Python 3.11+ são bem-sucedidas no primeiro mês.
-   **SC-006**: Os plugins gerados permitem que os assistentes de IA respondam a **90%** das perguntas sobre comandos CLI complexos sem "alucinar" ou pedir clarificação desnecessária.
-   **SC-007**: O `README.md` atualizado, incluindo GIF e tabela de comparação, tem uma **taxa de conversão de visitante para estrela no GitHub superior a 5%** após o lançamento no Hacker News.
-   **SC-008**: O crawler é capaz de processar **50 CLIs** (lotes de 10 em paralelo) e o output `--help` de CLIs com **até 10000 linhas**, com um tempo médio de processamento por CLI consistente com SC-004.
-   **SC-009**: A etapa de parsing (conversão do output raw `--help` para CLIMap JSON em memória) de um `--help` de **10000 linhas** é concluída em **menos de 5 segundos**.
-   **SC-010**: O sistema atinge uma **taxa de sucesso de crawling superior a 99%** e uma **disponibilidade de serviço superior a 99.5%** para o processo de atualização de plugins.
