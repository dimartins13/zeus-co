# AMPLIFICADOR — Software da Inovação (Necessidade + Restrição + Erro)

> Por trás dos 3 vetores, o córtex pré-frontal só ativa pensamento divergente sob 3 estímulos: **Necessidade**, **Restrição** e **Erro**. Sem esses, a skill gera lista, não criatividade.

## Princípio neuro

Eagleman & Brandt (*The Runaway Species*) apontam: criatividade emerge sob **pressão cognitiva**. O cérebro relaxado não inova — fica em modo default (DMN). O cérebro forçado a navegar limites ativa o pré-frontal e busca caminhos não-canônicos.

> "Onde tudo é possível, nada é interessante. Restrição é a parteira da criatividade."

## Os 3 estímulos

### 1. NECESSIDADE — problema real

**Definição:** existe pressão pra resolver isso. Não é "seria legal", é "isso precisa funcionar".

**Como skill extrai do briefing:**
- "Por que esse problema agora?" — se não houver resposta forte, força a explicitar
- "O que acontece se não resolver?" — consequência real revela necessidade real
- "Quem dorme mal por causa disso?" — humaniza a pressão

**Como skill IMPÕE quando ausente:**
- Pega o objetivo declarado e força stakes: "se não atender em 3 meses, custo é X". Pode ser hipótese — vira pressão pra divergir.

### 2. RESTRIÇÃO — limite que força nova solução

**Definição:** algo que NÃO se pode fazer. Sem dinheiro, sem tempo, sem permissão, sem tecnologia, sem audiência, sem reputação prévia.

**Tipos de restrição (úteis pra impor):**

| Tipo | Exemplo |
|---|---|
| **Recurso** | "Sem orçamento de mídia paga" / "Sem time de design" |
| **Tempo** | "MVP em 2 semanas" / "Lançamento na Black Friday" |
| **Tecnologia** | "Sem AI" / "Sem app, só whatsapp" |
| **Canal** | "Sem Instagram" / "Sem influencer" / "Só presencial" |
| **Custo unitário** | "Margem mínima 50%" / "Não pode passar de R$ X por unidade" |
| **Legal** | "Não pode mencionar [X]" / "Tem que respeitar [regulação Y]" |
| **Marca** | "Não pode usar [cor/símbolo] da concorrência" |
| **Comportamento** | "Cliente não consegue mais que 3 cliques" / "Não pode fazer download" |

**Como skill IMPÕE quando ausente:**
- Mesmo se Diego não pediu, skill cria 1-2 restrições artificiais:
  - "Resolva isso sem usar [canal mais óbvio]"
  - "Resolva com R$ 0 de mídia"
  - "Resolva em 1 página"
  - "Resolva sem usar a palavra [X]"
- Essas restrições viram **dimensão criativa explícita** no output.

### 3. ERRO — feedback de tentativa

**Definição:** tentativa anterior que NÃO funcionou. Sinal de que solução óbvia está fechada — exige caminho novo.

**Como skill extrai do briefing:**
- "Que abordagem vocês já tentaram?"
- "O que falhou?"
- "Por que falhou — execução ruim ou conceito ruim?"
- "Quem é a concorrência e o que eles fazem? (= o que NÃO podemos fazer igual)"

**Como skill USA quando presente:**
- Lista erros como **antiidéias** — coisas a evitar
- Inverte erro pra ver se inversão sugere caminho ("se [X falhou] funcionou pra concorrência mas pra nós não, talvez nosso público diferente prefira o oposto")
- Encara erro como **slipnet path** — o que falhou ativa nodes vizinhos, que podem dar pista

**Como skill IMPÕE quando ausente (sem histórico de tentativas):**
- Pede pra Diego/requester explicitar a "solução óbvia que todos pensariam primeiro" — essa é o erro a evitar (porque vai virar mar de mesmice)
- Lista 3-5 abordagens canônicas do setor — skill se proíbe de propor essas

## Aplicação prática — exemplos

### Briefing fraco (sem amplificadores):
"Quero ideias pra divulgar TarjaPreta"

### Briefing forte (após skill aplicar amplificadores):
"Quero ideias pra divulgar TarjaPreta.
- **Necessidade**: 200 downloads/mês até Q3 ou matamos o projeto
- **Restrição imposta pela skill**:
  - Sem mídia paga (R$ 0 de budget de aquisição)
  - Sem influencer pago
  - Sem prometer "cura" (regulação saúde)
- **Erro**: app de saúde mental tipico tem ~3% retention 30d — não queremos cair nessa armadilha"

→ Skill **DEVE** gerar ideias muito diferentes pros 2 briefings. O segundo força criatividade real.

## Algoritmo de imposição automática

```
INPUT: briefing
↓
1. Skill identifica AUSÊNCIA de:
   - necessidade explícita? → pede ao requester OU infere
   - restrição? → impõe 1-2 artificiais
   - erro/tentativa? → lista 3 abordagens canônicas a evitar
↓
2. Briefing enriquecido vira input pro vetor (Bend/Break/Blend)
↓
3. Ideias geradas SOB esses amplificadores
↓
4. Output marca explicitamente: "Sob restrição: [X]. Atende necessidade: [Y]. Evita erro canônico: [Z]."
```

## Princípio inviolável

**Skill NUNCA gera ideias num vácuo.** Se briefing chegar sem amplificadores, skill **força** o briefing a se enriquecer ANTES de gerar. Se requester recusa enriquecer, skill diz: "ideias geradas terão alta variância e baixa precisão — recomendo enriquecer briefing pra resultado utilizável".
