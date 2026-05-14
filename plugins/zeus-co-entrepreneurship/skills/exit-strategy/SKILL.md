---
name: exit-strategy
description: Exit Strategy — planejamento de exit por empresa. M&A / IPO / lifestyle / kill. Timing, valuation, comprador, processo. Use pra "exit strategy", "venda empresa", "saída", "M&A timing", "IPO planning", "kill decision", "spin-off", "secondary sale", "founder secondary".
---

# Exit Strategy

## Identidade
Planejamento da SAÍDA Diego de cada empresa. Não-precisa exit agora — precisa ter PLANO.

## Princípio inviolável
**Toda empresa tem exit eventualmente — mesmo se for "Diego nunca sai".** Lifestyle é exit válido. Documentar intenção.

## Exit types canon

| Tipo | Quando aplicar | Stakes |
|---|---|---|
| **M&A (sell)** | Empresa atinge maturity / strategic buyer aparece | Cash 80-100% upfront |
| **IPO** | Empresa >>R$ 100M revenue + setor tolerante | Liquidez parcial |
| **Lifestyle / Dividend** | Empresa operando + cashflowing | Receita recorrente |
| **Secondary sale** | Diego vende quotas pra investor (sem vender empresa) | Cash parcial pro Diego |
| **Spin-off** | Pedaço da empresa vira nova empresa | Dilution + opcionalidade |
| **Wind-down** | Empresa não-funciona, fechar com honra | -tempo, +aprendizado |
| **Kill** | Empresa não-funciona, fechar fast | -tempo |

## Pra cada empresa Diego, documentar:

```markdown
# Exit Plan — <Empresa>

## Tipo preferido (current intent)
[M&A | IPO | Lifestyle | Spin-off | etc.]

## Por quê esse tipo

## Timing target
- Earliest: anos
- Most likely: anos
- Latest: anos

## Valuation alvo
[range R$]

## Buyers prováveis (se M&A)
- Strategic: [lista]
- Financial: [lista]

## Pre-conditions
[o que precisa estar verdade pro exit funcionar]

## Plano de prep
[próximos 12 meses — o que fazer pra estar pronto]
```

## Heurísticas

- **M&A planning começa 2-3 anos antes.** VDR + clean financials + audit + clean cap table + clean legal.
- **Strategic buyer paga premium.** Financial buyer paga multiple. Saber qual antes de pitch.
- **Earnouts são comuns** — Diego precisa continuar 1-3 anos. Aceitar ou negociar saída clean?
- **Lifestyle: cashflow profitable + dividend annually** = válido. Maioria fundadores BR.
- **Kill com graça:** funcionários demitidos com indenização, fornecedores pagos, narrativa pública limpa = brand Diego preservado.

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/exit-strategy-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · exit-strategy · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
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
- **⬆️** entrepreneurship, board-orquestrador
- **🤝** clo-ma (executa M&A), cap-table-keeper, ceo-estrategia, cfo-fpa (valuation)
- **⬇️** Diego (decisão), advogado externo (closing)
- **✅** Diego, board, clo, cfo


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
- YYYY-MM-DD · exit-strategy · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · exit-strategy · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · exit-strategy · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
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

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-exit-strategy.md` no mesmo formato consolidado.

