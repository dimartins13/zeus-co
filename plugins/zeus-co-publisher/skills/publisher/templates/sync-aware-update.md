# Sync-Aware Update — {Empresa / Projeto}

> Workflow CRÍTICO quando outros operadores podem ter editado dados no ar.
> NUNCA pular passos. Cada passo previne perda de dados financeiros alheios.

**Empresa:** {nome}
**Projeto no servidor:** `/domains/plataouplomo.com/public_html/{projeto}/`
**Data update:** {YYYY-MM-DD HH:MM}
**Mudança proposta:** {1 frase do que Diego quer atualizar}

---

## PASSO 1 — Download estado atual (PRÉ-update snapshot)

```bash
# Com credenciais carregadas (do 1Password)
FTP_USER="[from 1Password]"
FTP_PASS="[from 1Password]"
FTP_HOST="147.93.37.172"
PROJETO="{projeto}"
LOCAL_BACKUP="/Users/diegomartins/Documents/Claude/Projects/{Empresa}/_Publicacoes/Backup/$(date +%Y-%m-%d_%H-%M)-pre-update"

mkdir -p "$LOCAL_BACKUP"
# Python ftplib download recursivo (script em backup-script.md)
python3 ftp-download.py --host $FTP_HOST --user $FTP_USER --pass $FTP_PASS \
  --remote /domains/plataouplomo.com/public_html/$PROJETO/ \
  --local "$LOCAL_BACKUP"
```

✅ Status: backup pré-update salvo em `_Publicacoes/Backup/{YYYY-MM-DD_HH-MM}-pre-update/`

## PASSO 2 — Diff vs Arquivo Final (último estado conhecido local)

```bash
diff -r "$LOCAL_BACKUP/api/dados.json" "/Users/diegomartins/Documents/Claude/Projects/{Empresa}/_Publicacoes/Arquivo Final/api/dados.json"
# OU diff inteligente JSON
python3 -c "
import json
with open('$LOCAL_BACKUP/api/dados.json') as f: ar = json.load(f)
with open('/Users/diegomartins/.../Arquivo Final/api/dados.json') as f: local = json.load(f)
# Comparar e listar diferenças
"
```

### Mudanças detectadas (feitas por outros operadores entre último update e agora):

| Campo | Valor anterior (local) | Valor atual (ar) | Quem mudou? | Quando? |
|---|---|---|---|---|
| {ex: expenses[CrazyFlips]} | 12 items | 15 items | Victor | 2026-05-05 |
| {campo} | {antes} | {depois} | {operador} | {data} |

**TOTAL de mudanças por outros:** {N}

## PASSO 3 — Decisão Diego

**Aplicar mudanças propostas SOBRE o estado atual do ar?** (preserva o que outros fizeram)

- ☐ SIM, fazer merge (recomendado)
- ☐ NÃO, abortar — quero revisar antes
- ☐ SOBRESCREVER (PERIGOSO — perde mudanças de outros) — pedir confirmação dupla

## PASSO 4 — Merge

Aplica mudanças do Diego sobre `dados.json` baixado do ar (não sobre Arquivo Final desatualizado):

```python
# Python merge inteligente
merged = ar_atual.copy()
for change in mudancas_diego:
    apply_change(merged, change)  # add/update sem remover o que outros adicionaram

# Save em local temp pra revisão
with open('/tmp/dados-merged.json', 'w') as f:
    json.dump(merged, f, indent=2)
```

✅ Versão merged em `/tmp/dados-merged.json` — revisar visualmente antes de subir.

## PASSO 5 — Upload merged

```bash
python3 ftp-upload.py --host $FTP_HOST --user $FTP_USER --pass $FTP_PASS \
  --local /tmp/dados-merged.json \
  --remote /domains/plataouplomo.com/public_html/$PROJETO/api/dados.json
```

✅ Versão merged no ar.

## PASSO 6 — Atualiza Arquivo Final

```bash
cp /tmp/dados-merged.json "/Users/diegomartins/Documents/Claude/Projects/{Empresa}/_Publicacoes/Arquivo Final/api/dados.json"
```

✅ Local agora reflete o que está no ar pós-update.

## PASSO 7 — Registra em LEARNINGS.md

Append em `{Empresa}/LEARNINGS.md`:
```markdown
## {YYYY-MM-DD} — Update Plata-ou-Plomo

- Mudança Diego: {descrição}
- Mudanças preservadas de outros: {N} (Victor: X, Cris: Y, etc)
- Merge: sucesso / conflito (resolvido por Diego)
```

## Próximos Movimentos

1. {se conflito não resolvido: pedir Diego decidir item por item}
2. Verificar URL no browser pós-update
3. Próximo backup: cron na quinta/segunda
