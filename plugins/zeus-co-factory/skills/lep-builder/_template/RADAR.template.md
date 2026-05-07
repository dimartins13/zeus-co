# RADAR — {ROLE_NAME}

> Ferramentas, MCPs e connectors que este LEP usa, está avaliando, ou quer.
> Atualizado automaticamente pelo cron semanal do departamento.

## ✅ Instalados (em uso ativo)

Ferramentas que este LEP **invoca diretamente** durante operação.

| Ferramenta | Tipo | Pra que serve neste role |
|---|---|---|
| {nome} | MCP / plugin / API | {finalidade} |
| ... | ... | ... |

## 🔍 Avaliando (testado, decisão pendente)

Ferramentas em piloto. Após decisão, sobem pra "Instalados" ou descem pra "Wishlist" (se gap continua) ou "Descartado".

| Ferramenta | Status do teste | Próxima ação |
|---|---|---|
| {nome} | {testando em X empresa} | {decidir até quando} |

## 🎯 Wishlist (gap identificado, sem solução ainda)

Funções que o LEP precisaria fazer mas não tem ferramenta adequada.

| Gap | Ferramenta ideal (se conhecida) | Workaround atual |
|---|---|---|
| {função faltante} | {nome se existe} | {como o LEP contorna hoje} |

## 📅 Radar Semanal (novidades pendentes de avaliação)

Cron preenche essa seção. Diego revisa e move pra Avaliando ou descarta.

- [{data}] **{nome}** — {fonte da descoberta}. {1 frase do que é}. Próxima ação proposta: {avaliar / instalar direto / descartar}.

## 🚫 Descartados

Histórico do que foi avaliado e não serviu, com razão. Evita re-avaliar.

| Ferramenta | Quando descartado | Razão |
|---|---|---|
| {nome} | {data} | {1 frase} |

---

*Atualização semanal automática pelo cron `{departamento}-weekly`.*
*Última varredura manual: {data}.*
