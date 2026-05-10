# AMPLIFICADOR — Memória + Atenção (Ativação cross-domain)

> Criatividade = ativação de associações dormentes (memória ampla) pela atenção focada (córtex pré-frontal). Sem memória rica, não há o que associar. Sem atenção, há ruído sem foco.

## Princípio neuro

O cérebro humano tem ~86 bilhões de neurônios, cada um conectando-se a milhares de outros (~100 trilhões de sinapses). Memória é distribuída — não armazenada em "arquivos", mas em **padrões de ativação cross-rede**.

> "Você lembra Picasso e cubismo. Mas quando alguém menciona 'fragmentar', sua rede de Picasso ativa também — sem você decidir." — Eagleman.

Criatividade explora isso intencionalmente: ativar memória de domínios distantes pra puxar associações dormentes pro problema atual.

## Os 2 mecanismos

### 1. MEMÓRIA AMPLA — substrato

A skill `cerebro-criativo` tem **4 camadas de memória sináptica**:

#### Camada 1 — Corpus interno curado
`corpus/cases-by-operation/{bend,break,blend}/` — ~180 cases canônicos cross-indústria, taggeados por:
- Operação (bend/break/blend)
- Domínio origem
- Domínio destino
- Setor
- Mecanismo neuro chave

#### Camada 2 — Léxicos cross-domain
`corpus/lexicons/` — 7 domínios distantes catalogados:
- música (ritmo, dissonância, registro, etc)
- arquitetura (material, escala, fluxo)
- biologia (simbiose, mutação, escala)
- gastronomia (textura, fermentação, ritual)
- esporte (regra, placar, fase, treino)
- religião (rito, devoção, hierarquia, sacralidade)
- jogos (mecânica, recompensa, narrativa, multiplayer)

#### Camada 3 — Memória contextual Zeus-CO
Lida em runtime:
- Memória global (`~/.claude/projects/.../memory/`)
- CLAUDE.md da empresa que pediu
- LEARNINGS.md específico
- Briefs anteriores
- Decisões registradas

#### Camada 4 — Cross-pollination LEP
Quando outro LEP chama, skill puxa contexto de LEPs **distantes** do caller:
- CFO chama → skill puxa memória CCO + CMO
- CCO chama → skill puxa memória CTO + CFO
- CTO chama → skill puxa memória CCO + COO
- naming-domain chama → skill puxa setores sem-relação com a empresa

Lógica: requester busca solução dentro do próprio domínio porque já está lá. Skill puxa o que ele NÃO veria sozinho.

### 2. ATENÇÃO FOCADA — seleção

Memória ampla sem foco = ruído. Atenção opera 3 disciplinas:

#### Disciplina A — Um vetor por vez
Bend OR Break OR Blend — não todos simultaneamente.
- Modo Solo: gera 3 ideias por cada vetor separadamente, depois compara
- Modo Cascata: aplica sequencialmente (Bend → Break → Blend), cada um com 100% de atenção

#### Disciplina B — Restrição como filtro
Restrições (do amplificador "Software-Inovação") atuam como **filtro de atenção**: só ideias que respeitam restrição passam. Isso é matematicamente similar ao "attention mechanism" em LLMs — só ativações relevantes são amplificadas.

#### Disciplina C — Distância semântica como métrica
Atenção busca ativação distante, não próxima. Algoritmo `distancia-forcada` (próximo arquivo) implementa isso.

## Como skill aplica memória + atenção no fluxo

```
1. RECEBE briefing
   ↓
2. PUXA memória contextual (Zeus-CO global + empresa específica)
   ↓
3. IDENTIFICA caller (LEP X ou Diego direto)
   ↓
4. ATIVA cross-pollination:
   - Se caller = CFO → puxa lexicons distantes de finance
   - Se caller = CCO → puxa lexicons distantes de criação (técnicos, biológicos)
   ↓
5. SELECIONA corpus cases:
   - 3-5 cases do corpus que estão em domínios distantes do briefing
   - Prioriza diversidade (não puxar 5 cases do mesmo setor)
   ↓
6. APLICA atenção:
   - Foca em 1 vetor (modo Solo) ou aplica sequencialmente (Cascata)
   - Mantém restrição como filtro durante geração
   ↓
7. GERA com ativação cruzada — cases + lexicons + briefing simultâneos
   ↓
8. REGISTRA novo learning na memória global (se output validado)
```

## Learning loop — memória cresce

Toda invocação validada (Diego/requester aprova ao menos 1 ideia) gera **registro** em memória global Zeus-CO:
- Briefing original
- Vetor aplicado
- Ideia escolhida
- Por que funcionou (rationale neuro)

Após N invocações, esses registros viram **cases internos do corpus** — patrimônio criativo Zeus-CO específico das empresas Diego.

## Anti-padrões a evitar

### 1. Memória só do domínio do briefing
Erro mais comum em "criatividade fraca": só puxa exemplos do mesmo setor.
- Briefing "marca de moda" → só puxa Nike/Zara/Off-White ❌
- Briefing "marca de moda" → puxa Nike + Liturgia católica + Esporte de combate + Música indie ✅

### 2. Atenção sem foco
Tentar gerar bend+break+blend simultaneamente → ideias mornas, sem profundidade.

### 3. Restrição não respeitada durante geração
"Sem mídia paga" e skill propõe campanha de Instagram Ads → ignorou amplificador. Erro grave.

## Princípio inviolável

**Skill SEMPRE puxa de pelo menos 2 domínios distantes do briefing.** Mesmo se briefing tá em "marketing", skill incorpora exemplo de música ou biologia. Caso contrário, vira ideação dentro da caixa — não criatividade neuro real.
