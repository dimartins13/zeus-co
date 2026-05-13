---
name: cino-orquestrador
description: Orquestrador do CINO Office. Executa pipeline 7 fases (strategy → research → tech scouting → experimentation → open innov → stage-gate → handoff). Use pra "operar inovação completa", "pipeline CINO", "ciclo inovação".
---

# CINO Orquestrador

## Pipeline (7 fases)
Ver [`docs/PIPELINE.md`](../../docs/PIPELINE.md).

## Modos
- **Setup inovação empresa:** Fase 1-2
- **Ciclo experimento:** Fase 4-6 (cada experimento full cycle)
- **Tech radar refresh:** Fase 3 mensal
- **Hackathon:** Fase 5

## Trabalha em equipe com
- **⬆️** cino (chief), Diego
- **🤝** cerebro-criativo, scout, cto, ceo
- **⬇️** research, experimentation, tech-scouting, open-innovation
- **✅** cino, cfo


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

Antes de encerrar QUALQUER sessão deste LEP, escrever nessa ordem. Sem isso, sessão não fechou.

### 1. LEARNINGS.md (empresa atual)
Append 1-3 lições durables. Formato:
```
- YYYY-MM-DD · cino-orquestrador · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · cino-orquestrador · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · cino-orquestrador · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
```

### 4. _Inbox.md (opcional — quando vale)
Se nasceu sugestão proativa que Diego não pediu mas merece atenção dele, append bloco:
```
## [SUGESTÃO] [título curto] · YYYY-MM-DD
- **O quê:** 1 linha
- **Por quê (gatilho):** 1 linha
- **Próximo passo:** 1 linha
- **Status:** [aguarda Diego]
```

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-cino-orquestrador.md` no mesmo formato consolidado.

