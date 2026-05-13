# PIPELINE — Zeus-CO Labs

> Tipo "Anthropic Research" mas pro Zeus-CO. Pesquisa aplicada ao PRÓPRIO sistema.
> Distinto de `scout` (que olha pra fora) — `labs` olha pra DENTRO e PROJETA avanço.

---

## Pipeline (8 fases)

### Fase 0 — Descoberta Interna do PRÓPRIO Zeus-CO
- Logs de todas as sessões LEPs
- Performance metrics (quais LEPs usados, frequência, custo, output quality)
- LEARNINGS cross-empresa
- _LEDGER cross-empresa (audit trails)

### Fase 1 — Performance audit dos LEPs
Owner: `skill-effectiveness-analyst`
- Quais LEPs são invocados mais? Quais nunca?
- Taxa de "Próximos Movimentos" cumpridos
- Custo médio por LEP / por sessão
- Output: `_Improvements/labs/performance-audit-YYYY-MM.md`

### Fase 2 — LLM SOTA monitoring
Owner: `llm-researcher`
- Papers novos (arXiv, HuggingFace papers)
- Releases Anthropic / OpenAI / Google
- New benchmarks
- New architectures (RAG, agentic, etc.)
- Output: `_Improvements/labs/llm-research-radar.md`

### Fase 3 — Prompt engineering optimization
Owner: `prompt-architect`
- Análise de prompts atuais nos SKILL.md
- Identifica padrões repetitivos (consolidar)
- Identifica anti-patterns
- Cache opportunities
- Output: `_Improvements/labs/prompt-optimization-YYYY-MM.md`

### Fase 4 — Safety + alignment monitoring
Owner: `safety-alignment-monitor`
- LEPs estão respeitando princípios invioláveis?
- Algum LEP deriva (drift) ao longo do tempo?
- Hard limits violados?
- Output: `_Improvements/labs/safety-report-YYYY-MM.md`

### Fase 5 — Architecture proposals
Owner: `labs-director`
- Baseado em fases 1-4, propor mudanças arquiteturais
- ADR-style proposals
- Output: `_Improvements/labs/architecture-proposals/`

### Fase 6 — Experimentation
Owner: `labs-orquestrador` cross `cino-experimentation`
- A/B test entre versões de SKILL.md
- Pilot novo padrão em 1 LEP antes de propagar
- Output: `_Improvements/labs/experiments/`

### Fase 7 — Propagação ou kill
Owner: `labs-director`
- Mudanças aprovadas → propagar via lep-builder
- Mudanças que falharam → kill + lessons learned

### Fase 8 — Reporting + handoff Diego
Owner: `labs-director`
- Mensal: report executivo
- Output: `_Improvements/labs/monthly-report-YYYY-MM.md` + ADOTADAS/DESCARTADAS

---

## Princípio inviolável

**Zeus-CO se auto-evolui ou vira obsoleto.** Labs é o motor de evolução. Sem labs, sistema vira monumento.

## Cadência canônica

- **Semanal:** performance audit (Fase 1)
- **Mensal:** LLM SOTA + prompt optimization + safety (Fases 2-3-4)
- **Trimestral:** architecture review (Fase 5)
- **Ad-hoc:** experimentation (Fase 6)

## Output canônico

`_Improvements/labs/` dentro de `~/Documents/Claude/Projects/` — separado do scout (que vive em `_Improvements/RADAR.md`).
