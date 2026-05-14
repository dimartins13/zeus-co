# Pipeline · Gamma — EXECUTÁVEL

> **Status**: MCP Gamma conectado (`mcp__2801b3d7-*`). Geração de deck/web/social via prompt.
> **Best fit**: decks rápidos com design decent + LP curta + social cards. Custa créditos.

## Quando o `design-lab-*` aciona Gamma

- `design-lab-deck` → gerar pitch/board/sales deck (5-15 slides) a partir de outline
- `design-lab-landing-page` → LP rápida (Gamma "website" mode)
- `design-lab-social-carousel` → carrossel multi-page (alternativo a IG carousel manual)

## Tools Gamma MCP disponíveis

| Tool | Função |
|---|---|
| `generate` | Gera deck/web/social a partir de prompt texto |
| `generate_from_template` | Usa template existente como base |
| `get_themes` | Lista temas disponíveis (paletas + fonts) |
| `get_folders` | Lista folders na conta Gamma |
| `get_gammas` | Lista decks/sites existentes |
| `read_gamma` | Lê estrutura de 1 gamma |
| `get_generation_status` | Polling status job assíncrono |

## Workflow padrão (deck novo)

### Passo 1 — Preparar outline antes (NUNCA pular)
Outline estruturado pré-Gamma:
```
- Title slide: <título + tagline>
- Slide 2: <problema/contexto>
- Slide 3-N: <argumentação seção por seção>
- Slide penúltimo: <CTA / próximos passos>
- Last: <thanks + contact>
```

Quanto melhor o outline, melhor o output. Não delegar outline pro Gamma — ele expande mal.

### Passo 2 — Escolher tema
```
Tool: mcp__2801b3d7-*__get_themes
Filtros: 
  - match direção visual escolhida (das 5)
  - cores compatíveis com brand-guide
```

### Passo 3 — Gerar
```
Tool: mcp__2801b3d7-*__generate
Args:
  - input_text: <outline estruturado>
  - format: "presentation" | "document" | "webpage" | "social"
  - text_options: { tone: "professional"/"casual"/"educational", length: "detailed"/"medium"/"brief", language: "pt"/"en" }
  - theme_name: "<nome do tema escolhido>"
  - num_cards: <N slides>
  - card_split: "auto" | "input_text"  ← se outline já tem separadores, usar "input_text"
  - additional_instructions: "<diretrizes específicas brand-guide>"
  - text_mode: "generate" | "preserve" | "condense"  ← preserve = não inventa texto, usa outline literal
```

### Passo 4 — Polling
```
Tool: mcp__2801b3d7-*__get_generation_status
Args: { generation_id }
Polling até status=completed (geralmente 30-90s)
```

### Passo 5 — Output
```
Output: URL do gamma criado
Save no _LEDGER.md da empresa: deck Gamma <URL> <título>
Diego abre URL, ajusta slides individuais se necessário, exporta PDF/PPTX
```

## Modos de uso (3 cenários)

### Modo "deck do zero" — output a partir de outline
- Use quando: deck novo, sem template
- Tool: `generate` direto
- Length: medium (cards inteligentes)
- text_mode: "generate" (Gamma inventa text se outline for sparse)

### Modo "deck a partir de template"
- Use quando: tem template aprovado (ex: pitch deck dope street)
- Tool: `generate_from_template`
- Args: { template_gamma_id, new_content }

### Modo "atualizar deck existente"
- Use quando: já tem deck no Gamma, só atualizar números/seções
- Tool: `read_gamma` → modify text → `generate_from_template` com novo content

## Boas práticas Gamma

- **Outline > prompt longo**: outline estruturado é 10× melhor que prompt narrativo
- **text_mode: preserve** se outline tem texto canônico (board pack, pitch específico)
- **text_mode: generate** se quer Gamma criativo (early stage idea)
- **Theme matters**: tema escolhido define 80% do visual final. Não economiza tempo aqui.
- **Não passar mais que 10-15 slides** num generate único — Gamma degrada qualidade
- **Para deck > 20 slides**: gerar em batches (intro+core, deep dive, appendix)

## Cost guardrails

- Gamma tem free tier limitado (Plus account: ~100 generates/mês)
- Cada `generate` consome 1 crédito
- Cuidado com re-gerar 5× o mesmo deck buscando perfeição — refine no Gamma UI > re-gerar

## Fallback (modo manual)

Se MCP off:
```
🟡 Gamma MCP não disponível. Manual:

1. Abre https://gamma.app
2. New AI > [Presentation / Document / Webpage]
3. Cola este outline preparado:
   <outline estruturado>
4. Theme: <tema sugerido>
5. Generate (1-2 min)
6. Cola URL do deck no chat — eu sigo (export PPT/PDF, etc)
```

## Cross com outras skills ZEUS-CO

- `cco-storytelling` cria outline narrativo antes de Gamma
- `cco-copy-master` revisa text gerado pelo Gamma (text_mode: generate sempre precisa review)
- `board-pack-builder` se for board deck (template específico)
- `ceo-fundraising` se for pitch fundraising (deck pattern específico)
- `cmo-product-marketing` se for launch deck
