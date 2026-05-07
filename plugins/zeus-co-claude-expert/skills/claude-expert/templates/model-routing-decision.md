# Model Routing — Qual modelo Claude usar quando

> Decisão por tarefa. Sonnet é DEFAULT. Opus só quando justifica 5x custo. Haiku quando cabe.

---

## Hierarquia padrão

| Tarefa | Modelo recomendado | Razão |
|---|---|---|
| Chat interativo geral | **Sonnet 4.6** | Default — melhor relação custo/capacidade |
| Implementação de código | **Sonnet 4.6** | Suficiente em 95% dos casos |
| Debug normal | **Sonnet 4.6** | |
| Debug complexo (>1h sem solução) | **Opus 4.7** | Vale 5x custo pra desbloquear |
| Refatoração ampla cross-files | **Opus 4.7** | Holds context melhor |
| Decisão estratégica de alto impacto (CEO LEP final call) | **Opus 4.7** | Decisão errada custa muito mais que 5x |
| Análise documento longo (PDF, código grande) | **Opus 4.7 (1M)** | Context window |
| Pesquisa web + síntese curta | **Haiku 4.5** | Suficiente, mais barato |
| Classificação / extração estruturada | **Haiku 4.5** | Ideal |
| Cron de manutenção (literatura, tools updates) | **Haiku 4.5** | Volume alto, complexidade baixa |
| Geração de boilerplate / template fill | **Haiku 4.5** | |
| Code review profundo | **Opus 4.7** | Captura mais nuance |
| Code review superficial / lint-style | **Sonnet** ou **Haiku** | |
| Conteúdo criativo (copy, narrativa) | **Sonnet 4.6** | Default; Opus quando direção criativa muito sutil |
| Tradução curta | **Haiku 4.5** | |
| Tradução técnica longa | **Sonnet 4.6** | |

## Custos relativos (referência)

- Haiku 4.5 = 1x (baseline)
- Sonnet 4.6 = ~3x
- Opus 4.7 = ~15x (1M context: ainda mais, verificar pricing atual)

## Regras práticas

1. **Comece sempre Sonnet.** Mude pra Opus só se travar ou se for decisão crítica.
2. **NUNCA mude modelo no meio da conversa.** Cache se invalida.
3. **Crons sempre Haiku** (a menos que cron faça análise complexa).
4. **Subagents** podem usar modelos diferentes do main — útil pra delegar pesquisa pesada pra Haiku.
5. **`/fast` mode** = Opus 4.6 com saída acelerada (não downgrade pra modelo menor).

## Decisão pra esta tarefa

- **Tarefa:** {descrição}
- **Modelo recomendado:** {qual}
- **Justificativa:** {1 frase}

## Próximos Movimentos

1. {executar com modelo recomendado}
2. {se travar, considerar upgrade}
3. {medir gasto após — entrar em audit mensal}
