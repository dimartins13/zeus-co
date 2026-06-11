---
name: human-motion
description: Decupagem cinematográfica de motion design pra Remotion (React + Typescript) ou Three.js (cena 3D nativa). Output - código React/Remotion completo + assets organizados, pronto pra render em mp4/webm/gif via `npx remotion render` ou pra rodar a cena Three.js em browser. Princípios duros - (1) CÂMERA 3D ATIVA - nunca composição plana; sempre tem dolly, push-in, orbit, crane, rack-focus simulado, ou parallax multi-layer com z-depth real; (2) PARALLAX COMO LINGUAGEM - elementos em camadas com profundidade (z), velocidade inversamente proporcional à distância da câmera; (3) QUADRUPLE EXIT - elementos saem do frame em 4 direções diferentes simultaneamente em momentos-chave (rompe a calmaria do horizontal, dá energia); (4) SEM VOZ HUMANA - motion design fala por timing, easing e composição; áudio é trilha + foley sutil, nunca voiceover (se pedir voiceover, mando pra `/human-cinematic`); (5) TIMING É RIGOROSO - frames-chave em 60fps, easing curves explícitas (cubic-bezier ou spring com config), nada de "linear" default; (6) HIERARQUIA DE ATENÇÃO - 1 elemento dominante por momento; resto suporta; (7) FRAME 1 e FRAME FINAL são posters - cada um sustenta como still cinematográfico isolado. Dois modos - REMOTION (componente React + composições + render config, usado pra ad/social/explainer com texto e dados) e THREE-JS (cena 3D pura, usado pra hero animado de site, product reveal em rotação, ambiente imersivo). Estrutura de output - `human-output/human-motion/{run_slug}/` com `src/` (componentes), `public/` (assets), `package.json`, `remotion.config.ts` OU `index.html` + `scene.ts` (Three.js), `manifest.json` (frame-key list + timing + decisões), `preview.mp4` quando o render local rodar. Use SEMPRE para "/motion", "/human-motion", "motion design", "Remotion", "Three.js", "animação 3D", "câmera 3D", "parallax", "Quadruple Exit", "explainer animado", "hero animado", "product reveal 3D", "ad animado sem voz", "vídeo motion sem locução", "loop de fundo animado", "site com cena 3D", "transição cinematográfica", "decupagem motion", "código React de motion", "render Remotion", "animar dado", "data viz animada", "logo reveal 3D". NÃO use para vídeo live action ou cinematográfico com pessoas/cenário real (→ `/human-cinematic`), nem pra still (→ `/human-image`), nem pra upscale (→ `/human-upscale`).
---

# Human Motion — Decupagem Cinematográfica de Motion Design

Você decupa uma intenção (briefing curto, asset, conceito) em **código de motion design**: Remotion (React+TS) ou Three.js puro. Câmera 3D ativa, parallax como linguagem, timing rigoroso, **zero voz humana**.

## Os 7 princípios duros

1. **Câmera 3D ativa.** Toda cena tem movimento de câmera explícito — dolly, push-in, orbit, crane, rack-focus simulado, ou parallax multi-layer com z-depth real. Composição plana é proibida (exceto frame-poster final, 12 frames).
2. **Parallax como linguagem.** Elementos em camadas com profundidade z; velocidade inversamente proporcional à distância. Layer próximo se move rápido, distante se move devagar.
3. **Quadruple Exit.** Nos momentos-chave (transição de bloco, climax), elementos saem do frame em **4 direções simultâneas** (top/bottom/left/right). Rompe a calmaria do horizontal, injeta energia.
4. **Sem voz humana.** Motion fala por timing, easing e composição. Áudio é trilha + foley sutil, nunca VO. Se pedir voiceover → manda pra `/human-cinematic`.
5. **Timing rigoroso.** Frames-chave em **60fps**, easing curves explícitas (`cubic-bezier(0.34, 1.56, 0.64, 1)` ou spring `{damping, stiffness, mass}`). Easing `linear` proibido como default.
6. **Hierarquia de atenção.** 1 elemento dominante por momento, resto suporta. Se 3 coisas competem, escolha 1 e deixa outras dim/blur/decel.
7. **Frame 1 e Frame Final como posters.** Cada um sustenta isolado como still cinematográfico. Se o frame final não cabe num post de IG, ele falhou.

## Pré-requisitos

```bash
node --version              # ≥18
npm --version
which ffmpeg                # pra render local
```

Pra Remotion:

```bash
npx create-video@latest --template=blank   # se nunca rodou
```

Pra Three.js puro: navegador moderno. Sem build step obrigatório (Vite opcional).

## Pasta de trabalho

```
human-output/human-motion/{run_slug}/
├── src/
│   ├── Root.tsx              ← composições Remotion
│   ├── MainSequence.tsx
│   ├── components/
│   │   ├── Camera.tsx
│   │   ├── ParallaxLayer.tsx
│   │   └── QuadExit.tsx
│   └── timing.ts             ← curvas + frames-chave centralizados
├── public/
│   ├── images/
│   ├── lottie/
│   └── audio/
├── remotion.config.ts
├── package.json
├── manifest.json             ← decupagem completa (frame-by-frame)
└── preview.mp4               ← render local (após `npx remotion render`)
```

Pra Three.js:

```
human-output/human-motion/{run_slug}/
├── index.html
├── scene.ts
├── camera-rig.ts
├── parallax-layers.ts
├── assets/
└── manifest.json
```

---

## Fluxo

### 1. Leia o briefing

Input pode ser:
- Frase curta ("hero animado pro site da Ventage, sensação premium e silenciosa, 8 segundos")
- Asset (logo SVG, foto produto, dados)
- Referência (link de motion que admira)
- Combinação

### 2. Decida o stack

| Sinais no input | Stack |
|---|---|
| Texto + dados + composições por cena + saída em vídeo | **Remotion** |
| Hero de site + interação real-time + 3D geométrico + sem texto pesado | **Three.js** |
| Loop curto de background pra site | **Three.js** (mais leve em runtime) |
| Ad de 10-30s pra mídia paga | **Remotion** (mp4 final, sem JS no browser do espectador) |
| Product reveal em rotação 360 | **Three.js** se interativo, **Remotion** se vídeo final |

### 3. Decupe em frames-chave

Toda peça motion é uma sequência de frames-chave (poses-chave). Decupa **antes** de codar:

```
00:00 (frame 0)    → poster inicial: produto pequeno no centro-baixo, fundo escuro
00:01 (frame 60)   → push-in 30%, layer texto entra de baixo com spring
00:03 (frame 180)  → orbit 15° à direita, dado-chave aparece (parallax)
00:05 (frame 300)  → Quadruple Exit: 4 elementos saem nos 4 cantos
00:06 (frame 360)  → câmera puxa pra wide, logo emerge centralizada
00:08 (frame 480)  → poster final: logo + tagline, slow drift
```

Cada frame-chave define: **câmera (posição/rotação/FOV)**, **elementos no frame**, **easing pra próximo**, **trilha (intensidade/corte)**.

### 4. Escreva o código

**Remotion** — usa `useCurrentFrame()`, `interpolate()` com easing explícito, `spring()` quando cabe orgânico:

```tsx
import {useCurrentFrame, interpolate, spring, useVideoConfig, Easing} from 'remotion';

export const PushIn: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const scale = spring({frame, fps, config: {damping: 12, stiffness: 80, mass: 1}});
  const z = interpolate(frame, [0, 180], [0, -200], {
    easing: Easing.bezier(0.34, 1.56, 0.64, 1),
    extrapolateRight: 'clamp',
  });
  return <div style={{transform: `translateZ(${z}px) scale(${scale})`}}>...</div>;
};
```

**Three.js** — câmera rig explícito + GSAP/own tween pro timing:

```ts
camera.position.set(0, 1.2, 5);
gsap.to(camera.position, {z: 2.5, duration: 1.5, ease: 'expo.out'});
gsap.to(camera.rotation, {y: Math.PI / 12, duration: 1.5, ease: 'expo.out'}, '<');
```

### 5. Centralize timing

Tudo numérico (frames-chave, easing config, durations) vai em `src/timing.ts` ou `camera-rig.ts`. **Não espalha mágica pelo código.**

### 6. Render local + entrega

```bash
cd human-output/human-motion/{run_slug}
npm install
npx remotion render src/Root.tsx Main preview.mp4 --concurrency=8
```

Three.js: serve `index.html` (live-server, Vite, etc.) e mostre a cena rodando.

Devolve: pasta + frame de poster + 1 linha:

> "Pasta em `human-output/human-motion/2026-06-02-ventage-hero/`, preview rodando em 6s60fps. Quer iterar timing, trocar trilha, ou mando pra produção?"

---

## Anti-padrões

- **Câmera estática + elementos voando.** Isso é after-effects de 2010, não motion 3D. Mexe a câmera.
- **Easing linear.** Nunca. Default = `cubic-bezier(0.34, 1.56, 0.64, 1)` (overshoot leve).
- **Texto chapado dominando.** Texto em motion é coadjuvante. Se a peça é "ler texto", manda pra carrossel.
- **Voiceover.** Se aparece, manda a peça pra `/human-cinematic`.
- **Mais de 3 layers competindo simultaneamente.** Hierarquia.
- **Frame final fraco.** Sempre frame-poster final. Sempre.

## Próximo passo

Cole o briefing + qualquer asset (logo, foto, dado, referência). Eu devolvo decupagem em frames-chave + escolha de stack pra você OK antes de codar.
