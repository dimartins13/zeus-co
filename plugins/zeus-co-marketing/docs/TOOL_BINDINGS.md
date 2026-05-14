# TOOL_BINDINGS — Quando usar qual ferramenta de design/criação

> Mapeamento canônico de ferramentas por intenção criativa.
> **Princípio:** ferramenta certa pra estágio certo. Não usar Adobe pra ideia preliminar; não usar Canvas Design pra produção final.

---

## Tabela canônica

| Intenção | Ferramenta | Quando usar |
|---|---|---|
| **Moodboard / KV preliminar** | `anthropic-skills:canvas-design` | Rascunho rápido de Big Idea visual. PNG/PDF. Custo baixo. |
| **HTML artefato interativo** | `anthropic-skills:web-artifacts-builder` | Landing preview, simulador, dashboard cliente. |
| **Geração imagem profissional** | Adobe MCPs (`image_*`, `fill_text`, etc.) | KV final pra deploy, retoque profissional, manipulação fina. |
| **Geração vídeo / motion** | Higgsfield (`mcp__dd613414-*__generate_video`) | Anúncio social, brand film, peça TikTok/Reels. |
| **Geração imagem rápida (alt)** | Higgsfield (`generate_image`) ou Adobe Firefly | Iteração rápida de variações de KV. |
| **Stock photo / vetor** | Freepik (`mcp__freepik__*`) | Quando precisa asset existente, não geração. |
| **Edição colaborativa** | Figma MCP | Quando Diego/equipe precisam revisar/editar. |
| **Template editável fácil** | Canva MCP (`mcp__8984f484-*`) | Posts sociais que equipe não-design vai usar. |
| **Apresentação / deck** | Gamma (`mcp__2801b3d7-*`) | Pitch deck, board pack, deck investor. |
| **Documento Office** | Adobe document_render_layout | Briefing oficial, contrato, manual. |
| **Storyboard / animação** | Adobe animate_design + Higgsfield | Roteiro publicitário visualizado. |
| **Naming + Domain** | `zeus-co-naming-domain` | Marca nova, drop com nome dedicado. |
| **Pesquisa criativa** | WebSearch + `zeus-co-marketing:processo-criativo-pesquisa` | Cannes, Effie, casos premiados. |
| **Imagem IA premium (estética)** | Midjourney v7+ (via WebFetch ou manual) | Default pra moodboard + KV preliminar |
| **Imagem IA realismo + rights** | Adobe Firefly v3 (via Adobe MCP) | Quando rights commerciais são críticos (campanha paga) |
| **Imagem IA controle prompt** | Flux Pro / Schnell (via API) | Produção realista de alta fidelidade |
| **Imagem IA com texto** | Ideogram | Pôsteres, packaging com tipografia |
| **Vídeo IA narrativo** | Sora (OpenAI) | Brand films, narrativa cinematográfica |
| **Vídeo IA controle direcional** | Runway Gen-4 | Workflow profissional img2vid |
| **Vídeo IA + áudio sincronizado** | Veo 3 via Higgsfield MCP | Realismo + áudio nativo |
| **Vídeo IA operacional** | Higgsfield MCP (acesso 30+ models) | Default Diego (já instalado) |
| **Voz / locução IA** | ElevenLabs | Voice clone, multilingual, signature voice |
| **Música IA** | Suno v4+ | Trilha sonora personalizada |
| **Lipsync / avatar IA** | HeyGen, Hedra | Apresentador virtual, dubbing |
| **Upscale + polimento IA** | Magnific, Topaz Video AI | Refinar gen antes de publicar |
| **Live commerce streaming** | OBS + Streamlabs | Setup técnico de live |
| **TikTok Shop ops** | TikTok Seller Center + Shopify AI Toolkit MCP | Setup catálogo + ads + affiliates |
| **CTV programmatic** | The Trade Desk / DV360 / Amazon DSP | DSPs pra inventário premium streaming |
| **CTV measurement** | Nielsen ONE BR / Comscore CTV | Brand lift + cross-screen |

---

## Regras de invocação

### 1. Hierarquia de qualidade
```
Canvas Design (ideação) → Adobe MCPs (produção) → Hand-off humano (se cliente externo)
```

Nunca pular do "Canvas Design" pro "deploy externo" — sempre passar por Adobe ou Figma pra polimento.

### 2. Hierarquia de custo
- **Canvas Design + WebSearch:** ~$0.10-$0.50 por uso
- **Adobe MCPs:** ~$0.20-$1.50 por imagem
- **Higgsfield vídeo:** ~$1-$5 por vídeo
- **Gamma deck:** ~$0.50-$2 por apresentação

Pra brainstorming/iteração, ficar em Canvas Design. Pra deliverable final, mover pra Adobe/Higgsfield.

### 3. Brand Guardian é gate antes de QUALQUER deploy externo
Toda peça gerada por qualquer tool acima passa por `zeus-co-cco-brand-guardian` antes de ir pra fora. Valida:
- Paleta dentro do `brand-guide.md`
- Tipografia consistente
- Tom alinhado com `writing-guide.md`
- Nenhuma palavra proibida
- Nenhum item do Don't visual

---

## Bindings por skill (quem chama qual tool)

### Skills criativas (`zeus-co-cco:`)
- `zeus-co-cco:cco-orquestrador` → invoca **Canvas Design** (KV preliminar) → Brand Guardian QA → escala pra Adobe se aprovado
- `zeus-co-cco:cco-art-director` → **Canvas Design** + **Higgsfield** (peças preliminares)
- `zeus-co-cco:cco-art-director` → **Canvas Design** + **Adobe MCPs** + **Higgsfield** (KV oficiais)
- `zeus-co-cco:cco-storytelling` → **Canvas Design** (storyboard) → **Higgsfield** (geração vídeo)
- `zeus-co-cmo:cmo-branding` → **Canvas Design** (mockup) → **Adobe** (logo final) → **Figma** (handoff equipe)
- `zeus-co-cco:cco-copy-master` → SEM tool visual (texto puro)
- `zeus-co-cerebro-criativo` → **Canvas Design** (moodboard de ideação)

### Skills sociais (`zeus-co-cco:cco-content-strategist` + similares)
- → **Canva MCP** (template editável)
- → **Higgsfield** (vídeo curto)
- → **Adobe** (versão final)

### Skills de produção (`zeus-co-cco:cco-creative-ops`)
- → **Adobe full suite** (entrega final)
- → **Figma** (handoff cliente)
- → **Gamma** (decks acompanhantes)

### Skills novas zeus-co-marketing
- `live-marketing` → **Figma** (layout evento) + **Canva** (sinalização)
- `marketing-promocional` → **Canva** (peças promo) + **Adobe** (peças finais)
- `marketing-afiliados` → **Canva** (banners parceiros) + **Gamma** (deck programa)
- `retail-media` → **Adobe** (banner marketplace) + **Canvas Design** (variações A/B)
- `creator-economy` → **Higgsfield** (briefing visual pra creator) + **Canva** (toolkit creator)
- `processo-criativo-pesquisa` → SEM tool visual (texto + WebSearch)

---

## Anti-padrões (não fazer)

- ❌ Usar Adobe pra primeiro rascunho (caro demais, slow)
- ❌ Usar Canvas Design pra deploy externo (qualidade não polida)
- ❌ Pular Brand Guardian antes de deploy
- ❌ Gerar vídeo com Higgsfield sem ter aprovado o KV/storyboard antes
- ❌ Usar Canva pra peça que vai pra mídia paga premium (resolução insuficiente)
- ❌ Cada skill criativa invocar TODOS os tools — define um caminho canônico por intenção
