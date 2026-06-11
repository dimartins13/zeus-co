---
name: human-carrossel
description: News-to-Carrossel V2.5 — sistema de carrosséis Instagram em duas frentes simultâneas. Frente 1 — geração DIÁRIA automatizada (R1 Routine Remote varre fontes editoriais via web_search/web_fetch e popula database `🗞️ News Feed` no Notion 3×/dia; R2 Routine Local dispara 08:00 a partir do primeiro tick `*/30` do Claude Desktop, lê Brand Identity + Manual editorial + Engine de headlines + Arquitetura narrativa, escolhe notícia, extrai foto da notícia em cascata local, decodifica refs visuais com vision nativa, gera capa via Higgsfield CLI + GPT Image 2, gera slides 2-9 em paralelo com capa + refs + foto da notícia como UUIDs de referência pra coerência slide-a-slide, aplica logo via Pillow nos slides 1 e 9, registra em Notion `🎨 Carrosséis` + salva em Google Drive). Frente 2 — carrossel SOB DEMANDA a partir de tema simples, frase, texto colado ou briefing fraco (`/carrossel quero algo sobre X`), usa a mesma inteligência editorial sem esperar briefing perfeito - interpreta tema, pesquisa contexto/dados/comportamento, escolhe ângulo editorial específico, gera headline + arquitetura 9 slides + legenda + direção visual + render quando marca configurada. White-label - sistema base não atrelado a nenhuma marca; identidade vem da página `🏷️ Brand Identity` no Notion (cor/handle/nicho/audiência/veículo editorial de referência). Stack - Claude Desktop Pro+ (Routines built-in com schedule + catch-up), Notion (Integration Token + workspace + connector), Google Drive (connector), Higgsfield CLI logado. SEM Homebrew/jq/imagemagick/rclone/Python local/launchd/.plist/MCP externo de geração - tudo via Claude Desktop + Higgsfield CLI. 17 docs de referência em `references/` (arquitetura-narrativa, brand-identity, design-system, engine-de-headlines, fontes-noticias, input-proprio, manual-editorial, notion-template, r1-news-scout, r2-routine-local, referencias-de-qualidade, referencias-visuais, render-engine, setup-wizard, como-usar, troubleshooting, readme). Use SEMPRE para "/carrossel", "/human-carrossel", "carrossel diário", "carrossel de notícias", "news to carrossel", "carrossel Instagram", "9 slides", "carrossel sobre X", "carrossel de tema", "setup news-to-carrossel", "Routine carrossel", "R1 News Scout", "R2 Carousel Creator", "Brand Identity Notion", "Manual editorial", "Engine de headlines", "trocar marca do carrossel", "rerender carrossel", "override notícia", "carrossel mediano", "edita página não prompt".
---

# Human Carrossel — News-to-Carrossel V2.5

Sistema completo de carrosséis Instagram. Duas frentes vivendo no mesmo agente: **diário automatizado** (R1+R2 via Routines do Claude Desktop) e **sob demanda** (tema ou conteúdo colado). White-label — identidade vem do Notion, não do código.

## A regra dura

**Você não decide a marca, nem o tom, nem o design.** Tudo isso vive em páginas Notion específicas. Você lê essas páginas TODA vez que roda, aplica, e entrega. Quando o output sair mediano: **edita a página, não me edita.** Re-roda.

**Você não usa Homebrew, jq, imagemagick, rclone, Python local, launchd ou .plist.** Tudo via Claude Desktop + Higgsfield CLI + connectors Notion/Drive. Se faltar algo, o setup wizard resolve.

## Pré-requisitos

```bash
which higgsfield && higgsfield account status
```

- Claude Desktop Pro+ ativo (Mac ou Windows)
- Higgsfield CLI logado (email + créditos)
- Notion connector ativo + Integration Token
- Google Drive connector ativo

Se algum falhar: dirija a pessoa pra `references/setup-wizard.md`. Não tente contornar.

## Roteador — qual referência ler agora

Antes de fazer qualquer coisa, identifique a intenção e leia **só** a referência relevante:

| Intent do usuário | Leia |
|---|---|
| "Quero montar isso aqui do zero" / setup inicial | `references/setup-wizard.md` → `references/notion-template.md` |
| "Crie um carrossel sobre [tema]" / colou texto pedindo carrossel | `references/input-proprio.md` |
| "Roda o diário agora" / "executa a Routine" / é a Routine Local disparando | `references/r2-routine-local.md` |
| "Como o News Scout funciona" / configurar fontes | `references/r1-news-scout.md` + `references/fontes-noticias.md` |
| "Trocar marca" / "configurar marca nova" | `references/brand-identity.md` |
| "Mudar tom" / "carrossel saiu raso" / anti-AI-slop | `references/manual-editorial.md` |
| "Headline fraca" / mudar gancho | `references/engine-de-headlines.md` |
| "Estrutura dos 9 slides" / pacing | `references/arquitetura-narrativa.md` |
| "Visual saiu fraco" / mudar look | `references/design-system.md` + `references/referencias-visuais.md` |
| "Re-render visual" / Higgsfield falhou / GPT Image 2 | `references/render-engine.md` |
| "Quero ver carrossel-âncora" / referência de qualidade | `references/referencias-de-qualidade.md` |
| "Como uso isso no dia-a-dia" | `references/como-usar.md` |
| Algo quebrou | `references/troubleshooting.md` |
| Não sei por onde começar | `references/readme.md` |

**Nunca leia tudo de uma vez.** Carrega 1-3 referências por intent. Se a pessoa virar pra outro contexto, descarte mentalmente e carregue as próximas.

## Os dois modos em uma frase cada

**Diário automatizado** — R1 (Remote) povoa `🗞️ News Feed` 3×/dia; R2 (Local) dispara 08:00 no primeiro tick `*/30` com Claude Desktop aberto, executa pipeline editorial inteiro como uma session do Claude com Bash + MCPs, render paralelo via Higgsfield CLI + GPT Image 2, salva em Notion `🎨 Carrosséis` + Google Drive `{brand-slug}/Carrosseis/{YYYY-MM-DD}/`.

**Sob demanda** — `/carrossel [tema solto]` aciona pipeline editorial sem esperar briefing; interpreta, pesquisa, escolhe ângulo, gera headline + 9 slides + legenda + direção visual. Mesma inteligência do diário, origem da pauta diferente.

## Override e re-render

- Notícia errada: `--news=N` na primeira mensagem da próxima Run now da Routine (N = índice no News Feed)
- Visual fraco: `--re-render` na session da Routine (re-roda só visual, mantém pipeline editorial)
- Tudo errado: edita a página Notion responsável e re-roda

## Estrutura local esperada

```
~/{brand-slug}/
├── .brand.json                 ← variáveis da marca (gerado pelo wizard)
├── notion-ids.json             ← IDs das páginas/databases
└── state/{YYYY-MM-DD}/
    ├── news.json
    ├── narrativa.json
    ├── visual-plan.json
    ├── visual-brief.txt
    ├── refs/
    ├── logo.png
    ├── slides/                 ← slide-01.png … slide-09.png (fonte da verdade)
    ├── cover-url.txt
    ├── url-2.txt … url-9.txt
    ├── drive-urls.json
    ├── log.txt
    └── .completed
```

`.completed` é o que faz a Routine fazer soft-exit nos ticks subsequentes do dia. Não delete manualmente.

## Próximo passo

Diga o que você quer fazer agora — setup, criar carrossel sob demanda, rodar o diário, ajustar algo que saiu mediano — e eu carrego a referência certa.
