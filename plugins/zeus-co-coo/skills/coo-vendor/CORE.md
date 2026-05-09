# CORE — Vendor Manager
> **Negocio dura. SLA explícito. Backup sempre pronto.**

## Workflow
1. RFP (Request for Proposal) com 3+ vendors
2. Scorecard 5 critérios (preço, qualidade, leadtime, comunicação, flexibilidade)
3. Negociação (preço + termos)
4. Contrato com SLA + cláusula saída + cap responsabilidade (ver `clo-contratos`)
5. Onboarding + integração
6. Scoreio trimestral
7. Renegociação anual

## Heurísticas
- 3 cotações sempre (reduz superfaturamento >40%)
- Single-source = risco. Multi-source = standard pra crítico
- Renegociação anual: meta -5%
- Vendor scoreio < 3.5/5 = colocar em watch
- Vendor scoreio < 2.5/5 = transição (com 90d aviso prévio)

## Templates herdados
- `templates/vendor-scorecard.md` (no plugin coo)
- `templates/make-vs-buy.md` (no plugin coo)
