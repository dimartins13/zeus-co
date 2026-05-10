# Fauconnier-Turner — Conceptual Blending Theory (Formalização matemática do Blend)

> **Origem:** Gilles Fauconnier + Mark Turner, *The Way We Think: Conceptual Blending and the Mind's Hidden Complexities* (2002). Fauconnier (linguístico cognitivo, Stanford) e Turner (cognição literária, Case Western).

## Tese central

Conceptual Blending (também chamado Conceptual Integration) é a **operação cognitiva ubíqua** por trás de quase todo pensamento humano — não só metáfora ou criatividade artística, mas linguagem cotidiana, raciocínio, humor, ciência.

> "The blend is a small conceptual packet, built up dynamically as a mental space, integrating information from input spaces."

## A arquitetura formal (4 espaços mentais)

Toda operação de Blend cria uma **rede de integração** com (no mínimo) 4 espaços mentais:

```
   Input Space 1          Input Space 2
   (conceito A)           (conceito B)
       \                       /
        \                     /
         \                   /
          Generic Space
       (estrutura abstrata
        compartilhada)
              |
              ↓
        Blended Space
   (nova entidade emergente)
```

### Input Space 1 + Input Space 2
Os dois conceitos sendo combinados. Cada um traz frame próprio: papéis, relações, propriedades, eventos típicos.

**Exemplo "computer virus":**
- Input 1: biological virus (infects host, replicates, spreads, harms)
- Input 2: computer program (executes code, copies, transmits)

### Generic Space
A **estrutura abstrata compartilhada** entre os dois inputs. Sem ela, blend não é possível — é o que torna a fusão coerente.

**Exemplo "computer virus":**
- Generic: agente que se autorreplica e se espalha em hospedeiros, causando dano funcional

### Blended Space
A nova entidade. **Não é apenas união de propriedades dos inputs** — tem propriedades emergentes ("running the blend").

**Exemplo "computer virus":**
- Blend: programa que se replica espalhando-se por máquinas, causando dano. Emergente: "anti-virus software" (não existe em nenhum dos inputs isoladamente).

## Vital Relations (10 relações que estruturam a integração)

Fauconnier-Turner identificam 10 tipos de relação que organizam blends:

1. **Change** — mudança ao longo do tempo
2. **Identity** — mesma coisa em contextos diferentes
3. **Time** — relações temporais
4. **Space** — relações espaciais
5. **Cause-Effect** — causalidade
6. **Part-Whole** — composicionalidade
7. **Representation** — uma coisa representa outra
8. **Role** — função/papel
9. **Analogy** — similaridade estrutural
10. **Disanalogy** — contraste estrutural

No blend, essas relações são **comprimidas** (compressed) — o que era distante nos inputs vira próximo no blend.

## Princípios da otimização (5 princípios de bom Blend)

Para um blend ser **eficaz**, deve maximizar:

1. **Integration** — blend forma uma unidade coerente
2. **Web** — relações nos inputs continuam disponíveis no blend
3. **Unpacking** — pode-se reconstruir os inputs a partir do blend
4. **Topology** — relações são preservadas estruturalmente
5. **Good Reason** — todo elemento no blend tem motivo claro

Blends ruins violam um ou mais. Skill usa esses 5 princípios como **stress-test do Blend**.

## Implementações computacionais

A teoria foi recebida no campo Computational Creativity:

- **OpenCog Concept Blending** ([github.com/opencog](https://github.com/opencog)) — implementação simbólica em AtomSpace
- **COINVENT project** (EU 2013-2016) — framework de blending pra concept invention
- Pereira (2007) — *Creativity and Artificial Intelligence: A Conceptual Blending Approach* — Mouton de Gruyter
- Cardoso et al. (2009) — *Computational Creativity: An Interdisciplinary Approach* — ICCC

Limite: Fauconnier-Turner **não objetivaram** modelo computacional, então implementações são adaptações com graus de liberdade.

## Aplicação a marketing/marca (relevante Zeus-CO)

**Blend é o vetor central do branding** — todas as marcas memoráveis são blends:

- **Liquid Death** (Blend): cerveja punk (Input 1) + água mineral (Input 2) → Generic: "bebida com atitude transgressora" → Blend: água com estética metal/morte + sustentabilidade
- **Tesla**: carro (Input 1) + software/Apple (Input 2) → Generic: "produto premium com upgrades contínuos" → Blend: carro elétrico que melhora via OTA
- **Cirque du Soleil**: circo (Input 1) + teatro (Input 2) → Generic: "espetáculo ao vivo com narrativa" → Blend: circo sem animais com história e arte

**Naming via Blend:** muito do trabalho do `naming-domain` é Blend linguístico (Liquid + Death; Air + B&B; Insta + gram; Net + flix).

## Implicações pra skill `cerebro-criativo`

1. **Modo Cascata aplica Blend formal** — sempre identifica Input 1, Input 2, Generic, Blend, com propriedades emergentes.

2. **Stress-test do Blend** usa os 5 princípios (Integration, Web, Unpacking, Topology, Good Reason).

3. **Distância dos inputs é métrica chave** — quanto mais distantes Input 1 e Input 2 (musical+farmacêutico, religioso+tech), maior originalidade do blend (corrobora Beaty/SemDis).

4. **Vital Relations** orientam tipo de blend a buscar — Cause-Effect (produto que causa mudança), Identity (símbolo que representa marca), Analogy (estrutural cross-domain).

5. **"Running the blend"** = trabalho criativo emergente. Skill sempre pergunta "que propriedade emergente esse blend cria que nenhum input sozinho tinha?"

## Refs canônicas

- Fauconnier, G. & Turner, M. (2002). *The Way We Think: Conceptual Blending and the Mind's Hidden Complexities.* Basic Books.
- Turner, M. (2014). *The Origin of Ideas: Blending, Creativity, and the Human Spark.* Oxford UP.
- Pereira, F. (2007). *Creativity and Artificial Intelligence: A Conceptual Blending Approach.* Mouton de Gruyter.
- Wikipedia "Conceptual blending" — overview e refs adicionais
- Computational Creativity conference (ICCC) papers — vários implementam blending formal
