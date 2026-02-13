<!--
Sync Impact Report:
Version change: 0.0.0 → 1.0.0
Modified principles: All (initial creation)
Added sections: Additional Constraints, Development Workflow
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated (general principles apply, no specific placeholders)
  - README.md: ⚠ pending (needs manual review for principle references)
  - docs/quickstart.md: ⚠ pending (needs manual review for principle references)
Follow-up TODOs: None
-->
# cli-plugins Constitution

## Core Principles

### Open CLI Specification (OCS)
O schema CLIMap JSON deve ser a descrição padrão e machine-readable para interfaces CLI, tal como o OpenAPI para REST APIs. Esta especificação deve ser aberta, versionada e com governança clara.
Justificativa: A ausência de um padrão para descrever CLIs de forma machine-readable limita a interoperabilidade. A padronização cria um ecossistema valioso e posiciona o CLIMap como a autoridade para este tipo de interface.

### Auto-Geração e Otimização para IA
Todo o conhecimento da CLI deve ser auto-gerado e otimizado para consumo por agentes de IA. Plugins e ferramentas devem ser gerados automaticamente a partir da saída `--help` das CLIs, man pages e outras fontes. O formato resultante (CLIMap) deve ser otimizado para LLMs, com progressive disclosure e eficiência de tokens.
Justificativa: A curadoria manual de conhecimento CLI não é escalável nem sustentável. A auto-geração garante frescura, abrangência e reduz as "alucinações" dos modelos de IA, melhorando a precisão e a confiança.

### Universalidade e Multi-Agente
A solução deve ser universal, funcionando com qualquer CLI e gerando output para múltiplos agentes de IA. O parser deve suportar várias famílias de formatos (Go/Cobra, Click, Rich-Click, man pages, etc.), e o CLIMap deve ser transpilável para formatos de plugins de diferentes assistentes de IA (Claude Code, GitHub Copilot, Cursor, Gemini, etc.).
Justificativa: O mercado de agentes de IA é fragmentado. A universalidade maximiza o alcance do projeto e posiciona o CLIMap como o formato de intercâmbio de facto para conhecimento CLI, reduzindo a dependência de plataformas específicas.

### Qualidade, Testabilidade e Confiança
O sistema deve garantir a qualidade do output, ser testável e fornecer níveis de confiança. O output deve ser preciso, completo e consistentemente formatado. Mecanismos para detetar e mitigar erros de parsing ou informação desatualizada devem ser implementados. O CLIMap deve incluir um `confidence` score.
Justificativa: A confiança do utilizador é crucial para a adoção, especialmente em comandos que afetam infraestrutura. A qualidade robusta é essencial para a credibilidade, e a testabilidade garante a sustentabilidade e resiliência do projeto.

### Foco no Ecossistema e Comunidade
Promover um ecossistema auto-sustentável e impulsionado pela comunidade, com um registo centralizado (cli-plugins.dev) para descoberta, instalação e publicação de plugins. Incentivar contribuições da comunidade e garantir que a propriedade da especificação seja neutra (Open Source Foundation).
Justificativa: O crescimento e a sustentabilidade a longo prazo dependem dos efeitos de rede e da padronização. Um registo acessível e uma governança aberta aceleram a adoção e a evolução do padrão.

## Additional Constraints

### Zero Dependencies (Core)
O core do crawler e gerador deve ter zero dependências externas para máxima portabilidade, segurança e confiança na cadeia de suprimentos. Dependências opcionais podem ser adicionadas para funcionalidades avançadas ou de UI, mas o núcleo deve permanecer leve.

### Segurança Robusta
Todas as operações de subprocessos devem ser realizadas de forma segura (e.g., `subprocess.run` sem `shell=True`), com validação rigorosa de inputs e sem a utilização ou hardcoding de segredos em código.

## Development Workflow

### Test-Driven Development (TDD)
Seguir um ciclo `Red-Green-Refactor` rigoroso para todas as novas funcionalidades e refactorizações, garantindo que os testes são escritos antes do código de produção.

### Micro-Commits e Validação Contínua
Fazer commits pequenos e frequentes, garantindo que cada commit introduz uma alteração funcional e que o código compila e passa os testes relevantes.

### CI/CD Automatizado
Manter um pipeline de CI/CD para automatizar testes, linting, e validação em cada push e Pull Request, garantindo a qualidade e a consistência.

### Spec-Driven Development
Utilizar especificações (OCS, CLIMap) como o driver primário para o desenvolvimento, garantindo que a implementação está alinhada com os requisitos e o design.

## Governance
Esta Constituição sobrepõe-se a todas as outras práticas e documentações do projeto. Quaisquer alterações a esta Constituição requerem documentação clara da proposta, aprovação pela liderança do projeto (ou por consenso da comunidade, se aplicável) e um plano de migração para quaisquer componentes dependentes. Todos os Pull Requests e revisões de código devem verificar a conformidade com estes princípios e diretrizes. A introdução de complexidade ou trade-offs arquiteturais deve ser justificada explicitamente em termos dos benefícios para o projeto e os seus utilizadores. O versionamento desta Constituição seguirá o versionamento semântico (MAJOR.MINOR.PATCH). Para orientação de runtime e desenvolvimento diário, consultar `CLAUDE.md` e `~/.claude-flow/CLAUDE_FLOW_REFERENCE.md`.

**Version**: 1.0.0 | **Ratified**: 2026-02-12 | **Last Amended**: 2026-02-12
