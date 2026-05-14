---
name: design-lab-motion-frames
description: Motion design, HyperFrames, animação stop-motion, GIFs animados, micro-interactions. Agrupa 5 skills detalhadas (animation-motion). Use pra 'motion', 'HyperFrames', 'GIF animado', 'stop motion', 'animação CSS', 'micro-interaction', 'loading state'.
---

# Design Lab Motion Frames

## Princípio
Motion = direção da atenção + feedback de estado. Cada frame justifica seu tempo. Sem propósito, motion é distração.

## Quando uso
- Hero motion em LP
- Loading state / skeleton
- Brand film (curto)
- IG Reels com motion próprio
- Email animado

## Output canônico
1. Storyboard (frame-by-frame)
2. Timing (easing curves, durations)
3. Output (GIF, MP4 loop, Lottie, CSS animation, HyperFrames code)
4. Asset breakdown (qual elemento se anima, como)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/animation-motion/`

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Critique Gate (auto-QA antes de retornar — 5 dimensões)

**Antes de devolver output pro Diego**, rodar mental critique nas 5 dimensões (Open Design pattern):

| Dim | Pergunta | Pass se... |
|---|---|---|
| **1. Philosophy** | Output reflete a direção visual escolhida (1 das 5)? | Paleta OKLch + type stack + spacing batem |
| **2. Hierarchy** | A leitura é clara em 3s a 1m de distância? | F-pattern / Z-pattern respected. 1 foco. |
| **3. Execution** | Detalhes técnicos corretos? | Sem typos, sem layout broken, sem cores fora do brand-guide |
| **4. Specificity** | Output é específico ao brief (não genérico)? | Nomes/dados reais da empresa, não placeholders |
| **5. Restraint** | Nada supérfluo? Se removo, falta? | < 5 elementos competindo por atenção |

**Decisão**:
- **5/5 pass** → entrega
- **4/5 pass** → entrega com flag explícito do gap ("⚠️ Specificity: usei placeholder X, preencher antes do final")
- **≤ 3/5 pass** → **refina antes** (não entrega rascunho ruim. Re-roda skill com aprendizado dos gaps)

**NÃO publicar/exportar sem 5/5 confirmado** se output é client-facing (board pack, fundraising deck, KV de campanha).

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-motion-frames-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-motion-frames · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`, `design-lab-landing-page`

### 🤝 Peers
- `cco-art-director`
- `design-lab-video-generation` (quando vídeo gerado)

### ⬇️ Downstream
- Higgsfield (image-to-motion)

### ✅ QA pair
- `cco-art-director`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-motion-frames · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-motion-frames · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-motion-frames.md`.
