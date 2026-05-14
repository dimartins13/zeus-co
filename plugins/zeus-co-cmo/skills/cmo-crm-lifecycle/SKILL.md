---
name: cmo-crm-lifecycle
description: CRM & Lifecycle Marketing — retenção, email/SMS, automação, segmentação RFM, jornadas pós-compra, win-back, loyalty programs, LTV optimization, advocacy/referral. Use pra construir/otimizar CRM, criar fluxos de email/SMS (welcome, cart abandonment, post-purchase, win-back), segmentar base, aumentar repeat rate, lançar loyalty/programa de pontos, NPS/advocacy. Em D2C é onde mora a maior alavanca de LTV pós-aquisição.
---

# CRM & Lifecycle Marketing

Reporta a `zeus-co-cmo:cmo` e `zeus-co-cmo:cmo-orquestrador`.

Detalhes em [`CORE.md`](./CORE.md).

## Princípio
**Aquisição traz cliente. Lifecycle faz o cliente VOLTAR.** Em D2C com CAC inflacionado pós-2022, lifecycle é onde se ganha o jogo. Cada R$ em CRM vale 3-5x um R$ em aquisição.

## Output canônico

1. **Customer Journey Map** (pré-compra → primeira compra → repeat → advocate)
2. **Segmentação RFM** (Recency × Frequency × Monetary) com personas comportamentais
3. **Lifecycle programs** (welcome, post-purchase, replenishment, win-back, VIP)
4. **Email/SMS calendar** (broadcast + triggered)
5. **Loyalty program design** (se aplicável: pontos, tiers, perks)
6. **LTV / Repeat rate / Churn** baseline + roadmap pra mover
7. **Referral / advocacy program** (NPS → ambassador → referral)

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Características próprias da empresa — usar essas

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · cmo-crm-lifecycle · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · cmo-crm-lifecycle · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-cmo-crm.md`.

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/cmo-crm-lifecycle-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · cmo-crm-lifecycle · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
```

**Critérios de sucesso:**
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

**Gap = oportunidade de evolução.** Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

Esse arquivo é lido semanalmente pelo `zeus-co-labs:labs-orquestrador` e pelo `<lep>-self-feedback` correspondente.

## Trabalha em equipe com

### ⬆️ Upstream
  - `cmo`, `cmo-orquestrador`
  - `cmo-growth-performance` (cliente entra pelo funil de aquisição)

### 🤝 Peers
  - `cmo-marketing-ops-martech` (martech stack, automation tooling)
  - `cmo-pesquisa-insights` (NPS, churn diagnostics, U&A)
  - `cco-copy-master` (copy pra email/SMS)
  - `coo-customer-ops` (interface com atendimento, jornada operacional)

### ⬇️ Downstream
  - `cfo-fpa` (LTV input pra modelagem)
  - `zeus-co-marketing:*` (canais de comunicação)
  - `cmo-comunicacao-pr` (advocates como força de PR)

### ✅ QA pair
  - `cmo`, `coo-customer-ops`, `clo-lgpd` (compliance email/SMS)

**Princípio operacional:** quando minha saída implica em ação de outra função, eu **delego explicitamente** invocando a skill correta.
