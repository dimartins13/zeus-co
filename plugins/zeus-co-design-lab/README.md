# zeus-co-design-lab

**DESIGN-LAB do ZEUS-CO** — laboratório de produção visual.

Curado a partir do projeto open-source [`nexu-io/open-design`](https://github.com/nexu-io/open-design) (Apache 2.0), adaptado para o ecossistema ZEUS-CO, integrado com Freepik / Higgsfield / Adobe Express / Gamma.

**Uso interno do portfolio Diego Martins.** Atribuição completa em [`NOTICE.md`](./NOTICE.md).

---

## Estrutura

```
zeus-co-design-lab/
├── .claude-plugin/plugin.json        ← v0.1.0
├── skills/                            ← 12 skills planas (entry points)
│   ├── design-lab-orquestrador        ← porta de entrada
│   ├── design-lab-discovery           ← questionário 7 perguntas
│   ├── design-lab-deck                ← decks/slides/pitch
│   ├── design-lab-landing-page        ← LP/web
│   ├── design-lab-magazine-editorial  ← editorial/lookbook
│   ├── design-lab-email-html          ← email HTML
│   ├── design-lab-social-carousel     ← IG/TT carousel
│   ├── design-lab-poster-key-visual   ← KV/poster/OOH
│   ├── design-lab-motion-frames       ← motion/GIF/HyperFrames
│   ├── design-lab-image-generation    ← AI image (Freepik/Higgsfield/Firefly)
│   ├── design-lab-video-generation    ← AI video (Higgsfield/Sora)
│   └── design-lab-design-system       ← DS tools + referência 66 DSes
└── resources/                         ← orquestrador puxa on-demand
    ├── design-systems/                ← 66 DSes (Apple, Stripe, Linear, etc)
    │   ├── _schema/                   ← formato canônico
    │   ├── genericos/                 ← 27 DSes neutros
    │   ├── tech-platforms/            ← 27 DSes tech (Vercel, Linear, Notion, etc)
    │   └── marcas-referencia/         ← 12 marcas (Apple, Stripe, etc — USO INTERNO)
    ├── padroes-core/                  ← 5 padrões + 8 prompts originais (.ts)
    │   ├── 01-schema-skill-frontmatter.md
    │   ├── 02-critique-5-dimensoes.md
    │   ├── 03-directions-visuais.md   ← 5 direções com paleta OKLch
    │   ├── 04-discovery-form.md
    │   ├── 05-loop-detect-discover-direct-deliver.md
    │   └── prompts-originais/
    ├── skills-detalhadas/             ← 51 SKILL.md upstream (Open Design) preservadas
    └── integracoes/                   ← 4 pipelines de integração
        ├── freepik-pipeline.md
        ├── higgsfield-pipeline.md
        ├── adobe-express-pipeline.md
        └── gamma-pipeline.md
```

## Como usar

### Entry point único: `design-lab-orquestrador`

```
Diego: "design-lab, monta KV pra drop de janeiro da dope street"
```

Orquestrador:
1. **Detect** — lê CLAUDE.md + brand-guide da dope street (Fase 0 obrigatória)
2. **Discover** — dispara `design-lab-discovery` (7 perguntas) se brief ambíguo
3. **Direct** — escolhe direção visual (1 das 5 em `resources/padroes-core/03-directions-visuais.md`)
4. **Deliver** — dispara `design-lab-poster-key-visual` + Freepik MCP + Higgsfield se hero gerado

### Invocação direta

Diego pode invocar skill vertical sem orquestrador:
- `"design-lab-deck, board pack mensal Crazyflips"`
- `"design-lab-landing-page, hero da Ventage"`
- `"design-lab-image-generation, gera 4 variants de hero AI pra dope street"`

## Diferenças vs upstream Open Design

| Aspecto | Open Design (upstream) | zeus-co-design-lab |
|---|---|---|
| Runtime | Daemon `pnpm tools-dev` + 12 agent adapters + BYOK proxy | Claude/Cowork nativo (sem daemon) |
| Skills | 107 (94 curadas de outros autores) | 51 detalhadas em `resources/` + 12 planas no matching |
| Design systems | 150 | 66 curados (genéricos + tech-platforms + marcas-ref) |
| Integrações | gpt-image-2, Seedance, HyperFrames, Grok | **Freepik MCP + Higgsfield + Adobe Express MCP + Gamma MCP** (próprias) |
| Idioma orquestrador | Inglês | pt-BR (skills upstream em inglês preservadas) |
| ZEUS-CO integration | N/A | bridge com `cco-orquestrador`, `cmo-orquestrador`, `cerebro-criativo` |

## Licença + atribuição

- Plugin: ZEUS-CO (Diego Martins) — uso interno
- Skills upstream: Apache 2.0 (nexu-io/open-design + 94 autores via `upstream:` no frontmatter de cada SKILL.md em `resources/skills-detalhadas/`)
- Design systems de marcas reais (Apple, Stripe, etc): **uso interno como referência**, NUNCA pra cliente concorrente direto. Detalhes em `NOTICE.md`.

## Self-Evaluation (Camada 1 do Sistema Vivo)

Cada uma das 12 skills planas tem bloco Self-Evaluation 3-modos (Cowork chat / Claude.ai web / autônomo). Feedback agregado pelo `zeus-co-labs:labs-orquestrador` cron sex 02:00.

## Status

- **v0.1.0** (2026-05-14) — primeira release. 12 skills planas + 51 detalhadas + 66 DSes + 5 padrões + 4 integrações.
- **Próximo**: integração real com Freepik MCP (já conectado no Cowork). Higgsfield adapter (via Chrome MCP ou API direta).
