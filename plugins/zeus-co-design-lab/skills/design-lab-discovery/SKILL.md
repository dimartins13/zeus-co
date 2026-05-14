---
name: design-lab-discovery
description: Discovery form — questionário canônico de 7 perguntas pra entender brief novo de produção visual antes de criar. Adaptado do Open Design (turn-1 question form). Use no início de QUALQUER brief novo que tem ambiguidade — substitui chutar direção. Frases-gatilho: 'discovery design', 'brief visual', 'questionário design', 'descobrir o que produzir', 'qual estilo'.
---

# Design Lab Discovery

## Princípio
Antes de criar, perguntar. 7 perguntas focadas extraem 80% do contexto que evita retrabalho.

## Quando uso
- Brief novo sem direção clara
- Cliente/Diego mudou de contexto
- Stakeholder diferente do usual

## Output canônico
1. 7 respostas estruturadas (público, propósito, tom, restrições, referências, formato, timeline)
2. Direção visual sugerida (1 das 5 das `padroes-core/03-directions-visuais.md`)
3. Skill vertical recomendada
4. Quaisquer riscos identificados (brand misalign, scope creep, asset gap)

## Resources (orquestrador puxa on-demand)
- `resources/padroes-core/04-discovery-form.md` (questionário canônico)
- `resources/padroes-core/03-directions-visuais.md` (mapping respostas → direção)

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-discovery-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-discovery · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `cmo-pesquisa-insights` (research deeper se necessário)

### ⬇️ Downstream
- Skills verticais (deck/LP/KV/etc) com contexto carregado

### ✅ QA pair
- `design-lab-orquestrador`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-discovery · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-discovery · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-discovery.md`.
