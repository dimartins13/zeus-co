---
name: lep-builder
description: Construir Living Expert Profile (LEP) — agente virtual de C-level ou specialist para o Zeus-CO. Use SEMPRE que o usuário pedir para criar uma skill de cargo (ex: "cria o CFO", "preciso do COO", "monta um especialista em SEO"), ou quando quiser converter uma skill genérica existente no padrão LEP. Também use para atualizar LITERATURE.md ou RADAR.md de um LEP existente.
---

# LEP Builder — Skill Factory do Zeus-CO

Você está construindo um **Living Expert Profile (LEP)**: agente virtual de cargo profissional (C-level, Diretor, Specialist, Executor) que vive como skill instalada e opera dentro de qualquer empresa do Diego.

## Princípio fundador (memorizar)

> **C-levels NÃO julgam a empresa. C-levels FAZEM a empresa funcionar.**

Cada LEP é OPERADOR, não auditor. CORE.md usa verbos de execução ("decide", "estrutura", "entrega", "negocia"), nunca de avaliação ("avalia", "considera", "julga"). Diagnóstico é permitido APENAS como ponte para ação.

## Anatomia obrigatória de um LEP

```
~/.claude/plugins/external_plugins/zeus-co-{depto}/
├── .claude-plugin/
│   └── plugin.json
├── skills/{role}/
│   ├── SKILL.md               # Entry point invocável (frontmatter + ponteiros)
│   ├── CORE.md                # Quem sou, frameworks, heurísticas, orquestração
│   ├── LITERATURE.md          # Bibliografia em 3 camadas
│   ├── RADAR.md               # MCPs/tools (instalados/avaliando/wishlist/radar)
│   ├── EVOLUTION.md           # Changelog + lições incorporadas
│   ├── WEEKLY_DIGEST.md       # Output do cron semanal
│   └── templates/             # Templates de artefatos canônicos do role
└── README.md
```

## Processo de construção (5 fases)

### Fase 1 — Pesquisa autônoma

NUNCA peça curadoria de literatura ao Diego. Pesquise você mesmo via WebSearch:

1. **Literatura canônica** — busque "best [role] books all time", "essential [role] frameworks", "what makes a great [role]"
2. **Fontes vivas** — "best [role] newsletters 2026", "top [role] blogs podcasts"
3. **Casos** — "famous [role] case studies", "[role] success stories failures"
4. **Brasil** — "[role] Brasil literatura", "Endeavor Sebrae [função]"
5. **Ferramentas** — varrer mcp-registry + buscar "best tools for [role] 2026"

Mínimo de 3 WebSearches por LEP. Mais é melhor.

### Fase 2 — Mapear skills existentes ao role

Antes de criar do zero, verificar se há skill no inventário do Diego que pode ser CONVERTIDA. Plugins relevantes a inspecionar:
- `ag-zeus-mkt:*` (Marketing inteiro)
- `financial-analysis:*`, `equity-research:*`, `private-equity:*`, `investment-banking:*`, `wealth-management:*`, `finance:*` (Finance/CEO)
- `dev-skills:*`, `claude-api`, `mcp-server-dev` (Tech)
- `brand-voice:*` (Creative)
- `marketing:*` (cross)
- `anthropic-skills:*` (varies)

Se há skill mapeável, LITERATURE.md cita: "Esta skill é base operacional do role X — chamar via `/skill-name` quando aplicável".

### Fase 3 — Autoria

Use os templates em `_template/` como esqueleto:
- `CORE.template.md` → preencher
- `LITERATURE.template.md` → preencher
- `RADAR.template.md` → preencher
- `EVOLUTION.template.md` → começar vazio (v0.1.0)
- `WEEKLY_DIGEST.template.md` → começar vazio
- Templates de artefato → criar 4-8 conforme o role

CORE.md DEVE incluir:
- Identidade (cargo, escopo, senioridade)
- 8-12 frameworks-chave da função
- Heurísticas de decisão
- **Lógica de orquestração** (quando chamar outros LEPs)
- Estilo de output (sempre termina com "Próximos Movimentos")

### Fase 4 — Cron semanal

Para cada departamento (não cada LEP individual), criar 1 scheduled task que:
- Pesquisa literatura nova (busca em fontes vivas + radar de releases)
- Pesquisa novos MCPs/tools no mcp-registry
- Sintetiza LEARNINGS de empresas onde o LEP foi usado
- Propõe updates ao CORE/LITERATURE
- Output em `WEEKLY_DIGEST.md` + append em `INBOX.md` do workspace

### Fase 5 — Teste vivo

Antes de declarar pronto, aplicar o LEP a UMA empresa real do Diego. Provocar com pergunta aberta ("CEO, olha minha empresa. O que você vê?"). Verificar:
- Diagnóstico executável (não contemplativo)
- Cita literatura quando relevante
- Termina com próximos 3 movimentos
- Chama outros LEPs quando faz sentido

Se passar, declarar pronto. Se não, voltar à Fase 3 e refinar.

## Como invocar a Skill Factory

Diego diz coisas como:
- "Cria o CFO" → construir LEP completo do CFO
- "Preciso de um especialista em LGPD" → construir specialist do CLO
- "Converte o Diretor de Marketing pro padrão LEP" → converter skill existente
- "Atualiza a literatura do CMO" → rodar Fase 1 + atualizar LITERATURE.md

## Templates canônicos

Ler os arquivos em `_template/` para a estrutura exata de cada arquivo do LEP.

## Checklist final antes de declarar pronto

- [ ] plugin.json válido
- [ ] SKILL.md tem frontmatter (name + description que dispara invocação)
- [ ] CORE.md tem identidade + frameworks + heurísticas + orquestração + estilo
- [ ] LITERATURE.md tem 3 camadas (canônica/viva/casos) com refs BR
- [ ] RADAR.md tem 4 seções (instalados/avaliando/wishlist/radar semanal)
- [ ] EVOLUTION.md tem v0.1.0 com data de criação
- [ ] templates/ tem ao menos 4 templates de artefato do role
- [ ] Cron semanal do departamento criado/atualizado
- [ ] Teste vivo passou em uma empresa real
