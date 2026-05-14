# PIPELINE — Marketing / Criação canônico do Zeus-CO

> **11 fases, ordem fixa.** Pular fase = entregar genérico.
> **Princípio inviolável:** Fase 0 OLHA PRA DENTRO. Fase 1-4 OLHAM PRA FORA. Fase 5+ CRIAM.
> **Atualização:** 2026-05-13 (Diego diretiva)

---

## Fase 0 — DESCOBERTA INTERNA (obrigatória, primeira)

**Owner:** orquestrador (`zeus-co-marketing`) + skill chamadora
**Output:** `_Areas/CMO/<projeto>/00-descoberta-interna.md`

Antes de qualquer pesquisa externa, LER da empresa:

### 0.1 Identidade + estágio
- `CLAUDE.md` — constituição empresa
- `00_INDEX.md` + `00_STAGE.md` — onde está
- `LEARNINGS.md` — o que aprendemos
- `BACKLOG.md` — o que ainda falta

### 0.2 Taste layer (se existir)
- `_Areas/CCO/brand-guide.md` — paleta, tipografia, do/don't
- `_Areas/CCO/writing-guide.md` — voz, tom, palavras proibidas, frases-âncora
- `_Areas/CEO/decision-criteria.md` — hard limits, North Star

### 0.3 Documentos base de construção
Varrer raiz da empresa procurando:
- `*BP*Financeiro*` — modelo financeiro
- `*Business*Plan*` — plano de negócios
- `*Manual*Operacional*` — como a empresa funciona
- `*Brand*Marketing*` — brand foundation
- `*Ecommerce*Estrategia*` — estratégia comercial
- `*Conceito*Criativo*` — conceitos passados
- `_NoName-Lab/`, `research/` — pesquisas anteriores

### 0.4 Histórico de campanhas (se existir)
- `_Areas/CMO/campanhas/` — campanhas anteriores
- `_Areas/CMO/analytics/` — performance histórica
- `_Areas/CCO/_Publicacoes/` — peças que foram pra fora
- `_LEDGER.md` — quem fez o quê quando

### 0.5 Síntese (output da Fase 0)
Documento `00-descoberta-interna.md` com 5 seções:
1. **Quem somos** (1 parágrafo, citando taste layer)
2. **O que já entregamos** (lista de campanhas + performance se houver)
3. **O que aprendemos** (lições durables das anteriores)
4. **O que não pode acontecer** (anti-padrões, palavras proibidas, hard limits)
5. **O que está em aberto** (gaps no BACKLOG relevantes pra essa campanha)

**Sem essa fase, NÃO avança.** É a base que evita repetir erro, copiar concorrente fora-de-marca, ou contradizer brand foundation.

---

## Fase 1 — BRIEFING (claro, mensurável)

**Owner:** CMO (`zeus-co-cmo`) recebe input do Diego.
**Skills:** `zeus-co-cmo:cmo-estrategia-marketing` ou similar.
**Output:** `_Areas/CMO/<projeto>/01-briefing.md`

Estrutura:
- **Objetivo** (1 frase, mensurável, com prazo)
- **KPI primário** (1, com baseline + meta)
- **KPIs secundários** (até 3)
- **Público-alvo** (persona específica, não "milennials")
- **Restrições** (budget, prazo, canais OFF, palavras proibidas — reusa Fase 0.4)
- **Mandatórios** (logos, claims legais, NFC para 2ndStreet, gates SECAP pra KingPanda, etc.)

---

## Fase 2 — PESQUISA EXTERNA (mercado + concorrentes)

**Owner:** `zeus-co-cmo:cmo-pesquisa-insights` + `zeus-co-cmo:cmo-pesquisa-insights`
**Output:** `_Areas/CMO/<projeto>/02-pesquisa-mercado.md`

Cobertura:
- Tamanho mercado + projeção
- Top 5 concorrentes diretos + posicionamento
- Top 3 indiretos
- Trends do setor (últimos 12 meses)
- White space (onde concorrente NÃO está)

---

## Fase 3 — COMPORTAMENTO + INSIGHT

**Owner:** `zeus-co-cmo:cmo-pesquisa-insights`
**Output:** `_Areas/CMO/<projeto>/03-insight.md`

- Jobs-to-be-done do público
- Gatilhos psicológicos relevantes
- Barreiras de compra
- **Insight Ouro** (1 frase que muda perspectiva — Lee Clow style)

---

## Fase 4 — BENCHMARK CRIATIVO + PROCESSO

**Owner:** `zeus-co-cmo:cmo-pesquisa-insights` + **`zeus-co-marketing:processo-criativo-pesquisa`** (NOVA)
**Output:** `_Areas/CMO/<projeto>/04-benchmark-criativo.md`

Cobertura DUPLA:
- **4a. O quê** — referências (Cannes, Effie, D&AD, El Ojo) que ressoam com brief
- **4b. Como** — processo criativo das referências (briefing → insight → ideia → execução). Aprender a AUTORIA, não só copiar o resultado.

---

## Fase 5 — PLANEJAMENTO ESTRATÉGICO

**Owner:** `zeus-co-cmo:cmo-estrategia-marketing` + `zeus-co-cmo:cmo-estrategia-marketing` + `zeus-co-cmo:cmo-estrategia-marketing`
**Output:** `_Areas/CMO/<projeto>/05-plano-estrategico.md`

- Posicionamento da campanha
- Frame estratégico (Playing to Win — onde jogar + como ganhar)
- Mensagem central
- Pilares de comunicação
- Tom + voz (reusa `writing-guide.md` da empresa)

---

## Fase 6 — BIG IDEA + CONCEITO

**Owner:** `zeus-co-cerebro-criativo` + `zeus-co-cco:cco-orquestrador` + `zeus-co-cco:cco-art-director`
**Output:** `_Areas/CMO/<projeto>/06-big-idea.md`

- Big Idea (1 frase, proprietária, escalável)
- Tagline (se aplicável — reusa sistema de messaging do `brand-guide.md`)
- Manifesto (3-5 parágrafos)
- Territory map (onde Big Idea se desdobra)

---

## Fase 7 — EXECUÇÃO CRIATIVA MULTI-FORMATO

**Owner:** múltiplos, **paralelos**, coordenados pelo orquestrador
**Output:** `_Areas/CMO/<projeto>/07-execucao/`

### 7a. Publicidade tradicional (filme + KV + OOH)
- `zeus-co-cco:cco-storytelling` — roteiro filme
- `zeus-co-cco:cco-art-director` — KV preliminar
- `zeus-co-cco:cco-copy-master` — copy hero + claims
- **Tool:** Claude Design (`anthropic-skills:canvas-design`) pra KV preliminar PNG/PDF
- **Tool produção final:** Adobe MCPs (image_generative_expand, document_render_layout)

### 7b. Marketing promocional ⭐ NOVO
- **`zeus-co-marketing:marketing-promocional`** — sampling, contests, sweepstakes, brindes, descontos
- **Tool:** `zeus-co-cco:cco-copy-master` pra mecânica + termos

### 7c. Marketing digital (search + social + display)
- `zeus-co-cmo:cmo-growth-performance` + `zeus-co-cmo:cmo-growth-performance`
- `zeus-co-cmo:cmo-growth-performance` — landing pages
- **Tool:** Meta Ads MCP (recomendado pelo scout) + Google Ads MCPs

### 7d. Social/Conteúdo
- `zeus-co-cco:cco-content-strategist` — calendário + criativos
- **Tools:** Canva MCP (templates), Figma MCP (design), Higgsfield (vídeo)

### 7e. Live marketing ⭐ NOVO
- **`zeus-co-marketing:live-marketing`** — eventos, drops físicos, ativações, brand experience
- **Tools:** Figma MCP (layouts evento), Canva (assets visuais)

### 7f. Marketing de afiliados ⭐ NOVO
- **`zeus-co-marketing:marketing-afiliados`** — programa, plataforma, comissionamento, recrutamento
- **Tools:** integração com plataformas (Hotmart/Eduzz/Awin via API)

### 7g. Retail media ⭐ NOVO
- **`zeus-co-marketing:retail-media`** — Mercado Ads, Amazon Ads, Magalu Ads, Shopee Ads
- Crucial pra Ventage (e-comm óculos) + 2ndStreet (marketplace)

### 7h. Creator economy ⭐ NOVO
- **`zeus-co-marketing:creator-economy`** — UGC ops, deals, micro/nano
- Distinto de `zeus-co-marketing:creator-economy` (esse é macro/A-list)

### 7i. PR + Comunicação corporativa
- `zeus-co-cmo:cmo-comunicacao-pr`

### 7j. CRM + Lifecycle (após captura)
- `zeus-co-cmo:cmo-crm-lifecycle` — onboarding, retenção, recuperação

### 7k. Live commerce ⭐ NOVO (2026-05-13)
- **`zeus-co-marketing:live-commerce`** — TikTok Live, Instagram Live Shopping, Shopee Live, ML Live, Magalu Live
- **Tools:** OBS/Streamlabs streaming, plataforma native checkout, Klaviyo (push pre-live)
- **Distinto de live-marketing** (eventos físicos BTL)

### 7l. TikTok Shop ⭐ NOVO (2026-05-13)
- **`zeus-co-marketing:tiktok-shop`** — implementação + gestão de TikTok Shop seller (4 alavancas: catálogo orgânico + ads + affiliates + lives)
- **Tools:** TikTok Seller Center, TikTok Ads Manager, Shopify AI Toolkit MCP

### 7m. AI Generative Creative ⭐ NOVO (2026-05-13) — TRANSVERSAL
- **`zeus-co-marketing:ai-generative-creative`** — Midjourney, Sora, Runway, Higgsfield, Flux, Adobe Firefly, ElevenLabs, HeyGen
- **TRANSVERSAL:** alimenta 7a (publicidade TVC), 7d (social), 7h (creator toolkit), 7k (live assets), 7n (CTV criativo)
- **Tools:** Higgsfield MCP (já instalado), Adobe MCPs, Canvas Design skill, web-artifacts-builder

### 7n. CTV / Streaming Ads ⭐ NOVO (2026-05-13)
- **`zeus-co-marketing:ctv-streaming-ads`** — YouTube CTV, Netflix Ads, Disney+ Ads, Globoplay, Prime Video Ads, Pluto TV, Samsung TV Plus
- **Tools:** DSPs (The Trade Desk, DV360), criativo TVC-ready (vem de 7a + 7m), Nielsen/Kantar measurement

---

## Fase 8 — PLANO DE CANAIS + BUDGET SPLIT

**Owner:** `zeus-co-cmo:cmo-growth-performance` + CMO
**Output:** `_Areas/CMO/<projeto>/08-plano-canais.md`

- Mix de canais (% budget cada)
- Calendário de flighting
- Frequência alvo por canal
- Mecânica de aprendizado (qual canal otimizar primeiro)

---

## Fase 9 — CALENDÁRIO + RÉGUA DE PUBLICAÇÃO

**Owner:** `zeus-co-cco:cco-content-strategist` + CMO
**Output:** `_Areas/CMO/<projeto>/09-calendario.md`

Formato:
- Tabela: data | canal | formato | copy | KV | KPI esperado | responsável
- Régua: pre-launch / launch / sustain / closing

---

## Fase 10 — ANALYTICS + LOOP DE OTIMIZAÇÃO

**Owner:** `zeus-co-cmo:cmo-marketing-ops-martech` + `zeus-co-cmo:cmo-marketing-ops-martech`
**Output:** `_Areas/CMO/<projeto>/10-analytics.md` (atualizado semanalmente)

- KPIs primário + secundários, medidos
- Aprendizado da semana
- Decisão de ajuste (mudar copy / canal / budget)
- **Loop:** updates voltam pra `LEARNINGS.md` da empresa pra próxima campanha

---

## Princípios transversais

1. **Olha pra dentro PRIMEIRO** (Fase 0). Sem isso, criação vira commodity.
2. **Fase 4 dupla (referência + processo)** — não basta saber o que funcionou, saber COMO foi feito.
3. **Multi-formato é regra, não exceção** — Fase 7 cobre 10 frentes. Diego pode escolher subset, mas orquestrador SUGERE o full.
4. **Tool bindings explícitos** — toda fase visual diz qual tool usar (`TOOL_BINDINGS.md`).
5. **Loop fecha em LEARNINGS** — toda campanha vira insumo da próxima.
6. **QA pair sempre** — Brand Guardian valida output criativo, Verificador Factual valida claims, CFO valida budget.
