# Template — Output 3B (formato canônico de retorno)

> Estrutura padrão de output da skill. Adaptada por modo.

## Output canônico (Modo Solo)

```markdown
## Cérebro Criativo — [Briefing em 1 linha]

### Briefing reconhecido
[Repete entendimento em 1-2 linhas. Pra confirmar alinhamento.]

### Amplificadores aplicados
- **Necessidade real identificada**: [X]
- **Restrições impostas pela skill**: [Y, Z]
- **Anti-padrões evitados**: [A, B, C]
- **Domínios distantes ativados**: [musica, religião, biologia]
- **Memória contextual puxada**: [LEARNINGS empresa Z]

### Top 3 ideias (rankeadas)

#### 1. [Nome curto] — Score TOTAL 4.5/5
- **Vetor**: Bend (importa lógica de [domínio X] pra [domínio Y])
- **Mecânica**: [2-3 frases]
- **Rationale neuro**: [1 frase] (cita slipnet / Fauconnier / Boden quando aplicável)
- **Distância semântica**: 5/5
- **Coerência (Fauconnier-Turner)**: 5/5
- **Atende**: necessidade ✅, restrição ✅, anti-padrão ✅
- **Defesa cross-setor**: [precedente análogo do corpus]
- **Propriedade emergente**: [...]
- **Modos de falha previsíveis**:
  - [Risco A — probabilidade média/alta/baixa]
- **Mitigações sugeridas**:
  - [Mitigação A]
- **Próximos Movimentos**:
  1. [Ação concreta]
  2. [Ação concreta]
  3. [Ação concreta]

#### 2. [Nome] — Score TOTAL X.X/5
[Mesma estrutura]

#### 3. [Nome] — Score TOTAL X.X/5
[Mesma estrutura]

### Outras 6 candidatas (descartadas no ranqueamento, listadas pra transparência)
- **Bend #1**: [resumo 1 linha + score]
- **Bend #2**: [...]
- **Break #1**: [...]
- **Break #2**: [...]
- **Blend #1**: [...]
- **Blend #2**: [...]

### Recomendação minha
Recomendo [ideia #N] porque [1 frase concisa].
Mas [ideia #M] tem maior originalidade — vale considerar se [contexto Z].
[Eventualmente: se Diego/caller pediu single rec, omite Top 3 e dá só uma]

### Open questions (se houver)
- [Pergunta pro Diego/caller decidir antes de implementar]

### Aprendizado a registrar
Se ideia escolhida tiver êxito, esta sessão vira parte do corpus interno. Skill cresce com uso.
```

## Output Modo Cascata

```markdown
## Cérebro Criativo — Cascata [Briefing]

### Etapa 1 — Bend
- Domínios distantes: [A, B, C]
- 3 Bend candidatos → escolhido: [Nome]
- Rationale: [...]

### Etapa 2 — Break sobre Bend
- Constraint da Bend quebrada: [...]
- 3 Break variações → escolhido: [Nome]
- Rationale: [...]

### Etapa 3 — Blend sobre Break
- Input 1 = output Break
- Input 2 = domínio distante [D]
- Generic Space: [...]
- Blended Space: [...]
- Propriedade emergente: [...]

### Conceito final
- **Nome**: [...]
- **Pitch 1 frase**: [...]
- **Distância acumulada**: 5/5
- **Coerência FT**: passa 5/5
- **Defesa narrativa** (2-3 frases pra apresentar):
  [...]

### Próximos Movimentos
1. ...
2. ...
3. ...
```

## Output Modo Suporte (API mode)

Adaptado ao formato pedido pelo caller:

### Formato "lista plana"
```
1. [Nome] (distância X/5) — [1 frase]
2. [Nome] (distância X/5) — [1 frase]
...
```

### Formato "detalhado"
```
1. [Nome]
   - Vetor: [X]
   - Mecânica: [...]
   - Distância: X/5
2. ...
```

### Formato "single recommendation"
```
Recomendação: [Nome]
Por quê: [parágrafo curto]
Próximos Movimentos: 1) ... 2) ...
```

## Output Modo Absurdo

```markdown
## Cérebro Criativo — Absurdo-Controlado [Briefing]

### Fase 1 — 10 absurdas
1. ...
2. ...
...

### Padrão emergente
- Regras vulneráveis: [...]
- Nodes distantes ativos: [...]

### Fase 2 — 3 viáveis-distantes
[Top 3 estrutura igual Solo, mas com origem absurda marcada]
```

## Output Modo Refinamento

```markdown
## Cérebro Criativo — Refinamento [Briefing]

### Ideia base (input)
[Descrição]

### Diagnóstico
- Vetor dominante: [X]
- Distância atual: X/5
- Pontos fracos: [...]

### Refinamentos aplicados
- [Camada 1]: [...]
- [Camada 2]: [...]

### Ideia refinada (output)
[Descrição revisada]

### Antes vs Depois
| Dimensão | Antes | Depois |
|---|---|---|
| Distância | X/5 | Y/5 |
| Coerência | X/5 | Y/5 |
| Defesa | [...] | [...] |
```

## Princípios do output

1. **Score sempre marcado** — Diego/caller decide informado
2. **Rationale neuro inline** — 1 frase, sem aula
3. **Próximos Movimentos sempre** — operador, não juiz
4. **Open questions só se necessário** — não enrolação
5. **Modo de falha previsível** — transparência sobre risco
6. **Defesa narrativa** — pra apresentar pra terceiros (pitch, board)
7. **Aprendizado registrado** — corpus cresce com uso
