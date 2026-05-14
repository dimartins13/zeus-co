---
name: design-lab-design-system
description: Design system tools — criar/auditar DS próprio + referência aos 66 design systems curados (Apple, Stripe, Linear, Notion, Anthropic, Vercel, Figma, etc). Use pra 'criar design system', 'auditar DS', 'tokens design', 'paleta OKLch', 'type system', 'spacing scale', 'componentes', 'referência Apple/Stripe/etc'.
---

# Design Lab Design System

## Princípio
DS = tokens + componentes + guidelines. Sem tokens, é coleção. Sem componentes, é palette. Sem guidelines, é arquivo morto.

## Quando uso
- DS novo de empresa
- Audit de DS existente
- Refresh de tokens (paleta, tipografia)
- Componente novo
- Cross-reference com Apple/Stripe/etc

## Output canônico
1. Tokens (cores OKLch, type scale, spacing, radii, shadows)
2. Componentes core (button, input, card, modal, nav)
3. Guidelines (do's/don'ts, exemplos certos/errados)
4. Referência de inspiração (1+ dos 66 DSes em `resources/design-systems/`)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/design-system-tools/`
- `resources/design-systems/` (66 DSes referência: genéricos + tech-platforms + marcas)
- `resources/design-systems/_schema/` (formato canônico)

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
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-design-system-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-design-system · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`, `cco-orquestrador`

### 🤝 Peers
- `cmo-branding` (brand guidelines macro)
- `cco-art-director`
- `cto-ux-ui` (DS técnico)

### ⬇️ Downstream
- Figma MCP (export tokens)
- Storybook (se aplicável)

### ✅ QA pair
- `cco-brand-guardian`, `cto-ux-ui`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-design-system · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-design-system · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-design-system.md`.
