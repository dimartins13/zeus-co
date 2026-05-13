# PIPELINE — COO Office

> COO opera **execução**. Tudo que acontece DEPOIS de venda fechada + produto criado é COO. Também: tudo que envolve QUALIDADE + PROCESSO.

---

## Fase 0 — Descoberta Interna (obrigatória)

- `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md`
- `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md`
- Manual operacional existente (se houver)
- Histórico de incidents (`_Areas/COO/incidents/`)

---

## Pipeline COO (11 fases)

### Fase 1 — SOP design (Process Engineering)
Owner: `coo-sops`
- Mapear processo crítico (SIPOC: Supplier, Input, Process, Output, Customer)
- Escrever SOP (Standard Operating Procedure)
- Identificar bottlenecks
- Output: `_Areas/COO/sops/<processo>.md`

### Fase 2 — Vendor selection
Owner: `coo-vendor`
- RFP, RFQ (Request for Quote)
- Vendor scorecard (preço + qualidade + tempo + risco)
- Contrato + SLA (com `clo-contratos`)
- Output: `_Areas/COO/vendors/<vendor>/agreement.pdf`

### Fase 3 — Supply chain
Owner: `coo-supply`
- Forecast de demanda (ligado com cmo + cfo-fpa)
- Sourcing + compras
- Inventory management (gestão de estoque)
- Output: `_Areas/COO/inventory.xlsx`

### Fase 4 — Logistics + fulfillment
Owner: `coo-logistics`
- Última milha (Correios, JadLog, Loggi, transportadora)
- Frete table
- Tracking + SLA delivery
- Logística reversa (devoluções)
- Output: `_Areas/COO/logistics-config.md`

### Fase 5 — Customer Operations (atendimento)
Owner: `coo-customer-ops`
- SAC (Service Center)
- Canais (WhatsApp, email, chat)
- Treinamento atendentes
- Escalation matrix
- Output: `_Areas/COO/customer-ops-playbook.md`

### Fase 6 — Returns + reverse logistics ⭐ NOVO
Owner: `coo-returns`
- Política de devolução/troca (CDC 7 dias + além)
- Processo reverso (logística + custodia + qualidade)
- Resseleção de produto retornado (revende? sucata? envia pra outlet?)
- Output: `_Areas/COO/returns-policy.md` + workflow

### Fase 7 — Quality Operations ⭐ NOVO
Owner: `coo-quality-ops`
- Quality control checkpoints
- Defect tracking (% defect, defect type)
- Root cause analysis (5 Whys, Fishbone)
- Continuous improvement (Kaizen)
- Output: `_Areas/COO/quality-metrics.xlsx`

### Fase 8 — PMO (Project Management Office) ⭐ NOVO
Owner: `coo-pmo`
- Projetos transversais multi-funcionais
- Methodology (Waterfall vs Agile vs Hybrid)
- Tracking + RAID log (Risks, Assumptions, Issues, Dependencies)
- Output: `_Areas/COO/projects/<project-name>/`

### Fase 9 — Ops Analytics + dashboards
Owner: `coo-diretor` + cruzamento com `cto-data`
- KPIs operacionais (NPS, CSAT, SLA delivery, defect rate, etc.)
- Dashboard tempo real
- Output: `_Areas/COO/ops-dashboard.html`

### Fase 10 — Reporting trimestral
Owner: `coo` (chief) + `coo-diretor`
- Ops review pra board
- Output: input pra `board-pack-builder`

### Fase 11 — Continuous improvement loop
Owner: `coo-quality-ops` + `coo-sops`
- Post-mortem de incidentes
- Atualização de SOPs
- Treinamento contínuo
- Output: `_Areas/COO/post-mortems/YYYY-MM-DD-<incident>.md`

---

## Princípio inviolável

**Processo NÃO documentado = processo que não escala.** SOP escrita > tribal knowledge. Sempre.
