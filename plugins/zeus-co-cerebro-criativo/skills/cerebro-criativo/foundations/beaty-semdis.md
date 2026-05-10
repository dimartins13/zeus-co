# Beaty & Johnson — SemDis (Métrica matemática de originalidade)

> **Origem:** Roger Beaty (Penn State, Beaty Lab) + Dan R. Johnson (Washington and Lee). Plataforma SemDis lançada 2021.
> Paper-chave: Beaty, R. E., & Johnson, D. R. (2021). "Automating creativity assessment with SemDis: An open platform for computing semantic distance." *Behavior Research Methods*, 53, 757–780.

## Tese central

> "Originalidade pode ser **medida matematicamente** pela distância semântica média entre o prompt e a resposta, no espaço de embeddings de modelos de linguagem."

A intuição: criatividade não é subjetiva-irredutível. Tem **proxy quantificável** — distância no espaço semântico. Quanto mais distante a resposta do prompt (mantendo coerência), mais original.

## O Alternate Uses Task (AUT) — caso de teste clássico

Tarefa de psicologia clássica: "Liste usos alternativos para um TIJOLO."
- Resposta 1: "construir parede" → distância semântica baixa (próxima do uso canônico)
- Resposta 2: "peso de papel" → distância média
- Resposta 3: "instrumento musical de percussão experimental" → distância alta
- Resposta 4: "âncora simbólica em ritual de despedida" → distância muito alta

Antes de SemDis: 3-5 raters humanos avaliavam cada resposta em escala 1-5 — caro, demorado, inconsistente.

Com SemDis: vetoriza prompt ("uses for brick") e resposta, calcula distância coseno. **r ≈ 0.6-0.8 correlação com raters humanos** — boa o suficiente pra muitos contextos.

## Como funciona tecnicamente

1. **Espaços semânticos múltiplos** — SemDis usa média de 5 modelos:
   - GloVe
   - word2vec (Google News)
   - LSA (Touchstone)
   - word2vec subtitle corpus
   - + um latente

2. **Pré-processamento** — remove stop words, normaliza
3. **Vetorização** — cada palavra vira vetor, frase = média/soma dos vetores
4. **Distância coseno** — entre vetor do prompt e vetor da resposta
5. **Output** — score 0-1, onde maior = mais distante = mais original

## Evolução 2023 (Beaty et al.) — LLMs > SemDis tradicional

Paper **"Beyond Semantic Distance: Automated Scoring of Divergent Thinking Greatly Improves with Large Language Models"** (Beaty et al., 2023, ScienceDirect):

- Fine-tuned LLMs **superam SemDis em correlação com raters humanos** (r ≈ 0.85+)
- Mas LLMs precisam treinamento supervisionado; SemDis é **não-supervisionado** — vantagem prática
- Para casos no Zeus-CO: **LLM judge** (Claude/GPT) pode estimar originalidade com prompt apropriado

## Implicações pra skill `cerebro-criativo`

### 1. Stress-test interno de originalidade

Após gerar 9 candidatas (3×3), skill auto-avalia cada uma:
- **Score 1** — "óbvia, próxima do briefing" (centroide do espaço conceitual)
- **Score 2** — "previsível, mas tem ângulo"
- **Score 3** — "razoavelmente distante, ainda coerente"
- **Score 4** — "distante, surpreendente, defensável"
- **Score 5** — "muito distante, alta tensão coerência ↔ surpresa"

Não é cálculo exato (não temos embeddings em runtime sempre) — é **avaliação reflexiva** usando o framework, simulando o que SemDis faria.

### 2. Originalidade ≠ Valor

Crítica importante: **distância sozinha não basta**. Resposta "esfaque toda a galáxia" pra "usos do tijolo" é distante MAS não-coerente, não-valiosa.

Por isso skill avalia 2 eixos:
- **Originalidade** (proxy SemDis) — distância do óbvio
- **Coerência/Valor** (princípios Fauconnier-Turner) — sustenta sob "running the blend"

Top ideias maximizam **ambos** — não só distância.

### 3. Cross-pollination forçada

Skill usa a métrica pra orientar puxada de corpus: prefere casos do corpus que estão em domínios **distantes** do briefing (distância semântica alta).

### 4. Reporting numérico

Output canônico marca distância semântica de cada ideia em score 1-5. Diego (ou requester) sabe imediatamente "essa é a segura, essa é a arriscada-distante".

## Plataforma SemDis (acesso público)

- **[semdis.wlu.psu.edu](https://semdis.wlu.psu.edu)** — calculadora online (Beaty Lab + Johnson)
- **[Open Creativity Scoring](https://openscoring.du.edu)** — Dumas et al., alternativa

Diego pode usar a plataforma direto pra benchmarks comparativos quando quiser **validar empiricamente** se uma ideia é distante.

## Refs canônicas

- Beaty, R. E., & Johnson, D. R. (2021). "Automating creativity assessment with SemDis: An open platform for computing semantic distance." *Behavior Research Methods*, 53, 757–780. [PMC8062332](https://pmc.ncbi.nlm.nih.gov/articles/PMC8062332/)
- Beaty, R. E., et al. (2023). "Beyond Semantic Distance: Automated Scoring of Divergent Thinking Greatly Improves with Large Language Models." [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1871187123001256)
- Dumas, D., & Dunbar, K. N. (2014). "Understanding fluency and originality: A latent variable perspective." *Thinking Skills and Creativity*, 14, 56-67.
- [Beaty Lab Penn State](https://beatylab.la.psu.edu/) — papers + recursos
- Olson, J. A., et al. (2020). "Naming unrelated words predicts creativity." *PNAS*, 118(25). Métrica DAT (Divergent Association Task).
