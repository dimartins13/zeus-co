---
version: 1.0.0
name: higgsfield-generate
description: |
  Gera imagem ou vídeo cinematográfico via Higgsfield AI. Default: GPT Image 2
  para imagem/design/texto, Seedance 2.0 para vídeo, Nano Banana 2/Pro para
  trabalho com referência/personagem, Marketing Studio para ads com avatares/
  produtos/hooks, Soul V2/Cinema/Cast/Location e Kling 3.0. Use quando: "gera
  uma imagem", "cria um vídeo", "anima essa foto", "image-to-video", "edita/
  estiliza/remixa essa imagem", "produz um clipe", "cria um ad", "faz vídeo
  UGC", "demo de produto", "unboxing", "vídeo de marca", "vídeo com apresentador",
  "importa produto pela URL", "cria avatar pra ad", ou "analisa viralidade de
  vídeo" (Virality Predictor / brain_activity). Suporta image-to-image,
  image-to-video, references, job/upload IDs e Marketing Studio. Encadeia com
  higgsfield-soul-id pra consistência de face/identidade. NÃO use para:
  treino de Soul Character (use higgsfield-soul-id), foto de produto branded
  (use higgsfield-product-photoshoot), cards de marketplace (use
  higgsfield-marketplace-cards), texto/chat/TTS.
argument-hint: "[prompt-ou-análise] [--model <nome>] [--image|--video <path-ou-id>]"
allowed-tools: Bash
---

# Higgsfield Generate (wrapper Zeus-CO)

## Identidade

Submete jobs pra qualquer modelo Higgsfield (35+). Cobre image/video genérico, Marketing Studio (ads branded com avatares/produtos/hooks/settings) e Virality Predictor (score de viralidade).

Eu **NÃO** sou o motor — sou o **wrapper Zeus-CO** que define gatilhos pt-BR + use cases canônicos pra invocar a skill oficial [`higgsfield-generate`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT). Conteúdo técnico profundo das 35+ modelos, Marketing Studio e Virality vive em `references/`.

## Pré-requisito one-time (Diego executa 1× no Terminal macOS)

```bash
# Instalar CLI
npm install -g @higgsfield/cli

# Autenticar (abre browser ~5s)
higgsfield auth login

# Verificar
higgsfield account status
```

> O MCP Higgsfield (já conectado no Cowork) é complementar mas não substitui o CLI usado pelas skills oficiais. As skills aqui chamam `higgsfield <comando>` via Bash.

## UX Rules

1. Conciso. Sem IDs crus, sem JSON dump no chat. Print só a URL da mídia gerada, ou o resumo textual do Virality Predictor.
2. Sem jargão interno. Não narrar "chamando higgsfield cost", "fazendo polling do job".
3. Responder em pt-BR. Flags técnicas (`--aspect_ratio 16:9`) ficam em inglês.
4. Não fazer batch de perguntas. Escolher um modelo default razoável e perguntar 1 coisa por vez só se realmente faltar.
5. Não pré-estimar custo nem otimizar pra modelo mais barato a menos que pedido. Default sempre na qualidade primeiro.

## Workflow

1. **Identificar intenção** (imagem? vídeo? marketing studio? virality analysis?)
2. **Escolher modelo** (default sensato — consultar `references/model-catalog.md` se incerto)
3. **Pegar inputs mínimos** (prompt + imagem opcional + aspect ratio)
4. **Submeter** via `higgsfield <comando>` apropriado
5. **Polling silencioso** até job pronto
6. **Entregar URL** + label curto

Detalhes profundos por sub-domínio em:
- `references/model-catalog.md` — 35+ modelos e quando usar cada um
- `references/marketing-modes.md` — Marketing Studio (avatares, produtos, hooks, settings)
- `references/marketing-ad-references.md` — biblioteca de referências de ads
- `references/marketing-avatars.md` — sistema de avatares
- `references/marketing-brand-kits.md` — brand kits
- `references/marketing-dtc-ads.md` — DTC ads
- `references/marketing-products.md` — gestão de produtos
- `references/marketing-setup-items.md` — configuração de itens
- `references/media-inputs.md` — formatos de input suportados
- `references/prompt-engineering.md` — como estruturar prompt
- `references/troubleshooting.md` — erros comuns

## Use cases canônicos no portfolio Zeus-CO

### UC1 — Ad com avatar pra campanha (CMO/marketing)
Marketing Studio + Soul-ID treinado. Cross com `zeus-co-marketing:ai-generative-creative` e `zeus-co-cmo:cmo-growth-performance`.

### UC2 — KV (Key Visual) cinematográfico de campanha
Soul V2/Cinema + prompt cinematográfico. Cross com `cco-art-director` e `processo-criativo-pesquisa`.

### UC3 — Vídeo de produto / unboxing pra Reels/TikTok
Seedance 2.0 ou Veo 3.1. Cross com `live-marketing` e `creator-economy`.

### UC4 — Anima foto estática (image-to-video)
Pra MVPs / mockups / asset reuse. Cross com `cco-creative-ops`.

### UC5 — Virality score antes de boost pago
Brain Activity / Virality Predictor analisa hook, attention, retention, distraction. Cross com `zeus-co-cmo:cmo-marketing-ops-martech` antes de gastar budget.

### UC6 — Brand video institucional
Soul Cinema + cast + location. Cross com `cco-storytelling` e `ceo-comms`.

## Self-Evaluation (3 modos)

### Modo A — Interativo Cowork desktop (Diego presente + filesystem)
Anotar 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/higgsfield-generate-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · higgsfield-generate · ambiente=cowork-chat · sucesso=[1-5] · gap=[...] · sugestao=[...] · empresa=[X]
```

### Modo B — Interativo Claude.ai web (sem filesystem)
Printar no chat:
```
Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=... · empresa=...
```

### Modo C — Autônomo (cron/scheduled, sem Diego)
Escrever no filesystem com heurística:
- PASS = output canônico + sem erro + dentro do tempo esperado
- PARTIAL = parcial OU warning
- FAIL = erro/timeout/output não-canônico

## Trabalha em equipe com

### Upstream (quem me chama)
- `zeus-co-marketing:marketing-orquestrador` (Fase 5 — execução criativa)
- `zeus-co-marketing:ai-generative-creative` (AI creative em escala)
- `cco-art-director` (KV cinematográfico)
- `cco-creative-ops` (produção criativa)
- `design-lab-image-generation` / `design-lab-video-generation`

### Peers
- `higgsfield-soul-id` (Soul Character pra identidade consistente)
- `cerebro-criativo` (gerar ideia antes; eu executo o visual)
- `processo-criativo-pesquisa` (referências antes de prompt)
- `video-vision-analysis` (analisar referência ANTES de gerar)

### Downstream (eu chamo)
- `cco-brand-guardian` (QA do output gerado)

### QA pair
- `cco-brand-guardian` (alinhamento com brand-guide)
- `clo-ip` (rights de uso de rostos/produtos quando aplicável)

## Channel Skill — não-LEP

Channel Skill (ferramenta tática de geração). Não tem identidade/pipeline próprios.

Despachada por:
- `zeus-co-cmo:cmo-orquestrador`
- `zeus-co-marketing:marketing-orquestrador`
- `cco` (orquestrador criativo)
- Diego direto ("gera imagem cinematográfica de X" / "cria vídeo Higgsfield de Y")

## Skill genérica — context vem da empresa

Capability reutilizável pra qualquer empresa do portfolio. Não hardcoda lógica por empresa.

Adaptar comportamento por empresa via **Fase 0 Descoberta Interna** obrigatória:
1. Ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`)
2. Aplicar tom/cor/aesthetic da empresa no prompt
3. Restrições de uso de imagem (rights, CONAR, compliance) vêm de `clo-setorial` / `clo-ip` da empresa, não desta skill

## Fim de sessão (3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · higgsfield-generate · [lição da geração] · [importa pra próximos]

### 2. BACKLOG.md
- [P0|P1|P2] · [próximo asset/variação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · higgsfield-generate · [UC1..UC6] · ~N turnos · path/URL

### 4. _Inbox.md (opcional — sugestão proativa)

Fallback: `_SessionRecaps/YYYY-MM-DD-higgsfield.md`

---

## Crédito + atribuição

Skill original: [`higgsfield-ai/skills`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT). Este SKILL.md é **wrapper Zeus-CO** com gatilhos pt-BR + use cases canônicos. Todo conteúdo técnico (model catalog, marketing studio, prompt engineering, troubleshooting) permanece em `references/` como o autor original publicou.
