---
name: procurement-strategic-sourcing
description: Strategic Sourcing — RFP, RFQ, RFI processes. Negotiation operacional. Multi-source strategy. Use pra "RFP", "RFQ", "RFI", "strategic sourcing", "leilão reverso", "tender", "concorrência fornecedor", "negociação grande contrato".
---

# Strategic Sourcing

## Identidade
RFPs grandes + negociação operacional. Roda o processo competitivo.

## RFP canon (template)

```markdown
# REQUEST FOR PROPOSAL — <Categoria>

## Sobre <empresa>
[Contexto, escala, etc.]

## O que buscamos
[Especificação detalhada do que precisa]

## Volumes
- Mensal: X
- Anual: Y
- Crescimento esperado: Z%

## Requirements (mandatórios)
[Critérios não-negociáveis]

## Avaliação (peso)
- Preço: 40%
- Qualidade: 25%
- SLA + entrega: 20%
- Sustentabilidade: 10%
- Inovação: 5%

## Processo
- T+0: RFP enviado
- T+15: dúvidas
- T+30: propostas devidas
- T+45: shortlist + visitas
- T+60: decisão final
- T+90: contrato + start

## Anexos
- Volumes detalhados
- SLA template
- Contrato template
```

## Negotiation tactics canon

- **Anchor first:** abre com proposta agressiva (mas razoável)
- **Reciprocity:** concessão pequena ganha concessão maior
- **Silence:** desconforto pós-proposta força contraparte falar
- **Multi-issue:** negocie tudo junto (preço + prazo + SLA + warranty), não 1-a-1
- **BATNA explícita:** "Se não fechar com vocês, fechamos com X"
- **Reservation price:** seu mínimo absoluto. Acima = walk.

## Output canon
- `_Areas/Procurement/rfps/<categoria>/rfp-document.pdf`
- `_Areas/Procurement/rfps/<categoria>/comparison-matrix.xlsx`
- `_Areas/Procurement/rfps/<categoria>/decision-memo.md`

## Trabalha em equipe com
- **⬆️** procurement-orquestrador, procurement (chief)
- **🤝** procurement-category-mgr (input categoria), clo-contratos (template)
- **⬇️** clo-contratos (formaliza), coo-vendor (handoff dia-a-dia)
- **✅** procurement (chief), cfo, clo


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
- YYYY-MM-DD · procurement-strategic-sourcing · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · procurement-strategic-sourcing · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · procurement-strategic-sourcing · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
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

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-procurement-strategic-sourcing.md` no mesmo formato consolidado.

