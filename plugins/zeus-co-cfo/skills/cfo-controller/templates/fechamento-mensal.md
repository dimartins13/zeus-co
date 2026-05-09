# Fechamento Mensal — {Empresa} — {YYYY-MM}

> SOP de fechamento contábil. Roda dia 5 do mês seguinte (após estabilização lançamentos).

**Empresa:** {nome}
**Mês de competência:** {YYYY-MM}
**Data fechamento:** {YYYY-MM-DD}
**Responsável:** Controller (LEP) + revisão CFO

---

## Pré-requisitos
- [ ] Backup Plata-ou-Plomo do mês completo (`~/Library/Zeus-CO-Backups/dashfin/{YYYY-MM-{último-dia}}/`)
- [ ] Extratos bancários do mês baixados
- [ ] NF-e emitidas e recebidas conferidas
- [ ] Comprovantes anexados em `Comprovantes de conta/{YYYY-MM}/`

## Conciliação 3-way

### 1. Banco × Plata-ou-Plomo
- Saldo banco no último dia útil: R$ {valor}
- Saldo Plata-ou-Plomo: R$ {valor}
- Diferença: R$ {valor} → {explicar e ajustar}

### 2. NF-e × Plata-ou-Plomo
- Total NF-e emitidas: R$ {valor}
- Total registrado em receitas: R$ {valor}
- Diferença: R$ {valor}

### 3. Comprovantes × Despesas registradas
- Total comprovantes anexados: R$ {valor}
- Total despesas Plata-ou-Plomo: R$ {valor}
- Despesas sem comprovante: {lista — investigar}

## Classificação

Conferir que cada lançamento está em conta correta:
- [ ] Receitas separadas por tipo (vendas, serviços, financeira)
- [ ] Despesas operacionais (S&M, R&D, G&A) classificadas
- [ ] CapEx vs OpEx separado
- [ ] Pessoal (salários, encargos, pro-labore) por modalidade
- [ ] Tributos por categoria

## DRE preliminar

| Linha | Valor |
|---|---|
| Receita Bruta | R$ {valor} |
| (-) Impostos s/ Receita | R$ {valor} |
| **Receita Líquida** | R$ {valor} |
| (-) COGS | R$ {valor} |
| **Margem Bruta** | R$ {valor} ({%}) |
| (-) S&M | R$ {valor} |
| (-) R&D | R$ {valor} |
| (-) G&A | R$ {valor} |
| **EBITDA** | R$ {valor} ({%}) |
| (-) Depreciação | R$ {valor} |
| **EBIT** | R$ {valor} |
| (+/-) Resultado Financeiro | R$ {valor} |
| (-) IR/CSLL | R$ {valor} |
| **Lucro Líquido** | R$ {valor} |

## Variance vs forecast (FP&A LEP cruza)

- Receita: realizado vs forecast = ±{%}
- OPEX total: realizado vs forecast = ±{%}
- Top 3 desvios identificados:
  1. {linha} — {motivo}
  2. {linha} — {motivo}
  3. {linha} — {motivo}

## Aprovação

- [ ] Controller revisou
- [ ] Diretor Financeiro aprovou
- [ ] CFO aprovou (se >R$ 100k movimentação)

## Próximos Movimentos

1. Enviar DRE pro CEO LEP até dia 7
2. Atualizar projeção rolling 12m (FP&A LEP)
3. Provisionar tributos pra próximo mês
4. Arquivar fechamento em `_Areas/CFO/fechamentos/{YYYY-MM}/`
