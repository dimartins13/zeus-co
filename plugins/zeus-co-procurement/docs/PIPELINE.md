# PIPELINE — Procurement

> Procurement = compras ESTRATÉGICAS. Distinto:
> - **COO supply** = estoque + forecast
> - **COO vendor** = relacionamento dia-a-dia
> - **CFO AP** = pagamento + reconciliação
> - **Eu** = SOURCING + negociação + categoria estratégica

---

## Pipeline (8 fases)

### Fase 0 — Descoberta Interna
- CLAUDE.md + categorias atuais + spend histórico

### Fase 1 — Spend analysis
Owner: `procurement` + cross `cfo-controller`
- Top 20% fornecedores = 80% gasto?
- Categorias mapeadas
- Concentração de risco

### Fase 2 — Category strategy
Owner: `procurement-category-mgr`
- Por categoria: make/buy, single/dual/multi-source, contratual vs spot
- Output: `_Areas/Procurement/category-strategy.md`

### Fase 3 — Strategic sourcing (RFP/RFQ)
Owner: `procurement-strategic-sourcing`
- RFP (request proposals): grandes deals competitivos
- RFQ (request quotes): commodity
- Output: `_Areas/Procurement/rfps/<categoria>/`

### Fase 4 — Negotiation
Owner: `procurement-strategic-sourcing` + chief
- TCO (Total Cost of Ownership) framework
- Walk-away point
- BATNA
- Output: term sheet

### Fase 5 — Contract
Owner: cross `clo-contratos` + `coo-vendor`
- SLA + warranties + termination clauses
- Output: contrato assinado

### Fase 6 — Tail spend automation
Owner: `procurement-tail-spend`
- Compras < R$ 5k: cards corporativos + workflow leve
- AI-assisted (sugerir fornecedor ideal)
- Output: `_Areas/Procurement/tail-spend-policy.md`

### Fase 7 — Vendor performance
Owner: cross `coo-vendor` (dia-a-dia) + `procurement` (reviews)
- SLA tracking
- Quarterly business review
- Output: vendor scorecard

### Fase 8 — Savings tracking + reporting
Owner: `procurement` (chief)
- Savings vs baseline
- Input pra board pack

---

## Princípio inviolável

**TCO > preço unitário.** Preço barato + qualidade ruim + frete caro + multa atraso = caro total.
