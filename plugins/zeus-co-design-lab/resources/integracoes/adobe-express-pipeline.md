# Pipeline · Adobe Express (via MCP)

> **Status:** MCP Adobe já conectado (`mcp__1c4e78c8-*`). Suite completa disponível.

## Quando o DESIGN-LAB (zeus-co-design-lab) aciona o Adobe

Para **peça publicitária finalizada** que precisa de:
- Edição precisa de imagem (brilho, contraste, cor, recorte)
- Geração de imagem com Firefly
- Animação de design existente
- Vetorização, remoção de fundo, expansão generativa
- Conversão / merge de PDF
- Edição de vídeo (corte, redimensionamento)
- Áudio (enhance speech, sumarização de mídia)

## Tools mais relevantes

| Tool                                          | Quando usar                                         |
|-----------------------------------------------|-----------------------------------------------------|
| `mcp__1c4e78c8-*__image_remove_background`    | Limpar foto pra usar em deck/peça                   |
| `mcp__1c4e78c8-*__image_generative_expand`    | Estender imagem (16:9 → 21:9 por exemplo)           |
| `mcp__1c4e78c8-*__image_vectorize`            | Converter raster em vetor (logo, ícone)             |
| `mcp__1c4e78c8-*__image_adjust_*`             | Brilho, contraste, exposição, cor, HSL              |
| `mcp__1c4e78c8-*__image_apply_*`              | Blur, halftone, glitch, tint, lens blur             |
| `mcp__1c4e78c8-*__create_firefly_board`       | Board de moodboard Firefly                          |
| `mcp__1c4e78c8-*__animate_design`             | Animar peça estática                                |
| `mcp__1c4e78c8-*__document_convert_pdf`       | Conversão de/para PDF                               |
| `mcp__1c4e78c8-*__video_resize`               | Reformatar vídeo (16:9 → 9:16 por exemplo)          |
| `mcp__1c4e78c8-*__search_design`              | Buscar template Adobe Express                       |
| `mcp__1c4e78c8-*__media_enhance_speech`       | Limpar áudio de podcast/voice over                  |

## Fluxo recomendado

```
1. Asset entra do Freepik ou Higgsfield
2. DESIGN-LAB (zeus-co-design-lab) decide se precisa de retoque Adobe:
   - Foto crua → recorte + ajuste cor + remoção de fundo
   - Imagem AI → upscale + ajuste fino
   - Vídeo → resize para formato alvo (9:16 social, 16:9 web)
3. Aciona tool Adobe específica
4. Output finalizado entra na peça
```

## Boas práticas

- **Não retocar em excesso.** Adobe MCP é poderoso mas pode "matar" a foto se você der 10 ajustes seguidos. Máximo 2-3.
- **Order matters.** Sempre: recorte → cor → efeitos. Não: efeito → cor → recorte.
- **Manter original.** Salvar versão antes de retoque, caso precise refazer.

## Quando NÃO usar Adobe

- Para design completo do zero → use `pptx-generator`, `web-artifacts-builder` ou Canva via outra integração
- Para edição rápida de vídeo simples → `remotion` (programático) é mais rápido
