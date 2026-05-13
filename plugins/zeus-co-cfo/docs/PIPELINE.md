# PIPELINE — CFO Office

> CFO opera 6 funções canônicas: P2P (Procure to Pay), O2C (Order to Cash), Treasury, FP&A, Tax, R2R (Record to Report).
> Princípio: **CFO mostra REALIDADE financeira, não conforto.**

---

## Fase 0 — Descoberta Interna (obrigatória)

- `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md`
- `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md`
- BP financeiro existente (se houver — `*BP*.xlsx`)
- Dashfin (Plata-ou-Plomo) dados da empresa
- `_Areas/Board/cap-table.xlsx` se existir

---

## Pipeline CFO (12 fases)

### Fase 1 — Setup contábil + plano de contas
Owner: `cfo-controller`
- Plano de contas (centros de custo + receita)
- Software contábil (Conta Azul, Omie, Bling, ERP)
- Regime tributário (Simples vs Presumido vs Real)
- Output: `_Areas/CFO/setup-contabil.md`

### Fase 2 — Cash flow forecast
Owner: `cfo-fpa` + `cfo-treasury`
- 12-meses rolling forecast
- Cenários (base / otimista / pessimista)
- Output: `_Areas/CFO/cash-flow-forecast.xlsx`

### Fase 3 — Default Alive checkpoint (cadência semanal)
Owner: `cfo-fpa`
- Runway atual + burn + projected break-even
- Output: linha em `_Areas/CFO/default-alive-log.md`

### Fase 4 — Unit economics
Owner: `cfo-fpa`
- CAC, LTV, payback, gross margin, contribution margin
- Por canal de aquisição
- Output: `_Areas/CFO/unit-economics.xlsx`

### Fase 5 — Accounts Payable (P2P)
Owner: `cfo-ap-specialist` ⭐ NOVO
- Aprovação de despesas (workflow)
- Pagamento fornecedores (cronograma)
- Reconciliação NF-e
- Output: `_Areas/CFO/ap-schedule.xlsx`

### Fase 6 — Accounts Receivable (O2C)
Owner: `cfo-ar-specialist` ⭐ NOVO
- Cobrança ativa
- Dunning automatizado
- Inadimplência tracking
- Output: `_Areas/CFO/ar-aging.xlsx`

### Fase 7 — Treasury + caixa
Owner: `cfo-treasury`
- Saldo diário
- Investimento curto prazo (CDI, RF)
- Bank reconciliation
- Output: `_Areas/CFO/treasury-daily.md`

### Fase 8 — Investimentos de caixa
Owner: `cfo-investimentos` ⭐ NOVO
- Caixa parado em CDI (default)
- Tesouro Direto (Selic, IPCA, prefixado)
- Fundos com liquidez D+0/D+1
- Política de investment policy escrita
- Output: `_Areas/CFO/investment-policy.md`

### Fase 9 — Tax + DARF
Owner: `cfo-tax`
- DARF mensal (IRPJ, CSLL, PIS, COFINS, ICMS, ISS)
- Planejamento tributário (regime)
- Reforma Tributária 2026 monitoring (IBS/CBS)
- Output: `_Areas/CFO/tax-calendar.md`

### Fase 10 — Fechamento mensal (R2R)
Owner: `cfo-controller`
- Reconciliação bancária
- Provisões + acruals
- DRE + BP + DFC mensais
- Output: `_Areas/CFO/closing-YYYY-MM.md`

### Fase 11 — Variance analysis
Owner: `cfo-fpa`
- Realizado vs orçado
- Drivers de variação
- Output: `_Areas/CFO/variance-YYYY-MM.md`

### Fase 12 — Reporting (board + Diego)
Owner: `cfo-diretor` + `cfo` (chief)
- Mensal: 1-page financial dashboard
- Trimestral: full pack ao board
- Output: link em `_Areas/Board/board-packs/`

---

## Princípio inviolável

**Default Alive checkpoint TODA SEMANA, mesmo quando não tem mudança.** Sem isso, fundador descobre crise tarde demais.
