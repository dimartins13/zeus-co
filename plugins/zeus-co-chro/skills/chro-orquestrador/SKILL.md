---
name: chro-orquestrador
description: Orquestrador do CHRO Office. Executa pipeline 9 fases (org design → recruiting → onboarding → comp → performance → L&D → culture → off-boarding → reporting). Use pra "operar people completo", "pipeline CHRO", "ritmo people".
---

# CHRO Orquestrador

## Pipeline (9 fases)
Ver [`docs/PIPELINE.md`](../../docs/PIPELINE.md).

## Modos
- **Setup People empresa:** Fases 1-3-4
- **Ciclo anual:** Fase 5 (performance) + Fase 4 review (comp)
- **Hire específico:** Fase 2 + Fase 3
- **Demissão:** Fase 8

## Trabalha em equipe com
- **⬆️** ceo-orquestrador, chro
- **🤝** clo-trabalhista, cfo, board:equity-vesting-manager
- **⬇️** chro-recruiting, chro-people-ops, chro-learning-development, chro-culture
- **✅** chro


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
- YYYY-MM-DD · chro-orquestrador · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · chro-orquestrador · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · chro-orquestrador · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
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

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-chro-orquestrador.md` no mesmo formato consolidado.

