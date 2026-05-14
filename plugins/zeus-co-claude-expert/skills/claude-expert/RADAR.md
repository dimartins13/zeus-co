# RADAR — Claude Platform Specialist

## ✅ Instalados (componentes Claude do Diego)

### Plugins core (oficiais)
- `claude-code-setup`, `claude-md-management`, `commit-commands`, `code-review`, `code-simplifier`
- `feature-dev`, `frontend-design`, `mcp-server-dev`, `agent-sdk-dev`, `claude-api`
- `playground`, `plugin-dev`, `pr-review-toolkit`, `security-guidance`, `session-report`
- `skill-creator`, `hookify`, `ralph-loop`, `explanatory-output-style`, `learning-output-style`
- LSP plugins (typescript, pyright, gopls, ruby, swift, csharp, etc — só ativar quando linguagem em uso)

### MCPs externos conectados
- 16 MCPs externos: asana, context7, discord, fakechat, firebase, github, gitlab, greptile, imessage, laravel-boost, linear, playwright, serena, supabase, telegram, terraform
- Custom: gemini-video, video, scheduled-tasks
- Plugins-ecosystem: 1c4e78c8 (Adobe), 220c44d9 (Google Drive), 2801b3d7 (Gamma), 3a7681c7 (Gmail), 3ca73a72 (Calendar), 60f907d8 (ClickUp), 796ab82d (Adobe Marketing), 8984f484 (Canva), Claude Preview, dd613414 (Higgsfield), fdcd0fac (Figma), Freepik, mcp-image, mcp-registry
- Plugins finance/marketing: brand-voice, financial-analysis, equity-research, private-equity, investment-banking, wealth-management, finance, marketing, dev-skills, zeus-co-cmo, zeus-co-cco, zeus-co-marketing, anthropic-skills

### Skills do Zeus-CO construídos hoje (Sprint A)
- `zeus-co-factory` (lep-builder)
- `zeus-co-ceo`, `cfo`, `coo`, `cmo`, `cco`, `cto`, `clo`
- `zeus-co-claude-expert` (este)

### Custom MCPs do Diego
- `gemini-video`, `video` (em `Claude Code e Higgsfield/00_Estudio/.credentials/wrappers/`)

## 🔍 Avaliando
*Nada em avaliação ativa.*

## 🎯 Wishlist (gaps de plataforma identificados)

| Gap | Tool ideal |
|---|---|
| **Token usage analytics dashboard** | Anthropic console + custom dashboard |
| **MCP performance monitoring** | Custom |
| **Skill activation tracking** (qual skill foi ativada quando) | Hook custom |
| **Cost per project breakdown** | Custom |
| **Cron run reports automated** | Já parcial via scheduled-tasks |
| **A/B testing prompts** | Manual via subagents |

## 📅 Radar Semanal

Cron `claude-expert-weekly` (sábado 10h) varre:
- **Anthropic blog + Claude Engineering blog** — features novos, deprecations
- **Claude Code Docs changelog** — novas docs e atualizações
- **Claude API Docs changelog** — novos endpoints, mudanças
- **anthropic-cookbook github** — novos notebooks/exemplos
- **awesome-claude-code github** — adições à curated list
- **Pricing page** — qualquer mudança de preço
- **mcp-registry** — novos MCPs disponíveis

Cron `claude-expert-audit` (mensal, dia 1 9h) faz audit profundo:
- Quantos tools ativos?
- CLAUDE.md tamanho atual vs ideal
- Skills com descriptions overlong
- Cost summary (se acessível)
- Recomendações de otimização

## 🚫 Descartados
*Vazio.*

## Princípio
**Antes de instalar QUALQUER plugin/MCP novo:**
1. Quanto adiciona ao input por turno (tool definitions)?
2. Quantas vezes/semana será usado de fato?
3. Existe alternativa lighter (skill em vez de MCP)?
4. Vale a economia de tempo do Diego pelo custo?

Se resposta a 3 ou 4 = "não claramente sim" → descartar ou colocar em wishlist.

---
