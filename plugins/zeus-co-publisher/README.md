# Zeus-CO — Publisher Specialist

Specialist transversal de publicação. Stack atual: **Hostinger shared hosting** + domínio **plataouplomo.com** + PHP + JSON files.

**Princípio:** NUNCA subir sem antes baixar. Outros operadores (Victor, Cris, Bia, Yago, Guilherme, Julia) podem ter atualizado dados no ar.

## 3 fluxos canônicos
1. **Backup** (cron seg/qui/dom 6h) — ar → `_Publicacoes/Backup/{YYYY-MM-DD}/`
2. **Sync-aware Update** — baixa ar → diff → merge → sobe → atualiza Arquivo Final
3. **Deploy novo** — cria estrutura PHP+JSON padrão Hostinger

## Estrutura padrão por empresa
```
[Empresa]/_Publicacoes/
├── Backup/
│   ├── 2026-05-07/    (snapshot do ar)
│   └── 2026-05-04/
└── Arquivo Final/      (versão fonte editável)
```

## ⚠️ Segurança

Credenciais FTP **NUNCA em arquivo**. Atualmente expostas em `Dash Financeiro/prompt-contexto-servidor.md` — mover pro 1Password (item: "Hostinger plataouplomo FTP").

## Cron
- `backup-publicacoes` — segundas/quintas/domingos 6h (Haiku)
