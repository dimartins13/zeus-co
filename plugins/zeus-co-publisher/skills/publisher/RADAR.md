# RADAR — Publisher

## ✅ Disponíveis

### FTP / SFTP
- **Bash + Python ftplib** — caminho atual padrão (sem MCP nativo Hostinger)
- **lftp** — CLI FTP avançado se disponível (`brew install lftp`)
- **rsync over SSH** — se Hostinger habilitar SSH (atualmente só FTP)

### File comparison
- **diff** (CLI) — para JSON simples
- **jq** — manipular JSON estruturado
- **Python json + difflib** — diff inteligente

### MCP relevantes
- `mcp__220c44d9...` (Google Drive) — para arquivar backups críticos secundários
- `mcp-image`, `gamma`, `canva` — para renderizar artefatos antes de publicar

### Skills do workspace
- `dev-skills:writing-plans` — quando deploy é complexo
- `marketing:performance-report` — quando o que vai pro ar é relatório

## 🔍 Avaliando
*Vazio.*

## 🎯 Wishlist

| Gap | Tool ideal |
|---|---|
| **MCP Hostinger nativo** | API Hostinger (existe limitada — investigar) |
| **MCP FTP genérico** | Não existe, criar via mcp-server-dev se justificar |
| **Cloudflare Pages MCP** | API Cloudflare (alternativa Hostinger pra sites estáticos) |
| **Vercel MCP** | API Vercel (pra projetos Next/React) |
| **GitHub Actions trigger** | gh CLI + actions (alternativa CI/CD) |

## 📅 Radar Semanal
*Cron pode rodar mensal pra avaliar novos PaaS (Cloudflare Pages, Vercel, Railway, Render) que possam complementar Hostinger.*

## ⚠️ Segurança crítica

**RED FLAG ATUAL:** credenciais FTP estão em texto plano em `/Users/diegomartins/Documents/Claude/Projects/Dash Financeiro/prompt-contexto-servidor.md`.

**Ação P0 ao Diego:**
1. Mover `Host`, `User`, `Pass` pro 1Password (item: "Hostinger plataouplomo FTP")
2. Substituir no `.md` por placeholder: `[1Password: Hostinger plataouplomo FTP]`
3. Próximas invocações Publisher leem do 1Password (manualmente Diego cola) ou pedem na hora

**NÃO subir** este arquivo Markdown com credenciais pra Git público nem repo do marketplace zeus-co.
