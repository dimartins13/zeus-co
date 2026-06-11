---
name: human-team
description: OpenSquad — sistema de squads de agentes IA colaborativos. Em vez de um único agente fazendo tudo sozinho, cria um TIME de agentes especializados que conversam entre si (round-table), dividem responsabilidades, criticam o trabalho um do outro, e sintetizam entregável final. Útil quando o problema é grande demais pra um agente só ou exige perspectivas distintas (criativo + técnico + financeiro + jurídico, ou diretor de arte + copywriter + estrategista + cliente). Dois modos - (1) BUILD - cria squad novo (define papéis, ordens de execução, critérios de qualidade, persiste o squad em `squads/{nome}.yaml` pra reusar); (2) RUN - executa squad existente sobre um briefing específico (lê briefing, roda turnos, registra debate em transcript markdown, sintetiza entregável final). Cada agente tem - nome, papel claro de UMA frase, expertise (3-5 bullets), mandato (o que faz e o que NÃO faz), critério de qualidade próprio, e tom. Squad tem - até 7 agentes (mais que isso vira ruído), modo de execução (round-table sequencial, debate adversarial, pipeline em cascata, ou fan-out + synth), número de rodadas (1-3 default), e moderador (1 dos agentes ou meta-agente). Output em `human-output/human-team/{squad-slug}/{run-slug}/` com transcript.md (debate completo), draft-final.md (síntese), assets/ (artefatos gerados durante o debate). Use SEMPRE para "/team", "/human-team", "/squad", "monta um squad", "OpenSquad", "agentes em time", "agentes colaborando", "time de agentes", "round-table", "debate de agentes", "perspectivas múltiplas IA", "preciso de várias cabeças", "comitê de IA", "mesa redonda IA", "criativo + estratégia + financeiro", "diretor de arte + copywriter + cliente", "agente que discute com outro agente", "decisão por consenso", "validação cruzada IA", "preciso bater conceito antes de virar peça". Não substitui CCO/CMO/CFO LEPs (que são executores fixos); complementa quando o briefing exige debate antes de execução. Quando o usuário já sabe o LEP certo (CMO faz isso, CFO decide aquilo), invoca direto o LEP, não o squad.
---

# Human Team — OpenSquad

Sistema de **squads de agentes IA colaborativos**. Um problema grande vira um time de agentes especializados que conversam, dividem trabalho, criticam um ao outro e sintetizam entregável. Mais útil quando uma única cabeça não basta.

## Quando usar (e quando NÃO usar)

**Use aqui quando:**
- O problema exige 3+ perspectivas distintas (ex: criativo + estratégico + financeiro + jurídico)
- Você quer **debate** antes da execução (testar conceito por contradição)
- Briefing é grande/ambíguo e precisa ser decomposto antes
- Quer **validação cruzada** — agente A propõe, agente B refuta, agente C sintetiza

**NÃO use aqui (use LEP direto) quando:**
- Você já sabe que é trabalho de CMO/CFO/CTO específico → invoca direto (`zeus-co-cmo`, `zeus-co-cfo`, etc.)
- Tarefa é execução pura sem ambiguidade → vai direto na skill executora
- Problema é pequeno (1-2 perspectivas resolvem) → não invente squad

## A regra dura

- **Máximo 7 agentes.** Acima disso, sinal de que o squad tá querendo abraçar problema demais. Divide em 2 squads.
- **Cada agente tem mandato de UMA frase.** Se precisa de parágrafo pra explicar o papel, o papel está confuso.
- **Cada agente tem "o que NÃO faz".** Tão importante quanto o que faz. Senão eles se sobrepõem.
- **Moderador é obrigatório.** Sem moderador o debate vira eco. Pode ser 1 dos 7 ou um meta-agente neutro.
- **Transcript é entregável de primeira ordem.** Não joga fora o debate — ele é onde mora a verdade. Final-draft sozinho perde o porquê.

## Pré-requisitos

Esta skill não exige CLI externo. Funciona dentro do próprio Claude (chat) ou via SDK quando rodada em rotina. Para persistência:

```bash
mkdir -p ~/human-team/squads ~/human-team/runs
```

Squads ficam em `~/human-team/squads/{nome}.yaml`. Runs em `human-output/human-team/{squad-slug}/{run-slug}/`.

---

## Modo BUILD — criar squad

### Estrutura do `.yaml` do squad

```yaml
squad: critique-creativo-marca
description: Squad pra avaliar conceito de campanha antes de virar peça final
mode: debate-adversarial         # round-table | debate-adversarial | pipeline | fan-out-synth
rounds: 2
moderator: maestro                # nome de 1 agente OU "meta"

agents:
  - name: diretor-arte
    role: Defende viabilidade visual e coerência estética do conceito
    expertise:
      - Direção de arte editorial e publicitária
      - Sistemas visuais de marca
      - Tipografia, paleta, hierarquia
    mandate: Avalia se o conceito tem "imagem-âncora" possível e é distintivo visualmente
    nao_faz: Não opina sobre legalidade nem ROI
    criterio_qualidade: "Tem imagem-âncora? É distintivo? Cabe no DNA da marca?"
    tom: Direto, designer sênior

  - name: copywriter-senior
    role: Defende clareza e potência da mensagem
    expertise:
      - Copy de campanha (long e short)
      - Hooks editoriais
      - Voz de marca
    mandate: Avalia se a mensagem central aguenta sem suporte visual
    nao_faz: Não opina sobre paleta nem mídia
    criterio_qualidade: "A frase única vende sozinha? Sem AI-slop?"
    tom: Cético, editorial

  - name: estrategista-marca
    role: Defende coerência com o DNA e o ciclo da marca
    expertise:
      - Plataforma de marca
      - Posicionamento
      - Equity tracking
    mandate: Avalia se o conceito reforça ou dilui o DNA atual
    nao_faz: Não escreve copy nem decide visual
    criterio_qualidade: "Move o ponteiro do posicionamento? Ou só consome atenção?"
    tom: Estratégico, calmo

  - name: cliente-cético
    role: Representa o cliente real — desconfortos, ressalvas, dúvidas
    expertise:
      - Negócio do cliente
      - Stakeholders internos
      - Crises passadas
    mandate: Levanta TODA dúvida que o cliente real levantaria
    nao_faz: Não propõe alternativa — só refuta
    criterio_qualidade: "Quais 3 perguntas o C-level faria? O conceito sobrevive?"
    tom: Ríspido, dono do negócio

  - name: maestro
    role: Sintetiza o debate em decisão clara
    expertise:
      - Síntese de divergência
      - Decisão sob incerteza
    mandate: Lê os 4 anteriores, sintetiza convergências, decide go/no-go ou itera
    nao_faz: Não defende uma das partes — sintetiza
    criterio_qualidade: "Resultado final é uma decisão executável?"
    tom: Neutro, decisor
```

### Modos de execução

| Mode | Como funciona | Quando usar |
|---|---|---|
| `round-table` | Cada agente fala 1 vez por rodada, em ordem fixa | Decisão exploratória, sem conflito esperado |
| `debate-adversarial` | Defensor vs refutador alternados, moderador sintetiza no fim | Testar conceito por estresse — recomendado pra criativo |
| `pipeline` | Agente 1 entrega → 2 critica → 3 reescreve → 4 valida → ... | Quando há ordem natural (briefing → conceito → copy → arte) |
| `fan-out-synth` | Todos respondem ao briefing em paralelo, meta-agente sintetiza | Brainstorm divergente, sem hierarquia |

## Modo RUN — executar squad

1. **Identifica** o squad (`squads/{nome}.yaml`) ou cria ad-hoc na hora
2. **Lê o briefing** (texto colado, link, pasta)
3. **Carrega DNA** da marca se houver (`DNA.md` no `pwd` ou `~/{brand-slug}/DNA.md`)
4. **Roda turnos** conforme `mode`/`rounds`. Cada turno = 1 agente falando ≤300 palavras. Sem monólogo.
5. **Modera ao fim de cada rodada**: moderador pergunta "onde estamos?", aponta convergência/divergência, decide se vai pra próxima rodada ou síntese
6. **Sintetiza** em `draft-final.md` — decisão executável, não relatório acadêmico
7. **Salva transcript** completo em `transcript.md`

### Output

```
human-output/human-team/{squad-slug}/{YYYY-MM-DD-run-slug}/
├── briefing.md         ← input que disparou o run
├── transcript.md       ← debate completo, agente por agente, rodada por rodada
├── draft-final.md      ← síntese executável do moderador
├── assets/             ← arquivos gerados durante o debate (sketches, copy drafts, etc.)
└── manifest.json       ← squad usado, agentes, rounds, mode, timing
```

## Squads de partida (templates sugeridos)

- `critique-creativo-marca` — diretor-arte + copywriter + estrategista + cliente-cético + maestro (debate-adversarial)
- `decisao-investimento` — CFO-analítico + CFO-cético + due-diligence + advogado-MA + comitê (pipeline)
- `nome-de-empresa` — naming-criativo + naming-funcional + lojista-domínio + jurídico-marcas + maestro (fan-out-synth)
- `ad-de-campanha` — planner + redator + diretor-arte + designer-sonoro + revisor (pipeline)

Não force template — squad bom é o que cabe no problema, não o que tem no catálogo.

## Anti-padrões

- **Squad eco-câmara** — 4 agentes que concordam. Tira 2, adversariza 1.
- **Squad pizza** — 7 agentes, cada um come uma fatia. Convém quebrar em 2 squads de 3-4.
- **Moderador parcial** — moderador defendendo lado. Troca de moderador ou usa meta.
- **Transcript jogado fora** — só salvar draft-final. Não. Salve transcript sempre.
- **Rodadas infinitas** — passou de 3 rodadas sem convergência? Squad está mal montado. Para e refaz.

## Próximo passo

Diga `build` (montar squad novo) ou `run {squad}` (rodar squad existente) + cole o briefing. Se for primeira vez, sugiro começar pelo template `critique-creativo-marca` aplicado num conceito que você já tenha esboçado.
