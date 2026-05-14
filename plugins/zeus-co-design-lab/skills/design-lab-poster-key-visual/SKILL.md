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
