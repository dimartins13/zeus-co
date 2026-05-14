---
name: design-lab-deck
description: Decks e apresentações — pitch deck, magazine deck, board pack visual, sales deck. Agrupa 5 skills detalhadas do upstream (guizang-ppt, magazine layouts, html-ppt, etc) + integração Gamma MCP + design systems Apple/Stripe/Linear como referência visual. Use SEMPRE pra 'deck', 'apresentação', 'slides', 'pitch deck', 'board pack', 'magazine deck', 'PPTX'.
---

# Design Lab Deck

## Princípio
Deck = narrativa em slides. Estrutura > beleza. Beleza vem da consistência visual aplicada com taste (não decoração).

## Quando uso
- Pitch fundraising / sales
- Board pack mensal/trimestral
- Magazine editorial-style
- All-hands
- Conference talk

## Output canônico
1. Outline de slides (5-15 max em pitch; 10-30 em board pack)
2. Direção visual escolhida + design system referência
3. Slides gerados (HTML/PPTX/Gamma)
4. Speaker notes (se aplicável)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/deck-slides/` (5 skills: guizang-ppt, html-ppt, magazine, etc)
- `resources/integracoes/gamma-pipeline.md`
- `resources/design-systems/` (Apple/Stripe/Linear referência)

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-deck-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-deck · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`, `cco-storytelling`

### 🤝 Peers
- `cco-copy-master` (copy de slide)
- `cmo-product-marketing` (messaging)
- `board-pack-builder` (pra board decks)
- `ceo-fundraising` (pra fundraising decks)

### ⬇️ Downstream
- Gamma MCP (export)
- `pptx` skill (Anthropic native, export PPTX)

### ✅ QA pair
- `cco-brand-guardian`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-deck · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-deck · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-deck.md`.
