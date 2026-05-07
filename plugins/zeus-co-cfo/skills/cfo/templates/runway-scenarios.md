# Runway Scenarios — {Empresa}

> 3 cenários (base / upside / downside) + sensibilidade nos drivers críticos.
> Decisão: qual ação tomar AGORA pra maximizar runway no cenário base e sobreviver no downside.

**Empresa:** {nome}
**Data da projeção:** {YYYY-MM-DD}
**Horizonte:** 18 meses

---

## Premissas por cenário

| Driver | Base | Upside | Downside |
|---|---|---|---|
| Crescimento receita MoM | +{X}% | +{X+5}% | +{X-10}% |
| Churn mensal | {%} | {%-1pp} | {%+2pp} |
| CAC | R$ {valor} | R$ {valor-10%} | R$ {valor+25%} |
| OPEX growth MoM | +{X}% | +{X-1}% | +{X+3}% |
| Tempo até captação (meses) | {N} | {N-3} | {N+9} |

## Resultados

### Cenário Base (probabilidade ~60%)

- Caixa M+12: R$ {valor}
- Runway: {N meses}
- Mês de break-even: M+{N} (ou "não atingido em 18m")
- Default: ALIVE / DEAD
- Captação necessária: R$ {valor} até {data}

### Cenário Upside (probabilidade ~20%)

- Caixa M+12: R$ {valor}
- Runway: {N meses}
- Mês de break-even: M+{N}
- Default: ALIVE
- Captação necessária: R$ {valor} (talvez não precisa)

### Cenário Downside (probabilidade ~20%)

- Caixa M+12: R$ {valor}
- Runway: {N meses}
- Mês de morte de caixa: M+{N}
- Default: DEAD
- Captação necessária: R$ {valor} URGENTE até {data}
- **Plano de contingência:** {cortes específicos a aplicar se downside materializar}

## Sensibilidade (single-driver swings)

Quanto runway muda se UM driver se mover ±20%, mantendo outros constantes?

| Driver | Runway baseline | Runway -20% | Runway +20% | Magnitude |
|---|---|---|---|---|
| Receita | {N} meses | {N} | {N} | {alta/média/baixa} |
| Churn | {N} | {N} | {N} | {alta/média/baixa} |
| CAC | {N} | {N} | {N} | {alta/média/baixa} |
| OPEX | {N} | {N} | {N} | {alta/média/baixa} |

**Driver mais sensível:** {qual} — implicação: foco operacional aqui.

## Decisão

**Recomendação:** {1 frase — qual cenário planejar pra + qual ação tomar}

## Plano

1. **Premissa base:** {operar como se cenário base materializa, mas...}
2. **Triggers de re-avaliação:** {se métrica X cair abaixo de Y por 2 meses seguidos, re-rodar este modelo}
3. **Se downside materializa:** {plano de corte pré-aprovado — qual % burn cortar, em quê}

## Próximos Movimentos

1. {data próxima atualização}
2. {ação imediata derivada do cenário recomendado}
3. {comunicar status pro CEO/board se mudou vs último mês}
