---
name: design-lab-social-carousel
description: Carrosséis Instagram, TikTok pra LinkedIn, posts série. 10-frame Instagram carousel pattern. Use pra 'carrossel', 'IG carousel', 'instagram série', 'post serie', 'LinkedIn carousel', 'TikTok slides'.
---

# Design Lab Social Carousel

## Princípio
Carrossel = micro-narrativa. Hook no slide 1, valor em 2-8, CTA em 9-10. Sem hook, não rola swipe.

## Quando uso
- IG content (D2C, lifestyle, B2B)
- LinkedIn educational
- TikTok slide format
- Reels com legenda em slide

## Output canônico
1. Hook frame (slide 1 — gancho viral)
2. Body frames (slides 2-8 — argumento)
3. CTA frame (slide 9-10 — ação)
4. Captions (caption principal + alt-text por slide)
5. Hashtag set

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/marketing-creative/` (carousel skills)
- Cross com `zeus-co-marketing:instagram-carousel-builder`

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-social-carousel-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-social-carousel · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `zeus-co-marketing:instagram-carousel-builder` (skill especializada existente)
- `cco-content-strategist`
- `cco-copy-master`

### ⬇️ Downstream
- Canva MCP / Adobe Express MCP (export)

### ✅ QA pair
- `cco-brand-guardian`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-social-carousel · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-social-carousel · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-social-carousel.md`.
