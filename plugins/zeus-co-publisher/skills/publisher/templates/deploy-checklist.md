# Deploy Checklist — {Projeto novo}

> Pra criar projeto novo no plataouplomo.com seguindo padrão Plata-ou-Plomo.

**Empresa:** {nome}
**URL alvo:** `https://plataouplomo.com/{projeto}/`
**Path servidor:** `/domains/plataouplomo.com/public_html/{projeto}/`

---

## Pré-deploy

- [ ] Empresa tem pasta `_Publicacoes/` criada
- [ ] `Arquivo Final/index.html` pronto e testado localmente
- [ ] `Arquivo Final/.htaccess` adaptado (rotas + segurança)
- [ ] `Arquivo Final/api/index.php` adaptado (router + dados específicos)
- [ ] `Arquivo Final/api/dados.json` schema inicial pronto
- [ ] `Arquivo Final/api/users.json` com hash bcrypt das senhas (NUNCA plaintext)
- [ ] CLO LEP validou: termos de uso + política privacidade publicados se coleta dados
- [ ] LGPD: identificou dados sensíveis e bases legais
- [ ] Auth: não usar mesmas creds de outros projetos (isolamento)

## .htaccess padrão (template)

```apache
RewriteEngine On

# Bloquear acesso direto a JSONs
<FilesMatch "\.(json|bak)$">
    Require all denied
</FilesMatch>

# Permitir api/index.php acessar JSON via PHP
<Files "index.php">
    Require all granted
</Files>

# Roteamento /api/* → api/index.php
RewriteRule ^api/(.*)$ api/index.php [L,QSA]

# CORS se necessário
Header set Access-Control-Allow-Origin "*"
```

## Deploy via FTP

```bash
PROJETO="{projeto}"
LOCAL="/Users/diegomartins/Documents/Claude/Projects/{Empresa}/_Publicacoes/Arquivo Final"
REMOTE="/domains/plataouplomo.com/public_html/$PROJETO"

# Cria pasta no servidor
python3 -c "
import ftplib
ftp = ftplib.FTP('147.93.37.172')
ftp.login('USER', 'PASS')
try: ftp.mkd('$REMOTE')
except: pass
"

# Upload tudo
python3 _Scripts/ftp-upload.py --host 147.93.37.172 --user USER --password PASS \
  --local "$LOCAL" --remote "$REMOTE"
```

## Pós-deploy validation

- [ ] Browser: `https://plataouplomo.com/{projeto}/` carrega index.html
- [ ] Login funciona (usuário criado em users.json)
- [ ] API responde: `https://plataouplomo.com/{projeto}/api/health` (ou endpoint test)
- [ ] CSS/JS carregam corretamente
- [ ] HTTPS (Let's Encrypt automático no Hostinger)
- [ ] Backup interno funciona: cria expense → verifica `api/backups/` no servidor
- [ ] CDN Cloudflare propagado (pode demorar 5-10 min)

## Registrar deployment

- Append em `{Empresa}/LEARNINGS.md`:
  ```markdown
  ## {YYYY-MM-DD} — Deploy inicial Plata-ou-Plomo {projeto}
  - URL: https://plataouplomo.com/{projeto}/
  - Auth: {N} usuários iniciais
  - Notes: {observações}
  ```
- Atualiza `_Publicacoes/PUBLICATIONS.md` (registro central da empresa)
- Notifica CCO se brand visual relevante
- Notifica CFO se traz dados financeiros novos

## Próximos Movimentos

1. Configurar cron backup pra incluir esse projeto
2. Convidar operadores (criar users no users.json com bcrypt)
3. Próximo backup: cron seg/qui/dom 6h
