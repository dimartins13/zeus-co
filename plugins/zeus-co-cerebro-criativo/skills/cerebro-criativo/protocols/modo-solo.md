# Modo SOLO — 1 desafio, 3 vetores em paralelo

> Modo padrão. Gera 3 ideias por vetor (Bend / Break / Blend) = 9 candidatas → top 3 refinadas.
> Uso típico: quando Diego ou LEP quer **várias opções pra escolher**.

## Quando usar Modo Solo

- Briefing tem 1 desafio claro
- Tempo disponível: 15-30 min de skill
- Resultado esperado: **diversidade de ideias** pra comparação informada
- Não precisa profundidade vertical — precisa amplitude horizontal

## Quando NÃO usar Modo Solo

- Profundidade vertical necessária → Modo Cascata
- Skill chamada por outra skill (API mode) → Modo Suporte
- Time tá travado em "bom senso" → Modo Absurdo-Controlado
- Já tem ideia base, só fortalecer → Modo Refinamento

## Protocolo (8 passos)

### 1. Recebe briefing + aplica amplificadores

Lê briefing. Aplica `amplifiers/software-inovacao.md`:
- Extrai necessidade real (ou impõe se ausente)
- Impõe 1-2 restrições artificiais (sempre)
- Lista 3 abordagens canônicas a EVITAR (anti-padrões)

Aplica `amplifiers/memoria-atencao.md`:
- Puxa memória contextual (CLAUDE.md, LEARNINGS.md da empresa)
- Identifica caller (LEP X ou Diego direto)
- Aciona cross-pollination se caller é LEP

### 2. Seleciona 3 domínios distantes do slipnet

Do `corpus/slipnet.md` — escolhe **node central do briefing** e ativa 3 links **FRACO (∙∙∙)**.

Ex. briefing "campanha TarjaPreta" → node "LANÇAMENTO" → links fracos: religião (rito de passagem), música (drop ao vivo), biologia (eclosão).

### 3. Aplica BEND com 3 ideias

Segue `operations/bend.md`:
- Para cada domínio distante, gera 1 ideia Bend
- Total: 3 ideias Bend (uma por domínio)
- Cada uma com mapeamento explícito

### 4. Aplica BREAK com 3 ideias

Segue `operations/break.md`:
- Lista 5 enabling constraints do briefing
- Aplica Eliminate, Modify, Reverse — 1 ideia cada
- Total: 3 ideias Break

### 5. Aplica BLEND com 3 ideias

Segue `operations/blend.md`:
- Para cada domínio distante, gera 1 ideia Blend (Input 1 = briefing + Input 2 = domínio)
- Identifica Generic Space + Blended Space + Propriedade Emergente
- Total: 3 ideias Blend

### 6. Stress-test em cada ideia

Aplica `algorithms/stress-test-semdis.md`:
- Score distância semântica (1-5) por ideia
- Aplica princípios Fauconnier-Turner pra coerência
- Avalia: atende necessidade? respeita restrição? evita erro canônico?

### 7. Ranqueia top 3

Pontuação ponderada:
```
score = 0.4 × distância + 0.3 × coerência + 0.3 × atende_restrição_e_necessidade
```

Top 3 = melhores pontuações. Pode ser 3 Bend, ou mix, ou 3 Blend — não importa o vetor, importa a qualidade total.

### 8. Apresenta output canônico

```markdown
## Modo Solo — [Resumo briefing]

### Amplificadores aplicados
- Necessidade real identificada: [X]
- Restrições impostas: [Y, Z]
- Erros canônicos a evitar: [A, B, C]

### Top 3 ideias (de 9 candidatas geradas)

#### 1. [Nome] — Vetor [Bend/Break/Blend], Distância X/5
- **Mecânica**: [como funciona]
- **Rationale neuro**: [1 frase]
- **Atende**: [necessidade Y, restrição Z]
- **Defesa**: [precedente cross-setor / propriedade emergente]
- **Próximos Movimentos**: 1) ... 2) ... 3) ...

#### 2. [Nome] — Vetor [X], Distância X/5
...

#### 3. [Nome] — Vetor [X], Distância X/5
...

### Outras 6 ideias geradas (descartadas no ranqueamento)
- Bend ideia 1 (score X): [resumo 1 linha]
- Bend ideia 2: ...
- ...

### Decisão sugerida
Recomendo [ideia N] porque [1 frase]. Mas [ideia M] tem maior originalidade — vale considerar se [contexto Z].
```

## Tempo esperado

- 5-10 min de skill (geração + stress-test + ranqueamento)
- Output denso mas legível em 3-5 min

## Exemplo de invocação

> "cerebro-criativo, big idea TarjaPreta modo Solo"

→ Skill retorna 9 candidatas geradas + top 3 refinadas.
