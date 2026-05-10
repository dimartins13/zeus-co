# Gärdenfors — Conceptual Spaces (Geometria do pensamento)

> **Origem:** Peter Gärdenfors, *Conceptual Spaces: The Geometry of Thought* (2000), MIT Press. Filósofo cognitivo da Lund University, Suécia.

## Tese central

> "Conceitos podem ser representados como **regiões em espaços geométricos multidimensionais**, onde cada dimensão é uma qualidade perceptual ou abstrata."

Gärdenfors propõe um **terceiro nível** entre símbolo (Fregeano) e conexionismo (redes neurais) — o nível **geométrico**, onde:
- Conceitos = regiões convexas num espaço multidimensional
- Cada dimensão = uma qualidade (cor, tamanho, peso, urgência, formalidade, etc)
- Distância entre conceitos = similaridade
- Centroide = exemplar protótipico

## Exemplo simples — espaço "frutas"

Dimensões: doçura, tamanho, cor (saturação), acidez, umidade

- "Limão" = região com alta acidez + média umidade + cor amarela + tamanho pequeno
- "Melancia" = região com alta doçura + alta umidade + tamanho grande + cor vermelha
- Distância(limão, melancia) = grande → conceitos distantes

## Conexão com embeddings modernos (word2vec, BERT, GPT)

A teoria foi formulada antes dos embeddings neurais, mas eles a confirmam empiricamente:
- Cada palavra/conceito vira **vetor de N dimensões** (300-1500 típico)
- Distâncias coseno/euclidianas no espaço refletem similaridades semânticas
- Operações vetoriais clássicas: `king - man + woman ≈ queen`

**Implicação:** todo LLM moderno opera num conceptual space implícito. Skill pode aproveitar isso explicitamente — quando geramos ideias, conscientemente forçamos **distância máxima** entre conceitos no embedding space.

## Aplicação a criatividade (Chella & Gaglio 2014)

No paper **"Creativity in Conceptual Spaces"** (ICCC 2014), Chella e Gaglio mostram que:
- Combinatorial creativity = nova combinação de regiões existentes no espaço
- Exploratory creativity = ocupar região antes vazia do espaço
- Transformational creativity = adicionar/remover dimensões do espaço

Isso mapeia perfeito no nosso framework Boden + Eagleman:
- Blend = combinar regiões distantes → emergência
- Bend = ocupar nova região (recontextualizar)
- Break = mudar dimensões (transformar espaço)

## Implicações pra skill `cerebro-criativo`

### 1. Distância semântica como métrica de originalidade

Diretamente conectado a Beaty/SemDis (próximo arquivo). Originalidade = distância no espaço conceitual. Skill mede e maximiza essa distância.

### 2. Dimensões explícitas por domínio

Cada léxico cross-domain em `corpus/lexicons/` tem dimensões explícitas:
- **Música:** ritmo, intensidade, dissonância, registro, instrumento, andamento
- **Arquitetura:** material, escala, simetria, luz, fluxo, tempo (idade)
- **Biologia:** escala, metabolismo, ciclo de vida, simbiose, mutação, ambiente
- **Etc.**

Quando puxamos do léxico, escolhemos **dimensões análogas** ao desafio — slippage controlado pelo espaço.

### 3. Convexidade = coerência

Regiões convexas no espaço de Gärdenfors representam conceitos coerentes. Quando Blendamos, queremos que o blend ocupe **região convexa** — não pontos desconexos. Princípio "Integration" de Fauconnier-Turner = convexidade aqui.

### 4. Centroide = protótipo

Quando o briefing diz "marca de moda", o centroide é "Nike/Apple/Zara". Skill **evita o centroide** — busca regiões da margem que ainda são reconhecíveis como "marca de moda".

## Aplicação prática — exemplo Zeus-CO

**Briefing:** "Big idea TarjaPreta (app saúde mental)"

**Espaço conceitual implícito:**
- Dimensões: estigma, formalidade clínica, intimidade, acessibilidade, urgência, gravidade
- Centroide (óbvio): "app calminho com voz suave"
- Margens (criativo): "app que parece thriller psicológico" / "app com estética religiosa" / "app que confronta antes de acolher"

Skill prefere margens. Distância no espaço = originalidade.

## Refs canônicas

- Gärdenfors, P. (2000). *Conceptual Spaces: The Geometry of Thought.* MIT Press.
- Gärdenfors, P. (2014). *The Geometry of Meaning: Semantics Based on Conceptual Spaces.* MIT Press.
- Chella, A. & Gaglio, S. (2014). "Creativity in Conceptual Spaces." ICCC 2014 paper.
- Bechberger, L. & Kühnberger, K-U. (2022). "Integrating Ontologies and Vector Space Embeddings Using Conceptual Spaces." Dagstuhl OASIcs.
- [MIT Press Conceptual Spaces book page](https://mitpress.mit.edu/9780262572194/conceptual-spaces/)
