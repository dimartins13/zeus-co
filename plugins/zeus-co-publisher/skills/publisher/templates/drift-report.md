# Drift Report — {Empresa}

> Quando o cron `backup-publicacoes` detecta que o ar mudou desde o último backup local.
> Significa: alguém editou no ar entre nossos snapshots. Precisa awareness antes do próximo update.

**Empresa:** {nome}
**Data deteção:** {YYYY-MM-DD HH:MM}
**Backup anterior:** {data N}
**Backup atual:** {data N+3 dias}

---

## O que mudou no ar (sem deploy local)

### Resumo
- Total de campos modificados: {N}
- Operadores envolvidos (estimativa por timestamp/autor nos dados): {Victor, Cris, etc}

### Detalhe por seção

#### `api/dados.json`

| Path | Mudança | Provável autor |
|---|---|---|
| `expenses[CrazyFlips]` | +3 items | Victor (operador desse projeto) |
| `suppliers[]` | +2 items | Cris |
| `roadmap[2ndStreet]` | 1 item updated | Victor |

#### `api/users.json`
*(qualquer mudança aqui é alerta — auth alterado)*

- {se vazio: "sem mudanças"}

## Impacto

- **Próximo update do Diego** vai precisar de **sync-aware merge** obrigatório
- Backups internos do servidor (`api/backups/`) preservam estados — usar pra rollback se erro

## Ação proposta

- [ ] Marcar este drift como "checked" em `_Publicacoes/PUBLICATIONS.md`
- [ ] Antes do próximo deploy local, OBRIGATÓRIO sync-aware-update
- [ ] Se mudança em `users.json` for inesperada → alerta P0 (CLO + CTO)

## Append em INBOX.md

```markdown
## ⚠️ [{data}] Drift {Empresa} — {N} mudanças no ar
- Operadores ativos: {lista}
- Próximo update local exigirá merge
```
