---
name: design-lab-discovery
description: Discovery form ATIVO — pergunta interativamente 7 perguntas pra entender brief novo de produção visual. Use NO INÍCIO de QUALQUER brief novo ambíguo. Adaptado do Open Design (turn-1 question form). Captura respostas via AskUserQuestion no Cowork, monta brief estruturado, escolhe direção visual + skill vertical correta, despacha. Frases-gatilho: 'discovery design', 'brief novo visual', 'questionário design', 'descobrir o que produzir', 'qual estilo', 'design-lab descoberta', 'brief de campanha', 'briefing'.
---

# Discovery — entrada interativa pra brief novo

## Princípio
**Antes de criar, perguntar.** 7 perguntas focadas extraem 80% do contexto que evita retrabalho. Pular discovery = chutar = retrabalhar.

## Quando uso (sempre que invocada)
- Brief novo sem direção clara
- Diego mudou de empresa/setor mid-sessão
- Stakeholder diferente do usual
- Sinto que "vou chutar muito" sem essas respostas

## Workflow EXECUTÁVEL — 7 perguntas em 3 turnos

### Turno 1 — Fundamentos (3 perguntas core)

Tool: `AskUserQuestion` com 3 questions:

**Q1 — Formato**
- Pergunta: "Qual o formato do entregável?"
- Opções: Deck/slides | Landing page | KV publicitário | Email HTML | Carrossel social | Magazine editorial | Motion/vídeo | Outro
- → mapeia pra skill vertical (`design-lab-deck`, `design-lab-landing-page`, etc)

**Q2 — Público**
- Pergunta: "Pra quem?"
- Opções: B2C massa | B2C nicho premium | B2B SaaS | B2B enterprise | Investidor | Board interno
- → influencia tom + direção

**Q3 — Urgência/Profundidade**
- Pergunta: "Quanto contexto pra capturar?"
- Opções: Rápido (skill direta sem mais discovery) | Médio (1-2 perguntas extras) | Profundo (turno 2 e 3 completo)

### Turno 2 — Direção (3 perguntas — só se "Médio" ou "Profundo")

Tool: `AskUserQuestion` com 3 questions:

**Q4 — Tom**
- Pergunta: "Tom da peça?"
- Opções: Sério/autoridade | Playful/casual | Editorial/sofisticado | Raw/edgy | Premium/luxuoso

**Q5 — Referência visual**
- Pergunta: "Tem referência de estilo que admira?"
- Opções: "Estilo Stripe/Linear (clean SaaS)" | "Estilo Apple (premium minimal)" | "Estilo Monocle (editorial)" | "Estilo Nike (bold consumer)" | "Sem referência clara — você decide"
- → mapeia pra 1 das 5 direções OKLch + 1 dos 66 DSes

**Q6 — Restrições brand**
- Pergunta: "Já tem brand-guide na empresa que devo respeitar?"
- Opções: Sim (vou ler `_Areas/CCO/brand-guide.md`) | Não, criar do zero | Sim mas pode flex

### Turno 3 — Detalhes (1 pergunta — só se "Profundo")

Tool: `AskUserQuestion` com 1 question:

**Q7 — Restrições + deadline**
- Pergunta: "Restrições / deadline / orçamento?"
- Opções: Sem deadline crítico | Esta semana | Hoje | Tem hard constraint que precisa saber (você descreve)

## Output canônico (após coletar respostas)

Monta brief estruturado em texto + salva em `~/Documents/Claude/Projects/<empresa>/_Areas/CCO/briefs/YYYY-MM-DD-<descricao>.md`:

```markdown
# Brief · <descricao> · <YYYY-MM-DD>

**Empresa**: <empresa>
**Formato**: <Q1>
**Público**: <Q2>
**Tom**: <Q4>
**Direção visual sugerida**: <1 das 5 direções> (baseado em Q5)
**Design system referência**: <1 DSes recomendado>
**Brand-guide existente**: <Q6 — path se aplicável>
**Deadline**: <Q7>
**Hard constraints**: <Q7 detalhe>

## Skill vertical disparada
`design-lab-<vertical>` — porque <Q1>

## Cross-skills a invocar
- <baseado em Q4 + Q5 + Q6>

## Risk flags identificados
- <ex: tom Q4 não bate com Q5 referência — perguntar Diego antes>
- <ex: brand-guide diz X mas direção sugerida diz Y — flag>
```

## Decision tree — Q5 → direção visual

| Q5 resposta | Direção | DSes match |
|---|---|---|
| "Estilo Stripe/Linear" | Modern Minimal | stripe, linear-app, vercel, anthropic, minimal |
| "Estilo Apple" | Modern Minimal (premium variant) | apple, premium, refined, elegant |
| "Estilo Monocle" | Editorial Monocle | editorial, warm-editorial, refined |
| "Estilo Nike (bold)" | Brutalist | bold, neobrutalism, nike |
| "Sem referência" | discovery sugere baseado em Q2+Q4 | depende |

## Decision tree — Q1 → skill vertical

| Q1 resposta | Skill |
|---|---|
| Deck/slides | `design-lab-deck` |
| Landing page | `design-lab-landing-page` |
| KV publicitário | `design-lab-poster-key-visual` |
| Email HTML | `design-lab-email-html` |
| Carrossel social | `design-lab-social-carousel` |
| Magazine editorial | `design-lab-magazine-editorial` |
| Motion/vídeo | `design-lab-motion-frames` OR `design-lab-video-generation` |
| Outro | `design-lab-orquestrador` decide |

## Critical decisões pré-discovery (não pulam)

1. **Empresa atual** identificada via working dir / contexto
2. **Fase 0 já rodou**: `CLAUDE.md` + `_Areas/CCO/brand-guide.md` + `LEARNINGS.md` da empresa lidos antes de Q1
3. **Sample sessions anteriores**: se já tem briefs no `_Areas/CCO/briefs/` similar, mencionar pra Diego

## Quando NÃO usar discovery (skip pra skill direta)

- Diego já mandou brief completo em texto (extrai dali, não pergunta de novo)
- Repetição de skill recente (ex: 3º deck mensal board pack — pattern conhecido)
- Brief "rápido" (Q3 = "rápido") — passa direto pra skill vertical com sumário curto

## Channel Skill — não-LEP

Esta é uma **skill ativa**, não passiva. Usa Tool calls (`AskUserQuestion`, `Write`) — não só descreve workflow.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-discovery-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-discovery · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web (Diego presente, sem fs)
Printa no chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · ...`

### Modo C — Autônomo
N/A — discovery é interativo, não roda autônomo.

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador` (despacha aqui quando brief ambíguo)

### 🤝 Peers
- `cmo-pesquisa-insights` (research deeper se preciso)
- `prototipagem/design-brief` skill upstream (formulário canônico em `resources/skills-detalhadas/prototipagem/design-brief/`)

### ⬇️ Downstream
- 11 skills verticais (deck, LP, KV, etc) com brief estruturado
- `_Areas/CCO/briefs/<arquivo>.md` da empresa (output salvo)

### ✅ QA pair
- `design-lab-orquestrador` (valida fit antes de despachar)

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-discovery · [padrão de brief detectado] · [importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [follow-up se discovery flagou risco] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-discovery · brief-captured · ~3-5 turnos · `_Areas/CCO/briefs/...`

### 4. _Inbox.md (opcional)
Se gap encontrado (ex: brand-guide inexistente) → SUGESTÃO criar.

**Fallback:** `_SessionRecaps/YYYY-MM-DD-discovery.md`.
