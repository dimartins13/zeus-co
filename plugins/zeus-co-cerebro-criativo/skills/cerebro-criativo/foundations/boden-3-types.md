# Boden — 3 Types of Creativity (Taxonomia formal)

> **Origem:** Margaret Boden, *The Creative Mind: Myths and Mechanisms* (1990, revisado 2004). Boden é filósofa cognitiva da Universidade de Sussex, pioneira em IA + criatividade.

## Tese central

Criatividade não é um fenômeno único. São **três operações cognitivas distintas**, cada uma com mecânica formal própria. Confundir as três = não conseguir replicar nenhuma.

> "Creativity is the ability to come up with ideas or artefacts that are new, surprising, and valuable."

Boden distingue ainda:
- **P-creativity** (psicológica) — nova pro indivíduo
- **H-creativity** (histórica) — nova pra toda a humanidade

E formaliza 3 mecanismos:

## Tipo 1 — Combinatorial Creativity (Combinatorial)

**Definição:** combina ideias **familiares** de formas não-familiares.

**Mecânica formal:** dado conjunto de conceitos {A, B, C, D, ...}, gera novos pares ou n-uplas {(A,B), (A,D), (B,C,F), ...} que não existiam antes.

**Espaço conceitual:** o conjunto base não muda — só as combinações.

**Exemplos Boden:**
- Metáfora poética ("a vida é uma jornada")
- Colagem dadaísta
- Mashup musical

**Limite:** não cria conceitos novos — recombina os existentes.

**Equivale a:** **Blend** (Eagleman) / **Combine** (SCAMPER)

## Tipo 2 — Exploratory Creativity

**Definição:** opera **dentro de um espaço conceitual estabelecido**, explorando suas bordas e descobrindo possibilidades antes não percebidas.

**Mecânica formal:** dado um espaço conceitual com regras R = {r1, r2, r3, ...}, gera artefatos que respeitam R mas ocupam regiões antes não habitadas do espaço.

**Espaço conceitual:** as REGRAS não mudam. A exploração se expande dentro delas.

**Exemplos Boden:**
- Mozart explorando sonatas dentro das regras do classicismo
- Jazz tradicional dentro das regras harmônicas estabelecidas
- Picasso início (período azul) — explorando dentro das regras do impressionismo

**Limite:** sempre haverá fronteiras do espaço — pra escapar precisa Tipo 3.

**Equivale a:** **Bend** (Eagleman) / **Substitute / Adapt / Put-to-other-uses** (SCAMPER)

## Tipo 3 — Transformational Creativity

**Definição:** muda as **regras** do espaço conceitual. Quebra ou modifica uma assunção fundadora (enabling constraint) do domínio.

**Mecânica formal:** dado espaço com regras R = {r1, r2, r3, ...}, modifica/remove/inverte ri pra criar espaço novo R' = {r1, ¬r3, r4, ...}.

**Espaço conceitual:** muda. O depois é incomensurável com o antes.

**Exemplos Boden:**
- Picasso cubismo — quebrou regra "perspectiva única" do Renascimento
- Schoenberg dodecafonismo — quebrou regra "tonalidade" da música ocidental
- Einstein relatividade — quebrou regra "tempo absoluto" da física newtoniana
- Duchamp ready-made — quebrou regra "arte = objeto feito pelo artista"

**Limite:** raro, alto risco (a quebra pode não gerar valor — só novidade).

**Equivale a:** **Break** (Eagleman) / **Eliminate / Modify / Reverse** (SCAMPER)

## Convergência com Eagleman/SCAMPER

| Boden | Eagleman | SCAMPER | O que muda |
|---|---|---|---|
| Exploratory | Bend | S, A, P | Posição no espaço |
| Transformational | Break | E, M, R | Regras do espaço |
| Combinatorial | Blend | C | Combinação fora do espaço |

Essa **convergência tripla** é fundação da skill — não estamos inventando framework, estamos unificando 3 famílias da literatura.

## Aplicação em IA / LLM (relevante 2024-2026)

Paper **"LLMs Can Realize Combinatorial Creativity"** (arxiv 2412.14141) propõe agente com 2 componentes:
1. **Generalization-level retrieval** — busca conceitos em níveis de abstração distintos
2. **Structured combinatorial process** — recombina sistematicamente

Resultado: +7-10% no benchmark OAG-Bench. Isso confirma que **agentes LLM se beneficiam de estrutura cognitiva formal Boden-style** vs. prompts genéricos "seja criativo".

## Implicações pra skill `cerebro-criativo`

1. **3 tipos = 3 protocolos distintos**, não gradação. Cada um tem entry point próprio em `operations/`.

2. **Transformational é o mais arriscado** — quebrar regra do espaço pode gerar nada de valor. Skill marca explicitamente "Atenção: Break atinge enabling constraint X — viabilidade requer validação humana".

3. **Combinatorial é o mais seguro** — combina dentro do conhecido. Bom pra ideação inicial.

4. **Exploratory é o mais frequente** — recontextualização é o trabalho de marca/marketing cotidiano.

5. **Generalization-level retrieval** (arxiv 2412.14141) inspira nosso algorithm `generalization-retrieval` — buscar corpus em níveis de abstração, não match exato.

## Refs canônicas

- Boden, M. (2004). *The Creative Mind: Myths and Mechanisms* (2nd ed.). Routledge.
- Boden, M. (2009). "Computer Models of Creativity." *AI Magazine* 30(3).
- Boden, M. (2018). *Artificial Intelligence: A Very Short Introduction.* Oxford UP.
- arxiv 2412.14141 (2024) — *LLMs Can Realize Combinatorial Creativity*. Mapping Boden → LLM.
- The Marginalian (2025) — "Decoding the Mystery of Intuition: Pioneering Philosopher of AI Margaret Boden on the Three Elements of Creativity"
