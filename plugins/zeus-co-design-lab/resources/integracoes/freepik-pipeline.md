# Pipeline · Freepik — EXECUTÁVEL

> **Status**: MCP nativo conectado. Tools `mcp__freepik__*` disponíveis no Cowork desktop.
> **Fallback**: se MCP off (Claude.ai web ou MCP desconectado), retornar instruction manual.

## Quando o `design-lab-*` aciona Freepik

- `design-lab-image-generation` → busca assets stock OR gera via Mystic
- `design-lab-poster-key-visual` → hero asset base pra KV
- `design-lab-landing-page` → hero image LP, ícones, ilustrações
- `design-lab-email-html` → header image
- `design-lab-magazine-editorial` → assets pra spreads

## Detecção de ambiente (gracioso degradante)

```
SE Bash tool disponível AND mcp__freepik__* carregado:
   → modo EXECUTAR (chama tools direto)
SE NÃO:
   → modo INSTRUÇÃO (devolve passos pra Diego fazer manual)
```

## Tools disponíveis (verificar via ToolSearch se deferred)

| Tool | Quando usar | Custo aprox |
|---|---|---|
| `mcp__freepik__search_resources` | Buscar fotos/ilustrações/vetores no banco | Inclusa subscription |
| `mcp__freepik__search_icons` | Buscar ícones | Inclusa |
| `mcp__freepik__get_resource_detail_by_id` | Detalhar 1 resource | Inclusa |
| `mcp__freepik__get_resource_download_formats` | Formatos disponíveis | Inclusa |
| `mcp__freepik__download_resource_by_id` | Download asset | Conta no quota |
| `mcp__freepik__text_to_image_mystic_sync` | Gerar imagem via Mystic | Cobra créditos (cuidado) |
| `mcp__freepik__detect_ai_image` | Validar se imagem é AI | Inclusa |
| `mcp__freepik__download_icon_by_id` | Download ícone | Inclusa |

## Workflow executável padrão (5 passos)

### Passo 1 — Validar disponibilidade MCP
```
Tool: ToolSearch
Query: "select:mcp__freepik__search_resources"
SE retorna schema → MCP ok, prossegue
SE não → fallback modo INSTRUÇÃO
```

### Passo 2 — Buscar candidatos
```
Tool: mcp__freepik__search_resources
Args:
  - term: "<termo do brief>"
  - filters: { content_type, license, orientation, color_dominant }
  - limit: 12
```

### Passo 3 — Apresentar pra Diego escolher
```
Output no chat:
  - 4-6 thumbnails com ID + preview URL + license
  - Diego escolhe 1-3 (com AskUserQuestion se interativo)
```

### Passo 4 — Download (só do escolhido)
```
Tool: mcp__freepik__download_resource_by_id
Args:
  - resource_id: <id escolhido>
  - format: png/jpg/svg (depende do uso)
```

### Passo 5 — Save em path canônico
```
Path: ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/YYYY-MM-DD-<descricao>.png
Append em _LEDGER.md da empresa: download Freepik <id> <license>
```

## Geração Mystic (alternativa search)

Quando NÃO acha asset adequado na busca, OR brief precisa de imagem única:

```
Tool: mcp__freepik__text_to_image_mystic_sync
Args:
  - prompt: "<prompt estruturado: subject + style + composition + lighting + post>"
  - aspect_ratio: "16:9" / "1:1" / "9:16"
  - style: realism / illustration / 3d / etc
  - resolution: 2k / 4k
Custo: ~1-3 créditos por geração (verificar quota antes)
```

**Boas práticas Mystic**:
- Prompt: 50-80 palavras, estruturado em ordem (subject → style → composition → lighting → post)
- Sempre gerar **4 variants** primeiro (aspect ratio quadrado pra economia), refinar depois
- Cross-check direção visual da skill (das 5: Editorial/Modern/Warm/Tech/Brutalist) antes de gerar

## Fallback (modo INSTRUÇÃO — quando MCP off)

Se ToolSearch não retorna `mcp__freepik__*`, devolver no chat:

```
🟡 Freepik MCP não disponível neste ambiente. Manual:

1. Abre https://www.freepik.com em browser
2. Busca: "<termo>"
3. Filtros recomendados: <baseados no brief>
4. Download: salva em ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/
5. Volta no chat e cola path local — eu sigo daqui
```

## Cost guardrails (Diego sempre alerta)

- Search/download asset normal → quota inclusa subscription (~1000/mês)
- Mystic generation → **conta créditos**. Antes de gerar > 4 variants, perguntar Diego.
- Premium assets → checa license antes (Editorial use only NÃO serve pra ad commercial)
- Salvar IDs + license em `_LEDGER.md` da empresa pra audit trail

## Cross com outras skills ZEUS-CO

- `cco-art-director` valida visual antes do download virar deliverable
- `cco-brand-guardian` cross-check fit com brand-guide
- `clo-contratos` se license tem restrições legais relevantes
