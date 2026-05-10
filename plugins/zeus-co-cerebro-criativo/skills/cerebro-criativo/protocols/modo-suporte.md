# Modo SUPORTE — API criativa pra outras skills

> Modo invocado por **outras skills/LEPs do Zeus-CO**. Skill retorna output **direto e tipado** no formato que a skill caller espera.
> Substitui "subagent" — é o entry point oficial pra invocação cross-skill.

## Como skills externas invocam

### Padrão de invocação

Skill caller invoca cerebro-criativo passando:
1. **Briefing** — desafio em texto livre
2. **Vetor preferido** (opcional) — bend / break / blend / qualquer
3. **Quantidade de ideias** — 1, 3, 5, 10 (default: 3)
4. **Formato de retorno** — lista plana / detalhado / single recommendation
5. **Restrições conhecidas** — se já tem
6. **Contexto da skill caller** — qual LEP está chamando + por quê

### Exemplos de invocação

#### `naming-domain` chamando

```
"cerebro-criativo:
 BRIEFING: gerar 10 nomes pra 2ndStreet (streetwear celebrity)
 VETOR: Blend (linguístico)
 QUANTIDADE: 10
 FORMATO: lista plana
 RESTRIÇÕES: máximo 2 sílabas, deve sugerir cultura urbana + status
 CONTEXTO: chamado por naming-domain pra Fase 1 (geração inicial)"
```

#### `CCO` chamando

```
"cerebro-criativo:
 BRIEFING: big idea pra campanha de lançamento TarjaPreta
 VETOR: qualquer
 QUANTIDADE: 3
 FORMATO: detalhado
 RESTRIÇÕES: sem mídia paga, sem prometer 'cura'
 CONTEXTO: chamado por CCO pra montar brand foundation"
```

#### `CEO` chamando

```
"cerebro-criativo:
 BRIEFING: reframe modelo de negócio Ventage (e-commerce óculos)
 VETOR: Bend (analogia distante)
 QUANTIDADE: 5
 FORMATO: lista detalhada
 RESTRIÇÕES: viabilidade BR
 CONTEXTO: CEO precisa de ângulos pra apresentar a Diego antes de fechar GTM"
```

#### `CFO` chamando

```
"cerebro-criativo:
 BRIEFING: reframe pitch runway pra investidor anjo BR
 VETOR: Bend
 QUANTIDADE: 3
 FORMATO: 1 frase cada
 RESTRIÇÕES: investidor BR conservador
 CONTEXTO: CFO preparando deck"
```

## Protocolo do Suporte (8 passos)

### 1. Parse de invocação
Skill lê parâmetros:
- briefing
- vetor (ou "qualquer")
- quantidade
- formato
- restrições
- contexto caller

### 2. Aplica amplificadores APENAS necessários
Em Modo Suporte, é o **caller que dirige** — então skill não impõe restrições extra a menos que o caller pediu ou são óbvias (legais, regulatórias).

### 3. Cross-pollination forçada pelo caller
Skill identifica LEP caller e puxa memória de LEPs **distantes**:
- naming-domain → puxa setores não-relacionados ao da empresa
- CCO → puxa CTO + CFO + COO
- CEO → puxa CMO + CFO
- CFO → puxa CCO + CMO
- CTO → puxa CCO + COO
- CLO → puxa CCO + CMO

### 4. Seleciona vetor
- Se vetor especificado → usa esse
- Se "qualquer" → seleciona automaticamente:
  - Briefing pede reframe → Bend
  - Briefing pede disrupção / nova categoria → Break
  - Briefing pede combinação / fusão → Blend
  - Briefing ambíguo → Solo mode (3 vetores em paralelo)

### 5. Gera ideias na quantidade pedida
- Aplica protocolo do vetor (`operations/bend.md` etc)
- NÃO faz Cascata por padrão (a menos que caller peça profundidade)

### 6. Stress-test rápido
- Score distância (1-5) por ideia
- Verifica restrições do caller
- Filtra incoerências óbvias

### 7. Formata output conforme pedido

#### Formato "lista plana"
```
1. [Nome / 1-liner] (distância X/5)
2. [Nome / 1-liner] (distância X/5)
...
```

#### Formato "detalhado"
```
Ideia 1: [Nome]
- Vetor: [bend/break/blend]
- Mecânica: [...]
- Distância: X/5
- Rationale neuro: [...]
```

#### Formato "single recommendation"
```
Recomendo: [Nome]
Por quê: [1 parágrafo]
Próximos Movimentos: 1) 2) 3)
```

### 8. Retorna ao caller

Skill **NÃO** apresenta floreio nem rationale teórico longo. Em Modo Suporte, output é **insumo** pra outra skill processar — então é direto.

## Quando Modo Suporte vira Modo Solo

Se caller passar parâmetros incompletos OU se briefing exigir profundidade que caller não pediu, skill pode:
1. Pedir esclarecimento ao caller (ideal)
2. Escalonar pra Modo Solo (gera 3×3) e devolver top 3
3. Sinalizar trade-off no output: "ideias geradas têm alta variância — recomendo refinar briefing"

## Princípios da API criativa

1. **Caller dirige** — skill cerebro-criativo se adapta ao formato pedido
2. **Sem floreio** — output direto, insumo pra próximo passo
3. **Distância sempre marcada** — caller precisa saber originalidade
4. **Rationale curto** — 1 frase, não aula
5. **Próximos Movimentos opcionais** — se caller pediu formato lista plana, omite
6. **Cross-pollination automática** — sempre puxa memória de LEPs distantes do caller

## Integração com docs Zeus-CO

Esta é a **interface oficial** pra outras skills chamarem cerebro-criativo. Mencionada em:
- `~/Documents/Claude/Projects/CHEAT-SHEET.md` (invocações copy-paste)
- `~/Documents/Claude/Projects/ZEUS-CO.md` (organograma)
- README dos plugins Chiefs (CCO, CMO, CEO, CFO, CTO, CLO, COO) — instrução de "quando chamar cerebro-criativo"

## Exemplo end-to-end

### Caller (naming-domain)
> "cerebro-criativo: BRIEFING: 10 nomes pra 2ndStreet, VETOR: Blend, QUANTIDADE: 10, FORMATO: lista plana com domínios distantes ativados"

### Output cerebro-criativo (Modo Suporte)
```
1. AXÉ STREET — Blend(streetwear + religião sincrética BR), distância 5/5
2. PANTHEON — Blend(streetwear + mitologia panteão grego), distância 4/5
3. SACRO — Blend(streetwear + cristianismo gótico), distância 5/5
4. NOVENA — Blend(streetwear + ritual católico contagem), distância 4/5
5. RACK — Blend(streetwear + esporte placar/inventário), distância 3/5
6. ROUND — Blend(streetwear + boxe round), distância 3/5
7. APEX — Blend(streetwear + biologia predador alfa), distância 4/5
8. NICHE — Blend(streetwear + biologia ecologia), distância 3/5
9. RIFF — Blend(streetwear + música hook), distância 4/5
10. ENCORE — Blend(streetwear + música retorno por demanda), distância 4/5
```

### naming-domain processa
naming-domain pega lista, aplica scoring matrix próprio (distinctiveness + phonetic + memorability + visual + legal), shortlist top 8, segue pipeline próprio (Fase 2-6).
