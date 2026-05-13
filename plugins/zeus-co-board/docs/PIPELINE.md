# PIPELINE — Board + Founders + Governance

> **Camada superior ao C-Suite.** Board não opera empresa. Board APROVA estratégia + monitora performance + protege fundador.
>
> **Princípio:** Diego é fundador + investidor + operador. Board é onde Diego "se separa" de si mesmo pra revisar decisões com distância crítica.

---

## Fase 0 — Descoberta Interna (obrigatória)

Antes de qualquer atividade de board, ler da empresa:

- `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md`
- `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md`
- `_Areas/CEO/decision-criteria.md` (hard limits + North Star)
- Material financeiro existente (BP, runway, default alive)
- Last board pack (se existir)
- Cap table atual + vesting status

**Sem isso, board opera no escuro.**

---

## Pipeline Board (9 fases)

### Fase 1 — Constituição (one-time, depois manutenção)
Owner: `board-governance`
- Definir estatuto: composição (Diego + advisors + sócios), quórum, periodicidade
- Definir reservas (matérias que SÓ Diego decide vs SÓ board decide)
- Estatuto vivo: documento `_Areas/Board/governance-charter.md` da empresa

### Fase 2 — Cap table foundation
Owner: `cap-table-keeper`
- Cap table atual (Diego + sócios + investidores + opções)
- Vesting schedule (Diego + funcionários + advisors)
- Waterfall (preferences, liquidation, anti-dilution)
- Atualizado a cada round / cada vesting milestone

### Fase 3 — Advisor scouting + onboarding
Owner: `board-advisors-management`
- Identificar gap de conhecimento da empresa
- Sourcing de advisor (network Diego + warm intros)
- Deal terms (equity 0.1-1% + cliff 1 ano + 4 anos vesting + comp opcional)
- Onboarding (NDAs, deck, hopes/asks Diego)

### Fase 4 — Board pack mensal/trimestral
Owner: `board-pack-builder`
- Template canônico: 1) Highlights 2) Métricas KPI North Star 3) Default Alive 4) Decisões pendentes 5) Risks
- Cadência: mensal pra board ativo, trimestral pra advisory
- Output: deck (Gamma) + memo escrito (Docx)

### Fase 5 — Reunião de board
Owner: `board-orquestrador` (orquestra)
- Pre-meeting: distribuir pack T-3 dias
- Meeting: facilitar agenda (highlights → métricas → decisões pendentes → strategic discussion)
- Post-meeting: minutes + ações + follow-ups

### Fase 6 — Decisão Type 1 (irreversível)
Owner: `decision-memo-author`
- Toda decisão **irreversível** (pivot, fundraise, M&A, hire C-level, demissão sócia) → memo ADR estilo
- Estrutura: Contexto → Opções → Trade-offs → Decisão → Consequências esperadas → Reversibilidade
- Arquivado em `_Areas/Board/decision-memos/YYYY-MM-DD-<topic>.md`

### Fase 7 — Equity events
Owner: `equity-vesting-manager`
- Hire C-level com equity grant
- Funcionário atingiu cliff
- Advisor terminou vesting
- Buyback de equity de ex-funcionário
- Cada evento atualiza cap table + cria decision memo

### Fase 8 — Founders office (Diego direto)
Owner: `founders-office`
- Decisões que Diego NÃO delega (vendas estratégicas iniciais, contratação primeiros 10, narrativa pública, fundraise pitch)
- Schedule + protect Diego time
- Anti-overhead: Diego em meeting >3h/dia = bloqueado pra board considerar reorg

### Fase 9 — Investor + Stakeholder relations
Owner: delegado a `zeus-co-ceo:ceo-ir` (já existe) + `board-orquestrador` coordena
- Investor updates mensais (5-7 KPIs + Highlights + Asks)
- Reuniões 1:1 com investidores ativos
- Crisis communication quando aplicável

---

## Quando esta camada NÃO atua

- Operação dia-a-dia → C-Suite (CEO/CFO/COO/CMO/CCO/CTO/CLO)
- Decisão Type 2 (reversível) → C-Level relevante decide
- Comunicação operacional → CMO/CCO

Board atua APENAS em: estratégia macro + decisões irreversíveis + governance + fundraise + investor relations + protecting founder time.
