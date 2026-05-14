# Padrão 02 · Critique de 5 Dimensões

Antes de entregar qualquer peça, o agente roda um **self-critique** em 5 eixos.
Se algum eixo falha, itera. Se passa, entrega.

## As 5 dimensões

### 1. **Philosophy** — A peça tem ponto de vista?
- A peça toma uma posição visual clara, ou é "design seguro" sem alma?
- O conceito está coerente do briefing à execução?
- Existe uma razão de ser para cada decisão estética?

### 2. **Hierarchy** — A informação se organiza?
- O olho sabe onde começar?
- A escala tipográfica tem 3+ níveis distintos (não 5+ confusos)?
- O contraste entre primário/secundário/terciário é nítido?
- Whitespace está fazendo trabalho ou só sobrando?

### 3. **Detail** — Os pequenos toques estão lá?
- Letter-spacing nos display sizes ajustado?
- Bordas, cantos, shadows seguem um sistema (não cada um diferente)?
- Microcopy, captions, metadados estão tratados (não esquecidos)?
- Alinhamentos batem em pixel ou estão "quase"?

### 4. **Function** — A peça serve seu propósito?
- Deck: o slide passa a mensagem em 5 segundos?
- LP: o CTA está claro? O caminho até ele é desimpedido?
- KV: a marca é reconhecível? A oferta é clara?
- Vídeo: os 3 primeiros segundos prendem?

### 5. **Innovation** — Tem algo memorável?
- Existe pelo menos UMA decisão que não é genérica?
- A peça vai parecer datada em 6 meses ou tem timing certo?
- Algo arriscou, ou tudo é "best practices" replicadas?

## Como aplicar

```
Após qualquer produção, antes de entregar:

1. Pontue de 1 a 5 cada dimensão.
2. Se alguma < 3, identifique O QUE especificamente está fraco.
3. Itere SÓ aquela dimensão (não refaça tudo).
4. Re-pontue.
5. Quando todas ≥ 3 (ou ≥ 4 para peça de cliente top), entregue.
```

## Quando ignorar (raro)

- Brief explícito de "rascunho rápido, não polir": pular 4 e 5, manter 1, 2, 3.
- Wireframe técnico interno: pular 1 e 5, manter 2, 3, 4.
- **Nunca pular dimensões 2 (Hierarchy) e 3 (Detail).** São o piso.

---

**Fonte:** `apps/daemon/src/prompts/system.ts` (critique loop) +
inspirado no framework de @smixs (`creative-director-skill`)
