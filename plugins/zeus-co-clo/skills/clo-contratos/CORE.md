# CORE — Contratos Manager
> **Redijo. Reviso. Negocio cláusulas críticas.**

## Tipos de contrato e cláusulas-chave

### NDA (bilateral)
- Definição "Informação Confidencial"
- Prazo (3-5y) + sobrevivência
- Devolução/destruição
- Foro

### Vendor Agreement / MSA
- Objeto + escopo
- SLA + penalidades
- Liability cap (favorável: cap = 12m fees)
- IP ownership (work-for-hire se vendor cria pra você)
- LGPD se processa dados (DPA anexo)
- Saída + multa rescisória

### Sócio (Acordo de Sócios)
- Vesting (4y / 1y cliff)
- ROFR / Drag-along / Tag-along
- Bad leaver vs Good leaver
- Non-compete + Non-solicit
- Quórum decisões (75% pra críticas)

### CLT vs PJ
- CLT: subordinação + habitualidade + onerosidade + pessoalidade (4 elementos)
- PJ: sem subordinação, autônomo, sem exclusividade
- PJ improper = passivo trabalhista alto

### Term Sheet (captação)
- Liquidation preference (1x non-participating é founder-friendly)
- Anti-dilution (weighted average broad-based >> full ratchet)
- Pro-rata rights
- Board composition
- Drag-along

## Templates
- `templates/nda-bilateral.md`
- `templates/vendor-agreement.md`
- `templates/socio-vesting.md`

## Heurísticas
- Sempre revisar com advogado humano antes de assinar
- Foro = sua cidade
- Lei aplicável = Brasil (a menos que cliente internacional)
- Liability cap protege ambos (não só vendor)
