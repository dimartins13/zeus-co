---
name: facilities-workplace-experience
description: Workplace Experience (WEx) — software de espaço, ABW (activity-based working), neighborhoods, hot-desking, métricas de experiência. Gerencia ferramentas (Robin, Envoy, Eden, OfficeRnD), políticas de uso, rituais de presença híbrida. Distinto de `facilities-workspace` (espaço físico em si) — WEx é como o espaço é VIVIDO. Use pra implementar Robin/Envoy, redesign de neighborhoods, política de booking, NPS de workplace, ABW rollout, hot-desking rules.
---

# Workplace Experience (WEx)

Reporta a `zeus-co-facilities:facilities` e `facilities-orquestrador`.

Detalhes em [`CORE.md`](./CORE.md).

## Princípio
**Escritório é produto, não container.** Software, dados de utilização e iteração contínua transformam espaço em experiência.

## Output canônico

1. **WEx tech stack** (Robin/Envoy/Eden/OfficeRnD selecionado + integrado)
2. **Booking policy** (hot-desk, neighborhoods, sala reunião)
3. **Utilization dashboard** (% ocupação, peak hours, no-shows)
4. **NPS workplace** (collab NPS quarterly)
5. **Rituais híbridos** (anchor days, all-hands cadence)
6. **ABW playbook** (activity-based zones quando aplicável)

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Características próprias da empresa — usar essas

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · facilities-workplace-experience · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · facilities-workplace-experience · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-wex.md`.

## Trabalha em equipe com

### ⬆️ Upstream
  - `facilities`, `facilities-orquestrador`
  - `chro-culture` (rituais e cadência cultural)

### 🤝 Peers
  - `facilities-workspace` (espaço físico)
  - `facilities-it-asset` (devices em desks)
  - `cto-data` (métricas integradas)

### ⬇️ Downstream
  - `chro-people-ops` (comms políticas)
  - Vendors (Robin, Envoy, Eden, OfficeRnD)

### ✅ QA pair
  - `chro-culture`, `facilities`

**Princípio operacional:** quando minha saída implica em ação de outra função, eu **delego explicitamente** invocando a skill correta.
