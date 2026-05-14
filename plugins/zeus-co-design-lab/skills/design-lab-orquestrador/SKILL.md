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
- `resources/padroes-core/04-discovery-form.md`
- `resources/skills-detalhadas/` (51 skills upstream pra consulta profunda)

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
