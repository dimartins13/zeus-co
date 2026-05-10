# AMPLIFICADOR — Distância Semântica (Métrica + Força geração)

> Criatividade não é vibe, é **distância no espaço conceitual**. Quanto mais distante a ideia do prompt, mais original (Beaty & Johnson 2021, SemDis). Skill **mede e força** essa distância.

## Princípio matemático

Dado um espaço semântico multidimensional E (Gärdenfors conceptual spaces, materializado em embeddings modernos):

```
Originalidade(ideia | prompt) = distância(vetor(ideia), vetor(prompt))
```

Onde:
- Vetor de cada conceito é representação de N dimensões (300-1500 em modelos modernos)
- Distância pode ser coseno, euclidiana, ou Manhattan
- Quanto maior, mais distante = mais original

**Insight crucial:** o cérebro humano opera num espaço semântico implícito desde o nascimento, refinado por experiência. Modelos de linguagem aprenderam esse espaço por proxy (vendo texto). Skill explora o espaço **conscientemente**.

## Como skill aplica em runtime (sem cálculo numérico real)

Skill não tem acesso direto a embeddings em runtime de prompt. Aproxima através de **avaliação reflexiva** disciplinada:

### Score 1-5 de distância semântica

| Score | Critério | Exemplo (briefing: "marca de moda") |
|---|---|---|
| **1** | Vocabulário do briefing repetido literalmente | "Marca de moda jovem urbana" |
| **2** | Variação do óbvio, mesma família | "Marca de roupa premium feita pra cidade" |
| **3** | Movimento lateral, ainda no setor | "Marca de moda que mistura roupa + acessório + colecionável" |
| **4** | Ângulo de domínio adjacente | "Marca de moda como label de música indie" |
| **5** | Cross-domain forte, surpresa estrutural | "Marca de moda como ordem religiosa secreta com hierarquia de iniciação" |

### Heurísticas pra estimar score

#### Sinais de score 1-2 (BAIXO — ruim)
- Usa as mesmas palavras do briefing como núcleo
- Concorrência direta já faz algo parecido
- "Faz sentido na primeira leitura sem ler 2x"

#### Sinais de score 3 (MÉDIO — aceitável mas não criativo)
- Movimento dentro do espaço, sem mudar dimensões
- Usa vocabulário do setor mas reorganizado
- "Faz sentido depois de pensar 5 segundos"

#### Sinais de score 4-5 (ALTO — criativo)
- Importa vocabulário de outro domínio
- Provoca reação "espera, como assim?"
- Coerente sob reflexão, mas não óbvio em 1ª leitura
- Tem propriedade emergente (não-decompúvel em "X + Y")

## Como forçar distância durante geração

### Técnica 1 — Cross-domain mandatório
Skill sempre puxa 2+ domínios distantes (`corpus/lexicons/`). Generation prompts incorporam vocabulário desses domínios.

### Técnica 2 — Inversão de centroide
Se centroide óbvio do espaço = "X", skill explicitamente **se proíbe** de propor algo no centroide. Lista 3 abordagens centroide → marca como "evitar".

### Técnica 3 — Anti-prompt
Skill gera **anti-ideia primeiro** ("a coisa mais óbvia e morna que existe pra esse briefing") — depois gera ideia que está semanticamente OPOSTA à anti-ideia.

### Técnica 4 — Generalization-level retrieval (arxiv 2412.14141)
Busca cases em **níveis de abstração distintos** do briefing.
- Briefing nível 0: "marca de moda"
- Nível 1: "marca de produto desejado"
- Nível 2: "símbolo de status cultural"
- Nível 3: "marcador de pertencimento tribal"
- Skill puxa cases nos níveis 2-3 (distantes), não nível 0.

## Stress-test SemDis (auto-avaliação)

Após gerar ideias, skill executa stress-test:

```
PARA CADA IDEIA:
  1. Estimar score distância (1-5)
  2. Se score < 3:
     - Marcar "BAIXA ORIGINALIDADE" no output
     - Sugerir variação cross-domain
  3. Se score 4-5:
     - Validar coerência (Fauconnier-Turner 5 princípios)
     - Se não passa coerência → reduzir score (distância sem valor)
  4. Apresentar score numérico no output
```

## Trade-off Originalidade × Valor

**Crítica importante:** distância sozinha não basta.

Exemplo absurdo: pra "marca de moda", a ideia "marca que vende ar embalado" tem distância 5/5 mas **valor 0** — ninguém quer.

Skill avalia **dois eixos**:
- **Originalidade** (proxy SemDis) — distância 1-5
- **Coerência/Valor** (princípios Fauconnier-Turner + stress-test) — 1-5

Top ideias maximizam **soma ponderada**:
```
Score_total = α × Originalidade + β × Coerência
```
Onde α=0.6 e β=0.4 (distância importa mais, mas coerência é gate).

## Output marca distância sempre

No output canônico, cada ideia carrega:
- "Distância semântica: 4/5" — visível ao requester
- Permite Diego escolher entre "ideia segura 3/5" ou "ideia arriscada 5/5"
- Não esconde — skill é transparente sobre própria avaliação

## Referência empírica externa (validação)

Diego pode validar empiricamente usando:
- **[semdis.wlu.psu.edu](https://semdis.wlu.psu.edu)** — calculadora SemDis (Beaty Lab)
- **[Open Creativity Scoring](https://openscoring.du.edu)** — Dumas et al.
- Plug prompt + resposta → score numérico real
- Comparar com auto-avaliação da skill — refinar calibração

## Princípio inviolável

**Skill nunca apresenta ideia sem score de distância semântica.** Marca sempre. Diego/requester precisa saber a "voltagem criativa" de cada candidata pra escolher informado.
