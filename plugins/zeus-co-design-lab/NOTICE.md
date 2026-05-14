# NOTICE — Atribuições

O **DESIGN-LAB (zeus-co-design-lab)** é uma estrutura curada para uso interno do ecossistema Zeus / ZEUS-CO.
A maior parte do conteúdo aqui foi importada do projeto open-source `nexu-io/open-design`
(Apache 2.0), que por sua vez agrega skills da comunidade.

Este NOTICE preserva atribuição na linhagem completa:

## 1. Projeto-fonte

- **Open Design** — [nexu-io/open-design](https://github.com/nexu-io/open-design)
  Licença raiz: **Apache 2.0**.
  Versão usada: snapshot main em maio/2026 (~v0.2.x conforme CHANGELOG).
  Autores principais: equipe nexu-io (Berlim) e ~23 colaboradores.

## 2. Padrões importados

Os 5 padrões em `padroes-core/` derivam direto dos prompts e arquitetura do Open Design,
notadamente:

- `padroes-core/prompts-originais/system.ts` — system prompt completo do designer agent
- `padroes-core/prompts-originais/directions.ts` — 5 escolas visuais com palette OKLch
- `padroes-core/prompts-originais/discovery.ts` — turn-1 question-form pattern
- `padroes-core/prompts-originais/deck-framework.ts` — framework de decks magazine-style
- `padroes-core/prompts-originais/critique-*.ts` — critique 5-dim
- (e os demais: `media-contract.ts`, `panel.ts`, `research-contract.ts`, `official-system.ts`)

## 3. Skills curadas — atribuições upstream

Das 51 skills importadas, a maioria carrega o campo `upstream:` em seu próprio
SKILL.md frontmatter, apontando para o autor original. Exemplos:

- `creative-director` — curated from [@smixs](https://github.com/smixs/creative-director-skill)
- `marketing-psychology`, `ad-creative`, `copywriting`, `paywall-upgrade-cro` — comunidade Open Design
- `gsap-*` — GreenSock animation patterns
- `fal-*` — wrappers para a API da FAL.ai
- `pptx`, `docx`, `pdf` — adapters Anthropic skills
- `imagegen`, `imagen`, `sora`, `replicate` — provider wrappers

Para a atribuição específica de cada skill, ver o cabeçalho YAML do respectivo
`SKILL.md` (campos `upstream:`, `category:` e a seção `## Source`).

## 4. Design Systems

Os 66 sistemas em `design-systems/` foram destilados em formato `DESIGN.md` (9 seções:
color, typography, spacing, layout, components, motion, voice, brand, anti-patterns)
no projeto Open Design. Eles são **descrições inspiradas** em produtos reais
(Linear, Stripe, Vercel, Apple, Notion etc.) — **uso exclusivamente interno como
referência tipográfica e cromática**, conforme princípio 4 do `README.md`.

Marcas registradas (Apple®, Stripe®, Linear®, Vercel®, Notion®, Airbnb®, Canva®,
Spotify®, Wise®, Revolut®, Slack®, Discord®, Miro®, Intercom®, Nike®, Mastercard®,
Duolingo®, GitHub®, Anthropic®, Claude®, Cursor®, Figma®, Framer®, Supabase®,
Lovable®, Raycast®, Resend®, Sanity®, PostHog®, Sentry®, MongoDB®, Replicate®,
Mistral AI®, OpenAI®, ElevenLabs®, x.AI®, Ollama®, ClickHouse®, Cohere®,
Hugging Face®) são propriedade de seus respectivos detentores. Nenhum endosso é
implicado por sua inclusão como referência neste laboratório.

## 5. Daemon e infraestrutura — NÃO importados

Deliberadamente excluímos o `apps/daemon`, `apps/web`, `packages/`, build scripts,
e toda a stack Node/SQLite do Open Design. O runtime do DESIGN-LAB (zeus-co-design-lab) é o
Claude/Cowork. Apenas o conteúdo (Markdown, TypeScript de prompt) foi
trazido como referência ou material composável.

## 6. Direitos do Zeus

Adaptações, traduções para pt-BR, agregador `00-orquestrador/SKILL.md`, pipelines
de integração (`integracoes/*`) e a curadoria/estrutura de pastas são originais
do ecossistema Zeus / ZEUS-CO (Diego, 2026).

---

**Última atualização:** 2026-05-14
**Snapshot upstream:** `nexu-io/open-design` main (maio/2026)
