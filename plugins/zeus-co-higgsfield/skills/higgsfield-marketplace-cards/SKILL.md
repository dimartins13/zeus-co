---
version: 1.0.0
name: higgsfield-marketplace-cards
description: |
  Gera visuais de cards de produto pra marketplace via Higgsfield: imagem
  principal compliant, imagens secundárias e módulos A+ style. Use quando o
  usuário pedir: "cards de listing marketplace", "card Mercado Livre", "card
  Amazon", "card Shopee", "imagens detalhe produto", "imagens secundárias",
  "infográfico de produto", "lifestyle listing", "A+ content", "set de imagens
  marketplace", "visual sales-ready de produto". Backend tem regras de
  compliance de marketplace e templates de prompt; esta skill só roteia
  intenção pro CLI. NÃO use para: fotografia genérica de marca/produto sem
  contexto de listing (use higgsfield-product-photoshoot), geração de vídeo
  ou UGC ad (use higgsfield-generate), treino de Soul Character (use
  higgsfield-soul-id).
argument-hint: "[--scope main|product-images|aplus|full-set] [prompt]"
allowed-tools: Bash
---

# Higgsfield Marketplace Cards (wrapper Zeus-CO)

## Identidade

Cria visuais marketplace-ready com `higgsfield marketplace-cards create`. O CLI chama backend enhancer (regras de marketplace + templates), cria jobs `nano_banana_2` e printa URLs.

Wrapper Zeus-CO sobre [`higgsfield-marketplace-cards`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT).

## Pré-requisito one-time

```bash
npm install -g @higgsfield/cli
higgsfield auth login
```

## UX Rules

1. Responder em pt-BR.
2. Perguntar no máximo 1 confirmação concisa antes de rodar.
3. Preferir imagem do produto. Se Diego mandar só texto/URL, prosseguir só quando os detalhes do produto estão claros.
4. **NÃO escrever prompts finais de geração** — backend enhancement é responsável.
5. Answer final: só URLs prontas + labels curtos.

## Escopo (--scope)

| Scope | Cria |
|---|---|
| `main` | 1 imagem principal compliant |
| `product-images` | imagem principal + 5 secundárias |
| `aplus` | imagem principal + 7 módulos A+ |
| `full-set` | principal + 5 secundárias + 7 A+ |

Pra subsets custom: `--asset main_image`, `--asset product_image`, `--asset aplus_module` (repetível).

## Workflow

1. **Identificar marketplace alvo** (Mercado Livre / Amazon BR / Shopee — cada um tem compliance diferente; backend trata)
2. **Pegar imagem do produto** (path/URL/upload ID)
3. **Escolher scope** (default razoável: `product-images` pra lançamento, `full-set` pra hero SKU)
4. **Submeter:** `higgsfield marketplace-cards create --scope <scope> --image <path>`
5. **Polling silencioso → entregar URLs**

## Use cases canônicos no portfolio Zeus-CO

### UC1 — Ventage: novo modelo de óculos entrando em ML + Amazon
Scope `full-set` (principal + secundárias + A+). Cross com `coo-supply` (estoque), `cco-brand-guardian` (alinhamento marca) e `clo-setorial` (regras CONAR + ML/Amazon).

### UC2 — 2ndStreet/dope street: peça streetwear listada em marketplace próprio
Scope `product-images`. Cross com `2ndstreet-cataloger:catalog-piece` (pipeline cataloging) e `cco-art-director`.

### UC3 — Crazyflips: drop NFT físico em e-commerce afiliado
Scope `aplus` (storytelling do drop importa mais que volume de fotos). Cross com `cco-storytelling`.

### UC4 — Refresh de SKU existente que está caindo conversão
Scope `main` (testar nova hero) + A/B no marketplace. Cross com `zeus-co-cmo:cmo-marketing-ops-martech` (métricas) e `coo-customer-ops`.

## Heurísticas

- **Hero SKU (top 20% receita):** `full-set` justifica investimento
- **Long-tail SKU:** `product-images` é suficiente
- **Lançamento:** `product-images` + monitorar conversão por 30d → se >benchmark, upgrade pra `full-set`
- **A/B test de hero:** `main --count 3` pra testar variações
- **Marketplace BR-specifics:** ML aceita até 12 imagens, Amazon até 9, Shopee até 9 — backend respeita

## Self-Evaluation (3 modos)

### Modo A — Cowork desktop
`_Pulse/skill-feedback/higgsfield-marketplace-cards-YYYY-MM-DD.md`

### Modo B — Claude.ai web
Printar no chat.

### Modo C — Autônomo
PASS/PARTIAL/FAIL heurístico.

## Trabalha em equipe com

### Upstream
- `coo-supply` (novo SKU pronto pra listar)
- `2ndstreet-cataloger:catalog-piece` (pipeline catalog)
- `zeus-co-cmo:cmo-growth-performance` (decide hero SKU)

### Peers
- `higgsfield-product-photoshoot` (versão branded sem compliance marketplace)
- `higgsfield-generate` (vídeo demo do produto pra listing video)
- `retail-media` (Mercado Ads / Amazon Ads consomem essas imagens)
- `tiktok-shop` (cards traduzidos pra TikTok Shop)

### Downstream
- `cco-brand-guardian` (QA antes de publicar no marketplace)
- `retail-media` (boost pago da listing depois)

### QA pair
- `cco-brand-guardian` (brand alinhada)
- `clo-setorial` (compliance Mercado Livre/Amazon/Shopee Brasil)

## Channel Skill — não-LEP

Despachada por: `coo-supply`, `zeus-co-cmo`, `2ndstreet-cataloger`, `retail-media`, Diego direto.

## Skill genérica — context vem da empresa

Antes de gerar cards pra empresa X:
1. Ler `_Areas/COO/skus.md` (info canônica do produto)
2. Ler `_Areas/CCO/brand-guide.md` (paleta/mood)
3. Ler `_Areas/CLO/compliance-marketplace.md` (restrições específicas por marketplace)
4. Salvar em `_Areas/Sales/marketplace-listings/<SKU>/`

## Fim de sessão

### LEARNINGS.md
- YYYY-MM-DD · higgsfield-marketplace-cards · [lição scope X funcionou pra marketplace Y]

### BACKLOG.md
- [P0|P1|P2] · [próxima SKU ou refresh] · Owner

### _LEDGER.md
- YYYY-MM-DD HH:MM · higgsfield-marketplace-cards · [UC1..UC4] · [scope] · [marketplace] · N imagens · paths/URLs

---

## Crédito + atribuição

Skill original: [`higgsfield-ai/skills`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT). Wrapper Zeus-CO com gatilhos pt-BR + integração `clo-setorial` (compliance marketplace BR) + paths canonical por empresa.
