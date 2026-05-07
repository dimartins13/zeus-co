# Growth Experiment — {Hipótese em 1 frase}

> Formato Reforge / Hacking Growth. Cada experimento valida UMA hipótese isolada.

**Empresa:** {nome}
**Experimento ID:** EXP-{NN}
**Owner:** {specialist}
**Status:** Running / Concluded

---

## Hipótese

**Acreditamos que** {mudança específica em ponto X}
**vai resultar em** {métrica Y movendo +Z%}
**porque** {razão de comportamento}.

## Métrica primária + secundárias

- **Primary:** {métrica + valor baseline + lift target}
- **Secondary (guardrail):** {métrica que não pode piorar}

## Setup

- **Audiência:** {quem entra no experimento}
- **Variantes:** Control vs Variant A (e B se aplicável)
- **Sample size mínimo:** {N usuários por variante para significância}
- **Duração estimada:** {N dias}
- **Stopping criteria:** {quando parar — significância, fim do prazo, quebra de guardrail}

## Resultados

| Métrica | Control | Variant A | Lift | Significância |
|---|---|---|---|---|
| Primary | | | | p={valor} |
| Secondary | | | | |

## Decisão

- ☐ **Ship** (variant ganhou + significância) → escalar para 100%
- ☐ **Iterate** (sinal mas não significativo) → rodar v2
- ☐ **Kill** (não funcionou) → arquivar com aprendizado

## Aprendizado (em 1 parágrafo)

{O que descobrimos sobre o cliente / produto / canal — válido até futuro experimento contradizer}

## Próximos Movimentos

1. {se ship: implementar production}
2. {próximo experimento sugerido}
3. {atualizar growth backlog}
