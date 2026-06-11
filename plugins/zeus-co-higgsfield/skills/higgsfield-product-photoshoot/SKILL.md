---
version: 1.0.0
name: higgsfield-product-photoshoot
description: |
  Gera imagens de produto com qualidade de marca via Higgsfield
  product-photoshoot (prompt enhancement sobre GPT Image 2 / gpt_image_2).
  Entry point pra visuais profissionais de marca/produto. Use quando:
  "foto de produto", "foto studio", "lifestyle image", "Pinterest pin",
  "hero/banner", "carousel", "ad creative", "Meta ads", "virtual try-on",
  "modelo vestindo", "pessoa segurando produto", "closeup com mãos",
  "produto flutuando/splash/levitando", "CGI/surreal de produto", "restyle",
  "variação sazonal/estética", ou qualquer produto, marca ou paid-social
  creative. 10 modos: product_shot, lifestyle_scene,
  closeup_product_with_person, moodboard_pin, hero_banner, social_carousel,
  ad_creative_pack, virtual_model_tryout, conceptual_product, restyle.
  Backend monta o prompt final — nunca escreva freehand. NÃO use para: text-
  to-image sem produto (use higgsfield-generate), vídeo de avatar branded
  (use higgsfield-generate Marketing Studio), cards de marketplace (use
  higgsfield-marketplace-cards), treino de Soul Character (use
  higgsfield-soul-id).
argument-hint: "[--mode <modo>] [--count N] [prompt]"
allowed-tools: Bash
---

# Higgsfield Product Photoshoot (wrapper Zeus-CO)

## Identidade

Geração de imagem de marca via `higgsfield product-photoshoot create`. O CLI chama um backend enhancer que mantém vocabulário fotográfico específico por modo + templates estruturais, depois submete pra `gpt_image_2` e retorna URLs.

Wrapper Zeus-CO sobre [`higgsfield-product-photoshoot`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT).

## Pré-requisito one-time

```bash
npm install -g @higgsfield/cli
higgsfield auth login
```

## UX Rules

1. Conciso. Printar SÓ URLs no reply final.
2. Responder em pt-BR. Modo names e flags CLI ficam em inglês.
3. Perguntar no máximo 4 perguntas curtas antes de submeter. Opções labeled, nunca open-ended.
4. Pular pergunta cuja resposta é óbvia do contexto (imagem uploadada, turn anterior, memória de marca).
5. **NUNCA escrever o prompt gpt_image_2 você mesmo** — backend monta.
6. Polling silencioso. Aguardar URLs prontas, entregar.

## Modos (10)

| Modo | Quando usuário quer... |
|---|---|
| `product_shot` | Foto pura de produto em studio |
| `lifestyle_scene` | Produto em uso, ambiente real |
| `closeup_product_with_person` | Closeup com mãos/pessoa interagindo |
| `moodboard_pin` | Pinterest pin estilo moodboard |
| `hero_banner` | Hero banner site / landing |
| `social_carousel` | Carrossel social (Insta/LinkedIn) |
| `ad_creative_pack` | Pack de variações pra Meta Ads |
| `virtual_model_tryout` | Modelo virtual vestindo/usando produto |
| `conceptual_product` | CGI/surreal, levitando, splash |
| `restyle` | Variação sazonal/estética de imagem existente |

## Workflow

1. **Identificar modo** (perguntar com opções labeled se ambíguo)
2. **Pegar imagem do produto** (path local OU URL OU upload ID)
3. **Pegar contexto MÍNIMO** (marca, mood, restrições de cor)
4. **Submeter:** `higgsfield product-photoshoot create --mode <modo> --image <path> [--count N]`
5. **Polling silencioso** → entregar URLs

## Use cases canônicos no portfolio Zeus-CO

### UC1 — 2ndStreet/dope street: catalog inicial de peça streetwear
Modo `product_shot` + `lifestyle_scene` + `virtual_model_tryout`. Cross com `2ndstreet-cataloger:catalog-piece` (catalog pipeline) e `cco-art-director` (mood).

### UC2 — Ventage: óculos novo modelo entrando em catálogo
Modo `product_shot` (3 ângulos) + `closeup_product_with_person`. Cross com `coo-supply` (estoque) e `cco-creative-ops`.

### UC3 — APP Motivacional / TarjaPreta: hero banner landing page
Modo `hero_banner`. Cross com `design-lab-landing-page` e `cco-art-director`.

### UC4 — Campanha sazonal: pack de variações pra Meta Ads
Modo `ad_creative_pack` (variações automáticas). Cross com `zeus-co-cmo:cmo-growth-performance` e `marketing-promocional`.

### UC5 — Pinterest pin pra captação orgânica
Modo `moodboard_pin`. Cross com `zeus-co-marketing:marketing-orquestrador`.

### UC6 — Conceitual CGI surreal pra brand campaign premium
Modo `conceptual_product`. Cross com `cco-art-director` e `cerebro-criativo`.

## Heurísticas

- **Cobertura mínima de catálogo de peça streetwear:** 1× `product_shot` + 1× `lifestyle_scene` + 1× `virtual_model_tryout` = 3 imagens
- **Cobertura mínima de hero landing:** 1× `hero_banner` + 1× `moodboard_pin` (apoio)
- **Pra Meta Ads:** sempre `ad_creative_pack` com `--count 4` (pra ter material A/B)
- **Restyle** é mais barato — usar pra variar imagem existente sem regerar do zero

## Self-Evaluation (3 modos)

### Modo A — Cowork desktop
`_Pulse/skill-feedback/higgsfield-product-photoshoot-YYYY-MM-DD.md`

### Modo B — Claude.ai web
Printar no chat.

### Modo C — Autônomo
PASS/PARTIAL/FAIL heurístico.

## Trabalha em equipe com

### Upstream
- `2ndstreet-cataloger:catalog-piece` (pipeline catalog precisa de imagens)
- `cco-art-director` (define mood/estilo)
- `design-lab-landing-page` (precisa hero banner)
- `design-lab-poster-key-visual` (precisa KV)
- `zeus-co-cmo:cmo-growth-performance` (precisa ad creative pack)

### Peers
- `higgsfield-generate` (texto-puro sem produto físico)
- `higgsfield-marketplace-cards` (versão compliant pra marketplace)
- `higgsfield-soul-id` (pra `virtual_model_tryout` com pessoa específica)
- `ai-generative-creative` (escala variações geradas)

### Downstream
- `cco-brand-guardian` (QA visual antes de publicar)
- `2ndstreet-cataloger:generate-content` (copy do produto vai junto)

### QA pair
- `cco-brand-guardian` (alinhamento brand-guide)
- `clo-ip` (rights de modelo/pessoa em `virtual_model_tryout`)

## Channel Skill — não-LEP

Despachada por: `cco-art-director`, `cco-creative-ops`, `2ndstreet-cataloger`, `zeus-co-cmo`, Diego direto.

## Skill genérica — context vem da empresa

Antes de gerar foto pra empresa X:
1. Ler `_Areas/CCO/brand-guide.md` (paleta, mood, restrições)
2. Ler `_Areas/CCO/writing-guide.md` (caption acompanhante quando aplicável)
3. Salvar URLs em `_Areas/CCO/produced-assets/YYYY-MM-DD-<produto>/`

## Fim de sessão

### LEARNINGS.md
- YYYY-MM-DD · higgsfield-product-photoshoot · [lição modo X funcionou pra Y]

### BACKLOG.md
- [P0|P1|P2] · [próxima variação ou modo] · Owner

### _LEDGER.md
- YYYY-MM-DD HH:MM · higgsfield-product-photoshoot · [UC1..UC6] · [modo] · N imagens · paths/URLs

---

## Crédito + atribuição

Skill original: [`higgsfield-ai/skills`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT). Wrapper Zeus-CO com gatilhos pt-BR + use cases ancorados nas 5 empresas do portfolio.
