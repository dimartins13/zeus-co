---
name: closeout-orchestrator
description: Fecha e grava a memória de QUALQUER projeto sob demanda, quando o Diego diz que está contente com um ponto da conversa e quer salvar tudo para o próximo chat. Detecta o(s) projeto(s) afetado(s), inventaria arquivos novos/modificados, cria run-note, atualiza 00_INDEX/_LEDGER quando seguro, marca fatos/deltas pendentes e responde com um recibo. GLOBAL — nunca específico de uma empresa. Frases-gatilho: "closeout", "/closeout-orchestrator", "fecha a conversa", "fecha o dia", "estou contente com este ponto", "grava tudo pro próximo chat", "atualiza a memória do projeto", "registrar trabalho", "sync project memory", "fecha o ponto", "salva o que fizemos". Aliases: /sync-project-memory, /fecha-o-dia, /registrar-trabalho.
---

# closeout-orchestrator — fechamento manual de memória (qualquer projeto)

Fechamento **sob demanda** quando o Diego está contente com um ponto e quer gravar tudo pro próximo chat, sem esperar o reconciliador diário das 23h. **Global**: funciona pra qualquer pasta em `/Users/diegomartins/Documents/Claude/Projects/`. **Nunca** assuma que é dope street — sempre detecte o(s) projeto(s).

## 0. Ler primeiro (fontes obrigatórias)
1. `/Users/diegomartins/Documents/Claude/Vault/00-SISTEMA-closeout-diario-global-projetos.md` (o protocolo-mãe; via **desktop-commander** se o chat não alcançar o Vault).
2. Do(s) projeto(s) ativo(s): `CLAUDE.md`, `00_INDEX.md`, `_LEDGER.md`, `LEARNINGS.md`, `BACKLOG.md` (os que existirem).
3. Arquivos novos/modificados relevantes no projeto e/ou citados na conversa.

## 1. Detectar o(s) projeto(s) afetado(s)
Combine sinais: (a) diretório atual; (b) arquivos citados na conversa; (c) caminhos modificados recentemente (`git status`/mtime); (d) nomes de projeto que o Diego mencionou. **Se >1 projeto → listar todos e tratar cada um separadamente** (uma run-note por projeto).
**NÃO é projeto (nunca fechar):** o symlink `Projects/Universidade-Conselho/` (é a doutrina do Vault, só leitura — aparece cheia mas não é projeto), pastas de sistema de nível topo (`_Modelo`, `_Arquivo`, qualquer `_*`) e o próprio Vault.

## 2. Inventário rápido
Arquivos novos/modificados relevantes desde o último closeout ou nas últimas 24–36h:
- extensões: `.md .html .pdf .docx .pptx .xlsx .csv`;
- estruturais: `CLAUDE.md 00_INDEX.md _LEDGER.md LEARNINGS.md BACKLOG.md`;
- artefatos: `_Publish/ _Areas/ research/ outputs/`.
Ignorar ruído: `.git/ .obsidian/` caches, builds, `node_modules/`, logs, mídia pesada não editada à mão, **dumps de backup/publicação arquivada** (`*/Backup/`, `*/backups/`, `_Publicacoes/*/`), e qualquer caminho atravessando o symlink `Universidade-Conselho/`. Contar artefatos de conteúdo — nunca enumerar pastas de asset/backup.

## 3. Classificar impacto (por mudança)
artefato novo · atualização de artefato · **decisão/fato durável** · **mudança de posicionamento/modelo/preço/identidade/estratégia** · rascunho/temporário · ruído.

## 4. Escrever a run-note
Local canônico:
```
/Users/diegomartins/Documents/Claude/Vault/11-runs/<slug-projeto>/AAAA-MM-DD-<slug>.md
```
Sem slug claro → `Vault/11-runs/sistema/AAAA-MM-DD-closeout-manual-<slug>.md`.
**Sem acesso ao Vault** → criar a run-note LOCAL no projeto (`Projects/<projeto>/_Areas/_closeouts/AAAA-MM-DD-<slug>.md`) e avisar no recibo: **"Vault pendente por falta de acesso"**.
A nota contém: contexto do trabalho · arquivos criados/alterados (caminhos exatos) · decisões · `FATO:`/`DELTA:` quando houver · pendências · **o que o próximo chat deve ler primeiro**. Frontmatter: `type: run, project: <slug>, valid_from: <data>, status: rascunho`.

## 5. Atualizar índice/ledger (quando SEGURO)
- `00_INDEX.md`: adicionar artefato novo importante (linha: caminho + o que tem + data).
- `_LEDGER.md`: 1 linha apontando pra run-note (`AAAA-MM-DD · closeout-manual · resumo · → run-note`).
- `LEARNINGS.md`/`BACKLOG.md`: só se houver aprendizado/pendência durável clara.

## 6. Fatos canônicos (cuidado)
Fato durável novo → registrar `FATO:` na run-note. Se seguro e não-sensível, criar/atualizar em `Vault/10-facts/<projeto>/`. **Se for estratégico/sensível (legal, financeiro, reputacional, equity, preço, posicionamento, identidade) → criar `fato-delta`/`pendente-validacao`, registrar o risco, e NUNCA sobrescrever o fato canônico antigo.** Nada de promoção automática — delta + risco sempre.

## 7. Verificar ANTES de responder
- Confirmar (ler de volta) que a run-note EXISTE no disco.
- Confirmar que `_LEDGER`/`00_INDEX` foram atualizados quando aplicável.
- Listar o que ficou pendente.
**Nunca dizer que gravou sem ter verificado o arquivo.**

## Formato de resposta (recibo)
```md
## Closeout executado

Projetos fechados:
- <Projeto> [+ outros, se houver]

Arquivos atualizados:
- <caminhos>

Run-note:
- <caminho exato>

Índice/ledger:
- atualizado / não aplicável / pendente

Fatos/deltas:
- FATO/DELTA: ... (ou "nenhum")

Pendências para próximo chat:
- ...
```

## Guardrails invioláveis
- Nunca dizer que gravou se não verificou o arquivo.
- Nunca sobrescrever fato canônico sensível sem registrar delta + risco.
- Nunca limitar o escopo a DopeStreet — sempre detectar o(s) projeto(s).
- **Não commitar/pushar.**
- **Não mover/deletar** arquivos sem pedido explícito.
- Sem acesso ao Vault → fallback local no projeto + avisar "Vault pendente".

## Relação com o reconciliador diário
Este é o fechamento **manual/imediato**. NÃO substitui o `Daily Global Project Closeout Reconciler` (rede de segurança das 23h). Um pega o que o outro deixou passar.
