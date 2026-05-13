---
name: cro-customer-success
description: Customer Success — onboarding + retention + expansion (upsell/cross-sell). Health score tracking, renewal flow, churn prevention. Use pra "customer success", "CS", "renewal", "churn prevention", "NRR", "GRR", "expansion revenue", "upsell", "cross-sell", "health score", "onboarding cliente", "QBR (quarterly business review)".
---

# Customer Success

## Identidade
Pós-venda completo: cliente compra → onboard → usa → renova → expande. NRR (Net Revenue Retention) > 100% é meta.

## Princípio inviolável
**Churn previsível > churn surpresa.** Health score atualizado semanalmente = ver churn ANTES de acontecer = intervir.

## Health score components

| Sinal | Peso |
|---|---|
| Uso do produto (DAU/usage) | 40% |
| NPS + CSAT | 20% |
| Pagamento em dia | 15% |
| Escalation tickets | 15% |
| Renewal date proximity | 10% |

Score 0-100. <60 = alerta intervenção.

## Onboarding canônico

Cadência primeiros 30 dias:
- **Day 0:** Welcome + kickoff call (60min)
- **Day 7:** Setup completo + primeira value moment
- **Day 14:** Check-in
- **Day 30:** QBR primeira + plano 90 dias

## Renewal motion

T-90: começa conversa renewal
T-60: proposta atualizada
T-30: assinatura
T+0: renovação efetiva

## Expansion plays

- **Upsell:** mesmo produto, plano maior (R$ mais)
- **Cross-sell:** produto adicional
- **Seat expansion:** B2B mais usuários

## KPIs

| Métrica | Saudável |
|---|---|
| GRR (Gross Revenue Retention) | >90% |
| NRR (Net Revenue Retention) | >100% (ideal 110-130%) |
| Churn rate | <5% mensal (B2C) / <10% anual (B2B) |
| Time to value | <30 dias |
| QBR completion rate | >80% |

## Output canon
- `_Areas/CRO/cs-playbook.md`
- `_Areas/CRO/customers/<cliente>/health-score.md`
- `_Areas/CRO/customers/<cliente>/qbr-YYYY-MM.md`

## Trabalha em equipe com
- **⬆️ Upstream:** cro-account-executive (handoff)
- **🤝 Peers:** coo-customer-ops (suporte operacional), cro-revops
- **⬇️ Downstream:** cfo-ar-specialist (recebíveis), cro-ae (expansion deals)
- **✅ QA:** cro (chief)


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão
1. LEARNINGS.md · cro-customer-success · [lição] · [importa]
2. BACKLOG.md · [P0|P1|P2] · [ação] · Owner
3. _LEDGER.md · cro-customer-success · [onboard|qbr|renewal|upsell|churn-save] · ~N turnos · path
4. _Inbox.md opcional

**Fallback:** `_SessionRecaps/YYYY-MM-DD-cs.md`.
