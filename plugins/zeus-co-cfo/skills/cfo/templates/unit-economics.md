# Unit Economics — {Empresa}

> Análise por unidade (cliente / pedido / transação). Determina se escala melhora ou piora resultado.
> Princípio: se unit econ não fecha, escalar piora a empresa. Resolver economics ANTES de pisar fundo.

**Empresa:** {nome}
**Unidade analisada:** {cliente / pedido / GMV / etc}
**Data:** {YYYY-MM-DD}

---

## Definição da unidade

O que conta como 1 unidade neste modelo? (ex: 1 cliente pagante mensal, 1 pedido completado, 1 transação processada)

## CAC — Customer Acquisition Cost

| Componente | Valor mensal |
|---|---|
| S&M total | R$ {valor} |
| Novos clientes adquiridos no mês | {N} |
| **CAC blended** | R$ {S&M / N} |

### CAC por canal
| Canal | Spend | Novos clientes | CAC canal |
|---|---|---|---|
| {canal A} | | | |
| {canal B} | | | |
| Organic | | | |

## LTV — Lifetime Value

### Cálculo simplificado
- ARPU mensal: R$ {valor}
- Margem bruta %: {%}
- Churn mensal %: {%}
- Lifetime (meses): 1 / churn = {N}
- **LTV = ARPU × Margem × Lifetime = R$ {valor}**

### Cálculo por cohort (mais preciso)

| Cohort | Mês 0 | Mês 3 | Mês 6 | Mês 12 | Receita acumulada |
|---|---|---|---|---|---|
| Jan/26 | | | | | |
| Fev/26 | | | | | |
| ... | | | | | |

## Métricas-chave

| Métrica | Valor | Benchmark | Status |
|---|---|---|---|
| LTV / CAC | {ratio} | ≥3 | {ok / atenção / problema} |
| CAC Payback (meses) | {N} | ≤12 (≤6 consumer) | {ok / atenção / problema} |
| Margem Bruta | {%} | ≥60% SaaS, ≥40% comércio | {ok / atenção / problema} |
| Contribution margin | {%} | ≥30% | {ok / atenção / problema} |
| Net Revenue Retention (NRR) | {%} | ≥100% saudável | {ok / atenção / problema} |

## Análise

**Diagnóstico:** {1 parágrafo — onde unit econ funciona, onde quebra}

**Decisão:** {1 frase — vamos atacar o quê primeiro}

## Plano de ação

1. {ação 1 — owner, prazo}
2. {ação 2}
3. {ação 3}

## Próximos Movimentos

1. {imediato}
2. {curto prazo}
3. {checkpoint próximo}
