# PIPELINE — CRO Office (Sales/Vendas)

> CRO converte demanda gerada pelo CMO em RECEITA. Distinto: CMO faz lead. CRO fecha venda + retém + expande.

---

## Fase 0 — Descoberta Interna (obrigatória)

- `CLAUDE.md` + estágio + modelo de receita
- `_Areas/CMO/` (demanda gerada que CRO converte)
- `_Areas/CFO/unit-economics.xlsx` (CAC/LTV alvo)

---

## Pipeline CRO (10 fases)

### Fase 1 — Sales motion design
Owner: `cro` + `cro-vp-sales`
- B2C self-serve / B2C high-touch / B2B SMB / B2B enterprise / marketplace
- Sales cycle length alvo
- Touch points até closing
- Output: `_Areas/CRO/sales-motion.md`

### Fase 2 — ICP refinement
Owner: `cro` + cruzamento `xpto-mk:estrategista-marketing`
- Ideal Customer Profile detalhado
- Buyer personas
- Output: `_Areas/CRO/icp.md`

### Fase 3 — Sales playbook
Owner: `cro-sales-enablement`
- Discovery questions
- Objection handling
- Pricing conversations
- Closing techniques
- Output: `_Areas/CRO/sales-playbook.md`

### Fase 4 — Pipeline + CRM setup
Owner: `cro-revops`
- CRM (HubSpot/Salesforce/Pipedrive) configurado
- Stages canon (Discovery → Qualification → Proposal → Negotiation → Closed)
- Forecast methodology
- Output: `_Areas/CRO/crm-config.md`

### Fase 5 — BDR / SDR motion (Top of Funnel)
Owner: `cro-bdr-mgr`
- Inbound qualification (MQL → SQL)
- Outbound prospecting (cadências, sequences)
- Lead scoring
- Output: `_Areas/CRO/bdr-playbook.md`

### Fase 6 — AE (closing) motion
Owner: `cro-account-executive`
- Discovery → Demo → Proposal → Negotiation → Close
- MEDDIC / SPIN selling
- Output: `_Areas/CRO/ae-playbook.md`

### Fase 7 — Customer Success (post-sale)
Owner: `cro-customer-success`
- Onboarding canônico
- Health score
- Renewal flow
- Expansion plays (upsell, cross-sell)
- Output: `_Areas/CRO/cs-playbook.md`

### Fase 8 — Sales analytics + forecast
Owner: `cro-revops`
- Pipeline metrics (conversion rates, velocity, ACV)
- Forecast (weighted pipeline)
- Win/loss analysis
- Output: `_Areas/CRO/sales-dashboard.md`

### Fase 9 — Compensation plan
Owner: `cro-vp-sales` + cross `cfo` + `clo-trabalhista`
- Comp plan (base + comissão + acelerador)
- Quotas
- SPIFFs (incentivos pontuais)
- Output: `_Areas/CRO/comp-plan.md`

### Fase 10 — Reporting
Owner: `cro` (chief)
- Mensal: forecast vs realizado
- Input pra `board-pack-builder`

---

## Princípio inviolável

**Toda demanda gerada pelo CMO mas não convertida = falha do CRO.** Não cobrar do CMO. Investigar pipeline + processo + capacidade time.
