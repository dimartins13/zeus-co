# Pipeline · Freepik

> **Status:** MCP nativo já conectado no setup. Tools `mcp__freepik__*` disponíveis.

## Quando o DESIGN-LAB (zeus-co-design-lab) aciona o Freepik

O orquestrador chama o Freepik quando a skill em execução precisa de:
- **Asset visual pronto** (foto, ilustração, ícone, vetor SVG)
- **Imagem gerada por IA Mystic** (geração via texto, controle de estilo)
- **Detecção de IA** (verificar se uma imagem é AI-generated)

Não aciona o Freepik para vídeo, áudio ou design final — esses vão por outros pipelines.

## Tools disponíveis

| Tool                                           | Função                                                |
|------------------------------------------------|-------------------------------------------------------|
| `mcp__freepik__search_resources`               | Busca recursos (foto, vetor, PSD) por keyword         |
| `mcp__freepik__search_icons`                   | Busca ícones específicos                              |
| `mcp__freepik__get_resource_detail_by_id`      | Detalhes de um recurso (formatos, licença)            |
| `mcp__freepik__get_resource_download_formats`  | Formatos disponíveis pra download                     |
| `mcp__freepik__download_resource_by_id`        | Download direto do asset                              |
| `mcp__freepik__download_icon_by_id`            | Download de ícone                                     |
| `mcp__freepik__text_to_image_mystic_sync`      | Gerar imagem nova via Mystic (text-to-image)          |
| `mcp__freepik__detect_ai_image`                | Verificar se imagem é AI-generated                    |

## Fluxo recomendado

```
1. Skill ativa identifica necessidade visual:
   ex: "preciso de foto de mesa de reunião executiva, tom warm, horizontal"

2. DESIGN-LAB (zeus-co-design-lab) chama mcp__freepik__search_resources com:
   - query: "executive meeting table warm light horizontal"
   - filters: orientation=horizontal, type=photo

3. Lê resultados (até 5 candidatos), avalia contra direção visual escolhida

4. Se candidato OK → mcp__freepik__download_resource_by_id
   Se nada bate → mcp__freepik__text_to_image_mystic_sync com prompt detalhado

5. Asset entra na pasta da peça em construção, skill prossegue
```

## Boas práticas

- **Direção visual primeiro.** Buscar "foto executivo" sem ter direção é convite a stock cliché. Use as 5 escolas (`padroes-core/03-directions-visuais.md`) para enriquecer a query.
- **Mystic para hero shots.** Para a foto principal de uma peça, vale gastar uma geração Mystic com prompt detalhado, ao invés de pegar stock.
- **Stock para auxiliares.** Ícones, texturas, padrões de fundo — busca direta.
- **Verificar licença sempre.** O `get_resource_detail_by_id` retorna a licença — Freepik Premium vs Free importa.

## Pipeline mais comum no Zeus

Para deck de cliente → busca Freepik por hero image + ícones para sub-slides + (opcional) Mystic para 1 frame específico que precisa ser único.

Para LP → Mystic para hero shot + Freepik para ilustrações secundárias.

Para social carousel → Mystic gera todas as 5 imagens com prompt consistente.
