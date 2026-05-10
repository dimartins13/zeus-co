# Algoritmo — GENERALIZATION-LEVEL RETRIEVAL

> Algoritmo de busca em **níveis de abstração distintos** do briefing. Inspirado em arxiv 2412.14141 ("LLMs Can Realize Combinatorial Creativity"). Permite skill puxar precedentes que não estão em match direto.

## Princípio

Ao buscar exemplos/precedentes no corpus, skill não busca match exato (briefing "marca de moda" → cases "marca de moda"). Busca em **níveis de abstração superiores** — onde marca de moda compartilha estrutura com marca de música, religião, jogo.

## Mecânica em 4 passos

### Passo 1 — Subir abstração do briefing

Skill toma briefing e gera **escada de abstração**:

#### Exemplo: briefing "marca de moda streetwear celebrity"
- **Nível 0** (literal): marca de moda streetwear celebrity
- **Nível 1**: marca de produto desejado
- **Nível 2**: símbolo de status cultural
- **Nível 3**: marcador de pertencimento tribal
- **Nível 4**: sistema de identidade social

Cada nível é uma generalização do anterior, removendo especificidade.

### Passo 2 — Buscar cases em níveis ALTOS

Skill busca corpus principalmente em **níveis 2-4** (não em 0-1).

Resultado para "marca de moda streetwear celebrity":
- **Nível 2** (símbolo de status cultural): Liquid Death (água), Tesla (carro), Supreme (skate elevado)
- **Nível 3** (marcador de pertencimento tribal): Crossfit (esporte), Apple cult (tech), Burning Man (festival)
- **Nível 4** (sistema de identidade social): Religião (congregação), Esporte (torcida), Universidade (alumni)

Cases em níveis altos têm distância vocabular alta MAS estrutura semelhante = ouro pra Bend/Blend.

### Passo 3 — Mapear estrutura abstrata

Para cada case nivel alto puxado, skill identifica:
- **O que torna esse case funcional no seu domínio?** (estrutura)
- **Como essa estrutura mapeia no briefing?**

#### Exemplo mapping

Case puxado: **Crossfit** (Nível 3 — marcador de pertencimento tribal)

Estrutura Crossfit:
- "Box" como espaço comum (não academia genérica)
- WOD diário compartilhado globalmente
- Linguagem própria (AMRAP, EMOM, Murph)
- Hierarquia por performance, não dinheiro
- Comunidade tribal (#crossfitter como identidade)

Mapeamento pro briefing (marca de moda streetwear celebrity):
- "Box" → drop store / espaço fixo da marca
- WOD diário → "fit do dia" curado por celebridades
- Linguagem própria → glossário 2ndStreet (já tem "RACK", "DROP", etc)
- Hierarquia por performance → ranking de quem usa antes / coleciona / styling
- Comunidade tribal → #2ndStreeter como identidade

### Passo 4 — Geração informada pela estrutura abstrata

Skill gera ideias usando a **estrutura** do case puxado, não o vocabulário direto.

Ideia resultante:
> "2ndStreet como Crossfit do streetwear: drop store como 'box', look diário curado por celebrity como 'WOD', glossário próprio, ranking de styling, comunidade #2ndStreeter."

Distância: 5/5 (Crossfit é domínio distante de moda)
Coerência: alta (estrutura abstrata mapeada cuidadosamente)
Originalidade: ninguém pensaria em moda como Crossfit sem o algoritmo

## Por que funciona (literatura)

Paper arxiv 2412.14141 mostra que LLMs com retrieval em níveis de generalização (não match exato) ganham +7-10% em benchmarks de criatividade combinatorial. Mecanismo:
- Match exato → fica preso no centroide do domínio
- Match nível alto → puxa estruturas funcionais cross-domain

É análogo a como cérebro humano faz analogia profunda — Hofstadter chamou isso de "perception of structure" no Copycat.

## Exemplos de escadas de abstração

### Briefing: "App de saúde mental"
- Nível 0: app saúde mental
- Nível 1: produto digital de auto-cuidado
- Nível 2: prática regular de auto-aperfeiçoamento
- Nível 3: ritual diário transformacional
- Nível 4: sistema de mudança comportamental sustentada

Cases nível 2-4 puxados: Crossfit, Religião, Duolingo, Meditação budista, Fitness influencer comunidade.

### Briefing: "Modelo de negócio Ventage (e-commerce óculos)"
- Nível 0: e-commerce óculos
- Nível 1: produto físico vendido online
- Nível 2: marca acessório lifestyle
- Nível 3: declaração de identidade pessoal
- Nível 4: sistema de auto-expressão

Cases nível 2-4: Yeezy, Apple Watch, Tatuagem, Skate brand, Joia familiar.

### Briefing: "Pitch de runway pra investidor anjo BR"
- Nível 0: pitch runway investidor
- Nível 1: apresentação financeira pra captação
- Nível 2: pedido de aporte sob promessa de retorno
- Nível 3: troca de confiança presente por valor futuro
- Nível 4: contrato fiduciário de cooperação

Cases nível 2-4: Casamento (compromisso futuro), TED Talk (promessa de transformação), Pre-order Apple (paga antes), Crowdfunding Kickstarter, Religião (fé em futuro).

## Integração com slipnet

Algoritmo Generalization-Retrieval usa slipnet (`corpus/slipnet.md`) pra navegar entre níveis:
- Briefing identifica node central
- Slipnet expõe links FRACO (∙∙∙) = domínios distantes
- Cada link FRACO frequentemente é case em nível 3-4 de abstração

Os dois algoritmos (Distância Forçada + Generalization-Retrieval) trabalham juntos:
- Distância Forçada **força** geração distante
- Generalization-Retrieval **encontra** os candidatos certos pra puxar

## Princípio inviolável

**Skill NUNCA puxa do corpus em match exato.** Sempre sobe pelo menos 2 níveis de abstração antes de selecionar precedentes. Match exato → óbvio. Match nível alto → criativo.

## Output reportado

Skill explicita no output:
```
### Generalization-retrieval aplicado
- Briefing nível 0: [...]
- Subiu pra nível 3: [...]
- Cases puxados desse nível: [A, B, C]
- Estrutura abstrata mapeada: [...]
```

Caller vê não só ideia, mas o **raciocínio cross-domain** que gerou.
