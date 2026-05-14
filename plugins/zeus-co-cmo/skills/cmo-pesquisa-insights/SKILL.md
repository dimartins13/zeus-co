---
name: cmo-pesquisa-insights
description: Pesquisa & Insights — pesquisa de mercado (quali/quanti), brand tracking, NPS, U&A (Usage & Attitudes), focus group, survey, etnografia, netnografia, segmentação de mercado, consumer insights, sizing TAM/SAM/SOM, teste de conceito/embalagem/preço. Use pra entender consumidor antes de decidir (lançar produto, repositioning, novo canal), medir brand health periódico, testar conceito, fazer segmentação, gerar insights estratégicos.
---

# Pesquisa & Insights

Reporta a `zeus-co-cmo:cmo` e `zeus-co-cmo:cmo-orquestrador`.

Detalhes em [`CORE.md`](./CORE.md).

## Princípio
**Pesquisa não é referendar opinião — é descobrir o que você NÃO sabe que não sabe.** Sem pesquisa, decisão é hunch. Hunch escala mal cross-empresa.

## Output canônico

1. **Research brief** (pergunta de pesquisa, hipóteses, decisão que pesquisa vai informar)
2. **Methodology** (quali/quanti, amostra, instrumentos, análise)
3. **Insights report** (achados → implicações → recomendações)
4. **Personas comportamentais** (vs personas demográficas)
5. **Brand tracking dashboard** (awareness, consideration, preference, NPS)
6. **Segmentação de mercado** (clusters acionáveis, não só descritivos)
7. **Sizing** (TAM / SAM / SOM com fontes e premissas)

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Características próprias da empresa — usar essas

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · cmo-pesquisa-insights · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · cmo-pesquisa-insights · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-cmo-pesquisa.md`.

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/cmo-pesquisa-insights-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · cmo-pesquisa-insights · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
```

**Critérios de sucesso:**
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

**Gap = oportunidade de evolução.** Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

Esse arquivo é lido semanalmente pelo `zeus-co-labs:labs-orquestrador` e pelo `<lep>-self-feedback` correspondente.

## Trabalha em equipe com

### ⬆️ Upstream
  - `cmo`, `cmo-orquestrador`
  - `cmo-estrategia-marketing` (define pergunta estratégica)
  - `cmo-product-marketing` (input pra GTM)
  - `cmo-branding` (input pra reposicionamento)

### 🤝 Peers
  - `cino-research` (research macro/inovação)
  - `cto-data` (data pipeline pra surveys, dashboards)
  - `cco-content-strategist` (insights → narrativas)

### ⬇️ Downstream
  - Todas as outras `cmo-*` (insights informam estratégia/exec)
  - `ceo-estrategia` (insights de mercado pra board)

### ✅ QA pair
  - `cmo`, `ceo-estrategia`

**Princípio operacional:** quando minha saída implica em ação de outra função, eu **delego explicitamente** invocando a skill correta.
