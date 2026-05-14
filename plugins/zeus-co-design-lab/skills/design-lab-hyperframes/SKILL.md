---
name: design-lab-hyperframes
description: HyperFrames — embed live HTML interativo dentro de canvas/templates de design. Pattern do Open Design v0.7 (HTML-in-Canvas end-to-end rendering). Use pra prototipagem interativa sem 'imagine que é clickável' — elementos HTML funcionam de verdade dentro do frame de design. Bridge entre design estático e produto navegável. Frases-gatilho: 'hyperframes', 'HTML in canvas', 'protótipo interativo', 'design clickável', 'mock funcional', 'embed HTML em frame'.
---

# HyperFrames — HTML interativo em canvas de design

## Princípio
**Designer não deveria dizer "imagine que isso é clickável".** HyperFrames = HTML real embarcado em template de design. Conversão "mockup → protótipo funcional" sem trocar de ferramenta.

## Origem
Pattern do upstream `nexu-io/open-design` v0.7.0 (release 13-mai-2026, PR #866). Em fase de desenvolvimento ativo, ainda não maduro. Nossa implementação é **adapter conceitual** — não importamos runtime deles (depende do daemon Express + SQLite).

## Quando uso
- Apresentar protótipo de LP/app pro stakeholder que precisa **interagir**, não só ver
- Test de hypothesis UX antes de codar feature
- Design review onde botões precisam realmente clicar
- Demo cliente B2B com elementos funcionais (form input, hover states, scroll)
- Pitch deck com mini-demo embarcado (replace static screenshot)

## Output canônico

1. **Frame estrutural** (canvas-style template do skill destino — LP, deck, magazine)
2. **HTML embarcado** em região específica do frame:
   - Form fields (interativos, validáveis)
   - Buttons (com hover + click feedback)
   - Scroll containers (overflow real)
   - Mini iframes (preview de outra page)
3. **Comportamento** definido (onClick → ação fake, onSubmit → state local)
4. **Export modes**:
   - **HTML standalone** (.html — funciona em qualquer browser)
   - **Embed em deck** (slide com iframe interno)
   - **Asset estático** (fallback PNG do estado inicial)

## Como funciona tecnicamente (Cowork)

### Modo A — Cowork desktop com web-artifacts-builder
```
1. Skill design-lab-hyperframes orquestra
2. Define wireframe estrutural do canvas (frame)
3. Identifica "regiões interativas" (HTML zones)
4. Invoca anthropic-skills:web-artifacts-builder pra gerar HTML real
5. Composita: canvas frame + HTML zones embarcadas
6. Output: single .html standalone, executa em browser
```

### Modo B — Sem web-artifacts-builder
```
Fallback: gera HTML simples sem framework (vanilla JS + CSS)
Limitações: sem React/shadcn, sem state complexo
```

### Modo C — Cowork Scheduled (autônomo)
```
N/A pra HyperFrames — depende de output visual + interação humana
```

## Patterns canônicos (4 use cases)

### Pattern 1 — LP com hero clickável
- Frame: full-width hero section (1920x1080 canvas)
- HTML embed: CTA button real + email signup form + scroll indicator
- Output: hero standalone .html, dropável em qualquer LP final

### Pattern 2 — Deck com mini-demo
- Frame: slide 16:9
- HTML embed: pequeno protótipo de produto (3-5 telas, navegáveis)
- Output: slide HTML com iframe interno, exporta como standalone OR insere em PPT/Gamma deck

### Pattern 3 — App screen interativo
- Frame: mobile mockup (375x812 iPhone)
- HTML embed: tela do app real, com botões clicáveis
- Output: .html standalone responsive

### Pattern 4 — Form review pré-build
- Frame: editorial 1200x800
- HTML embed: form completo (5-10 fields, validação local)
- Output: .html testável, valida UX antes de eng codar

## Limitações honestas

- **Não substitui Figma + dev handoff** — é prototipagem rápida, não design system
- **HTML interno é vanilla ou React simples** — sem backend, sem auth real
- **Estado é local (in-memory)** — refresh perde
- **Não exporta pra PPT preservando interatividade** — só HTML standalone preserva HTML
- **Limite ~200KB HTML por frame** (perde performance em frames grandes)

## Channel Skill — não-LEP

Skill ativa (gera HTML real via `anthropic-skills:web-artifacts-builder`), não passiva.

## Critique Gate (auto-QA antes de retornar — 5 dimensões)

**Antes de devolver output pro Diego**, rodar mental critique nas 5 dimensões (Open Design pattern):

| Dim | Pergunta | Pass se... |
|---|---|---|
| **1. Philosophy** | Output reflete a direção visual escolhida (1 das 5)? | Paleta OKLch + type stack + spacing batem |
| **2. Hierarchy** | A leitura é clara em 3s a 1m de distância? | F-pattern / Z-pattern respected. 1 foco. |
| **3. Execution** | Detalhes técnicos corretos? | Sem typos, sem layout broken, HTML válido, sem console errors |
| **4. Specificity** | Output é específico ao brief (não genérico)? | Nomes/dados reais da empresa, não placeholders |
| **5. Restraint** | Nada supérfluo? Se removo, falta? | < 5 elementos competindo por atenção |

**Decisão**:
- **5/5 pass** → entrega
- **4/5 pass** → entrega com flag explícito do gap
- **≤ 3/5 pass** → refina antes (não entrega rascunho ruim)

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-hyperframes-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-hyperframes · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web
Printa no chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · ...`

### Modo C — Autônomo
N/A — HyperFrames depende de output visual + revisão humana.

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`
- `design-lab-landing-page` (quando hero precisa interatividade)
- `design-lab-deck` (quando slide quer mini-demo)

### 🤝 Peers
- `anthropic-skills:web-artifacts-builder` (motor HTML real)
- `cto-ux-ui` (review UX antes de prototyping)
- `cco-art-director` (validar direção visual do frame)

### ⬇️ Downstream
- Output `.html` standalone → pasta `_Areas/CCO/prototipos/<empresa>/YYYY-MM-DD-<descricao>.html`
- Eventualmente vira input pra `cto-pm` codar feature real

### ✅ QA pair
- `cco-brand-guardian` (consistência visual)
- `cto-ux-ui` (HTML válido + a11y básica)

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-hyperframes · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação follow-up] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-hyperframes · prototipo-criado · ~N turnos · `_Areas/CCO/prototipos/...`

### 4. _Inbox.md (opcional)
Se HyperFrame revelou gap real de UX → SUGESTÃO codar feature.

**Fallback:** `_SessionRecaps/YYYY-MM-DD-hyperframes.md`.

## Roadmap futuro (do upstream Open Design)

O Open Design v0.7 introduziu HyperFrames mas ainda está evoluindo. Features que monitorar:
- **HyperFrames v2** (planejado): state management cross-frame
- **Multi-frame composition**: vários HyperFrames numa só prototype
- **Export pra Figma/Sketch**: bridge com tooling tradicional

Refresh trimestral via `zeus-co-labs:labs-orquestrador` revisa se vale puxar features novas.
