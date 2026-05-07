# MVP Scope — {Produto / Feature}

> Cortar 80% para entregar 20% que valida hipótese. Princípio: MVP é experimento, não produto-de-estimação.

**Empresa:** {nome}
**Produto/Feature:** {nome}
**Hipótese a validar:** {1 frase do CEO LEP}
**Métrica de validação:** {1 métrica que confirma/refuta}

---

## Sem-corte (lista bruta de features pensadas)

- {feature 1}
- {feature 2}
- ... (lista completa, sem julgamento)

## Cortes obrigatórios

Para cada feature acima, classificar:

| Feature | Categoria | Decisão |
|---|---|---|
| {feature} | Must-have (sem isso, hipótese não testa) | INCLUIR |
| {feature} | Should-have | DEFER |
| {feature} | Nice-to-have | NÃO FAZER |
| {feature} | Pode ser fake (Wizard of Oz) | FAKE |

## Escopo final do MVP

### Inclui (must-haves)
1. {feature}
2. {feature}
3. {feature}

### Wizard of Oz (humano fingindo automação)
- {processo que será manual no MVP, automatizar depois}

### Defer (próximo sprint pós-validação)
- {feature}

### Não fazer
- {feature — explicitar pra evitar scope creep}

## Stack escolhido

(Referenciar `tech-stack-decision.md` ou inline)

- Frontend: {}
- Backend: {}
- Banco: {}
- Hosting: {}
- Outras: {}

## Cronograma

| Semana | Entrega |
|---|---|
| 1 | Setup + auth |
| 2 | Core flow #1 |
| 3 | Core flow #2 |
| 4 | Polish + tracking + launch |

## Critério de sucesso (volta pra hipótese)

- ☐ Métrica de validação atinge {threshold} em {prazo}
- ☐ Não atinge → revisar hipótese, não adicionar features

## Próximos Movimentos

1. Aprovar escopo (Diego + CEO LEP)
2. Setup repo + dependências
3. Daily check até semana 4
