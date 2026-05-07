# RADAR — Pulse

## ✅ Instalados (fontes de dados)

### ClickUp (PRINCIPAL fonte de tarefas)
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_get_workspace_hierarchy` — estrutura
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_filter_tasks` — buscar tarefas P0/P1
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_search` — search geral
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_get_task` + `_get_task_comments` + `_get_task_time_entries`
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_get_time_entries` — burn de tempo
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_get_task_time_in_status` — tempo em status (parado?)
- `mcp__60f907d8-3487-44b5-af75-cfd30ec35afe__clickup_get_chat_channels` + messages

### Dash Financeiro (PRINCIPAL fonte de custos)
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/dashboard-financeiro.html` — visualização
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/server/app.py` — Flask backend
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/server/users.json` — auth
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/Comprovantes de conta/` — comprovantes
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/extrair-dados.html` — extrator
- `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/Plata-ou-Plomo-Documentacao.md` — sistema doc

### Estado das empresas (lê do disco)
- Cada `[empresa]/00_STAGE.md` — checklist progresso
- Cada `[empresa]/LEARNINGS.md` — lições (cross-empresa)
- Cada `[empresa]/BACKLOG.md` — backlog atual
- Cada `[empresa]/_Areas/CFO/` — modelos financeiros, default-alive

### Comunicação
- `/Users/diegomartins/Documents/Claude/Projects/INBOX.md` — append alertas P0

## 🔍 Avaliando
*(vazio)*

## 🎯 Wishlist

| Gap | Tool ideal |
|---|---|
| **Hostinger billing direto** | API Hostinger sem MCP oficial |
| **Stripe billing por empresa** | Stripe MCP completo |
| **Cartão crédito gastos categorizados** | Bank/Brex API integration |
| **Notion task tracking complementar** | Notion MCP (já tem mas pra projetos não-ClickUp) |
| **Calendar burn time** | Google Calendar (já MCP) — mapear tempo Diego por empresa |

## Estratégia de pulling

Pra evitar pulls grandes a cada chamada:
1. Cache local (esta sessão) de hierarchy ClickUp
2. Filter tasks com query específica (P0/P1 + due date < 14d)
3. Dash Financeiro lido apenas semanalmente (gastos não mudam rápido) — exceto se Diego pede explicitamente
4. Cron diário roda Haiku pra reduzir custo
