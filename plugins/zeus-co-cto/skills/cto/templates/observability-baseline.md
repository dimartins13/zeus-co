# Observability Baseline — {Empresa}

> Mínimo necessário pra você ENXERGAR o que está acontecendo. Sem observability, debugging é tortura.

**Empresa:** {nome}
**Stack:** {referenciar tech-stack-decision}

---

## 4 camadas básicas

### 1. Errors
- **Tool:** Sentry
- **O que captura:** exceptions, stack traces, user context
- **Alerta:** Slack / Telegram quando error rate > X%

### 2. Logs
- **Tool:** {Vercel logs / Hostinger / Logtail / Logflare}
- **Retenção mínima:** 30 dias
- **Buscável:** sim, com filter por user/route/timestamp

### 3. Performance / Uptime
- **Tool:** UptimeRobot (free) ou BetterStack
- **Endpoints monitorados:** {lista}
- **Alerta:** SMS + email quando down

### 4. Product analytics
- **Tool:** {PostHog / Plausible / Amplitude / Mixpanel / GA4}
- **Eventos chave rastreados:**
  - {evento 1}
  - {evento 2}
- **Funnel principal:** {etapas}

## Setup checklist

- [ ] Sentry projeto criado + DSN nas env vars
- [ ] Logs centralizados em ferramenta com search
- [ ] UptimeRobot apontando pros endpoints críticos
- [ ] Analytics tool com tracking eventos chave
- [ ] Dashboards básicos (errors, latência, uptime, conversão)
- [ ] Alertas configurados (Slack/email/SMS)

## Custos

| Tool | Plano | Custo/mês |
|---|---|---|
| Sentry | Developer | $0 |
| Logs | | |
| Uptime | Free | $0 |
| Analytics | | |
| **Total** | | **R$ {valor}** |

## Próximos Movimentos

1. Setup Sentry esta semana
2. Definir 5 eventos analytics chave
3. Criar dashboard único Notion/Mode com todos KPIs
