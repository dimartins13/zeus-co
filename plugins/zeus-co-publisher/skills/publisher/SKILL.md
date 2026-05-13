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


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

Antes de encerrar QUALQUER sessão deste LEP, escrever nessa ordem. Sem isso, sessão não fechou.

### 1. LEARNINGS.md (empresa atual)
Append 1-3 lições durables. Formato:
```
- YYYY-MM-DD · publisher · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · publisher · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · publisher · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
```

### 4. _Inbox.md (opcional — quando vale)
Se nasceu sugestão proativa que Diego não pediu mas merece atenção dele, append bloco:
```
## [SUGESTÃO] [título curto] · YYYY-MM-DD
- **O quê:** 1 linha
- **Por quê (gatilho):** 1 linha
- **Próximo passo:** 1 linha
- **Status:** [aguarda Diego]
```

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-<topic>.md` no mesmo formato consolidado.

## Trabalha em equipe com

> Skill ISOLADA é skill subutilizada. Eu opero conectado.
> Skills da família **Zeus-CO** se invocam mutuamente via description matching do Cowork.
> Ver mapa completo em [ZEUS-CO-ECOSYSTEM.md](/Users/diegomartins/Documents/Claude/Projects/ZEUS-CO-ECOSYSTEM.md).

### ⬆️ Upstream (de onde vem meu input)
  - qualquer LEP que entrega artefato

### 🤝 Peers (com quem co-crio)
  - cto-devops

### ⬇️ Downstream (pra quem entrego)
  - Hostinger (deploy)

### ✅ QA pair (quem valida meu output antes do deploy)
  - cco-brand-guardian (peça)
  - clo-compliance (claim)

**Princípio operacional:** quando minha saída implica em ação de outra função (legal/financeiro/criação/ops/tech), eu **delego explicitamente** invocando a skill correta, não "executo no escuro".
