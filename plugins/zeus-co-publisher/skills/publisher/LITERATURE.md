# LITERATURE — Publisher

## Camada 1 — Documentação técnica do stack

### Plata-ou-Plomo (sistema próprio Diego)
- `Dash Financeiro/Plata-ou-Plomo-Documentacao.md` — visão completa sistema
- `Dash Financeiro/prompt-contexto-servidor.md` — contexto deploy Hostinger ⚠️ contém credenciais

### Hostinger
- [Hostinger File Manager](https://www.hostinger.com/tutorials/website/how-to-use-file-manager) — GUI alternativa ao FTP
- [Hostinger SSH Access](https://support.hostinger.com/en/articles/1583296-how-to-access-and-use-ssh) — se plano permitir
- [Hostinger API](https://developers.hostinger.com/) — limitada, focada em domínios/email

### PHP + JSON pattern
- [PHP file_put_contents docs](https://www.php.net/manual/en/function.file-put-contents.php)
- [PHP password_verify docs](https://www.php.net/manual/en/function.password-verify.php)
- [.htaccess Apache directives](https://httpd.apache.org/docs/current/howto/htaccess.html)

### FTP via Python
- [ftplib stdlib Python](https://docs.python.org/3/library/ftplib.html)
- [Paramiko SFTP](https://www.paramiko.org/) (se SFTP)

## Camada 2 — Padrões de deploy

### Imutabilidade vs mutabilidade
- **Imutável** (Vercel, Netlify, Cloudflare Pages): cada deploy é versão nova, rollback fácil
- **Mutável** (Hostinger shared): sobrescreve arquivos no servidor — risco de race condition

→ Por isso o **sync-aware update** é crítico no setup atual.

### Backup strategies
- **Snapshot completo** (atual padrão Plata-ou-Plomo) — mantém últimos 10 internamente + 30 dias de cópias locais
- **Append-only log** (event sourcing) — alternativa futura se sistema crescer
- **Versioned JSON** (cada save vira `dados.YYYY-MM-DD-HH-MM-SS.json`) — debug-friendly

### Conflict resolution
- **Last-write-wins** (perigoso em equipe) — o que evitar
- **Diff + manual review** (atual recomendado) — Diego decide
- **Operational transform** (Google Docs style) — overkill pra esse caso

## Camada 3 — Cases

| Caso | Lição |
|---|---|
| Git merge conflicts | Manual review > auto-merge em dados estruturados |
| Wikipedia edit conflicts | Lock pessimista > lock otimista em alta colaboração |
| Notion blocks CRDT | Operational transform escala mas é complexo demais pra pequena equipe |
| Google Sheets multi-edit | Real-time é ideal mas requer infra robusta — não cabe Hostinger shared |

## Camada 4 — Brasil

### LGPD aplicado a publicações
- Dados financeiros = dados sensíveis (Art. 5º II)
- Auth obrigatório, não publicar URLs sem proteção
- Logs de acesso obrigatórios pra controles
- DPO designado quando volume justifica

### Hostinger BR
- Datacenter SP disponível (latência baixa)
- Suporte BR responde rápido
- Preços em real

## Camada 5 — Skills mapeadas

- `dev-skills:writing-plans` — para deploys complexos
- `dev-skills:systematic-debugging` — quando publish falha
- `marketing:performance-report` — quando publica relatório
- Bash + Python (built-in) — execução do FTP
