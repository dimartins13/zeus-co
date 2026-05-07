# Tech Stack Decision — {Empresa / Componente}

> Decisão de stack. Por padrão: BORING (maduro + bem documentado + ecossistema grande).

**Empresa:** {nome}
**Componente:** {Frontend / Backend / Banco / Auth / Email / Analytics / Hosting / etc}
**Date:** {YYYY-MM-DD}
**Decisor:** CTO LEP / Diego

---

## Contexto

- Volume esperado: {N usuários / req/s}
- Time disponível: {Diego solo / + N devs}
- Budget: R$ {valor}/mês
- Time-to-launch: {N semanas}
- Restrições: {compliance, latência, BR-specific}

## Opções

| # | Stack | Custo/mês | Time-to-prod | Maturidade | Pros | Contras |
|---|---|---|---|---|---|---|
| A | {ex: Next.js + Supabase} | R$ X | 2 semanas | Alto | | |
| B | {ex: Rails + Postgres + Heroku} | R$ Y | 3 semanas | Alto | | |
| C | {ex: Bubble (no-code)} | R$ Z | 1 semana | Médio | | |
| D | Não fazer (defer) | 0 | 0 | n/a | Foco em outra coisa | Perde janela |

## Recomendação

**Vou usar {opção X} porque {razão central}.**

Trade-off principal: {o que ganho vs o que perco}.

## Reversibilidade

- Mudar de {A} para {B} depois custa: {N semanas + R$X}
- Quando seria justificado: {gatilho — ex: "se passar de 10K MAU"}

## Plano de implementação

1. {passo 1 — owner, prazo}
2. {passo 2}
3. {passo 3}

## Próximos Movimentos

1. {ação imediata}
2. {primeira entrega}
3. {checkpoint}
