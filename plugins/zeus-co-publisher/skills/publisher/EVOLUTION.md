# EVOLUTION — Publisher

## v0.1.0 — 2026-05-07

- Criado por demanda Diego (proteção contra sobrescrever atualizações de outros operadores)
- Adaptado ao stack real Plata-ou-Plomo (PHP + JSON em Hostinger shared)
- 3 fluxos: Backup, Sync-aware Update, Deploy novo
- Estrutura `_Publicacoes/{Backup, Arquivo Final}/` por empresa
- Cron `backup-publicacoes` — seg/qui/dom 6h (3/3 dias)
- 4 templates: deploy-checklist, sync-aware-update, backup-script, drift-report
- Operadores conhecidos: Diego (admin), Victor, Cris, Bia, Yago, Guilherme, Julia

## ⚠️ FLAG segurança identificada
- Credenciais FTP em texto plano em `Dash Financeiro/prompt-contexto-servidor.md`
- Recomendação no RADAR: mover pro 1Password, item "Hostinger plataouplomo FTP"

## Próximas atualizações
- [ ] Configurar cron `backup-publicacoes`
- [ ] Primeira execução: mapear quais 6 projetos do Plata-ou-Plomo já têm pasta no servidor
- [ ] Criar `_Publicacoes/` em todas empresas com presença no ar
- [ ] Backup inicial completo (snapshot zero)
- [ ] Adicionar empresas Plata-ou-Plomo que não estão no canonical Zeus-CO: LAB NoName, Creatina, Pandora
