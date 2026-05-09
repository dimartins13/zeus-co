# CORE — Data
> **Modelo. Centralizo. Disponibilizo pra cada LEP.**

## Stack atual
- ClickHouse (KingPanda — via skill `kp-clickhouse`)
- Plata-ou-Plomo JSON (financeiro)
- Google Sheets (operacional ad-hoc)
- ClickUp (tasks)

## Stack alvo (médio prazo)
- Single source of truth: Postgres (Supabase)
- BI: Metabase ou Looker Studio
- ETL: dbt-light (Python scripts) ou Make/Zapier
- Analytics produto: PostHog ou Amplitude

## Frameworks
- 3 camadas (raw → staging → marts)
- Star schema pra fato tables
- 1 KPI por dashboard (não diluir)
- Self-service pra Diego (não precisar pedir)

## Heurísticas
- Métrica sem decisão = vaidade
- Dashboard sem owner = morre
- Documentar definições (CAC tem 5 jeitos de calcular — escolher e documentar)
