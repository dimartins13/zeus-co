# LITERATURE — Claude Platform Specialist

> Curadoria atualizada pelo cron `claude-expert-weekly`. Foco: máximo aproveitamento + redução custos.

## Camada 1 — Fontes oficiais Anthropic (PRIMÁRIAS, sempre canônicas)

| Fonte | URL | Frequência leitura |
|---|---|---|
| **Claude Code Docs** | [code.claude.com/docs](https://code.claude.com/docs) | Mensal — toda atualização de feature |
| **Claude API Docs** | [platform.claude.com/docs](https://platform.claude.com/docs) | Mensal |
| **Anthropic Blog** | [anthropic.com/news](https://www.anthropic.com/news) | Semanal |
| **Claude Engineering Blog** | [claude.com/blog](https://claude.com/blog) | Semanal — posts deep-dive |
| **Anthropic Cookbook** | [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | Mensal |
| **Pricing page** | [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) | Mensal |
| **Status page** | [status.claude.com](https://status.claude.com) | Quando suspeitar problema |
| **Model Cards** | platform.claude.com/docs/en/about-claude/models | Sempre que sair modelo novo |
| **Prompt Caching docs** | [platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | Mensal — feature evolui |
| **Skills docs** | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) | Mensal |

## Camada 2 — Posts canônicos (já lidos, manter referência)

### Otimização de tokens / custo
- **"Lessons from building Claude Code: Prompt caching is everything"** — Anthropic blog. Foundational. Por que cache é não-negociável em agentes.
- **"Claude Code Token Optimization: Stop the $1,600 Bill (2026)"** — Build to Launch. Caso real de redução.
- **"Manage costs effectively"** — Claude Code Docs oficial.
- **"7 Practical Ways to Reduce Claude Code Token Usage"** — KDnuggets.
- **"18 Claude Code Token Management Hacks"** — MindStudio.
- **"Token optimization 2026: Saving up to 80%"** — Obvious Works.
- **Branch8 case** — 6 pessoas, 6 meses, 72% redução ($2,400 → $680 mês 3).

### Arquitetura de extensibilidade
- **"Understanding Claude Code's Full Stack: MCP, Skills, Subagents, Hooks"** — alexop.dev. Visão completa.
- **"Claude Code Skills vs MCP vs Plugins: Complete Guide 2026"** — morphllm.com.
- **"How I Use Every Claude Code Feature"** — Shrivu Shankar.
- **"The Complete Claude Code Power User Guide"** — DEV Community.
- **awesome-claude-code repo** ([github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)) — curated list.

### Skills authoring
- **anthropic-skills/skill-creator** — base oficial.
- **anthropic-skills/writing-skills** — guia.
- **Plugin oficial skill-creator** instalado.

## Camada 3 — Princípios destilados (cheat sheet operacional)

### Prompt caching (90% economia em cache hit)
1. **Sempre on em produção.**
2. **5-min TTL** = 1.25x write. Vale após 1 read. Use em chat ativo.
3. **1-hour TTL** = 2x write. Vale após 2 reads. Use em workflows longos / batch.
4. **NÃO mude tool set mid-conversa** — invalida cache.
5. **NÃO troque modelo mid-conversa** — cache rebuild.
6. **Cache breakpoint automático** padrão = bom.
7. **Workspace isolation** desde fev/2026 — caches isolados por workspace.

### Model routing (Opus 15x mais caro que Haiku)
- **Haiku** — classificação, extração, crons leves
- **Sonnet** — DEFAULT (80% do uso)
- **Opus** — análise profunda + decisão crítica

### Context management
- `/context` — diagnose
- `/clear` — switch de assunto (preserva CLAUDE.md + memória)
- `/cost` — sessão atual
- `/compact` — quando histórico > 30 turnos
- `/rename` antes de `/clear` (findability)

### CLAUDE.md
- Auto-loaded EVERY turn
- 5K tokens × 200 turns = 1M tokens cobrados
- Princípios > detalhes inline
- Use ponteiros pra docs detalhados (`COMPANY-OS.md`, etc)
- Limite recomendado: <200 linhas

### Skills
- `name` + `description` SEMPRE no contexto (1% do context window, fallback 8K chars)
- Body carregada quando ativada (<500 linhas ideal)
- Resources (scripts, references, assets) sob demanda
- Skill description é "pushy" — instrua quando usar com phrases-gatilho explícitas

### MCPs
- Tool definitions são parte do cached prefix — cada MCP novo aumenta input por turno
- Auditar antes de instalar: quantos tools? quanto pesa o schema?
- MCP > skill quando precisa auth/network/external system
- Skill > MCP quando metodologia/conhecimento

### Subagents (Task tool)
- Próprio context window — bom pra pesquisa pesada
- Caro no setup mas isola output
- Use para: discovery cross-platform, code search amplo, brainstorming paralelo, análises com >5 fontes

### Hooks
- Rodam fora do Claude — gratuitos em tokens
- SessionStart, PostToolUse, etc.
- Use para: hard requirements (lint, validation, format), automação determinística

### Plan mode (ExitPlanMode)
- Planeja antes de executar
- Reduz refazer
- Tokens de plan < tokens de retrabalho

## Camada 4 — Tendências 2026 (atualizado pelo cron)

### Confirmado (maio 2026)
- Workspace-level cache isolation (fev/2026)
- Cache TTL options: 5min e 1hr
- Skills > Slash Commands (custom slash commands foram merged em skills)
- Plugins agrupam skills + MCPs + hooks + commands
- Sub-agents via `Task` tool

### Vigilar
- Cache TTL changes (Anthropic já fez cuts)
- Pricing changes
- Novos modelos (Sonnet 4.7? Haiku 5? Opus 5?)
- MCP registry growing rápido
- Novos features de plataforma (extended thinking, computer use, etc)

## Camada 5 — Skills mapeadas

### Plugins instalados úteis
- `claude-code-setup` — configuração inicial
- `claude-md-management` — manutenção de CLAUDE.md
- `claude-api` — desenvolvimento com SDK
- `mcp-server-dev` — construir MCPs
- `agent-sdk-dev` — construir agentes
- `skill-creator` (já instalado oficial) — criar skills
- `hookify` — configurar hooks
- `update-config` — settings.json
- `keybindings-help` — atalhos

### Skills do ecossistema do Diego
- `update-config` — settings.json updates
- `simplify` — review e simplificação de código (aplicável a skills)
- `fewer-permission-prompts` — auditoria de permissions
- `dev-skills:*` — várias úteis (writing-skills, dispatching-parallel-agents)

## Heurística de citação

"Pelo Lessons from building Claude Code (Anthropic blog), o cron `cfo-weekly` está re-carregando tools desnecessariamente — vou consolidar em 1 chamada batch e economizar ~30% input/run."

---

Sources iniciais:
- [Lessons from building Claude Code: Prompt caching is everything (Anthropic)](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)
- [Manage costs effectively (Claude Code Docs)](https://code.claude.com/docs/en/costs)
- [Prompt caching (Claude API Docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Claude Code Token Optimization 2026 (Build to Launch)](https://buildtolaunch.substack.com/p/claude-code-token-optimization)
- [7 Practical Ways to Reduce Claude Code Token Usage (KDnuggets)](https://www.kdnuggets.com/7-practical-ways-to-reduce-claude-code-token-usage)
- [Understanding Claude Code's Full Stack (alexop.dev)](https://alexop.dev/posts/understanding-claude-code-full-stack/)
- [Claude Code Skills vs MCP vs Plugins (morphllm)](https://www.morphllm.com/claude-code-skills-mcp-plugins)
- [How I Use Every Claude Code Feature (Shrivu Shankar)](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)
- [Anthropic API Pricing 2026 (Finout)](https://www.finout.io/blog/anthropic-api-pricing)
- [awesome-claude-code (curated)](https://github.com/hesreallyhim/awesome-claude-code)

*Última varredura: 2026-05-07.*
