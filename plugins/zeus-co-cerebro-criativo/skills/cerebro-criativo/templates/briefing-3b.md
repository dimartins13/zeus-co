# Template — Briefing 3B (input pra cerebro-criativo)

> Use este template pra enriquecer briefing antes de invocar skill. Briefing rico = output rico.

## Briefing 3B

### 1. Contexto
- **Empresa / projeto**: [nome]
- **Setor**: [setor]
- **Estágio**: [MVP / validação / scale / refresh]

### 2. Desafio
- **Em 1 frase**: [...]
- **Por que agora**: [...]
- **Quem dorme mal por causa disso**: [...]

### 3. Amplificadores (Software-Inovação)

#### Necessidade
- **O que precisa funcionar**: [...]
- **Stake real se não funcionar**: [...]
- **Prazo**: [...]

#### Restrições (impostas ou conhecidas)
- **Recurso**: [budget, time, ferramentas]
- **Tempo**: [...]
- **Legal/regulatório**: [...]
- **Marca/posicionamento**: [não pode parecer X / soar como Y]
- **Outras**: [...]

#### Erros (tentativas anteriores)
- **Já tentei**: [abordagens passadas]
- **Falhou porque**: [diagnóstico]
- **Concorrência faz**: [3 abordagens canônicas a evitar]

### 4. Configuração da invocação

- **Modo preferido**: [Solo / Cascata / Suporte / Absurdo / Refinamento / "Skill decide"]
- **Vetor preferido**: [Bend / Break / Blend / Qualquer]
- **Quantidade de ideias**: [1 / 3 / 5 / 10]
- **Formato esperado**: [lista plana / detalhado / single rec / cascata profunda]

### 5. Caller / Contexto

- **Quem está chamando**: [Diego direto / CCO / CMO / outra skill X]
- **Por quê** (uso pretendido): [pra apresentar pra board / pra brief de agência / pra naming / etc]
- **Próximo passo após receber ideias**: [...]

### 6. Memória relevante

- **Empresa-CLAUDE.md**: já tem info? Pode complementar?
- **Decisões anteriores relacionadas**: [se houver]
- **Stakeholders cuja reação interessa**: [Akkari, Neymar, board, regulador, etc]

---

## Versões resumidas

### Briefing minimo (skill aceita)
```
Empresa: [X]
Desafio: [Y]
Restrição: [Z]
Modo: Solo
```

### Briefing rápido (skill prefere)
```
Empresa: [X]
Desafio: [Y]
Necessidade: [Z]
Restrição: [W]
Anti-padrão (concorrência faz): [A]
Modo: [B]
Vetor: [C]
Quantidade: [N]
```

### Briefing completo (output ótimo)
[Usa todas as 6 seções acima]

---

## Quando briefing chega incompleto

Skill **NÃO** chuta amplificadores que poderiam dar errado. Em vez disso:
1. Pede esclarecimento pro caller pra 1-2 amplificadores chave
2. Se caller insiste em prosseguir sem, skill IMPÕE restrições artificiais transparentemente e marca no output
3. Se LEP caller passou contexto, skill infere do contexto e marca como "inferido"

## Princípio inviolável

**Briefing pobre = output pobre.** Skill PODE devolver "preciso de mais info em X, Y, Z" antes de gerar — não vai criar no vácuo.
