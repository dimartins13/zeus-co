---
name: design-lab-poster-key-visual
description: KVs publicitários — key visual de campanha, poster, OOH, billboard, peça estática. Agrupa creative-direction skills + image generation. Use pra 'KV', 'key visual', 'poster', 'OOH', 'billboard', 'peça publicitária', 'campanha estática'.
---

# Design Lab Poster Key Visual

## Princípio
KV = 1 imagem icônica + headline-killer + brand mark. Lê em 3 segundos a 50 metros. Senão, não é KV.

## Quando uso
- Campanha 360 (KV principal)
- Drop específico
- Sazonal (Black Friday, drops temáticos)
- OOH/billboard

## Output canônico
1. Concept statement (1 frase, ideia central)
2. Visual reference (mood board) + direção (das 5 do padrão)
3. KV asset (Freepik composto OU Higgsfield gerado)
4. Headline-killer (3-5 variants pra teste)
5. Adapt formats (story 9:16, post 1:1, OOH 3:1, billboard 9:1)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/creative-direction/`
- `resources/skills-detalhadas/image-generation/`
- `resources/integracoes/freepik-pipeline.md`
- `resources/integracoes/higgsfield-pipeline.md`

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-poster-key-visual-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-poster-key-visual · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `cco-art-director`
- `cerebro-criativo` (big idea)
- `cco-copy-master` (headline)

### ⬇️ Downstream
- Freepik / Higgsfield / Adobe Express MCP

### ✅ QA pair
- `cco-brand-guardian`, `cco-art-director`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-poster-key-visual · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-poster-key-visual · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-poster-key-visual.md`.
