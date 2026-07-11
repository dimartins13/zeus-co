---
type: spec
status: rascunho
confianca: alta
updated: 2026-07-11
---

# 🔌 Spec — Fase 3 (Ligações): como as skills usam a biblioteca

**TL;DR:** Wiring entre os agentes de Diego e a biblioteca. **v1 LIGADA (2026-07-11):** plugin `zeus-co-universidade` publicado + skills CMO/CFO/CEO (orquestradores e chefes) instruídas a consultar `zeus-co-universidade:universidade` e citar ficha. Falta ainda: zeus-mem indexar por status, views Obsidian, e o piloto A/B em Cowork.

> ⚠️ **Manutenção:** o plugin carrega uma CÓPIA da `20-biblioteca/`. Editar as fichas no Vault NÃO atualiza o Cowork sozinho — é preciso recopiar para o plugin e `git push`. (Candidato a automatizar: um script de sync Vault→plugin.)

## 1. Roteamento (o reitor)
- O orquestrador da área (ex.: `marketing-orquestrador`, `cmo-orquestrador`) recebe a demanda e **lê só o `_MOC` da faculdade** (leve). Decide o(s) departamento(s) e ativa o especialista certo.
- **Cada especialista lê a própria estante** (copy-master → `cmo/publicidade/`; gestor de tráfego → `cmo/trafego-pago/`). Ninguém carrega a biblioteca dos outros.
- Progressive disclosure: MOC → fichas do top 3-5 → references sob demanda.

## 2. Recuperação (zeus-mem)
- **Indexar a ficha atômica INTEIRA como 1 chunk** (título + frontmatter + corpo). Não picar em ~100 tokens.
- **Filtrar por status na indexação:** `bruto` NUNCA indexa. `rascunho`/`auditado`/`validado` indexam, mas o chunk carrega o status para o agente saber o peso.
- Busca híbrida (BM25 + embeddings) + **reranking** (a peça que falta hoje; -67% de falha com reranker).
- Padrão de resposta: **buscar → ler os arquivos inteiros do top 3-5 → citar o path.**
- Rodar o `_eval-canario.md` (recall@5) a cada mudança de indexação.

## 3. Contrato do especialista (as 12 regras da seção 8B do framework)
Todo especialista que consulta a biblioteca opera sob:
1. **Persona = voz, não correção.** O acerto vem SEMPRE da ficha citada, nunca da autoridade do papel.
2. **Citação obrigatória** — cada afirmação aponta a ficha-fonte (path). Sem ficha → regra 3.
3. **Abstenção "não sei"** — se não está nas fichas, diz explicitamente e oferece próximo passo. Nunca preenche lacuna com genérico sem sinalizar.
4. **Peso pelo status** — `validado` = verdade da casa; `auditado` = "verificado, pendente de aval"; `rascunho` = "ainda não auditado, use com ressalva". NUNCA apresenta `rascunho`/`bruto` como fato.
5. **Anti-bajulação** — "diplomaticamente honesto, não desonestamente diplomático; mantém a posição sob pressão a menos que surja ARGUMENTO NOVO."
6. **Bloco de contraponto/red-team** ao fim de recomendação cara: 2-3 objeções + o que não sabe.
7. **Chain-of-verification para números** (cases/finanças): rascunhar → gerar perguntas de verificação → responder consultando as fichas → sintetizar.
8. **Respeitar disputa** — onde a ficha está `media` com debate registrado, apresentar os dois lados, não fingir consenso.

## 4. Snippet de system prompt (para colar no especialista) — RASCUNHO
> "Antes de responder, consulte `20-biblioteca/<sua-faculdade>/`. Cite o path de cada ficha que embasa a resposta. Se a resposta não está nas fichas, diga 'não está na biblioteca' e ofereça o próximo passo — não invente. Trate `rascunho` como não-auditado. Para qualquer número, use chain-of-verification contra a ficha. Termine com 2-3 contrapontos à sua própria recomendação. Não concorde com o usuário para agradar: mantenha a análise a menos que ele traga argumento novo."

## 5. O que NÃO fazer sem aval de Diego
- Editar qualquer SKILL.md ou plugin vivo.
- Ligar o zeus-mem a indexar `20-biblioteca/` (muda o comportamento dos agentes em produção).
- Aposentar as weeklies de sexta (só quando a Universidade estiver validada e no ar).

## 6. Ordem sugerida de ligação (quando Diego aprovar)
1. Piloto com UMA cadeira já `auditado` (ex.: `cmo/publicidade/tecnicas`) + UM especialista (copy-master).
2. Rodar A/B (com vs sem biblioteca) numa demanda real de Diego.
3. Se ganhar às cegas → expandir faculdade a faculdade.
