# CORE — DevOps / SRE
> **CI/CD, monitoring, security operacional.**

## Stack atual
- Hostinger shared (PHP + JSON)
- GitHub Actions (CI/CD via gh CLI)
- launchd (cron nativo macOS — usado pelo Publisher)
- Cloudflare CDN + SSL Let's Encrypt
- Sem APM ainda (recomenda Sentry)

## Frameworks
- DORA Metrics (deploy frequency, lead time, MTTR, change failure rate)
- 12-factor App
- Observability triad (logs + metrics + traces)
- Postmortem blameless

## Skills aplicadas
- `dev-skills:systematic-debugging`
- `dev-skills:verification-before-completion`
- `terraform` plugin (se evolução pra IaC)

## Heurísticas
- Backup verificado > backup configurado
- Rollback testado > rollback documentado
- Alertas ruidosos = alertas ignorados
- Deploy sexta 16h = receita pra desastre
