# LITERATURE — CTO

## Camada 1 — Canônica (10 obras)

| Obra | Autor (ano) | Por que importa |
|---|---|---|
| **The Mythical Man-Month** | Fred Brooks (1975) | Brooks's Law. Hoje vale ainda mais com agentes AI. |
| **The Pragmatic Programmer** | Hunt & Thomas | Clássico de boas práticas. Fundamentos atemporais. |
| **Designing Data-Intensive Applications** | Martin Kleppmann (2017) | Bíblia moderna de sistemas distribuídos. |
| **Inspired** | Marty Cagan (2008/2017) | Product management. Outcome > feature. |
| **The Lean Startup** | Eric Ries (2011) | MVP, build-measure-learn aplicado a tech. |
| **Accelerate** | Forsgren, Humble, Kim (2018) | DORA metrics. Como times de alta performance operam. |
| **Working Backwards** | Bryar & Carr (2021) | Modelo Amazon (PR/FAQ, S-team, two-pizza teams). |
| **Boring Technology Manifesto** | Dan McKinley (essay) | Por que escolher tech "chata". Resgate de bom senso. |
| **Software Engineering at Google** | Winters/Manshreck | Como Google opera engenharia em escala. |
| **Building Microservices** | Sam Newman | Quando microserviços valem (e quando não). |

### Bônus contemporâneo
- **Paul Graham essays sobre tech** — "Hackers and Painters", "The Refragmentation"
- **Ben Thompson Stratechery** — análise de plataformas e tech business
- **Martin Fowler blog** — patterns e arquitetura

## Camada 2 — Fontes vivas

### Newsletters
- **The Pragmatic Engineer** (Gergely Orosz) — gold standard de eng leadership
- **High Growth Engineer** — eng careers + practices
- **Bytes** — JS/React weekly
- **TLDR** — daily tech news
- **Software Lead Weekly**
- **Refactoring** — code quality

### Brasil
- **DevTo BR** — comunidade
- **Code/Drops (Rocketseat)** — tutoriais BR
- **PHPLover, RubyOnRailsBrazil** — comunidades específicas
- **Locaweb blog** — hosting BR

### Podcasts
- **Software Engineering Daily**
- **The Changelog**
- **Hipsters.tech** (BR — Alura)
- **Lex Fridman** (entrevistas com tech leaders)
- **Acquired** — histórias de empresas tech

### Comunidades
- **HackerNews** — diário
- **dev.to**
- **Reddit r/ExperiencedDevs, r/cscareerquestions**
- **Discord servers** (Vercel, Supabase, Next.js)

## Camada 3 — Cases (12)

| Caso | Empresa | Lição |
|---|---|---|
| Stripe DX | Stripe | Documentation as product. API design pristine. |
| Shopify monolith → modular | Shopify | Não fragmentou em microserviços. Monolito modular. |
| Basecamp ruby majestic monolith | Basecamp | Anti-microservices. Foco em simplicidade. |
| GitHub scaling | GitHub 2008-2024 | Rails monolito até bilhões de requests. |
| Slack realtime | Slack | WebSockets em escala global. |
| Notion architecture | Notion | Block-based data model. |
| Figma multiplayer | Figma | CRDT em browser. Eng feat. |
| Vercel edge | Vercel | Edge computing como produto. |
| Supabase Postgres-first | Supabase | Open-source alternative to Firebase. |
| Discord migration Go → Rust | Discord | Quando migrar linguagem (apenas quando dor justifica). |
| Twitter "fail whale" | Twitter early | Lição: monitoring é vida. |
| Hashicorp open-core | Hashicorp | OSS + comercial. Modelo replicável. |

## Camada 4 — Brasil

### Cases BR
- **Nubank Clojure** — escolha pragmática (linguagem rara mas adequada). Mantém até hoje.
- **iFood scale** — Java + Kotlin + Kafka pra real-time. Ops pesada.
- **Stone tech stack** — Elixir + Phoenix em fintech. Concorrência de alto volume.
- **Magazine Luiza modernization** — legado Java + microserviços + cloud.
- **Mercado Livre** — uma das maiores eng techs LatAm. Java/Kotlin core.
- **Locaweb** — provedor BR. Conhecimento de mercado BR.

### Particularidades BR
- **Pix integration** — toda fintech/checkout precisa nativo. APIs de cada banco.
- **NF-e API** — emissão automática via SEFAZ. Bling, Tiny, Conta Azul oferecem.
- **LGPD compliance** — by design. CTO decide arquitetura de dados pra ser compliant.
- **Hospedagem BR vs internacional** — latência matter. AWS São Paulo, GCP, Locaweb, KingHost, Hostinger SP.
- **Custo cloud em real** — preço dolarizado afeta decisão. Hostinger e BR providers podem ser mais econômicos pra cargas pequenas.

## Camada 5 — Skills mapeadas

### `dev-skills:*` (12 skills)
- writing-plans, executing-plans, writing-skills, requesting-code-review, receiving-code-review, test-driven-development, systematic-debugging, verification-before-completion, dispatching-parallel-agents, subagent-driven-development, using-git-worktrees, brainstorming, finishing-a-development-branch, using-superpowers

### Anthropic dev
- `anthropic-skills:*` (mesmas + brainstorming, executing-plans, dispatching-parallel-agents, using-superpowers)
- `claude-api` — Claude API integration
- `mcp-server-dev` — construir MCPs
- `agent-sdk-dev` — construir agentes
- `playwright` — automação browser
- `context7` — docs atualizados de libs

### Plugins úteis para CTO
- `serena` — code intelligence
- `greptile`, `github`, `gitlab` — repo intelligence
- `firebase`, `supabase` — backends
- `terraform` — IaC
- `linear` — issue tracking
- `Claude Preview` — preview rápido

### Web building
- `anthropic-skills:web-artifacts-builder` — artifacts ricos
- `anthropic-skills:canvas-design`

---

Sources usadas:
- The Pragmatic Engineer
- Boring Technology Manifesto (Dan McKinley)
- DORA report (Accelerate)
