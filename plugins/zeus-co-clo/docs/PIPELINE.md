# PIPELINE — CLO Office

> CLO opera **legal, compliance, IP, regulação setorial, contratos**. Não substitui advogado humano em casos críticos — orquestra preparação + monitora exposição.

---

## Fase 0 — Descoberta Interna (obrigatória)

- `CLAUDE.md` + estatuto + contratos existentes + regulação aplicável

---

## Pipeline CLO (11 fases)

### Fase 1 — Estrutura societária
Owner: `clo-contratos` + `cap-table-keeper` cross
- LTDA / SA / Holding
- Acordo de quotistas
- Output: `_Areas/CLO/estrutura-societaria.md`

### Fase 2 — Compliance baseline
Owner: `clo-compliance`
- Programa de compliance (Lei 12.846/13 Anticorrupção)
- Código de conduta
- Canal de denúncia
- Output: `_Areas/CLO/compliance-program.md`

### Fase 3 — LGPD foundation
Owner: `clo-lgpd`
- Política de privacidade
- Termos de uso
- RoPA (Registro de Operações de Tratamento)
- DPO designation
- Output: `_Areas/CLO/lgpd-foundation.md`

### Fase 4 — IP foundation
Owner: `clo-ip`
- INPI marca registro
- Patentes se aplicável
- Copyright (software, conteúdo)
- Output: `_Areas/CLO/ip-portfolio.md`

### Fase 5 — Regulação setorial
Owner: `clo-setorial`
- Mapeamento regulatório (SECAP, ANVISA, ANCINE, BACEN, etc.)
- Licenças necessárias
- Compliance cadence
- Output: `_Areas/CLO/regulation-map.md`

### Fase 6 — Trabalhista
Owner: `clo-trabalhista`
- CLT vs PJ vs MEI vs sócio
- Vesting de equity em CLT (passivo)
- Demissão handbook
- Output: `_Areas/CLO/trabalhista-policy.md`

### Fase 7 — Contratos lifecycle
Owner: `clo-contratos`
- Templates (NDAs, vendor, customer, partner)
- Contract Lifecycle Management (CLM)
- Renovações + monitoramento prazos
- Output: `_Areas/CLO/contracts-CLM.md`

### Fase 8 — Litigation (defensivo) ⭐ NOVO
Owner: `clo-litigation`
- Mapping de processos ativos
- Reservas judiciais (provisão CFO)
- Estratégia defensiva
- Output: `_Areas/CLO/litigation-log.md`

### Fase 9 — M&A + transações estruturais ⭐ NOVO
Owner: `clo-ma`
- Due diligence preparation
- SPA (Share Purchase Agreement) negotiation
- Closing checklists
- Output: `_Areas/CLO/transactions/`

### Fase 10 — Risk dashboard
Owner: `clo` (chief)
- Top risks mapeados
- Mitigation status
- Reporting trimestral
- Output: `_Areas/CLO/risk-dashboard.md`

### Fase 11 — Reporting
Owner: `clo` (chief) + `clo-orquestrador`
- Input pra `board-pack-builder`
- Briefings pro Diego

---

## Princípio inviolável

**Decisão legal de impacto > R$ 100k = advogado humano externo, não só LEPs.** LEP prepara, humano valida.
