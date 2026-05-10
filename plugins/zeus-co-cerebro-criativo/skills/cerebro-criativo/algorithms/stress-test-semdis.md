# Algoritmo — STRESS-TEST SEMDIS (auto-avaliação de originalidade)

> Algoritmo de auto-avaliação. Após gerar ideias, skill aplica este algoritmo pra calcular **score de originalidade** (proxy SemDis) e **score de coerência** (Fauconnier-Turner) pra cada ideia.

## Princípio

Skill não confia em intuição estética. Avalia cada ideia em 2 eixos quantificados, marca score numérico, decide top/descartar com base em critério explícito.

## Mecânica em 6 passos

### Passo 1 — Para cada ideia gerada, calcula Score Originalidade

Escala 1-5 baseada em distância semântica estimada:

| Score | Critério |
|---|---|
| **1** | Reproduz vocabulário do briefing literalmente. Concorrência direta faz algo idêntico. "Faz sentido em 1 segundo." |
| **2** | Variação trivial. Mesma família semântica. "Faz sentido em 2 segundos." |
| **3** | Movimento lateral. Mesmo setor mas combinação não-óbvia. "Faz sentido em 5 segundos de reflexão." |
| **4** | Importa vocabulário/estrutura de domínio adjacente. Provoca "interessante, como assim?" |
| **5** | Cross-domain forte. Estrutura inteira importada. Coerente após reflexão, surpreendente em 1ª leitura. |

#### Heurísticas pra estimar

- **Reading the brief test**: alguém lendo a ideia conseguiria adivinhar o briefing? Sim → score baixo. Não → score alto.
- **Concorrência test**: a concorrência teria pensado nisso? Sim → score baixo.
- **Domain crossing test**: vocabulário/estrutura veio de qual domínio? Mesmo = baixo. Distante = alto.

### Passo 2 — Para cada ideia, calcula Score Coerência

Aplica os **5 princípios Fauconnier-Turner** (de `foundations/fauconnier-turner.md`):

| Princípio | Pergunta de avaliação |
|---|---|
| **Integration** | Ideia forma unidade coerente OU é colagem desconexa? |
| **Web** | Relações dos inputs originais continuam visíveis no resultado? |
| **Unpacking** | Dá pra explicar a ideia de volta aos componentes originais? |
| **Topology** | Estrutura preservada (papéis, sequências, hierarquias)? |
| **Good Reason** | Cada elemento tem motivo claro? Sem decoração random? |

Score Coerência (1-5):
- 5/5 → passa todos os 5 princípios
- 4/5 → passa 4
- 3/5 → passa 3 (borderline)
- ≤2/5 → ideia frágil, descartar ou refazer

### Passo 3 — Para cada ideia, calcula Score Atende

3 verificações binárias:
- **Necessidade atendida?** (✅/❌)
- **Restrição respeitada?** (✅/❌)
- **Anti-padrão evitado?** (✅/❌)

Score: 1-3 (uma estrela por ✅).

### Passo 4 — Score total

```
Score_total = (0.4 × Originalidade) + (0.3 × Coerência) + (0.3 × Atende)
```

Normalizado pra 1-5.

- **Score total ≥ 4** — top ideia, apresentar
- **Score 3-3.9** — aceitável, apresentar se top scarce
- **Score < 3** — descartar ou refazer

### Passo 5 — Identificar modo de falha previsível

Para cada ideia top, skill explicita:
- **Risco principal**: o que pode dar errado?
- **Probabilidade**: alta/média/baixa
- **Mitigação**: como reduzir risco?

Exemplos:
- "TarjaPreta como liturgia auto-confissão" → Risco: parecer esoterista demais. Mitigação: linguagem secular do app, símbolos abstratos não-religiosos.
- "Crazyflips como panteão religioso BR" → Risco: ofender comunidades religiosas. Mitigação: nomes inventados, não direto de Umbanda/Candomblé.

### Passo 6 — Apresenta scores no output

Output canônico exibe:

```markdown
### Ideia N: [Nome]
- **Score Originalidade**: 4/5
- **Score Coerência**: 5/5 (passa 5/5 FT princípios)
- **Score Atende**: 3/3
- **Score TOTAL**: 4.0/5

**Modos de falha previsíveis**: [Lista]
**Mitigações sugeridas**: [Lista]
```

## Exemplo completo

### Ideia gerada
"**TarjaPreta como liturgia de auto-confissão**" — app com ritos diários estruturados como missa, comunidade como congregação.

### Cálculo

**Originalidade:**
- Reading the brief test: alguém leria isso e adivinharia "app de saúde mental"? Não diretamente — ele puxaria "religião" primeiro.
- Concorrência test: Calm/Headspace/BetterHelp pensariam nisso? Não.
- Domain crossing: vocabulário 100% religioso, estrutura sacra. Cross-domain forte.
- **Score: 5/5**

**Coerência (FT 5 princípios):**
- Integration: missa diária 10 min é unidade coerente. ✅
- Web: relação "fiel ↔ rito" mapeia "usuário ↔ check-in diário". ✅
- Unpacking: dá pra explicar como "saúde mental + religião como modelo de devoção sustentável". ✅
- Topology: hierarquia (sacerdócio = curadoria, congregação = comunidade) preservada. ✅
- Good Reason: cada elemento (rito, comunidade, peça sagrada) tem motivo conceitual. ✅
- **Score: 5/5**

**Atende:**
- Necessidade (engajamento sustentável saúde mental BR)? ✅
- Restrição (sem prometer "cura")? ✅ — rito é compromisso, não cura
- Evita anti-padrão (voz suave + diário + IA terapeuta)? ✅
- **Score: 3/3**

**Score TOTAL** = 0.4×5 + 0.3×5 + 0.3×5 = **5.0/5** (máximo possível)

**Modos de falha:**
- Risco 1: parecer esoterista pra público secular (probabilidade média)
- Risco 2: ofender religiosos por banalizar liturgia (probabilidade baixa-média)
- Mitigação: usar linguagem secular ("rito" sim, "missa" não), símbolos abstratos

## Limite — auto-avaliação não é objetiva

Algoritmo é **proxy estimado**, não SemDis real. Para validação dura, Diego pode:
1. Submeter prompt + resposta no [semdis.wlu.psu.edu](https://semdis.wlu.psu.edu)
2. Comparar score plataforma vs auto-avaliação skill
3. Calibrar com feedback

## Princípio inviolável

**Skill SEMPRE apresenta scores numéricos**, mesmo em Modo Suporte. Caller precisa saber distância pra escolher informado. Sem score, output é palpite — não cérebro criativo.
