# Hofstadter — Slipnet, Copycat e arquitetura cognitiva pra analogia (Bend formal)

> **Origem:** Douglas Hofstadter + Melanie Mitchell + Fluid Analogies Research Group (FARG), Indiana University. Hofstadter é autor de *Gödel, Escher, Bach* (1979) e *Fluid Concepts and Creative Analogies* (1995).

## Tese central

> "Analogia não é uma habilidade entre outras — é o núcleo da cognição."

Hofstadter argumenta que **toda criatividade é, em última instância, analogia** — fazer-A-parecer-com-B sob restrições. O laboratório FARG construiu múltiplos sistemas pra modelar isso computacionalmente: Copycat, Letter Spirit, Phaeaco, Tabletop, Numbo, Seeqsee.

## Copycat — arquitetura tripartite

Domínio de Copycat: analogias com sequências de letras. Ex: *"abc → abd; ijk → ?"* — a resposta criativa não é "ijd" (literal) nem "ijl" (sucessor da última) mas algo que captura a **regra abstrata** ("substitua o último por seu sucessor").

A arquitetura tem 3 componentes:

### 1. SLIPNET — rede de conceitos com pesos

Estrutura: grafo de **nodes** (conceitos como "letter", "successor", "leftmost") conectados por **links com pesos**. Cada node tem **nível de ativação** que varia em runtime.

**Mecânica:**
- Quando um node ativa, espalha ativação pelos vizinhos proporcional ao peso do link
- Nodes próximos no slipnet são "facilmente confundíveis" (slip = deslize)
- Nodes distantes requerem mais processamento pra conectar

**Por que importa pro Bend:** o slipnet é literalmente um modelo de **sinapses formalizadas** — conexões com peso. Diego apontou que skill precisa de "substrato sináptico". Slipnet É esse substrato.

### 2. WORKSPACE — área de trabalho

Onde a analogia parcial vai sendo construída. Estruturas (bonds entre letras, grupos, correspondências) emergem aqui. Workspace pode reorganizar conforme processamento avança.

### 3. CODERACK — agentes paralelos (codelets)

Pequenos processos que rodam em paralelo, cada um propondo/avaliando estrutura no workspace. Probabilísticos: codelets de alta prioridade rodam mais. Comportamento emerge do conjunto.

## Princípios FARG (aplicáveis sem rodar o código)

Mesmo sem implementar runtime simbólico Copycat, podemos extrair princípios:

1. **Conceitos são fluidos** — significado depende do contexto, não é fixo. Mesmo conceito ativa diferente em situações diferentes.

2. **Sinapses têm peso** — algumas conexões são fortes (letter↔alphabet), outras fracas (letter↔mountain). Criatividade explora as fracas.

3. **Pressão de coerência + pressão de surpresa** — sistema busca analogia que seja **estruturalmente sólida** (coerência) e **não-óbvia** (surpresa). Tensão entre os dois.

4. **Slippage controlado** — deixar um conceito "deslizar" pra outro próximo no slipnet (letter→successor→sucessor). Erros virtuosos.

5. **Bottom-up + top-down simultâneo** — codelets bottom-up (notar padrões) e top-down (impor hipóteses) competem. Sem hierarquia rígida.

## Implementações open-source (referências)

Repos vivos pra inspirar nossa skill (sem necessariamente integrar runtime):

- **[github.com/fargonauts/copycat](https://github.com/fargonauts/copycat)** — port Python moderno (~5000 LOC). Mantenedores: Lucas Saldyt + J. Alan Brogan.
- **[github.com/Paul-G2/copycat-js](https://github.com/Paul-G2/copycat-js)** — JS port (2023). Mais acessível pra rodar no browser.
- **[github.com/Alex-Linhares/FARGonautica](https://github.com/Alex-Linhares/FARGonautica)** — coleção de arquiteturas FARG + literatura.
- **[github.com/eraoul/Fluid-Concepts-and-Creative-Analogies](https://github.com/eraoul/Fluid-Concepts-and-Creative-Analogies)** — projeto baseado em múltiplos sistemas do livro.

## Aplicação na skill `cerebro-criativo`

**NÃO vamos rodar Copycat real** (requer runtime simbólico que LLM não tem direto). Vamos incorporar **3 princípios estruturais**:

### Princípio 1 — Slipnet como corpus estruturado

Nosso `corpus/slipnet.md` é uma representação textual de slipnet:
- Lista nodes (conceitos centrais por domínio)
- Lista links com pesos qualitativos (forte/médio/fraco)
- Skill consulta antes de gerar pra ativar nodes distantes

### Princípio 2 — Slippage controlado em geração

Quando puxa um conceito, deixa "deslizar" pra vizinho próximo (synonyms, hyponyms, antonyms). Isso é exatamente como o cérebro associa.

### Princípio 3 — Pressão dupla (coerência + surpresa)

Cada ideia gerada é avaliada em 2 eixos:
- **Coerência** — faz sentido estrutural? (princípios Fauconnier-Turner)
- **Surpresa** — está distante do óbvio? (distância semântica Beaty)

Top ideias maximizam ambos.

## Crítica e limites

- Copycat só opera em domínio de letras — generalização pra outros domínios é desafio aberto
- FARG architectures não escalam pra conhecimento amplo do mundo (LLMs hoje fazem isso melhor)
- **Mas** a arquitetura cognitiva continua relevante como **prescritor de estrutura** pra raciocínio criativo

## Refs canônicas

- Hofstadter, D. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid.* Basic Books — fundação.
- Hofstadter, D. & FARG (1995). *Fluid Concepts and Creative Analogies.* Basic Books — Copycat e outros sistemas.
- Mitchell, M. (1993). *Analogy-Making as Perception.* MIT Press — tese PhD sobre Copycat.
- Hofstadter, D. & Sander, E. (2013). *Surfaces and Essences: Analogy as the Fuel and Fire of Thinking.* Basic Books.
- [Wikipedia "Copycat (software)"](https://en.wikipedia.org/wiki/Copycat_(software))
- [HofstadterianArchitecture notes](https://notes.fringeling.com/HofstadterianArchitecture/)
