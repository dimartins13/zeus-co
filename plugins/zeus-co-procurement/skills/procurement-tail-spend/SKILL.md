---
name: procurement-tail-spend
description: Tail Spend — compras pequenas (< R$ 5k) automatizadas via cards corporativos + AI. Não vale rodar RFP. Foco: velocidade + controle + compliance básica. Use pra "tail spend", "compras pequenas", "card corporativo", "expense management", "Caju", "Conta Simples", "Stark Bank cards", "indirect spend automation".
---

# Tail Spend

## Identidade
Os 80% das transações que valem 20% do spend. Não vale processo formal — vale automação.

## Princípio inviolável
**Processo pesado em tail spend = oposto do ROI.** Spend < R$ 5k: card + workflow leve + AI sugere fornecedor.

## Stack canon BR

| Tool | Função |
|---|---|
| **Caju** | Card flexível BR (VR/VA + custom limits) |
| **Conta Simples** | Cards corporativos + expense mgmt |
| **Stark Bank** | Cards + Pix + virtual cards |
| **Mercado Pago Conta PJ** | Cards + Pix |
| **Pluggy** | Open Finance integration |

## Workflow tail spend canon

```
1. Funcionário precisa comprar algo (< R$ 5k)
2. Submete request (Slack bot, Notion form, etc.)
3. AI checa: categoria + budget mensal + histórico fornecedor
4. Aprovação:
   - Auto < R$ 500 (recorrente)
   - Manager < R$ 2k
   - C-Level R$ 2-5k
5. Card virtual gerado com limite + categoria
6. Compra feita
7. Reconciliação automática via Open Finance
```

## Budget per category (mensal)

| Categoria | Budget recomendado | Owner |
|---|---|---|
| Software/SaaS | R$ X / dev | CTO |
| Travel | R$ Y / pessoa | CHRO |
| Office supplies | R$ Z / pessoa | Facilities |
| Marketing tools | R$ W / mkt | CMO |

## Trabalha em equipe com
- **⬆️** procurement (chief)
- **🤝** cfo-ap-specialist (reconciliação), cfo-treasury (card limits)
- **⬇️** funcionários (consumo)
- **✅** cfo-controller (compliance)


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
- YYYY-MM-DD · procurement-tail-spend · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · procurement-tail-spend · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · procurement-tail-spend · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
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

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-procurement-tail-spend.md` no mesmo formato consolidado.

