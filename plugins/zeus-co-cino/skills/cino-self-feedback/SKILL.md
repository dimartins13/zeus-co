---
name: cino-self-feedback
description: Camada 2 do Sistema Vivo — Audit semanal das skills do CINO (Innovation). Lê todos os `_Pulse/skill-feedback/cino*-YYYY-MM-DD.md` da semana, identifica padrões de gap/sucesso, e gera relatório em `_Improvements/cino-RADAR-YYYY-WW.md`. Use SEMPRE pra "auditar CINO", "feedback Innovation", "evolução CINO", "como está o Innovation", "melhorar CINO", "saúde do Innovation", "skill health CINO". Invocação típica: semanal (cron sexta) OU manual sob demanda.
---

# CINO Self-Feedback — Camada 2 do Sistema Vivo

## Identidade
Audit reflexivo das skills do CINO (Innovation). Não opero — observo e relato.

## Princípio inviolável
**Eu não invento melhorias. Eu detecto padrões nos dados que as próprias skills geraram.** Se 5 sessões registraram "gap=output canônico não tem item X", isso é signal — não opinião.

## Input (de onde leio)
1. **Skill feedback files** (Camada 1):
   ```
   ~/Documents/Claude/Projects/_Pulse/skill-feedback/cino-*.md
   ~/Documents/Claude/Projects/_Pulse/skill-feedback/cino-*-*.md   # specialists
   ```
2. **LEARNINGS.md de cada empresa** com refs a esta família de skills
3. **Audit logs** do Cowork (quando disponíveis)

## Processo (5 passos)

### 1. Agregação
- Lista todas as invocações da família `cino*` na semana
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

### 4. Output: `_Improvements/cino-RADAR-YYYY-WW.md`
Estrutura:
```markdown
# RADAR CINO — Semana YYYY-WW

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

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/cino-self-feedback-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · cino-self-feedback · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[portfolio]
```

## Trabalha em equipe com

### ⬆️ Upstream
  - cron `labs-weekly` (sexta 02:00)
  - Diego (sob demanda)

### 🤝 Peers
  - Outros `<lep>-self-feedback` skills (consolida via labs)

### ⬇️ Downstream
  - `zeus-co-labs:labs-orquestrador` (agregador global)
  - `_Improvements/cino-RADAR-YYYY-WW.md` (output)

### ✅ QA pair
  - `zeus-co-labs:skill-effectiveness-analyst`
  - Diego (review do RADAR)

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra avaliar a família CINO em qualquer escopo. Como opera sobre logs agregados, lê arquivos de TODAS as empresas (não de uma só).

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md (portfolio global, em `~/Documents/Claude/Projects/LEARNINGS.md`)
- YYYY-MM-DD · cino-self-feedback · [lição] · [por que importa]

### 2. BACKLOG.md (portfolio global)
- [P0|P1|P2] · [ação derivada do RADAR] · Owner

### 3. _LEDGER.md (portfolio global)
- YYYY-MM-DD HH:MM · cino-self-feedback · audit-weekly · ~N turnos · `_Improvements/cino-RADAR-YYYY-WW.md`

### 4. _Inbox.md (opcional)
Findings 🔴 Type 1 sempre viram entry em _Inbox global pra Diego ver.

**Fallback:** `_SessionRecaps/YYYY-MM-DD-cino-feedback.md`.
