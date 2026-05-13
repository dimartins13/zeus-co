---
name: portfolio-allocation
description: Portfolio Allocation — alocação de tempo + capital + atenção Diego cross-portfolio. Três Horizontes aplicados ao portfolio. Decisões mensais de foco. Use pra "alocação Diego cross-empresas", "portfolio allocation", "tempo Diego", "kill or scale", "concentração portfolio", "three horizons portfolio", "review portfolio mensal".
---

# Portfolio Allocation

## Identidade
Decisão de ONDE Diego coloca atenção essa semana. Não-tudo-igual.

## Princípio inviolável
**Atenção dividida igual entre 5 empresas = NENHUMA recebe atenção suficiente.** Concentração de atenção = unfair advantage Diego.

## Framework canon: Three Horizons portfolio

```
H1 (60% atenção Diego): empresa em PMF / scaling
H2 (30%): empresas validando ou crescendo
H3 (10%): novas ideas / experiments

Total: 100% atenção alocada.
```

## Pra cada empresa Diego, classificar:

| Empresa | Horizon | % atenção Diego | Razão |
|---|---|---|---|
| <empresa> | H1 | 30% | Operação inicial — drops |
| <empresa> | H2 | 15% | MVP — produtora confirma |
| <empresa> | H2 | 15% | MVP — app launch decisão |
| <empresa> | H2 (regulated) | 15% | Gate SECAP pendente |
| <empresa> | H3 | 10% | Modelo aguarda definição |
| Plata-ou-Plomo | H1 (infra) | 10% | Manutenção |
| **Outros / novos** | H3 | 5% | — |

Total: 100%

## Review mensal canônico

`_Areas/Entrepreneurship/portfolio-allocation-YYYY-MM.md`:

```markdown
# Portfolio Allocation — YYYY-MM

## Alocação previa
[tabela acima]

## Alocação real (medida)
[Diego registra horas/empresa]

## Drift analysis
- Onde divergiu?
- Por quê?
- Correção?

## Decisões do mês
- Subir alocação X? Cortar Y? Pausar Z?

## Next month allocation target
[próximo mês]
```

## Sinais de re-alocação

- **Subir alocação:** uma empresa atinge PMF / sinal forte
- **Cortar alocação:** empresa estagnada 6+ meses
- **Pausar (sleep):** sem destino claro, mas não vale kill
- **Kill:** sem fit + alocação ruim + sem capital pra continuar

## Trabalha em equipe com
- **⬆️** entrepreneurship, founders-office (cross)
- **🤝** pulse (dados objetivos cross-empresa), ceo-orquestradores (status cada empresa)
- **⬇️** Diego (decisão final)
- **✅** Diego, board (re-allocations significativas)


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
- YYYY-MM-DD · portfolio-allocation · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · portfolio-allocation · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · portfolio-allocation · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
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

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-portfolio-allocation.md` no mesmo formato consolidado.

