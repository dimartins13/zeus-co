# Customer Ops Playbook — {Empresa}

> Playbook operacional de atendimento ao cliente. Define canais, SLAs, escalation, métricas.

**Empresa:** {nome}
**Versão:** v{n}
**Última revisão:** {YYYY-MM-DD}

---

## 1. Canais de atendimento

| Canal | Cobertura | SLA primeira resposta | SLA resolução |
|---|---|---|---|
| Email | 24/7 (resposta business hours) | 4h | 24h |
| WhatsApp | business hours | 30min | 4h |
| Chat in-app | business hours | 5min | 1h |
| Telefone | (se houver) | imediato | - |

## 2. Tipos de ticket + SOP

| Tipo | Frequência esperada | SOP de tratamento |
|---|---|---|
| Dúvida de produto | Alta | `templates/sop-duvida-produto.md` |
| Problema entrega | Média | `templates/sop-problema-entrega.md` |
| Solicitação troca/devolução | Média | `templates/sop-troca-devolucao.md` (PROCON 30d) |
| Reclamação qualidade | Baixa | `templates/sop-reclamacao-qualidade.md` |
| Solicitação especial / VIP | Baixa | Escalation direto Diego |

## 3. Escalation

| Sintoma | Nível 1 | Nível 2 | Nível 3 |
|---|---|---|---|
| Ticket > 24h sem resposta | CS rep | COO LEP | Diego |
| NPS detractor (≤6) | CS rep | CS lead | CMO LEP (loop) |
| Reclamação pública (Reclame Aqui, redes) | CS lead | COO + CMO LEP | Diego |
| Risco jurídico (PROCON, ação) | CS lead | CLO LEP | Diego |

## 4. Métricas

| Métrica | Meta | Frequência |
|---|---|---|
| FCR (First Contact Resolution) | ≥70% | Semanal |
| Tempo médio resposta | <30min business hours | Semanal |
| NPS pós-atendimento | ≥9 | Mensal |
| CSAT por interação | ≥4.5/5 | Diária |
| Volume tickets / cliente ativo | <0.1 | Mensal |

## 5. Dashboard (onde acompanhar)

- Notion / Sheets: tabela de tickets abertos
- Reclame Aqui: monitorar reputação
- Redes sociais: monitor de menções

## Próximos Movimentos

1. {ação imediata pra implementar/atualizar}
2. {treinamento ou ferramenta a implantar}
3. {checkpoint mensal}
