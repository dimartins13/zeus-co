---
name: design-lab-orquestrador
description: Porta de entrada do DESIGN-LAB. Recebe brief de produção visual, roda Fase 0 (Descoberta Interna), aplica discovery form, escolhe direção visual, dispara skill correta + integra com Freepik/Higgsfield/Adobe Express/Gamma quando necessário. Use SEMPRE pra 'design-lab', 'produção visual', 'criar peça', 'design completo', 'pipeline visual', 'do brief ao entregável'. Despacha pras 11 skills verticais (deck, LP, magazine, email, social, KV, motion, image, video, prototype, design-system).
---

# Design Lab Orquestrador

## Princípio
Brief vira entregável visual em 4 fases: Detect (entender brief + empresa) → Discover (questionário 7 perguntas + design system de referência) → Direct (escolher direção visual: Editorial Monocle/Modern Minimal/Warm Soft/Tech Utility/Brutalist) → Deliver (skill vertical + integração externa).

## Quando uso
- Brief novo de produção visual sem skill específica clara
- Multi-formato (deck + LP + KV juntos)
- Quando precisa de discovery antes de produzir
- Curadoria de design system de referência

## Output canônico
1. Brief estruturado (4 Ws + tom + restrições)
2. Direção visual escolhida (1 das 5 + paleta OKLch)
3. Skill vertical disparada com contexto carregado
4. Pipeline de integração ativado se aplicável (Freepik/Higgsfield/Adobe/Gamma)

## Resources (orquestrador puxa on-demand)
- `resources/padroes-core/05-loop-detect-discover-direct-deliver.md`
- `resources/padroes-core/03-directions-visuais.md` (5 direções com OKLch)
- `resources/padroes-core/directions-quick-ref.md` ← **NOVO v0.2** quick lookup brief→direção
- `resources/padroes-core/04-discovery-form.md`
- `resources/skills-detalhadas/INDEX.md` ← **NOVO v0.2** mapping skill plana → detalhadas
- `resources/design-systems/INDEX.md` ← **NOVO v0.2** lookup brief→DS
- `resources/skills-detalhadas/` (51 skills upstream pra consulta profunda)
- `resources/integracoes/*.md` (4 pipelines executáveis — Freepik/Higgsfield/Adobe/Gamma)

## Features v0.7 do Open Design (upstream)

Open Design v0.7 (13-mai-2026) introduziu 3 features importantes. Nosso plugin tem **paridade parcial** e roadmap pra alcançar:

### 1. HyperFrames (HTML-in-Canvas)
**Status**: ✅ implementado como `design-lab-hyperframes` skill (v0.2).
**Diferença**: upstream usa daemon Express; nosso usa `anthropic-skills:web-artifacts-builder` (Cowork nativo).

### 2. Critique Theater Phase 7 (state machine + replay)
**Status**: 🟡 paridade parcial via **Critique Gate** (5-dim auto-QA) que cada skill geradora roda antes de retornar.
**Falta vs upstream**: state machine + replay capabilities (refresh-safe). Nosso é stateless: roda critique uma vez por output. Sem replay loop server-side.
**Decisão**: aceitar gap por enquanto. Diego não tem N horas de refinement em loop — Cowork chat já permite ele refinar manualmente quando 4/5. Revisar quando upstream estabilizar Phase 8+.

### 3. Auto-Memory Store cross-runs
**Status**: ✅ paridade total via **Sistema Vivo Zeus-CO** já em produção:
- Memórias persistentes em `~/.claude/projects/-Users-diegomartins-Documents-Claude-Projects/memory/`
- LEARNINGS.md por empresa (chat-protocol-aware via SKILL Fim de sessão)
- Self-Evaluation Camada 1 → labs-orquestrador semanal Camada 3
- Brand guidelines + decision criteria persistem em `_Areas/CCO/`, `_Areas/CEO/`

Nossa implementação **supera o upstream** porque:
- Vive separado por empresa (não global)
- Aprende cross-empresa via labs-orquestrador
- Tem tier 🟢🟡🔴 auto-aplicação

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-orquestrador-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-orquestrador · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `zeus` (gateway global)
- `cmo-orquestrador` (campanhas integradas)
- `cco-orquestrador` (criação macro)
- Diego direto

### 🤝 Peers
- `cmo-product-marketing` (positioning)
- `cco-art-director` (direção visual)
- `cmo-branding` (brand consistency)
- `cerebro-criativo` (big idea)

### ⬇️ Downstream
- 11 skills verticais internas (deck/LP/magazine/email/social/KV/motion/image/video/prototype/DS)
- Pipelines externos (Freepik, Higgsfield, Adobe Express, Gamma)
- `cco-copy-master` quando precisa de copy refinado

### ✅ QA pair
- `cco-brand-guardian` (consistência marca)
- `cmo` (fit estratégico)

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-orquestrador · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-orquestrador · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-orquestrador.md`.
