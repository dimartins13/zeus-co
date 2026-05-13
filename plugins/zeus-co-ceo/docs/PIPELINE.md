# PIPELINE — CEO Office

> **CEO opera a empresa.** Board governa. C-Suite executa funcional. CEO decide direção + alinha tudo.
> **Princípio:** Diego é o CEO virtual de TODAS as empresas. Esse pipeline é o que o LEP CEO executa em cada uma.

---

## Fase 0 — Descoberta Interna (obrigatória)

Antes de qualquer ação do CEO, ler da empresa:
- `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md`
- `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + `_Inbox.md`
- `_Areas/CEO/decision-criteria.md` (hard limits + North Star)
- Última pulse/board pack se existir
- Status Default Alive (CFO LEP — se houver)

---

## Pipeline CEO (10 fases)

### Fase 1 — Diagnóstico de estágio
Owner: `ceo` (chief) + `ceo-estrategia`
- Em qual estágio a empresa está? (Ideia/Validação/MVP/Lançamento/Operação/Escala)
- Quais artefatos canônicos faltam pra esse estágio?
- Output: estágio confirmado + lista de gaps

### Fase 2 — Definição (ou refinamento) de North Star
Owner: `ceo-north-star-keeper`
- 1 métrica que captura valor entregue ao cliente
- Threshold healthy + dangerous
- Cadência de medição (semanal/mensal)
- Output: `_Areas/CEO/north-star.md`

### Fase 3 — OKRs trimestrais
Owner: `ceo-okrs-keeper`
- 3-5 Objectives qualitativos
- 3-4 Key Results quantitativos por Objective
- Cascading: OKRs CEO → OKRs C-Levels → OKRs funcionários
- Output: `_Areas/CEO/okrs-YYYY-Q.md`

### Fase 4 — Modelo de negócio (Lean Canvas / BMC)
Owner: `ceo-estrategia`
- Lean Canvas (early-stage)
- Business Model Canvas (estágios maduros)
- Validação de hipóteses críticas
- Output: `_Areas/CEO/lean-canvas.md` ou `business-model-canvas.md`

### Fase 5 — Default Alive checkpoint (cadência semanal)
Owner: `ceo` invoca `zeus-co-cfo:cfo-fpa`
- Runway atual + burn + projected break-even
- Se Default Dead → reorg/captação/corte
- Output: linha em `_Areas/CEO/default-alive-log.md` semanal

### Fase 6 — 1on1s com C-Suite
Owner: `ceo` + `ceo-chief-of-staff` (logística)
- 1on1 mensal com cada C-Level
- Pauta canônica: highlights/lowlights/asks
- Output: `_Areas/CEO/1on1s/<C-Level>/YYYY-MM.md`

### Fase 7 — Alocação de capital + recursos
Owner: `ceo` + `zeus-co-cfo:cfo`
- Budget anual + revisões trimestrais
- Hire plan (quem contratar quando)
- Tempo Diego allocation cross-portfolio
- Output: `_Areas/CEO/capital-allocation-YYYY.md`

### Fase 8 — Narrativa estratégica
Owner: `ceo` + `ceo-comms`
- North Star em prosa
- Manifesto interno (pra time)
- Manifesto externo (pra investor/customer/imprensa)
- Output: `_Areas/CEO/strategic-narrative.md`

### Fase 9 — Fundraising (quando aplicável)
Owner: `ceo-fundraising` + `ceo-ir`
- Quando captar (use Default Alive)
- Quanto captar (use modelo de runway)
- Quem captar de (investor mapping)
- Como captar (pitch deck + data room)
- Output: `_Areas/CEO/fundraising-Round-X/`

### Fase 10 — Decisão Type 1 (escalation pro board)
Owner: `ceo` invoca `zeus-co-board:decision-memo-author`
- Toda decisão irreversível formalizada em memo ADR
- Aprovação board necessária se na lista de matérias reservadas
- Output: `_Areas/Board/decision-memos/YYYY-MM-DD-<topic>.md`

---

## Princípio inviolável

**C-levels NÃO são juízes — são operadores.** CEO especialmente. Output sempre termina com "Próximos Movimentos" (3 ações concretas) — nunca em "diagnóstico contemplativo".

Verbos que usa: decido, estruturo, alinho, contrato, demito, alocando, lanço, pivoto, captou, fechou.
Verbos que evita: avalio, considero, reflito, ponderando.
