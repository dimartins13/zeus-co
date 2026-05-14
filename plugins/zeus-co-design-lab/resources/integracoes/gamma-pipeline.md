# Pipeline · Gamma (via MCP)

> **Status:** MCP Gamma já conectado (`mcp__2801b3d7-*`). Geração de deck via prompt.

## Quando o DESIGN-LAB (zeus-co-design-lab) aciona o Gamma

Para **deck rápido** quando:
- Cliente precisa de pitch em 2h e não há tempo pra montagem manual
- Volume alto de decks similares (várias propostas com mesma estrutura)
- Refinamento de slide isolado dentro de deck existente

Não aciona Gamma para:
- Deck premium investidor (use `pptx-generator` com template editorial)
- Deck com identidade visual rigorosa do cliente (Gamma tem template próprio)

## Tools disponíveis

| Tool                                          | Função                                              |
|-----------------------------------------------|-----------------------------------------------------|
| `mcp__2801b3d7-*__generate`                   | Gerar deck completo a partir de prompt              |
| `mcp__2801b3d7-*__generate_from_template`     | Gerar a partir de template Gamma específico         |
| `mcp__2801b3d7-*__get_generation_status`      | Polling de status (geração é async)                 |
| `mcp__2801b3d7-*__get_gammas`                 | Listar decks gerados                                |
| `mcp__2801b3d7-*__read_gamma`                 | Ler conteúdo de deck existente                      |
| `mcp__2801b3d7-*__get_themes`                 | Listar temas visuais disponíveis                    |
| `mcp__2801b3d7-*__get_folders`                | Organização do workspace                            |

## Fluxo recomendado

```
1. DESIGN-LAB (zeus-co-design-lab) recebe brief de deck
2. Avalia: estilo cliente rigoroso ou flexível?
   - Rigoroso → vai para skill pptx-generator com template custom
   - Flexível / urgência → segue para Gamma
3. Constrói prompt detalhado (10 slides, mensagens por slide, tom)
4. mcp__2801b3d7-*__generate
5. Polling de status até completar
6. read_gamma para revisão
7. Se precisa ajuste → re-generate com prompt refinado
   Se precisa polimento → exportar PPTX e ajustar via pptx-generator
```

## Boas práticas

- **Prompt detalhado vence prompt curto.** "Deck sobre nosso produto" gera lixo. "Deck investidor 10 slides: 1=problema com stat X, 2=mercado de R$ Y, 3=nossa solução em 3 bullets, …" gera ouro.
- **Escolha o tema antes.** get_themes primeiro, pegar tema alinhado ao tom visual.
- **Gamma + Adobe = combo.** Gamma faz estrutura rápida, Adobe MCP retoca imagens dos slides depois.

## Limitações conhecidas

- Sem controle pixel-perfect do layout
- Templates Gamma têm "cara" reconhecível (pode ser problema pra cliente premium)
- Export para PPTX nem sempre preserva formatação 100%
