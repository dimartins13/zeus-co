# Token Audit — {Workspace ou Sessão}

> Auditoria de uso de tokens. Roda mensal (cron) ou sob demanda.
> Output: lista priorizada de otimizações com economia esperada.

**Workspace:** {nome — ex: "Diego — Documents/Claude/Projects"}
**Data audit:** {YYYY-MM-DD}
**Período coberto:** {últimos 30 dias / sessão atual / etc}

---

## 1. Snapshot de uso atual

### Por dimensão
| Dimensão | Volume | Custo estimado |
|---|---|---|
| CLAUDE.md auto-loaded | {N tokens × M turnos = X tokens cobrados} | R$ {valor} |
| Memória global | {N tokens} | R$ {valor} |
| Tool definitions (todos MCPs ativos) | {N tokens × M turnos} | R$ {valor} |
| Skill descriptions | {N tokens × M turnos} | R$ {valor} |
| Histórico médio | {N tokens × M turnos} | R$ {valor} |
| Saída (output) | {N tokens × M turnos × 5x} | R$ {valor} |
| Cache hits (-90%) | {N hits × cost} | R$ {valor} |
| Cache writes (+25%/100%) | {N writes × cost} | R$ {valor} |
| **TOTAL** | | **R$ {valor}/mês** |

### Por modelo
| Modelo | % uso | Custo |
|---|---|---|
| Haiku | {%} | R$ |
| Sonnet | {%} | R$ |
| Opus | {%} | R$ |

### Por tipo de chat
| Tipo | Tokens médios/sessão | Frequência |
|---|---|---|
| Chats interativos | | |
| Crons automáticos | | |
| Subagents | | |

## 2. Findings (top 5 desperdícios)

### Finding 1 — {ex: "CLAUDE.md de 5.000 tokens carregado em 200+ turnos/mês"}
- **Custo atual:** R$ {valor}/mês
- **Causa:** {descrição}
- **Recomendação:** {ação}
- **Custo pós:** R$ {valor}/mês
- **Economia:** R$ {valor} ({%})

### Finding 2 — ...
### Finding 3 — ...
### Finding 4 — ...
### Finding 5 — ...

## 3. Quick wins (implementar agora)

- [ ] {ação 1 — economia esperada}
- [ ] {ação 2}
- [ ] {ação 3}

## 4. Decisões maiores (avaliar)

- [ ] {ação que muda arquitetura — discutir com CTO LEP}
- [ ] {desinstalar plugin X — confirmar com Diego}

## 5. Próximos Movimentos

1. {quick win mais impactante esta semana}
2. {audit em sessão específica suspeita}
3. {data próxima audit mensal}
