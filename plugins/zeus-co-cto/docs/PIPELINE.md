# PIPELINE — CTO Office

> CTO opera **tech + produto digital + dados + AI + segurança**. Princípio: **Boring Tech > Shiny Tech** (Choose Boring Technology, Dan McKinley).

---

## Fase 0 — Descoberta Interna (obrigatória)

- `CLAUDE.md` + tech stack atual + repositórios + infra

---

## Pipeline CTO (12 fases)

### Fase 1 — Stack decision (foundation)
Owner: `cto` + `cto-architect`
- Frontend, backend, database, hosting
- Boring tech default (HTML/CSS/JS + PostgreSQL + Hostinger PHP/Node)
- Output: `_Areas/CTO/stack-decision.md`

### Fase 2 — Architecture
Owner: `cto-architect`
- System design + diagrams
- Service boundaries + APIs
- Scaling plan
- Output: `_Areas/CTO/architecture.md`

### Fase 3 — Product roadmap
Owner: `cto-pm`
- Discovery (user research)
- PRDs (Product Requirements)
- Prioritization (RICE/ICE)
- Output: `_Areas/CTO/roadmap.md`

### Fase 4 — UX/UI Design
Owner: `cto-ux-ui`
- User flows + wireframes
- Design system
- Prototype
- Output: `_Areas/CTO/design-system.md`

### Fase 5 — Engineering execution
Owner: `cto-vp-eng`
- Sprints + code review
- Stack maintenance
- Output: GitHub commits

### Fase 6 — Quality (testing + automation)
Owner: `cto-qa`
- Test strategy
- Automation framework
- E2E + integration + unit
- Output: `_Areas/CTO/test-strategy.md`

### Fase 7 — DevOps + Infrastructure
Owner: `cto-devops`
- CI/CD pipeline
- Monitoring + observability
- Deploy strategy
- Output: `_Areas/CTO/devops-runbook.md`

### Fase 8 — Security ⭐ NOVO
Owner: `cto-security`
- Threat modeling
- Pentest cadence
- Incident response plan
- LGPD compliance tech (cross com clo-lgpd)
- Output: `_Areas/CTO/security-policy.md`

### Fase 9 — Data engineering + analytics
Owner: `cto-data`
- ETL pipelines
- Data warehouse
- Dashboards
- Output: `_Areas/CTO/data-architecture.md`

### Fase 10 — AI / ML ⭐ NOVO
Owner: `cto-ai-ml`
- Use case prioritization
- LLM API integrations (Claude, OpenAI)
- Custom models (when needed)
- AI governance + cost control
- Output: `_Areas/CTO/ai-strategy.md`

### Fase 11 — Tech debt + refactor
Owner: `cto-vp-eng` + `cto-architect`
- Tech debt log
- Refactor budget (20% sprint time)
- Output: `_Areas/CTO/tech-debt-log.md`

### Fase 12 — Reporting
Owner: `cto` (chief)
- Tech KPIs (uptime, deployment frequency, MTBF, MTTR)
- Output: input pra `board-pack-builder`

---

## Princípio inviolável

**Boring Tech.** Cada nova tecnologia tem "innovation token" que custa caro. Gaste tokens onde gera diferenciação real, não em moda.
