---
name: design-lab-magazine-editorial
description: Layouts editoriais — magazine spread, lookbook, brand book, manifesto, brochure. Agrupa 5 skills detalhadas (templates-editoriais) + design systems editoriais (Monocle-style, Apple Pages, Notion Public). Use pra 'magazine', 'editorial', 'lookbook', 'brand book', 'manifesto', 'brochura', 'spread editorial'.
---

# Design Lab Magazine Editorial

## Princípio
Editorial = ritmo + tipografia + hierarquia. Espaço branco é decisão de design, não falta de conteúdo.

## Quando uso
- Lookbook D2C (drop apparel/moda)
- Brand book / manual de marca
- Magazine de marca (Monocle-style)
- Manifesto / op-ed visual

## Output canônico
1. Grid editorial (12 col padrão)
2. Type pairing (heading + body + accent)
3. Spread layout (pages 2-3, 4-5, etc)
4. Asset call-out (fotos, ilustrações)
5. Output HTML/PDF

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/templates-editoriais/`
- `resources/design-systems/genericos/` (warm-editorial, monocle-style)
- `resources/padroes-core/03-directions-visuais.md` (Editorial Monocle direction)

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-magazine-editorial-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-magazine-editorial · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `cco-storytelling`
- `cco-art-director`
- `cmo-branding`

### ⬇️ Downstream
- `pdf` skill (Anthropic native)
- Adobe Express MCP (export final)

### ✅ QA pair
- `cco-brand-guardian`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-magazine-editorial · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-magazine-editorial · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-magazine-editorial.md`.
