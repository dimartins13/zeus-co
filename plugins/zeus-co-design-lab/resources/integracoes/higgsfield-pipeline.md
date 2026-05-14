# Pipeline · Higgsfield — EXECUTÁVEL

> **Status**: Sem MCP nativo dedicado. Integração via **Claude in Chrome MCP** (`mcp__Claude_in_Chrome__*`) OR API REST direta.
> **Premium**: Higgsfield cobra por geração — sempre validar Diego antes de queimar créditos.

## Quando o `design-lab-*` aciona Higgsfield

- `design-lab-image-generation` → quando precisa de imagem **premium** (cinematic, photoreal) que Freepik Mystic não entrega
- `design-lab-video-generation` → vídeo gerado AI (Higgsfield Soul/DoP)
- `design-lab-motion-frames` → image-to-motion (animação curta da imagem base)
- `design-lab-poster-key-visual` → hero quando KV grande de campanha

## Detecção de ambiente (gracioso degradante)

```
Modo A — Cowork desktop com Chrome MCP ativo + sessão Higgsfield logada
  → executa via Chrome MCP (navega, gera, baixa)

Modo B — Cowork desktop sem Chrome MCP
  → fallback Modo INSTRUÇÃO (Diego abre browser, gera, cola path)

Modo C — Claude.ai web (sem Bash)
  → só Modo INSTRUÇÃO
```

## Workflow modo A (Chrome MCP)

### Passo 1 — Validar Chrome MCP + sessão Higgsfield
```
Tool: ToolSearch
Query: "select:mcp__Claude_in_Chrome__navigate"
SE retorna schema → Chrome MCP ok

Tool: mcp__Claude_in_Chrome__navigate
URL: https://higgsfield.ai

Tool: mcp__Claude_in_Chrome__read_page
→ Verificar se está logado (procura "Sign in" → não logado, pedir Diego logar manual)
```

### Passo 2 — Gerar
```
Tool: mcp__Claude_in_Chrome__navigate
URL: https://higgsfield.ai/create

Tool: mcp__Claude_in_Chrome__form_input
campo: prompt
valor: <prompt estruturado>

Tool: mcp__Claude_in_Chrome__left_click
selector: botão "Generate"

Aguarda ~30-90s (Higgsfield gera 4-8 variants)
```

### Passo 3 — Capturar resultados
```
Tool: mcp__Claude_in_Chrome__read_page
Extract: URLs das variants geradas

Tool: mcp__Claude_in_Chrome__upload_image
(ou screenshot pra apresentar pra Diego escolher)
```

### Passo 4 — Diego escolhe + download
```
AskUserQuestion: qual variant (1/2/3/4)?

Tool: mcp__Claude_in_Chrome__left_click
selector: download button da variant escolhida
→ baixa pra ~/Downloads/

Tool: Bash
mv ~/Downloads/<arquivo recém-baixado> ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/
```

## Workflow modo B/C (INSTRUÇÃO)

Devolve no chat:

```
🟡 Higgsfield via Chrome MCP não disponível. Manual:

1. Abre https://higgsfield.ai/create
2. Login (se não tiver)
3. Cola este prompt: "<prompt estruturado já preparado>"
4. Settings recomendados:
   - Aspect ratio: <X> (baseado no brief)
   - Model: Soul / DoP (depende: Soul=cinematic, DoP=photoreal)
   - Variants: 4 (começa)
5. Generate (espera ~30-90s)
6. Baixa o que escolheu pra ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/
7. Volta no chat e cola path — eu sigo
```

## Cost guardrails (CRÍTICO — Higgsfield é caro)

- **Sempre perguntar Diego antes de gerar** se for > 1 batch (4 variants)
- Cada geração ~$0.50-2.00 dependendo de model/resolution
- Soul model = cinematic = MAIS caro
- DoP = photoreal = menos caro
- Image-to-motion = MAIS caro ainda

**Regra**: nunca queimar > $5 sem aprovação explícita.

## Prompts boas práticas (Higgsfield específico)

Diferente de Midjourney/Mystic, Higgsfield responde melhor a:
- **Cena cinematográfica**: descrever câmera, lighting, lens, mood (não só subject)
- **Reference photo**: upload reference image antes pra style transfer
- **Director's brief** style: "Wide angle, low key lighting, shot from below, golden hour, dramatic"
- Evita: prompts curtos genéricos. Higgsfield premia detalhe.

Template prompt Higgsfield:
```
[SHOT TYPE] of [SUBJECT] in [LOCATION], [LIGHTING], [MOOD/STYLE].
Camera: [lens info, angle, distance].
Post: [color grade, film stock reference if aplicável].
```

Exemplo:
```
Medium close-up of streetwear model wearing oversized denim jacket on São Paulo
underground subway platform, harsh fluorescent lighting from above, gritty editorial mood.
Camera: 50mm, eye level, 1.5m distance.
Post: Kodak Portra 400 film grain, slight desaturation in shadows.
```

## Cross com outras skills ZEUS-CO

- `cerebro-criativo` antes pra big idea (não desperdiça crédito Higgsfield em ideia ruim)
- `cco-art-director` valida a referência visual ANTES do prompt
- `cco-brand-guardian` valida fit brand após geração
- `cfo-controller` se queimar > $50 num mês precisa registrar

## Sobre tornar Higgsfield MCP nativo

Higgsfield ainda não tem MCP oficial. Quando lançar (eles têm API REST documentada), construir adapter:
- Wrap REST endpoints em ferramentas MCP
- Auth via API key (1Password vault)
- Add custos por chamada no `_LEDGER.md` global
