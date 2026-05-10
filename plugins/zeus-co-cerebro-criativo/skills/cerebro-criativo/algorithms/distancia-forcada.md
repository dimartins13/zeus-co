# Algoritmo — DISTÂNCIA FORÇADA (forçar geração em domínios distantes)

> Algoritmo que **força** a skill a gerar ideias semanticamente distantes do briefing, não próximas. Implementa em runtime LLM o que Beaty/SemDis mede e Gärdenfors formaliza.

## Princípio

Por default, LLMs tendem a propor associações **próximas** ao prompt (alta probabilidade no espaço de embedding). Criatividade exige o oposto — associações **distantes**. Algoritmo de Distância Forçada inverte esse default.

## Mecânica em 5 passos

### Passo 1 — Identificar centroide do briefing

Skill extrai do briefing:
- **Categoria explícita**: "marca de moda", "app de saúde mental", "fintech"
- **Vocabulário próximo**: termos que coocorrem naturalmente com a categoria
  - moda → "tendência", "coleção", "lookbook", "passarela", "público feminino/masculino"
  - saúde mental → "ansiedade", "terapia", "calma", "respiração", "diário"

Esse vocabulário forma o **centroide** que skill **deve evitar** na geração.

### Passo 2 — Listar 3 abordagens canônicas

Skill explicitamente lista 3 abordagens que QUALQUER concorrência poderia propor:
- Marca de moda → "app + e-commerce", "celebrity endorsement", "campanha minimalista P&B"
- Saúde mental → "voz suave", "interface clean", "respiração guiada", "diário de gratidão"

Skill marca essas como **anti-padrão a evitar**.

### Passo 3 — Selecionar 3 domínios distantes (slipnet)

Do `corpus/slipnet.md` — pega node central + lista links **FRACO (∙∙∙)**.

Escolhe 3 domínios que:
- Não compartilham vocabulário com o briefing
- Têm dimensões análogas (Gärdenfors) mas em terreno distante
- Estão no léxico cross-domain (música, biologia, arquitetura, etc)

### Passo 4 — Gerar com restrição vocabular

Skill aplica restrição explícita durante geração:
- **Permitido usar**: vocabulário do briefing + vocabulário dos 3 domínios distantes
- **Proibido usar**: vocabulário das 3 abordagens canônicas (listadas no Passo 2)
- **Bonus**: ideias que importam **estrutura** (não apenas palavras) de domínio distante recebem score maior

### Passo 5 — Auto-validar distância

Após cada ideia gerada, skill se pergunta:
- "Essa ideia poderia ter saído sem ter consultado o domínio distante X?"
  - Sim → distância baixa (1-2)
  - Não → distância alta (4-5)
- "Vocabulário canônico anti-padrão aparece?"
  - Sim → reduzir score
  - Não → manter score

## Exemplo aplicado

### Briefing
"Big idea pra TarjaPreta — app de saúde mental BR"

### Passo 1 — Centroide
- Vocabulário próximo: "ansiedade, depressão, calma, respiração, mindfulness, diário, terapia, autocuidado, bem-estar"

### Passo 2 — Anti-padrão (evitar)
1. "Voz suave + interface clean + meditação guiada"
2. "Diário emocional + tracker de humor + lembrete diário"
3. "Chat com IA terapeuta + matching com profissional"

### Passo 3 — 3 domínios distantes (slipnet links fracos do node "PRODUTO" + "MARCA")
1. **Religião** — rito, confissão, peregrinação, sacralidade
2. **Cinema noir** — preto/branco, voz over melancólica, narrativa em capítulos
3. **Esporte de combate** — round, técnica, treinador, knockout

### Passo 4 — Gerar com restrição vocabular

**Vocabulário permitido:** {saúde mental + religião + noir + combate}
**Proibido:** "voz suave", "interface clean", "diário", "matching"

#### Ideia gerada A:
"**TarjaPreta como liturgia de auto-confissão**" — app onde usuário tem ritos diários estruturados como missa, 10 min "sagrados" por dia, peças sacralizadas (não banalizadas), comunidade como congregação.
- Domínio distante: religião
- Distância: 5/5
- Não usa: nenhum vocabulário anti-padrão

#### Ideia gerada B:
"**TarjaPreta como diretor noir do seu inconsciente**" — check-ins viram capítulos cinematográficos, voz over melancólica, paleta P&B com flashes de vermelho, insight = "twist do filme".
- Domínio distante: cinema noir
- Distância: 5/5
- Não usa anti-padrão

#### Ideia gerada C:
"**TarjaPreta como treinador de combate com seus demônios**" — técnicas de respiração viram "rounds", insights = "golpes", recaída = "knockout aceito", treinamento progressivo gamificado.
- Domínio distante: esporte de combate
- Distância: 5/5
- Não usa anti-padrão

### Passo 5 — Auto-validação

Pergunta de cada uma: "essa poderia ter saído sem o domínio distante?"
- A: NÃO — religião é estrutura central
- B: NÃO — noir é estética e estrutura
- C: NÃO — combate é metáfora central

→ Distância semântica alta confirmada.

## Comparação — sem distância forçada

Sem o algoritmo, skill geraria provavelmente:
- "App com voz suave que registra emoções" (anti-padrão #1)
- "Diário emocional gamificado" (anti-padrão #2)
- "IA terapeuta com matching" (anti-padrão #3)

Distância: 1-2/5. Inútil.

## Variações do algoritmo

### Variação 1 — Distância vocabular ultra
Skill **se proíbe** de usar QUALQUER vocabulário do domínio do briefing. Só descreve a ideia usando vocabulário dos 3 domínios distantes. Mais radical, gera ideias 5/5 mas requer "tradução" pra requester.

### Variação 2 — Distância acumulativa
Em Modo Cascata, cada etapa aumenta distância: Bend (3/5) → Break (4/5) → Blend (5/5). Algoritmo verifica em cada etapa se distância cresceu.

### Variação 3 — Anti-prompt
Skill primeiro gera **anti-ideia** ("a coisa mais óbvia e morna que existe") — depois força ideia semanticamente OPOSTA. Útil em Modo Absurdo.

## Métrica reportada

Cada ideia no output canônico carrega:
```
Distância semântica: X/5
Domínios distantes ativados: [A, B, C]
Anti-padrões evitados: [Z, W]
```

## Integração com outros algoritmos

- **Pre-condição** pra `stress-test-semdis.md` — score só faz sentido se algoritmo foi aplicado
- **Complementar** ao `generalization-retrieval.md` — distância vocabular + busca em níveis de abstração

## Princípio inviolável

**Skill NUNCA gera sem aplicar algoritmo Distância Forçada.** Mesmo em Modo Suporte (chamado por outra skill), aplica — só pula reportagem se output for "lista plana".
