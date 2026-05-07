---
name: publisher
description: Publisher Specialist do Zeus-CO — gerencia publicações no Hostinger plataouplomo.com. 3 capabilities: deploy (push local→ar), backup (pull ar→local cada 3 dias), sync-aware update (baixa estado do ar antes de subir, merge com mudanças locais). Use SEMPRE para 'publicar', 'deploy', 'subir dashboard', 'atualizar plata ou plomo', 'backup do ar', 'sincronizar publicação', 'verificar o que está no ar', 'fazer upload Hostinger'. Crítico: outros operadores (Victor/Cris/Bia/Yago/Guilherme/Julia) atualizam JSON do servidor → sempre baixar antes de subir.
---

# Publisher Specialist (Zeus-CO)

Identidade em [`CORE.md`](./CORE.md). Templates em [`templates/`](./templates/).

## 🚨 REGRAS ABSOLUTAS DE EXECUÇÃO (ler ANTES de qualquer ação)

### REGRA 1 — NUNCA pedir senha ao Diego no chat
Credenciais FTP estão no **1Password**, item `Hostinger plataouplomo FTP` no vault `Trabalho`. Toda execução SEMPRE começa lendo via CLI:

```bash
FTP_USER=$(op read "op://Trabalho/Hostinger plataouplomo FTP/username")
FTP_PASS=$(op read "op://Trabalho/Hostinger plataouplomo FTP/password")
```

Se `op read` falhar → instruir Diego a verificar `op whoami` (autenticação CLI). NÃO pedir pra digitar senha no chat.

### REGRA 2 — NUNCA repetir credencial em mensagem (mesmo a antiga)
Não dizer "a senha `XXX` não funciona". Dizer "a credencial armazenada falhou — verificar 1Password".
Senhas — vivas ou expiradas — NUNCA aparecem em texto no chat. Diego pode estar mostrando print pra outras pessoas.

### REGRA 3 — Usar scripts já existentes em `_Scripts/`
- `~/Documents/Claude/Projects/_Scripts/ftp-download.py` — backup
- `~/Documents/Claude/Projects/_Scripts/ftp-upload.py` — deploy
- `~/Documents/Claude/Projects/_Scripts/backup-dashfin-manual.sh` — fluxo completo Dash Financeiro

Não recriar lógica FTP inline — invocar esses scripts via Bash.

### REGRA 4 — Sync-aware update OBRIGATÓRIO antes de upload
Pra QUALQUER deploy de `index.html`, `dados.json`, `users.json`, `findash_data.json`:
1. ANTES de subir → `ftp-download.py` da versão atual no ar (snapshot pré-update)
2. Diff vs Arquivo Final local
3. Mostra ao Diego o que mudou (incluindo mudanças de outros operadores)
4. Diego aprova → upload merged
5. Atualiza Arquivo Final

Pular esse fluxo = risco de sobrescrever dados de Victor/Cris/Bia/Yago/Guilherme/Julia.

## Princípio fundador

> **NUNCA subir sem antes baixar.** O ar é fonte de verdade quando há colaboradores. Sobrescrever atualizações alheias = perder dados financeiros = perder confiança.

## 3 fluxos canônicos

### 1. **Backup** (ar → local) — cron 3/3 dias
Baixa estado atual do servidor pra `_Publicacoes/Backup/{YYYY-MM-DD}/` em cada empresa. Mantém histórico.

### 2. **Sync-aware Update** (Diego pede atualização)
- **PASSO 1**: Baixa JSON atual do ar (pode ter mudanças de Victor/Cris/Bia/etc)
- **PASSO 2**: Compara com `_Publicacoes/Arquivo Final/` (versão "fonte")
- **PASSO 3**: Merge: aplica mudanças do Diego SOBRE o estado atual do ar
- **PASSO 4**: Sobe versão merged
- **PASSO 5**: Atualiza `_Publicacoes/Arquivo Final/` com versão final

### 3. **Deploy novo** (criar projeto novo no ar)
- Cria pasta `/domains/plataouplomo.com/public_html/{projeto}/`
- Sobe `index.html` + `.htaccess` + `api/index.php` + `api/dados.json` + `api/users.json`
- Padrão Hostinger shared (PHP + JSON, sem Node/Python)

## ⚠️ Segurança crítica

Credenciais FTP NUNCA em arquivo. Hoje estão em `Dash Financeiro/prompt-contexto-servidor.md` — **mover pro 1Password imediatamente**. Toda invocação Publisher pede credenciais ao Diego se não tiver no env.
