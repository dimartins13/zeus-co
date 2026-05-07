# 3-Statement Model — {Empresa}

> Modelo integrado P&L + Balance Sheet + Cash Flow. Driver-based (5-7 drivers operacionais, não SKU-by-SKU).
> Atualização: mensal. Revisão de premissas: trimestral.

**Empresa:** {nome}
**Versão:** v{n}
**Período coberto:** Histórico {N} meses + Forecast {N} meses
**Última atualização:** {YYYY-MM-DD}

---

## 1. Drivers operacionais (5-7 max)

Os números que TUDO depende. Mudar premissa aqui propaga em P&L/BS/CF.

| Driver | Valor atual | Premissa M+1 | Premissa M+12 |
|---|---|---|---|
| {ex: clientes ativos} | {valor} | {valor} | {valor} |
| {ex: ARPU mensal} | R$ {valor} | R$ {valor} | R$ {valor} |
| {ex: churn mensal} | {%} | {%} | {%} |
| {ex: CAC} | R$ {valor} | R$ {valor} | R$ {valor} |
| {ex: COGS %} | {%} | {%} | {%} |
| {ex: headcount} | {N} | {N} | {N} |
| {ex: salary médio} | R$ {valor} | R$ {valor} | R$ {valor} |

## 2. Income Statement (P&L)

| | M0 | M+1 | M+3 | M+6 | M+12 |
|---|---|---|---|---|---|
| **Receita Bruta** | | | | | |
| (-) Impostos s/ Receita | | | | | |
| **Receita Líquida** | | | | | |
| (-) COGS | | | | | |
| **Margem Bruta** | | | | | |
| Margem Bruta % | | | | | |
| (-) S&M | | | | | |
| (-) R&D / Produto | | | | | |
| (-) G&A | | | | | |
| **EBITDA** | | | | | |
| (-) Depreciação | | | | | |
| (-) Amortização | | | | | |
| **EBIT** | | | | | |
| (+/-) Resultado Financeiro | | | | | |
| (-) IR/CSLL | | | | | |
| **Lucro Líquido** | | | | | |

## 3. Balance Sheet

| | M0 | M+12 |
|---|---|---|
| **ATIVO** | | |
| Caixa | | |
| Recebíveis | | |
| Estoque | | |
| Imobilizado | | |
| Intangível | | |
| **Total Ativo** | | |
| **PASSIVO** | | |
| Fornecedores | | |
| Empréstimos | | |
| Provisões | | |
| **Total Passivo** | | |
| **PATRIMÔNIO LÍQUIDO** | | |
| Capital social | | |
| Reservas/Lucros acumulados | | |
| **Total Passivo + PL** | | |

## 4. Cash Flow Statement

| | M+1 | M+3 | M+6 | M+12 |
|---|---|---|---|---|
| **Operacional** | | | | |
| Lucro líquido | | | | |
| (+) Depreciação/Amortização | | | | |
| (+/-) Variação working capital | | | | |
| **= Caixa Operacional** | | | | |
| **Investimento** | | | | |
| (-) CapEx | | | | |
| **= Caixa Investimento** | | | | |
| **Financiamento** | | | | |
| (+) Captação | | | | |
| (-) Amortização empréstimos | | | | |
| (-) Distribuição lucros | | | | |
| **= Caixa Financiamento** | | | | |
| **Variação líquida caixa** | | | | |
| Caixa inicial | | | | |
| **Caixa final** | | | | |

## 5. Métricas-chave derivadas

- **Burn Multiple:** Net Burn / Net New ARR = {valor}
- **Magic Number:** Net New ARR / S&M = {valor}
- **CAC Payback:** {meses}
- **LTV/CAC:** {ratio}
- **Rule of 40:** Growth + EBITDA margin = {valor}%
- **Runway:** {meses}

## Próximos Movimentos

1. Validar premissa #{N} com {input específico}
2. Atualizar modelo com dados M+1 dia X
3. Apresentar para CEO/board no formato investor-update
