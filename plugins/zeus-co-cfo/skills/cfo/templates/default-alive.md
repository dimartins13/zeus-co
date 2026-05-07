# Default Alive Checkpoint — {Empresa} — {YYYY-MM-DD}

> Pelo Paul Graham. Pergunta semanal: com runway atual + crescimento atual, atingimos profitabilidade ANTES de queimar caixa?
> Se SIM = Default Alive. Se NÃO = Default Dead → 2 únicas opções: cresce ou corta.

**Empresa:** {nome}
**Estágio:** {Operação / Validação / etc.}
**Data:** {YYYY-MM-DD}
**Periodicidade:** Semanal (toda sexta)

---

## Snapshot atual (números)

| Métrica | Valor |
|---|---|
| Caixa atual (R$) | {valor} |
| Burn mensal líquido (R$) | {valor} |
| Receita mensal atual (R$) | {valor} |
| Crescimento receita MoM (%) | {valor} |
| Runway nominal (meses) | Caixa / Burn = {N} |

## Default Alive Calculation

### Premissas
- Receita cresce a {X}%/mês mantendo trajetória atual
- Custos fixos crescem a {Y}%/mês
- Custos variáveis = {Z}% da receita

### Projeção mês a mês até intersecção

| Mês | Receita | Custos | EBITDA | Caixa final |
|---|---|---|---|---|
| M0 | {R} | {C} | {R-C} | {C0} |
| M+1 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

### Resultado

- **Default ALIVE?** {Sim / Não}
- **Mês de break-even projetado:** M+{N}
- **Caixa no break-even:** R$ {valor} (positivo se ALIVE)
- **Mês de morte de caixa (se DEAD):** M+{N}

## Decisão

**{ALIVE → continuar trajetória atual.}**
ou
**{DEAD → recomendo {Cortar X% do burn} OU {Acelerar receita via Y}. Não fazer nada significa morte em M+{N}.}**

## Cenário stress (-20% receita, +15% custo)

Mesmo cálculo com premissas pessimistas. Se mesmo no stress fica ALIVE, posição confortável. Se DEAD apenas no stress, monitorar semanal.

## Próximos Movimentos

1. {ação imediata se DEAD; ou check mantém alive}
2. {comunicar pra CEO/board se mudou status vs semana anterior}
3. {data próximo checkpoint}
