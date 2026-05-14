---
name: clo-self-feedback
description: Camada 2 do Sistema Vivo — Audit semanal das skills do CLO (Legal). Lê todos os `_Pulse/skill-feedback/clo*-YYYY-MM-DD.md` da semana, identifica padrões de gap/sucesso, e gera relatório em `_Improvements/clo-RADAR-YYYY-WW.md`. Use SEMPRE pra "auditar CLO", "feedback Legal", "evolução CLO", "como está o Legal", "melhorar CLO", "saúde do Legal", "skill health CLO". Invocação típica: semanal (cron sexta) OU manual sob demanda.
---

# CLO Self-Feedback — Camada 2 do Sistema Vivo

## Identidade
Audit reflexivo das skills do CLO (Legal). Não opero — observo e relato.

## Princípio inviolável
**Eu não invento melhorias. Eu detecto padrões nos dados que as próprias skills geraram.** Se 5 sessões registraram "gap=output canônico não tem item X", isso é signal — não opinião.

## Input (de onde leio)
1. **Skill feedback files** (Camada 1):
   ```
   ~/Documents/Claude/Projects/_Pulse/skill-feedback/clo-*.md
   ~/Documents/Claude/Projects/_Pulse/skill-feedback/clo-*-*.md   # specialists
   ```
2. **LEARNINGS.md de cada empresa** com refs a esta família de skills
3. **Audit logs** do Cowork (quando disponíveis)

## Processo (5 passos)

### 1. Agregação
- Lista todas as invocações da família `clo*` na semana
- Conta por skill: # invocações × média de sucesso × gaps únicos

### 2. Detecção de padrões
Padrões que importam:
- **Skill com sucesso médio < 3.5** → falha recorrente
- **Mesmo gap em 3+ sessões** → bug estrutural na skill
- **Skill nunca invocada** → triggering fraco ou skill irrelevante
- **Gap "sugestão" recorrente** → evolução natural pedida

### 3. Tier de prioridade
Cada finding vira recomendação com tier:
- 🟢 **Auto-aplicar** (cosmético, refrasear description, normalizar metadata)
- 🟡 **Aprovar Diego** (mudar output canônico, adicionar specialist, refactor)
- 🔴 **Decisão Type 1** (deprecar skill, mudar arquitetura)

### 4. Output: `_Improvements/clo-RADAR-YYYY-WW.md`
Estrutura:
```markdown
# RADAR CLO — Semana YYYY-WW

## Stats agregadas
- Invocações total: N
- Sucesso médio: X.X / 5
- Skills com falha (<3.5): [list]
- Skills nunca invocadas: [list]

## Findings
### 🟢 Auto-aplicáveis (N)
- [skill] · [problema] · [proposta]

### 🟡 Aprovação Diego (N)
- [skill] · [problema] · [proposta] · [impacto estimado]

### 🔴 Type 1 (N)
- [skill] · [problema] · [memo necessária]
```

### 5. Loop pro labs-orquestrador
Output enviado pra `labs-orquestrador` consolidar com outros LEPs em RADAR_EVOLUCAO_WEEKLY global.

## Quando NÃO operar
- Não tem feedback file da semana → reporta "sem dados, aguardando primeira semana"
- < 3 invocações na semana → estatisticamente irrelevante, não tira conclusão
- Skill recém-criada (< 14 dias) → dar tempo de tração antes de avaliar

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

Sistema vivo opera em **3 ambientes** distintos. Adaptar comportamento:

### Modo A — Interativo Cowork desktop (Diego presente + filesystem disponível)
Escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/clo-self-feedback-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · clo-self-feedback · ambiente=cowork-chat · sucesso=[1-5] · gap=[gap ou "nenhum"] · sugestao=[1 frase] · empresa=[<empresa>]
```

### Modo B — Interativo Claude.ai web / sem filesystem (Diego presente, sem Bash)
**Printar Self-Evaluation NO CHAT** no fim do output (Diego copia pra Project Knowledge se quiser preservar):
```
📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=... · empresa=...
```
NÃO tentar escrever filesystem (vai falhar).

### Modo C — Autônomo (cron launchd / Cowork Scheduled, sem Diego presente)
Escrever no filesystem com nota **heurística** (não tem Diego pra dar 1-5):
```
- YYYY-MM-DD HH:MM · clo-self-feedback · ambiente=[cron-launchd|scheduled-task] · sucesso=auto · gap=[detectado via heurística: missing canônico, timeout, error] · sugestao=[se aplicável] · empresa=[<empresa>]
```
Heurística pra `sucesso=auto`:
- **PASS** = output cumpriu output canônico + sem erro + dentro do tempo esperado
- **PARTIAL** = output cumpriu parcialmente OU warning
- **FAIL** = erro, timeout, output não-canônico

### Critérios de sucesso (Modo A, com Diego)
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

### Gap = oportunidade de evolução
Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

### Fluxo no labs-orquestrador
- Modo A + B + C são agregados separadamente (sample sizes diferentes)
- Modo A é fonte primária de signal (Diego feedback real)
- Modo C é fonte secundária (regression detection — skill quebrou em produção?)
- Modo B é capturado por copy-paste manual do Diego pra Project Knowledge

## Trabalha em equipe com

### ⬆️ Upstream
  - cron `labs-weekly` (sexta 02:00)
  - Diego (sob demanda)

### 🤝 Peers
  - Outros `<lep>-self-feedback` skills (consolida via labs)

### ⬇️ Downstream
  - `zeus-co-labs:labs-orquestrador` (agregador global)
  - `_Improvements/clo-RADAR-YYYY-WW.md` (output)

### ✅ QA pair
  - `zeus-co-labs:skill-effectiveness-analyst`
  - Diego (review do RADAR)

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra avaliar a família CLO em qualquer escopo. Como opera sobre logs agregados, lê arquivos de TODAS as empresas (não de uma só).

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md (portfolio global, em `~/Documents/Claude/Projects/LEARNINGS.md`)
- YYYY-MM-DD · clo-self-feedback · [lição] · [por que importa]

### 2. BACKLOG.md (portfolio global)
- [P0|P1|P2] · [ação derivada do RADAR] · Owner

### 3. _LEDGER.md (portfolio global)
- YYYY-MM-DD HH:MM · clo-self-feedback · audit-weekly · ~N turnos · `_Improvements/clo-RADAR-YYYY-WW.md`

### 4. _Inbox.md (opcional)
Findings 🔴 Type 1 sempre viram entry em _Inbox global pra Diego ver.

**Fallback:** `_SessionRecaps/YYYY-MM-DD-clo-feedback.md`.
