# Design Systems INDEX — Quick Lookup

> 66 design systems curados pra inspiração visual. Orquestrador puxa on-demand.
> **Como usar**: pra cada brief, escolhe **1-2 DSes** com mood matching. Não misturar 5+.

## Genéricos (27) — neutros, sempre seguros

| DS | Mood | Paleta dominante | Usa quando |
|---|---|---|---|
| `default` | base safe | neutral grays | brief sem direção clara |
| **`editorial`** | magazine | warm + serif heavy | lookbook, brand book, manifesto |
| **`minimal`** | clean | white + 1 accent | SaaS, B2B, professional |
| **`modern`** | contemporary | OKLch precise + sans | tech, startups jovens |
| `bold` | impacto | high contrast | drops, lançamentos, statements |
| `brutalism` | raw | preto + cores diretas | undergrond, streetwear, manifesto |
| `neobrutalism` | playful raw | bright + harsh shadows | drops jovem, gaming, web3 |
| `corporate` | conservative | navy + grays | enterprise, finance B2B |
| `dithered` | nostalgic | 8-bit pixel | retro tech, gaming, niche |
| `doodle` | handcrafted | playful sketches | indie, hand-made, artisanal |
| `dramatic` | cinematic | dark + saturated | premium, luxo, editorial premium |
| `elegant` | refined | muted + serif | luxury fashion, beauty, premium |
| `energetic` | high-energy | neon + bold | fitness, gaming, youth |
| `expressive` | art-driven | varied palettes | creative agencies, artistic |
| `friendly` | warm welcoming | soft colors | wellness, education, kids |
| `glassmorphism` | iOS-style | translucent + blur | apps mobile, fintech moderno |
| `luxury` | high-end | gold + black | premium goods, hotels, luxo |
| `neon` | cyber | electric + dark BG | gaming, web3, late-night |
| `premium` | upmarket | dark + restrained | enterprise high-tier |
| `professional` | trusted | blue + structured | B2B, consulting, professional services |
| `refined` | curated | minimal warm | boutique, artisanal premium |
| `retro` | throwback | 70s/80s/90s | nostalgic, cult, music |
| `sleek` | modern minimal | metallic clean | electronics, gadgets, tech |
| `storytelling` | narrative | varied per chapter | brand films, manifestos |
| `vibrant` | colorful | saturated bright | youth, fashion, social-first |
| `vintage` | aged | sepia + faded | heritage, artisanal, retro brands |
| **`warm-editorial`** | Monocle-style | cream + serif + earth | lifestyle magazine, editorial moderno |

## Tech Platforms (27) — referência de empresa real

Use pra brief "estilo Stripe" / "como Linear" / "vibe Notion" etc.

| DS | Categoria | Característica visual marcante |
|---|---|---|
| `apple` | Hardware/SaaS | Sans precision + cinematic photography + glass |
| `anthropic` | AI/SaaS | (curado de awesome-design-skills) |
| `claude` | AI/SaaS | Orange accent + warm editorial |
| `cohere` | AI | Coral accent + clean minimal |
| `mistral-ai` | AI | Vibrant tricolor + bold geometric |
| `openai` | AI | Dark + green accent + dense |
| `x-ai` | AI | Black + grayscale + utilitário |
| `huggingface` | AI/Community | Yellow + emoji + playful |
| `replicate` | AI/Infra | Mono + minimal SaaS |
| `ollama` | AI/Local | Llama-themed + warm |
| `linear-app` | Productivity | Dark + purple + pixel-perfect |
| `notion` | Productivity | Off-white + serif + emoji |
| `cursor` | Developer | Dark + accent + AI-first |
| `lovable` | No-code | Bright + playful + accent gradient |
| `framer` | Design/No-code | Bold + animated + brand-forward |
| `figma` | Design | Multi-color brand + interactive |
| `github` | Developer | Dark + green + dense info |
| `raycast` | Productivity | Native macOS feel + warm |
| `vercel` | Infra/Deploy | Mono + black + sharp triangles |
| `stripe` | Payments | Soft gradients + indigo + premium SaaS |
| `supabase` | Database | Green + dark + modern dev |
| `mongodb` | Database | Green + clean enterprise |
| `clickhouse` | Database | Yellow + dense + analytics |
| `sentry` | Observability | Purple + dark + dev |
| `posthog` | Analytics | Cream + playful + indie |
| `sanity` | CMS | Clean + minimal + creator |
| `elevenlabs` | Voice AI | Dark + audio waveform + premium |
| `resend` | Email | Soft + indigo + utility |

## Marcas Referência (12) — **USO INTERNO**, nunca pra cliente concorrente

| DS | Setor | Característica visual |
|---|---|---|
| `airbnb` | Travel | Soft pink + lifestyle photography |
| `canva` | Design/SaaS | Multi-color + playful + accessible |
| `discord` | Comms | Purple + dark + gamer |
| `duolingo` | Education | Bright green + mascot + gamified |
| `intercom` | SaaS | Soft + conversational + helpful |
| `mastercard` | Financial | Red + orange + iconic gradient |
| `miro` | Collaboration | Yellow + playful + creative |
| `nike` | Apparel/Sport | Bold + minimal + iconic swoosh |
| `revolut` | Fintech | Dark + neon + premium |
| `slack` | Comms | Multi-color + friendly + playful |
| `spotify` | Music | Green + dark + cover-art driven |
| `wise` | Fintech | Bright green + simple + global |

## Match brief → DS (decision tree)

```
Setor?
├── D2C/lifestyle/moda → editorial OR warm-editorial OR vintage (dependendo do tom)
├── SaaS B2B → minimal OR linear-app OR stripe
├── Tech/AI → modern OR anthropic OR claude OR mistral-ai
├── Fintech → premium OR wise OR revolut (dependendo do segmento)
├── E-commerce mass → friendly OR airbnb
├── Gaming/streetwear → bold OR neobrutalism OR neon
├── Luxury → elegant OR luxury OR dramatic
├── Wellness/edu → friendly OR storytelling
└── Enterprise/financial → corporate OR professional

Tom?
├── Sério → minimal, corporate, premium, refined
├── Playful → friendly, lovable, doodle, neobrutalism
├── Editorial → editorial, warm-editorial, storytelling
├── Raw/edgy → brutalism, neobrutalism, neon
└── Premium → luxury, premium, dramatic, elegant

Brand novo vs estabelecido?
├── Novo → escolha 1 dos genéricos como anchor
└── Estabelecido → use brand-guide próprio da empresa + 1 DS como referência específica de execução
```

## Como ler um DESIGN.md (formato canônico)

Cada DS tem:
1. **Frontmatter** (`od:` tags): mood, style, palette type
2. **Palette** (OKLch precise): primary, secondary, neutral steps 0-1000
3. **Type stack**: headings + body + accent fonts
4. **Spacing scale**: base + multipliers
5. **Component patterns**: button, card, hierarchy do/don't
6. **Voice notes**: tone, phrases-âncora, palavras proibidas (quando aplicável)

Open file `resources/design-systems/_schema/DESIGN.md` pra ver template canônico completo.
