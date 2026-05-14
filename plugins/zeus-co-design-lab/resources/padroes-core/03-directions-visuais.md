# Padrão 03 · 5 Direções Visuais (com paleta OKLch determinística)

Quando a marca não está definida, o orquestrador oferece estas 5 escolas como
ponto de partida. Cada uma vem com palette OKLch, font stack e posture cues
**concretos** — nada de improviso.

> **Pra detalhe técnico completo** (valores OKLch exatos, referências, posture
> cues por escola), ver `prompts-originais/directions.ts`.

## 1. Editorial — Monocle / FT magazine

- **Quando usar:** briefs editoriais, publicações, content marketing premium
- **Display:** Iowan Old Style / Charter / Georgia (serif)
- **Body:** sistema (sans humanista)
- **Paleta:** papel `oklch(98% 0.004 95)` + tinta `oklch(20% 0.018 70)` + 1 acento editorial
- **Posture:** sem sombras, sem cards arredondados, bordas + whitespace fazem o trabalho
- **NÃO usar para:** SaaS, dashboards, e-commerce utilitário

## 2. Modern Minimal — Linear / Vercel

- **Quando usar:** SaaS B2B, tech, dev tools, produto digital
- **Display:** Inter Variable (peso 510-590, negative letter-spacing -1.5px no 72px)
- **Body:** Inter Variable peso 400-510
- **Paleta:** dark-mode-native `oklch(15% 0.005 270)` + brand indigo `oklch(60% 0.18 270)`
- **Posture:** dark canvas, bordas semi-transparentes (rgba white 0.05), shadows multi-layer

## 3. Warm Soft — Stripe Atlas / Notion

- **Quando usar:** brand humano, serviço, fintech amigável, edu
- **Display:** Söhne / Inter (peso médio)
- **Body:** sans humanista
- **Paleta:** off-white quente `oklch(97% 0.012 80)` + acentos saturados quentes
- **Posture:** rounded-2xl, sombras suaves, fotos ou ilustração com toque humano

## 4. Tech Utility — Vercel CLI / Cursor

- **Quando usar:** dashboard, ferramenta interna, doc técnica, IDE
- **Display:** Geist Mono / IBM Plex Mono
- **Body:** Geist Sans / Inter
- **Paleta:** monocromático com 1 highlight elétrico (cyan, lime ou magenta)
- **Posture:** grid denso, dados-first, hierarquia por mono vs sans

## 5. Brutalist Experimental — Off-White / The Browser Company

- **Quando usar:** drop, lançamento de marca jovem, edição limitada, statement
- **Display:** Söhne Breit / Druk / Migra (display brutalist)
- **Body:** mono ou serif contrastante
- **Paleta:** alto contraste, cor saturada cortando preto/branco puro
- **Posture:** asymmetric, layouts quebrados intencionalmente, tipo é o protagonista

## Como o orquestrador aciona

1. No discovery form, pergunta 5 ("Brand context") com radio:
   - "Já tenho brand spec — vou compartilhar"
   - "Combinar com site/screenshot de referência"
   - **"Escolher uma direção pra mim"** → abre 2º question-form com as 5 escolas
2. Usuário escolhe 1 das 5
3. Orquestrador injeta o spec da escola (palette OKLch, fonts, posture) direto no `:root` do template

---

**Fonte:** `apps/daemon/src/prompts/directions.ts` (284 linhas, Apache 2.0)
