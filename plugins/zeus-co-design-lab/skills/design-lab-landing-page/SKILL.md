---
name: design-lab-landing-page
description: Landing pages e web artifacts — LP D2C, LP SaaS, hero section, pricing page, feature page. Agrupa 3 skills detalhadas (web-artifacts) + design systems modernos (Vercel/Stripe/Linear) + AI generative pra hero image. Use pra 'landing page', 'LP', 'home page', 'hero', 'pricing page', 'feature page', 'site novo'.
---

# Design Lab Landing Page

## Princípio
LP = conversão + tom de marca. Hero → social proof → benefits → CTA. Cada seção tem 1 objetivo, não 3.

## Quando uso
- LP nova de produto / feature
- Redesign de home existente
- LP de drop específico (D2C)
- Pricing page

## Output canônico
1. Wireframe estrutural (seções + flow)
2. Copy por seção (hero, benefits, social proof, CTA)
3. Visual direction (paleta OKLch + tipografia)
4. Hero asset (gerado via Freepik/Higgsfield ou referência)
5. HTML/React output (via web-artifacts-builder)

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/web-artifacts/`
- `resources/integracoes/freepik-pipeline.md` (hero image)
- `resources/design-systems/tech-platforms/` (Vercel, Stripe, Linear)

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
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-landing-page-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-landing-page · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `cmo-growth-performance` (CRO, conversão)
- `cmo-product-marketing` (positioning + messaging)
- `cco-copy-master` (copy)
- `cto-ux-ui` (UX)

### ⬇️ Downstream
- `anthropic-skills:web-artifacts-builder` (output React)
- Freepik/Higgsfield (hero asset)

### ✅ QA pair
- `cco-brand-guardian`, `cmo-growth-performance`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-landing-page · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-landing-page · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-landing-page.md`.
