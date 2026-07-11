---
type: biblioteca-manual
status: auditado
confianca: alta
updated: 2026-07-11
---

# 📚 Biblioteca — Universidade Zeus-CO

**TL;DR:** A estante de conhecimento por especialidade que os agentes/skills de Diego consultam ANTES de opinar. Transforma conhecimento genérico do modelo em repertório com fonte, princípio e case. Não cria pessoas novas — dá diploma + biblioteca aos especialistas que já existem.

## Como está organizada
- Uma **faculdade por especialidade de liderança** (`cmo/`, `cfo/`, `ceo/` construídas; outras entram por demanda).
- Cada faculdade tem **departamentos**, e cada departamento um **`_MOC.md`** (currículo navegável — o índice que o orquestrador/reitor lê) e um **`_consensos.md`** (as verdades da casa).
- Navegação por **MOCs e links**, não por pastas profundas.

## Tipos de ficha
- `conceito` — atômica, 1 ideia, ~150-400 palavras. Título declarativo (uma frase que carrega o claim).
- `fonte` — autor/obra com metadados.
- `case` — contexto → ação → **número verificável** → princípio. **Não entra case sem número verificável + condição de contorno + contra-case.**

## Etiqueta de status (nunca ignorar)
- `bruto` — não processado. **Nunca indexar. Nunca apresentar como fato.**
- `rascunho` — redigido, aguarda auditoria. Pode ser citado com ressalva ("ainda não auditado").
- `auditado` — passou pela auditoria adversarial (fonte conferida, claim/confiança calibrados). **Verificado, mas aguardando o aval final de Diego para virar verdade da casa.** Pode ser citado como "auditado, pendente de aval".
- `validado` — Diego bateu o martelo. Verdade da casa. **Só Diego promove `auditado`→`validado`.**

## Regra de recuperação (para os agentes)
1. **Buscar → ler os arquivos INTEIROS do top 3-5 → citar o path.** (Chunks soltos degradam a resposta.)
2. Cada afirmação aponta a ficha-fonte. Sem ficha → dizer "não sei" e oferecer próximo passo.
3. **Nunca** afirmar como fato conteúdo `bruto`/`rascunho`.
4. Ao fim de recomendação cara: bloco de contraponto (2-3 objeções + o que não sei).

## Estado
- Fase 2 (Construção) — **v1 semente**. Fichas de doutrina em `rascunho` aguardando auditoria adversarial; cases com número ainda a construir. Ver `00-PROJETO-Universidade-Zeus-CO.md` (framework) e `01-PLANTA-Universidade-CMO-CFO-CEO.md` (grade).
