# Alert Protocol — Pulse

> Como decidir se algo é P0/P1/P2 e quem notificar.

---

## P0 — Ação imediata (notificar HOJE)

| Trigger | Critério |
|---|---|
| Runway < 3 meses | CFO LEP `default-alive.md` indica DEAD |
| Compliance gap urgente | Ex: KingPanda operando sem licença SECAP |
| Bug crítico produção | Site fora do ar, checkout quebrado |
| Vazamento dados | LGPD incident — 72h pra ANPD |
| Multa / processo recebido | Qualquer notificação judicial/CONAR/ANPD |
| Cofounder/sócio sai abruptamente | Crise de gestão |

**Protocolo P0:**
1. Append imediato em `INBOX.md` no topo com flag 🚨🚨
2. Notificação push (se configurada)
3. Invoca LEP responsável imediatamente em prompt sugerido
4. Se Diego não responde em 24h, escala (re-append + tag urgência)

## P1 — Ação esta semana

| Trigger | Critério |
|---|---|
| Tarefa P0 ClickUp parada > 7 dias | Tempo em status > 7d |
| Burn 20%+ acima orçado | Verificar Dash Financeiro vs plano CFO |
| OKR off-track 50%+ no meio do trimestre | <50% atingido em sem 6/13 |
| Vendor crítico falhou SLA | Identificar via `coo-vendor-scorecard` |
| NPS detractor recorrente | ≥3 detractors no mês mesmo motivo |

**Protocolo P1:**
1. Append em INBOX seção "P1 da semana"
2. Daily pulse menciona top 3 P1
3. Weekly digest cobre todos

## P2 — Acompanhar

| Trigger | Critério |
|---|---|
| Health score caiu 1+ ponto vs semana anterior | Comparativo |
| Cron LEP não rodou | Erros de execução |
| Documentação desatualizada > 30d | LEARNINGS sem update |
| Tarefa parada 4-7d | Quase virando P1 |

**Protocolo P2:**
1. Aparece no portfolio pulse (semanal segunda 8h)
2. Não interrompe Diego no meio da semana

---

## Notificação por LEP

| LEP | Trigger típico | Mensagem |
|---|---|---|
| **CFO** | Runway, burn, unit econ deteriorando | "[Empresa] runway X meses, burn +Y%. Ação: ..." |
| **CLO** | Compliance gap, contrato vence, multa | "[Empresa] [obrigação] em [N] dias. Ação: ..." |
| **CEO** | OKR off-track, decisão pivot | "[Empresa] OKR [n] em X% — re-priorizar?" |
| **COO** | SLA vendor, processo quebrado | "[Empresa] vendor [X] não entregou [Y]. Ação: ..." |
| **CMO** | Canal CAC inflando, NPS caindo | "[Empresa] CAC canal [X] +Y%. Pausar e ajustar?" |
| **CCO** | Inconsistência brand, conteúdo defasado | "[Empresa] [touchpoint X] divergente brand voice. Audit." |
| **CTO** | Bug, downtime, segurança | "[Empresa] [bug crítico]. Patch em [tempo]." |

---

## Anti-padrão (não fazer)

- Disparar P0 pra tudo (vicia ignorar)
- Daily alert vazio só pra mostrar "rodei"
- Reportar dados sem ação ("burn está alto" ❌ vs "burn alto, cortar X poupa Y" ✅)
- Esperar Diego perguntar pra reportar P0
