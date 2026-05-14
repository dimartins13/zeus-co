---
name: design-lab-image-generation
description: Geração de imagens via AI — Freepik Mystic, Adobe Firefly, Higgsfield. Agrupa 6 skills detalhadas (image-generation) + 4 pipelines de integração. Use pra 'gerar imagem AI', 'Freepik', 'Higgsfield', 'Firefly', 'Mystic', 'imagem stock AI', 'render produto AI', 'hero image AI'.
---

# Design Lab Image Generation

## Princípio
AI generative = direção humana + iteração. Sem brief preciso, sai genérico. Sem iteração, sai medíocre.

## Quando uso
- Hero image LP/email/deck
- Produto rendering (D2C apparel)
- Mood reference pra campanha
- Asset stock impossível de achar no Freepik library

## Output canônico
1. Prompt estruturado (subject + style + composition + lighting + post-process)
2. Direção visual ancorada (1 das 5 + design system referência)
3. 4-9 variants iniciais
4. Iteração refinement (upscale, edit, expand)
5. Asset final em formatos canônicos

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/image-generation/`
- `resources/integracoes/freepik-pipeline.md`
- `resources/integracoes/higgsfield-pipeline.md`
- `resources/integracoes/adobe-express-pipeline.md`

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
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-image-generation-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-image-generation · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
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
- `cmo-growth-performance` (creative testing em escala)

### ⬇️ Downstream
- Freepik MCP (search + Mystic gen)
- Higgsfield (premium gen)
- Adobe Express MCP (refine)

### ✅ QA pair
- `cco-art-director`, `cco-brand-guardian`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-image-generation · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-image-generation · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-image-generation.md`.
