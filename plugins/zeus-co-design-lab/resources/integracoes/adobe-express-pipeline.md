# Pipeline · Adobe Express + Firefly — EXECUTÁVEL

> **Status**: MCP Adobe conectado (`mcp__1c4e78c8-*`). Suite completa: image edit + animate + generative + document.
> **Best fit**: refine/edit + animate + export final. Não é primary generator (use Freepik Mystic ou Higgsfield pra geração).

## Quando o `design-lab-*` aciona Adobe Express

- `design-lab-image-generation` → **refine** imagem gerada (background remove, color adjust, generative expand)
- `design-lab-poster-key-visual` → finalize KV (resize multi-aspect, color grade)
- `design-lab-motion-frames` → animate design via `animate_design`
- `design-lab-magazine-editorial` → document render (PDF final)
- `design-lab-deck` → export PPT-style refinado

## Detecção de ambiente

```
Modo A — Cowork desktop com MCP Adobe conectado
  → executa via mcp__1c4e78c8-*__*

Modo B/C — Claude.ai web OU MCP off
  → instrução manual (abre Adobe Express browser)
```

## Tools Adobe MCP disponíveis (subset relevante)

### Image edit (mais usados)
| Tool | Quando usar |
|---|---|
| `image_remove_background` | Cortar BG de produto/pessoa |
| `image_crop_and_resize` | Multi-aspect (1:1, 9:16, 3:2, 16:9) |
| `image_generative_expand` | Estender canvas (outpaint) |
| `image_fill_area` | Generative fill |
| `image_select_by_prompt` | Seleção semântica (ex: "select shirt") |
| `image_select_subject` | Auto subject selection |
| `image_apply_color_overlay` | Color treatment |
| `image_adjust_*` | Brightness/contrast/saturation/temperature/highlights/shadows |
| `image_apply_preset` | Aplicar preset salvo |
| `image_apply_lens_blur` | Blur bokeh |
| `image_apply_glitch_effect` | Glitch creative |
| `image_apply_halftone` | Halftone (vintage editorial) |
| `image_vectorize` | Raster → SVG |
| `image_add_grain` | Film grain |
| `image_auto_straighten` | Endireitar fotos |

### Document
| Tool | Quando usar |
|---|---|
| `document_convert_pdf` | Convert PDF |
| `document_render_layout` | Render layout document |
| `document_render_vector` | Render vector |
| `document_merge_data_layout` | Merge data → layout (mail merge style) |

### Generative
| Tool | Quando usar |
|---|---|
| `change_background_color` | Trocar BG color |
| `animate_design` | Animação de design |
| `create_firefly_board` | Board Firefly |
| `font_recommend` | Sugestão tipográfica |
| `fill_text` | Preencher área com text |

### Asset management
| Tool | Quando usar |
|---|---|
| `asset_search` | Buscar asset Adobe Stock |
| `asset_license_and_download_stock` | License + download |
| `asset_preview_file` | Preview |
| `asset_inline_preview` | Preview inline |

### Video
| Tool | Quando usar |
|---|---|
| `video_create_quick_cut` | Quick cut video |
| `video_resize` | Resize video multi-aspect |

## Workflow padrão (refine imagem)

### Caso 1: Refinar imagem AI-gerada
```
1. Asset originado de Freepik Mystic ou Higgsfield
2. Tool: mcp__1c4e78c8-*__image_remove_background (se precisar isolar)
3. Tool: mcp__1c4e78c8-*__image_adjust_color_temperature (warm/cool fit direção)
4. Tool: mcp__1c4e78c8-*__image_apply_grain (se Editorial Monocle direction)
5. Tool: mcp__1c4e78c8-*__image_crop_and_resize → multi-aspect
6. Save: ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/final/
```

### Caso 2: Multi-aspect resize pra campanha 360
```
Input: 1 KV master (3:2 ratio típico)
Output: 1:1 (Instagram post), 9:16 (Story/Reels), 16:9 (LP hero), 4:5 (Pinterest), banner 3:1 (OOH)

Loop:
For each aspect_ratio in [1:1, 9:16, 16:9, 4:5, 3:1]:
  Tool: image_crop_and_resize
  Args: { src, target_aspect: ratio, smart_crop: true }
  Save: assets/final/<name>-<ratio>.jpg
```

### Caso 3: Animate hero
```
Input: imagem hero estática
Tool: animate_design
Args: { 
  src, 
  animation_type: "parallax" | "fade" | "subtle_motion",
  duration: 3-5s,
  output_format: "mp4" | "gif"
}
```

## Boas práticas

- **Adobe Express é "polish", não "criação"**: comece pelo Freepik/Higgsfield, refine no Adobe
- **Batch ops > single ops**: se for 1 imagem só, abre o app. Pipeline MCP vale pra > 3 ops
- **Save originais**: nunca substitua source. Sempre `<name>-final.png` em pasta separada
- **Multi-aspect = sempre exigido** em campanha (D2C: pelo menos 1:1 e 9:16)
- **Vector preferred** pra logo/icon: rasterize só no final

## Fallback (modo manual)

Se MCP off:
```
🟡 Adobe MCP não disponível. Manual:

1. Abre https://express.adobe.com
2. Login (Adobe ID)
3. Upload <arquivo>
4. Aplique: <lista de operações específicas>
5. Export multi-aspect
6. Salva em ~/Documents/Claude/Projects/<empresa>/_Areas/CCO/assets/final/
7. Volta no chat com paths — eu sigo
```

## Cross com outras skills ZEUS-CO

- `cco-art-director` aprova **antes** dos refinements (não refinar errado)
- `cco-brand-guardian` valida cores/grain/treatment alinha brand
- `cmo-growth-performance` se for creative pra ads (multi-aspect obrigatório)
