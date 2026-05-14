---
name: design-lab-video-generation
description: Geração de vídeo via AI — Higgsfield, Sora, Runway. Agrupa 3 skills detalhadas (video-generation) + pipeline Higgsfield. Use pra 'gerar vídeo AI', 'Higgsfield video', 'Sora', 'Runway', 'video stock AI', 'hero video LP', 'IG Reels gerado AI'.
---

# Design Lab Video Generation

## Princípio
Video AI = 80% prompt, 20% post. Iteração com seed + variação. Sora/Higgsfield ainda 2-10s clips — pensar em cuts.

## Quando uso
- Hero video em LP
- IG Reels rápido
- TikTok native
- Brand film curto
- Drop announce video

## Output canônico
1. Shot list (cenas + transições)
2. Prompt por cena (style + motion + camera + lighting)
3. Output 2-10s clips por cena
4. Edit (corte, sound, sub) se aplicável
5. Asset final (MP4, MOV, GIF)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/video-generation/`
- `resources/integracoes/higgsfield-pipeline.md`

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-video-generation-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-video-generation · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `design-lab-motion-frames` (motion design)
- `cco-art-director`
- `cmo-growth-performance` (video testing)

### ⬇️ Downstream
- Higgsfield MCP (premium gen)

### ✅ QA pair
- `cco-art-director`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-video-generation · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-video-generation · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-video-generation.md`.
