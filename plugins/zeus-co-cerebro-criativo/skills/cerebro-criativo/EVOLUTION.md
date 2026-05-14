# EVOLUTION — Cérebro Criativo (Changelog)

## v0.1.0 — 2026-05-10 (release inicial)

### Construído
- **SKILL.md** — entry point + auto-trigger keywords ricas
- **CORE.md** — identidade + framework unificado Boden+Eagleman+Fauconnier+Hofstadter + 3 vetores + 2 amplificadores + 5 modos + lógica orquestração
- **foundations/** — 6 references teóricos:
  - `eagleman-3b.md` (Bend/Break/Blend)
  - `boden-3-types.md` (combinatorial/exploratory/transformational)
  - `fauconnier-turner.md` (Conceptual Blending Theory + 4 espaços + 5 princípios otimização)
  - `hofstadter-slipnet.md` (Copycat arquitetura tripartite + FARG)
  - `gardenfors-spaces.md` (Conceptual Spaces + embeddings)
  - `beaty-semdis.md` (métrica distância semântica)
- **operations/** — 3 protocolos operacionais:
  - `bend.md` (10 passos + SCAMPER S/A/P)
  - `break.md` (10 passos + SCAMPER E/M/R)
  - `blend.md` (10 passos + Fauconnier-Turner 4 espaços + 5 princípios)
- **amplifiers/** — 3 amplificadores:
  - `software-inovacao.md` (necessidade + restrição + erro)
  - `memoria-atencao.md` (4 camadas + cross-pollination LEP)
  - `distancia-semantica.md` (métrica + algoritmo de forçar distância)
- **corpus/** — memória sináptica:
  - `bend-cases.md` (~60 cases canônicos cross-indústria)
  - `break-cases.md` (~60 cases canônicos)
  - `blend-cases.md` (~60 cases canônicos)
  - `slipnet.md` (rede conceitual com pesos qualitativos)
  - `lexicons/musica.md` + `arquitetura.md` + `biologia.md` + `gastronomia.md` + `esporte.md` + `religiao.md` + `jogos.md`
- **protocols/** — 5 modos de operação:
  - `modo-solo.md` (3×3 candidatas → top 3)
  - `modo-cascata.md` (Bend → Break → Blend sequencial)
  - `modo-suporte.md` (API criativa pra outras skills)
  - `modo-absurdo-controlado.md` (Geneplore: divergent → convergent)
  - `modo-refinamento.md` (fortalece ideia existente)
- **algorithms/** — 3 algoritmos:
  - `distancia-forcada.md` (força geração em domínios distantes)
  - `stress-test-semdis.md` (auto-avaliação 1-5 originalidade + coerência)
  - `generalization-retrieval.md` (busca em níveis de abstração)
- **templates/** — 3 artefatos:
  - `briefing-3b.md` (input pra invocar skill)
  - `output-3b.md` (formato canônico de retorno)
  - `rationale.md` (defesa neuro por ideia)
- **LITERATURE.md** — bibliografia 4 camadas
- **RADAR.md** — tools, MCPs, repos GitHub, plataformas

### Princípios fundadores estabelecidos
1. Operador, não juiz — gera ideias, não palpita
2. Distância semântica > proximidade — sempre cross-domain
3. Restrição é amiga — impõe se ausente
4. Cross-domain sempre — 2+ domínios distantes
5. Rationale defendível — vetor + mapping + propriedade emergente
6. Memória cresce — learnings viram corpus
7. Aprovação humana final — geramos, Diego escolhe

### Decisões arquiteturais
- **Standalone plugin** (não dentro do plugin zeus-co-cmo) — porque capability é transversal, todos LEPs invocam
- **Modo dual** — marketing-primary auto-trigger + suporte transversal explícito
- **Nome PT** (cerebro-criativo) — alinha com origem da pesquisa neuro (Diego)
- **Framework unificado** — Boden + Eagleman + Fauconnier-Turner + Hofstadter + Beaty + Eberle, não framework único

### Princípio fundador
> "Cérebro criativo não é magia. É processo computacional executado por redes neurais sob pressão cognitiva (necessidade + restrição + erro), formado por 3 operações distintas (Bend/Break/Blend) ativando memória ampla via atenção focada."

---

## v0.2.0 — [TODO — incrementos planejados]

### Backlog v0.2
- [ ] Cron `cerebro-criativo-weekly` segunda 8h (auto-update literatura + radar)
- [ ] Integração Granola — puxar transcripts de reuniões criativas Diego
- [ ] Integração Figma — gerar mood board referenced (output visual)
- [ ] Adicionar +50 cases ao corpus (BR-specific + 2026 fresh)
- [ ] Adicionar 2 léxicos novos (cinema + tipografia)
- [ ] Refinar algorithm distância-forçada com benchmarks reais SemDis
- [ ] Learning loop ativo — invocações validadas viram corpus
- [ ] Documentar interface cross-skill em CHEAT-SHEET.md Zeus-CO

### Backlog v0.3+
- [ ] Multi-blend (3+ inputs simultâneos) — Fauconnier-Turner avançado
- [ ] Modo "stress-test externo" — Diego pode benchmark com SemDis platform real
- [ ] Tendências culturais BR cron (Twitter trending, Globo, manifestações culturais)
- [ ] Mood board output em Figma file via MCP
- [ ] Versioning de conceitos (Bend v1 → v2 → v3 com diffs)

---

## Notas de design (decisões registradas)

### Por que NÃO dentro do ecossistema ZEUS-CO
Inicialmente considerado mora em `zeus-co (cmo+marketing+cco):cerebro-criativo`, mas elevou-se a plugin standalone porque:
- Pesquisa aprofundada revelou capability transversal (Boden 3 types funcionam pra qualquer função)
- Outras skills (não-marketing) precisam chamar de forma natural
- Status de specialist próprio é coerente com naming-domain/pulse/publisher/claude-expert

### Por que nome PT (não EN)
Diego é founder BR, base de empresas BR, e a pesquisa neuro foi originalmente passada em PT. Nome em PT (`cerebro-criativo`) sinaliza:
- Alinhamento com origem da pesquisa
- Coerência com `zeus-co-cmo + zeus-co-marketing + zeus-co-cco` (skills marketing já em PT)
- Não-pretensão de internacionalização imediata (Zeus-CO opera BR-first)

### Por que 5 modos e não menos
3 modos seriam mínimo (solo, cascata, suporte). Adicionados Absurdo (caso de destrava) e Refinamento (caso de já-tem-ideia) porque:
- Resolvem casos de uso REAIS de Diego (já travado vs já decidido)
- Cada um tem mecânica distinta (não é só "alteração de parâmetros do mesmo modo")

### Por que score 1-5 e não 0-1 (como SemDis real)
Skill aproxima SemDis sem cálculo real de embedding. Escala 1-5 é:
- Mais intuitiva pra humanos
- Compatível com mental model "stars rating"
- Suficiente granular pra ranqueamento

### Trade-off escolhido — não roda Copycat real
Considerado integrar runtime simbólico de Copycat (Python via subprocess). Decidido NÃO porque:
- Requer Python env + deps managed
- Domínio Copycat (letras) é limitado, requer adaptação
- Princípios estruturais (slipnet, slippage, coerência+surpresa) podem ser incorporados como protocolo prompt-driven
- LLM moderno já faz bem o trabalho com princípios certos
- Diego não é programador — instalação complexa = barreira

Pode ser revisitado em v0.5+ se benchmarks comparativos justificarem.
