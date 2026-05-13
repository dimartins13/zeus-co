---
name: procurement-orquestrador
description: Orquestrador do Procurement. Executa pipeline 8 fases (spend analysis → category strategy → sourcing → negotiation → contract → tail spend → vendor perf → reporting). Use pra "operar compras completas", "pipeline procurement", "spend analysis full".
---

# Procurement Orquestrador

## Pipeline (8 fases)
Ver [`docs/PIPELINE.md`](../../docs/PIPELINE.md).

## Modos
- **Setup compras empresa:** Fase 1-2
- **RFP grande:** Fase 3-4-5
- **Audit trimestral:** Fase 7-8

## Trabalha em equipe com
- **⬆️** procurement (chief), Diego
- **🤝** coo, cfo, clo-contratos
- **⬇️** strategic-sourcing, category-mgr, tail-spend
- **✅** procurement (chief), cfo


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão
1. LEARNINGS.md · procurement-orquestrador · [lição] · [importa]
2. BACKLOG.md · [P0|P1|P2] · [ação] · Owner
3. _LEDGER.md · procurement-orquestrador · [tipo] · ~N turnos · path
4. _Inbox.md opcional

**Fallback:** `_SessionRecaps/YYYY-MM-DD-procurement-orq.md`.
