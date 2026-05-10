# BREAK — Protocolo operacional (Quebrar / Desconstrução)

> Equivale a **Transformational Creativity** (Boden) — muda enabling constraints do espaço conceitual.
> SCAMPER: **Eliminate / Modify / Reverse**.
> Fundação cognitiva: Gärdenfors — adiciona/remove dimensões do espaço.

## Quando usar Break

- Briefing pede **disrupção** (não evolução)
- Mercado saturado, todos jogam pelas mesmas regras
- Pivot via quebra de premissa central
- Reduzir complexidade de produto via remoção (não adição)
- "E se a gente removesse [X] que todo mundo considera obrigatório?"
- "E se invertêssemos o jeito que isso acontece?"
- Repensar processo/SOP/operação (uso COO)

## Quando NÃO usar Break

- Briefing pede algo familiar com twist — use Bend
- Briefing pede combinação de coisas existentes — use Blend
- Stakeholders avessos a risco — Break é o vetor mais arriscado (pode gerar zero valor)

## Protocolo (10 passos)

### 1. Recebe briefing e extrai núcleo
- O que é o produto/conceito/processo a quebrar?
- Qual a forma atual (estrutura, partes, sequência)?

### 2. Lista enabling constraints (Boden)
Toda solução nesse domínio assume O QUÊ?

Faz lista explícita de 5-10 assunções. Ex. para "loja de roupa":
- Assume **loja física**
- Assume **estoque próprio**
- Assume **temporadas (verão/inverno)**
- Assume **tamanhos padronizados (P/M/G)**
- Assume **vendedor humano no atendimento**
- Assume **devolução possível**
- Assume **provador físico**
- Assume **caixa registradora**

### 3. Aplica 3 técnicas Break × cada constraint = quantas combinações forem

#### Técnica A — ELIMINATE (SCAMPER E)
Remove constraint. "E se [X] simplesmente não existisse?"
- Ex: "Loja sem estoque próprio" → drop-shipping, marketplace
- Ex: "Loja sem provador físico" → AR try-on, retornos infinitos

#### Técnica B — MODIFY DIMENSION
Pega uma dimensão (tamanho, frequência, duração, formato) e modifica radicalmente.
- Ex: "Loja com 1 peça de cada modelo (não estoque) — leilão"
- Ex: "Loja aberta só 3 dias por mês"
- Ex: "Loja onde cada peça muda de dono a cada 6 meses (revenda integrada)"

#### Técnica C — REVERSE (SCAMPER R)
Inverte fluxo, papel, ordem ou polaridade.
- Ex: "Cliente entrega peça, marca fabrica" (reverso do estoque-primeiro)
- Ex: "Marca paga cliente pra usar (reverso de cliente paga marca)"
- Ex: "Lançamento começa com edição limitada, sucesso = scale" (reverso do tradicional)

### 4. Gera 3-5 ideias mais radicais
Cada ideia carrega:
- **Constraint quebrada**: qual assunção foi removida/modificada/invertida
- **Espaço novo**: que regras o novo espaço tem (R' = R - {ri} + {r'i})
- **Distância semântica estimada** (4-5 típico — Break é o mais distante)

### 5. Stress-test de viabilidade
Break é arriscado. Pra cada ideia:
- **Hipótese de valor**: por que isso vale a pena? Quem ganha?
- **Hipótese de viabilidade**: pode operacionalizar? Que recurso/skill exige?
- **Hipótese de desejabilidade**: alguém quer isso? Não-óbvio = também pode ser não-desejado.
- **Modo de falha óbvio**: como isso quebra? (use Pre-Mortem)

### 6. Filtra
Mantém só ideias que passam stress-test em valor + viabilidade (desejabilidade é hipótese a testar).

### 7. Rankeia
Top 3 por **distância × atende necessidade × viabilidade**.

### 8. Rationale neuro inline
"Break do enabling constraint [X]. Resultado: espaço novo onde [Y]. Distância semântica 5/5."

### 9. Identifica precedentes
Pra cada Break, busca no corpus: "alguém já quebrou assunção similar em outro setor?" Liga ao precedente — dá tração pra defender.

### 10. Próximos Movimentos
Sempre incluir **teste de hipótese de desejabilidade** — Break sem validação é fé, não estratégia. Sugerir MVP mínimo de teste pra cada ideia.

## Exemplos resolvidos

### Exemplo 1 — Briefing: "Repensar modelo 2ndStreet (revenda streetwear celebrity)"

**Assunções listadas:**
- Assume curadoria centralizada
- Assume autenticação por sócios celebrity
- Assume marketplace típico (vendedor lista, comprador escolhe)
- Assume preço fixo
- Assume entrega após pagamento
- Assume "usado" como inferior

**Break A (Elimine "curadoria centralizada")**: 2ndStreet vira **plataforma de leilão peer-to-peer** com autenticação automática AI + Akkari spot-check só nos top 10% de valor. Distância 4/5.

**Break B (Reverse "usado é inferior")**: 2ndStreet vira **"NEYMARO VINTAGE"** — usar Neymar passou a ser status > comprar novo. Distância 5/5. Quebra de assunção cultural.

**Break C (Modify "preço fixo" → "preço dinâmico cultural")**: Peças sobem de preço com cada celebridade que usa publicamente. Distância 5/5. Reverso do mercado físico de luxo.

### Exemplo 2 — Briefing: "Repensar SOP de fechamento mensal (Dash Financeiro)"

**Assunções:**
- Assume fechamento no fim do mês
- Assume agrega tudo em 1 relatório
- Assume revisão sequencial (categoria por categoria)
- Assume aprovação humana de cada item

**Break A (Modify "fim do mês" → "fluxo contínuo")**: fechamento incremental diário — fim do mês é apenas snapshot. Distância 4/5.

**Break B (Eliminate "relatório agregado")**: cada categoria virou stream próprio com alerta on-anomaly. Sem "relatório mensal" — só alertas e dashboard live. Distância 5/5.

## Erros comuns em Break

1. **Quebrar coisa errada** — assunção quebrada não era central. Mudou nada.
2. **Quebrar coisa essencial** — produto vira não-produto. Ex: "loja sem produto" = não é loja.
3. **Não testar desejabilidade** — Break parece genial mas ninguém quer. Mercado pune Break não validado.
4. **Confundir Break com Bend** — Break muda regra do espaço. Bend muda contexto preservando regra. Se ainda é "a mesma coisa em outro contexto", é Bend, não Break.

## Output canônico esperado

```markdown
## Break — [Resumo do desafio em 1 linha]

### Ideia 1: [Nome curto]
- **Constraint quebrada**: [assunção fundadora removida/modificada/invertida]
- **Espaço novo**: [como o novo espaço funciona]
- **Distância semântica**: X/5
- **Defesa neuro**: [1 frase]
- **Precedente cross-setor**: [quem já fez Break similar em outro lugar]
- **Hipótese de desejabilidade a testar**: [MVP mínimo]
- **Modo de falha óbvio**: [como isso pode dar errado]
- **Próximos Movimentos**: 1) ... 2) ... 3) ...

[repetir pra ideia 2 e 3]
```
