# 5 Direções Visuais — Quick Reference

> Match brief → 1 direção em <5s. Cada direção tem paleta OKLch determinística pronta pra aplicar.
> Detalhes completos em `03-directions-visuais.md`.

## Decision tree (rápido)

```
Brief é editorial / magazine / lifestyle?
├── Sim → Direção 1: Editorial Monocle

Brief é SaaS / B2B / tech moderno / clean?
├── Sim → Direção 2: Modern Minimal

Brief é wellness / artisanal / warm / brand orgânico?
├── Sim → Direção 3: Warm Soft

Brief é developer / utility / dense info / pragmático?
├── Sim → Direção 4: Tech Utility

Brief é underground / drop streetwear / manifesto / raw?
├── Sim → Direção 5: Brutalist
```

## As 5 direções

### 1. **Editorial Monocle**
- **Vibe**: magazine sofisticada, Monocle/Wallpaper, lookbook moderno
- **Paleta core (OKLch)**: cream `oklch(96% 0.02 80)` + ink `oklch(15% 0.02 250)` + accent earth `oklch(45% 0.10 30)`
- **Type**: Playfair Display (heading) + Inter (body) + accent serif italic
- **Spacing**: generoso (1.5× base), grid 12-col com gutters largos
- **Use quando**: D2C apparel, lookbook, brand manifesto, magazine de marca
- **DSes match**: editorial, warm-editorial, refined

### 2. **Modern Minimal**
- **Vibe**: SaaS top-tier, Linear/Vercel/Stripe, B2B contemporâneo
- **Paleta core (OKLch)**: white `oklch(99% 0.005 250)` + ink `oklch(20% 0.02 250)` + accent vibrant `oklch(55% 0.20 264)`
- **Type**: Inter / Geist (heading + body) + accent mono `JetBrains Mono`
- **Spacing**: preciso (1.25× base), grid 12-col rígido
- **Use quando**: LP de SaaS, dashboard, pricing page, B2B contemporâneo
- **DSes match**: minimal, modern, linear-app, vercel, stripe, anthropic

### 3. **Warm Soft**
- **Vibe**: wellness, artesanal, brand orgânico, Notion-like
- **Paleta core (OKLch)**: warm white `oklch(97% 0.02 70)` + sienna `oklch(35% 0.08 40)` + accent terracotta `oklch(60% 0.13 30)`
- **Type**: Fraunces (heading) + Inter (body) + accent script (Caveat)
- **Spacing**: confortável (1.4× base), rounded corners (8-12px)
- **Use quando**: wellness, beleza orgânica, marca friendly, editorial soft
- **DSes match**: friendly, warm-editorial, notion, posthog

### 4. **Tech Utility**
- **Vibe**: developer-first, GitHub/Linear dark, dense info, pragmático
- **Paleta core (OKLch)**: dark base `oklch(18% 0.01 250)` + accent neon `oklch(70% 0.25 145)` (green) ou `oklch(70% 0.20 264)` (blue)
- **Type**: Geist Mono (heading) + Inter (body) + accent mono
- **Spacing**: denso (1.0× base), grid pixel-perfect, sharp corners
- **Use quando**: developer docs, dashboard analytics, terminal-style, infra
- **DSes match**: linear-app, github, vercel, sentry, supabase, claude

### 5. **Brutalist**
- **Vibe**: raw, manifesto, drops underground, neobrutalism playful
- **Paleta core (OKLch)**: pure black `oklch(0% 0 0)` + pure white `oklch(100% 0 0)` + 1 spot color saturated `oklch(60% 0.30 30)` (red/orange/yellow)
- **Type**: Inter Black / Archivo Black (heading harsh) + Inter (body) + mono ASCII art
- **Spacing**: erratic (mix 0.5× e 2.5×), borders 2-4px solid, harsh shadows
- **Use quando**: drop streetwear, manifesto, undergrund, anti-establishment
- **DSes match**: brutalism, neobrutalism, bold

## Anti-padrões (NÃO escolher quando)

- **Editorial Monocle**: brief precisa de conversão imediata (e-commerce, SaaS LP) → muito refinado, perde CTA
- **Modern Minimal**: brief é luxury ou lifestyle premium → muito frio, perde alma
- **Warm Soft**: brief é tech B2B sério → vira fofinho, perde autoridade
- **Tech Utility**: brief é D2C massa → developer-vibe afasta consumidor
- **Brutalist**: brief é enterprise / wealth / fintech tradicional → grita anti-establishment, gera desconfiança

## Como o orquestrador escolhe (workflow)

1. Lê brief (Fase 0 + discovery se necessário)
2. Identifica **setor** + **tom** + **estágio** + **público**
3. Aplica decision tree (acima)
4. Sugere 1 direção principal + 1 alternativa
5. Diego confirma ou ajusta
6. Aplica paleta OKLch + type stack + spacing scale aos outputs
7. Cross-check com brand-guide existente da empresa (não pode brigar)
