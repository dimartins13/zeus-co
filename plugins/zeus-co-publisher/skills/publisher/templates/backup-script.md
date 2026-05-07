# Backup Script — FTP Hostinger plataouplomo

> Script Python pra download recursivo do servidor. Roda no cron `backup-publicacoes` (seg/qui/dom 6h).

## Pré-requisitos

- Python 3 (já no Mac)
- Credenciais FTP do 1Password (item "Hostinger plataouplomo FTP")
- Pasta `_Publicacoes/Backup/` existe em cada empresa (criada pelo Sprint B do Publisher)

## ftp-download.py (esqueleto)

```python
#!/usr/bin/env python3
"""
FTP recursive download — Hostinger plataouplomo.
Uso:
  python3 ftp-download.py --host HOST --user USER --pass PASS \
    --remote /domains/plataouplomo.com/public_html/PROJETO/ \
    --local /Users/.../Empresa/_Publicacoes/Backup/YYYY-MM-DD/
"""
import argparse, ftplib, os, sys
from pathlib import Path

def download_recursive(ftp, remote_dir, local_dir):
    Path(local_dir).mkdir(parents=True, exist_ok=True)
    ftp.cwd(remote_dir)
    items = []
    ftp.retrlines('LIST', items.append)
    for line in items:
        parts = line.split(maxsplit=8)
        name = parts[-1]
        if name in ('.', '..'): continue
        is_dir = line.startswith('d')
        if is_dir:
            download_recursive(ftp, name, os.path.join(local_dir, name))
            ftp.cwd('..')
        else:
            local_path = os.path.join(local_dir, name)
            with open(local_path, 'wb') as f:
                ftp.retrbinary(f'RETR {name}', f.write)
            print(f"  ✓ {os.path.relpath(local_path)}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--host', required=True)
    p.add_argument('--user', required=True)
    p.add_argument('--password', required=True)  # NÃO --pass (palavra reservada)
    p.add_argument('--remote', required=True)
    p.add_argument('--local', required=True)
    args = p.parse_args()
    
    print(f"Connecting to {args.host}...")
    with ftplib.FTP(args.host) as ftp:
        ftp.login(args.user, args.password)
        print(f"Downloading {args.remote} → {args.local}")
        download_recursive(ftp, args.remote, args.local)
    print("✓ Download complete")

if __name__ == '__main__':
    main()
```

## Salvar em

```
~/Documents/Claude/Projects/_Scripts/ftp-download.py
```

(Pasta `_Scripts/` no root pra utilities cross-empresa)

## ftp-upload.py — análogo

Mesmo padrão, mas com `STOR` em vez de `RETR`. Usado pelo sync-aware-update.

## Cron `backup-publicacoes` (chama esse script)

```bash
#!/bin/bash
# Chamado pelo scheduled-task do Cowork
# Pega creds do 1Password (op CLI: brew install 1password-cli)
FTP_USER=$(op read "op://Personal/Hostinger plataouplomo FTP/username")
FTP_PASS=$(op read "op://Personal/Hostinger plataouplomo FTP/password")
FTP_HOST="147.93.37.172"

DATE=$(date +%Y-%m-%d)

for empresa_pair in "Crazyflips:crazyflips" "2ndStreet:2ndstreet" "Ventage:ventage"; do
  IFS=':' read -r EMPRESA PROJETO <<< "$empresa_pair"
  LOCAL="/Users/diegomartins/Documents/Claude/Projects/$EMPRESA/_Publicacoes/Backup/$DATE"
  
  mkdir -p "$LOCAL"
  python3 ~/Documents/Claude/Projects/_Scripts/ftp-download.py \
    --host "$FTP_HOST" --user "$FTP_USER" --password "$FTP_PASS" \
    --remote "/domains/plataouplomo.com/public_html/$PROJETO/" \
    --local "$LOCAL" || echo "⚠️ Falha em $EMPRESA"
done

# Cleanup backups > 30 dias
find ~/Documents/Claude/Projects/*/\_Publicacoes/Backup/* -maxdepth 0 -type d -mtime +30 -exec rm -rf {} \;
```

## Próximos Movimentos

1. Diego cria item 1Password "Hostinger plataouplomo FTP" com host/user/pass
2. Instala op CLI: `brew install 1password-cli && op signin`
3. Salva ftp-download.py em `_Scripts/`
4. Testa download manual de 1 projeto antes de ativar cron
