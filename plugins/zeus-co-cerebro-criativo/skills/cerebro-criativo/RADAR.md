# RADAR — Cérebro Criativo (Tools, MCPs, recursos externos)

> Mapa de ferramentas, MCPs, plataformas e recursos externos que a skill **conhece** ou pode chamar. Cron semanal atualiza.

## MCPs relevantes (Zeus-CO ecosystem)

### MCPs já instalados
- **WebSearch** — pra puxar refs frescas, validar tendências, casos atuais
- **WebFetch** — fetch de papers, artigos, posts
- **Files (`220c44d9...`)** — Google Drive pra puxar materiais Diego doou
- **ClickUp (`60f907d8...`)** — tasks e contexto operacional
- **MCP registry** — pra descobrir novos MCPs criativos

### MCPs potencialmente úteis (avaliar)
- **Notion MCP** — se Diego documenta brand books lá
- **Figma MCP (`fdcd0fac...`)** — pra ler/escrever design files (skill pode gerar mood board referenced)
- **Adobe MCP** — pra geração de imagens (Firefly board)
- **Freepik MCP** — busca de assets visuais
- **mcp-image** — geração de imagens descritas

## Plataformas externas (linkáveis nas refs)

### Validação criatividade
- **[semdis.wlu.psu.edu](https://semdis.wlu.psu.edu)** — calculadora SemDis (Beaty Lab PSU)
- **[openscoring.du.edu](https://openscoring.du.edu)** — Open Creativity Scoring (Dumas et al.)
- **DAT** (Divergent Association Task) — Olson et al. 2020

### Pesquisa creativity
- **[computationalcreativity.net](https://computationalcreativity.net)** — ICCC conference + proceedings
- **arxiv.org cs.AI** — papers atuais
- **researchgate.net** — papers + autores
- **Beaty Lab Penn State** — [beatylab.la.psu.edu](https://beatylab.la.psu.edu)

### Inspiração criativa
- **Brand New** — [underconsideration.com/brandnew](https://www.underconsideration.com/brandnew) — branding case studies
- **Cannes Lions Archive** — premiados publicidade
- **D&AD** — premiados design + advertising
- **Creative Review** — magazine criativo
- **Eye on Design** — AIGA blog
- **It's Nice That** — daily creative inspiration

### Cases & analytics
- **WARC** — marketing effectiveness research
- **CBInsights** — startup intelligence
- **Crunchbase** — startup database
- **Trendwatching** — trend reports

## Repos GitHub de referência

### Computational creativity
- [fargonauts/copycat](https://github.com/fargonauts/copycat)
- [Paul-G2/copycat-js](https://github.com/Paul-G2/copycat-js)
- [Alex-Linhares/FARGonautica](https://github.com/Alex-Linhares/FARGonautica)
- [eraoul/Fluid-Concepts-and-Creative-Analogies](https://github.com/eraoul/Fluid-Concepts-and-Creative-Analogies)
- [opencog/opencog](https://github.com/opencog/opencog) — concept_blending example

### LLM creative agents (estado-da-arte)
- Awesome AI Agents 2026 — [caramaschiHG/awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026)
- Autonomous Agents papers — [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents)

## Outras skills Zeus-CO relacionadas

### Skills que ESTA skill invoca (quando precisar)
- Nenhuma direta — cerebro-criativo é geração pura. Outras skills que esta consulta são via Memory/Reads.

### Skills que invocam ESTA skill
- **`naming-domain`** — Fase 1 de geração de nomes
- **`zeus-co-cco`** — big idea, brand foundation, conceito de campanha
- **`zeus-co-cmo`** — growth experiments, canais não-óbvios, GTM
- **`zeus-co-ceo`** — reframe estratégico, narrativa investor
- **`zeus-co-cfo`** — pitch financeiro reframe
- **`zeus-co-cto`** — alternativas de stack, agent-vs-build
- **`zeus-co-clo`** — ângulos não-óbvios em compliance
- **`zeus-co-coo`** — redesign processo via SCAMPER
- **`zeus-co-pulse`** — caso queira "reframe do problema" antes de diagnóstico
- **`zeus-co-cmo:* + zeus-co-marketing:*`** — 25 specialists de marketing (publicidade-criativa, direção-arte, roteiro-publicitário, etc.)

### Skills brand-voice complementares
- **`brand-voice:enforce-voice`** — aplica brand guidelines em conteúdo (cerebro-criativo gera, brand-voice aprova)
- **`brand-voice:generate-guidelines`** — gera guidelines (cerebro-criativo pode ser usado pra gerar parâmetros distintivos)

## Cron de auto-atualização (proposto)

### `cerebro-criativo-weekly` — segunda-feira 8h
**Tarefa:** busca em arxiv + ICCC + GitHub por:
- Papers novos com keywords "computational creativity", "conceptual blending LLM", "divergent thinking"
- Repos novos com tag "creativity-framework", "ideation"
- Cases de Bend/Break/Blend novos em [Brand New](https://www.underconsideration.com/brandnew) última semana

**Output:** atualiza `WEEKLY_DIGEST.md` com:
- Lista de achados
- Decisão "incorporar / observar / ignorar"
- Se "incorporar": adiciona ao corpus relevante

**Implementação proposta:** Cowork scheduled task (leve, não crítico — pode rodar quando app aberto).

## Limites do RADAR

- Skill **não tem internet em runtime** — só consulta o que está no corpus interno. Buscas externas requerem WebSearch tool explícita.
- Cron semanal é **separado** da invocação real — atualiza corpus, não rodando junto com geração.
- MCPs visuais (Figma, Adobe) são **complementos** — skill principal é texto.

## Próximos updates do RADAR (backlog)

- [ ] Adicionar mais MCPs visuais (Figma, Adobe Firefly) pra geração mood board
- [ ] Investigar integração com plataformas open creativity scoring pra validação dura
- [ ] Avaliar plugin pra puxar tendências culturais BR (Twitter trending, Globo, etc)
- [ ] Avaliar integração com Granola (Diego doa transcripts de reuniões criativas)
