# TOOL_BINDINGS — CTO Office

| Intenção | Ferramenta |
|---|---|
| **Code work** | `dev-skills:*` (10 skills oficiais) + Claude Code |
| **Claude API** | `claude-api` skill |
| **Subagents** | `dev-skills:subagent-driven-development` + `dev-skills:dispatching-parallel-agents` |
| **TDD** | `dev-skills:test-driven-development` |
| **Plans** | `dev-skills:writing-plans` + `dev-skills:executing-plans` |
| **Reviews** | `dev-skills:requesting-code-review` + `dev-skills:receiving-code-review` |
| **Worktrees** | `dev-skills:using-git-worktrees` |
| **Debugging** | `dev-skills:systematic-debugging` |
| **Verification** | `dev-skills:verification-before-completion` |
| **Finishing** | `dev-skills:finishing-a-development-branch` |
| **Skills creation** | `anthropic-skills:skill-creator` + `lep-builder` |
| **MCP development** | `claude-plugins-official:mcp-server-dev` |
| **Architecture diagrams** | Miro MCP / Figma MCP |
| **Database (Postgres)** | Supabase MCP (instalado mas subutilizado conforme scout) |
| **Hostinger deploy** | `zeus-co-publisher:publisher` |

## Bindings por skill

- `cto` (chief) → orquestra + `claude-expert`
- `cto-vp-eng` → dev-skills:* + Claude Code direto
- `cto-pm` → ClickUp + Notion + Linear (se houver)
- `cto-ux-ui` → Figma MCP + Canvas Design
- `cto-data` → Supabase MCP + xlsx + cto-clickhouse (KP-specific)
- `cto-devops` → GitHub Actions + Hostinger FTP scripts
- `cto-qa` → dev-skills:test-driven-development + Playwright
- `cto-orquestrador` ⭐ NEW → coordena
- `cto-security` ⭐ NEW → WebSearch (OWASP) + clo-lgpd cross
- `cto-ai-ml` ⭐ NEW → claude-api + claude-expert + WebSearch (state of art)
- `cto-architect` ⭐ NEW → Miro + ADR docs
