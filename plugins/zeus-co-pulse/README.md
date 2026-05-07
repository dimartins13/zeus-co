# Zeus-CO — Pulse (Portfolio Health Specialist)

Specialist transversal que cruza **ClickUp** (tarefas) + **Dash Financeiro** (gastos) + **estado disco** (00_STAGE.md, LEARNINGS.md, BACKLOG.md) e produz painel acionável.

**Princípio:** Mostro só o que precisa de ação. Não relatório contemplativo.

## 3 formatos
1. **Pulse Empresa** — `pulse 2ndStreet`
2. **Pulse Portfolio** — `pulse` (sem args)
3. **Daily Alert** — cron 8h, só dispara se P0

## Health Score (5 dimensões)
Runway (25%) + Stage progress (25%) + Task velocity (20%) + Burn vs plan (15%) + Compliance (15%) = N/5

## Estrutura
- `skills/pulse/SKILL.md` + CORE + LITERATURE + RADAR
- `skills/pulse/templates/` — pulse-empresa, pulse-portfolio, daily-alert, alert-protocol

## Cron
- `pulse-daily` 8h (Haiku) — só notifica se P0
