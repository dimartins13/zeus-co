# Zeus-CO

> Virtual C-Suite operating system for serial founders. Built for [Diego Martins](https://github.com/diegomartins) operating 5+ companies in parallel (KingPanda iGaming, 2ndStreet fashion resale, Crazyflips NFT/audiovisual, Ventage retail, TarjaPreta digital wellbeing).

## What it is

11 Living Expert Profiles (LEPs) + Skill Factory. Each LEP is a senior virtual professional that **operates** (doesn't audit) within any company in your portfolio.

## Plugins

### 7 Chiefs (C-Suite)
- **zeus-co-ceo** — Founder office orchestrator. Vision, OKRs, fundraising, capital allocation.
- **zeus-co-cfo** — Modeling, runway, unit economics, cap table, BR tax structure.
- **zeus-co-coo** — Process design, SOPs, supply chain, vendor mgmt, customer ops.
- **zeus-co-cmo** — Marketing dept orchestrator. Delegates to ag-zeus-mkt's 25 specialists.
- **zeus-co-cco** — Brand foundation, identity, narrative, brand voice, creative direction.
- **zeus-co-cto** — Stack decisions (Boring Tech principle), MVP scoping, agent-first automation.
- **zeus-co-clo** — Contracts, LGPD, BR sectoral regulation (iGaming SECAP, audiovisual ANCINE), IP/trademark INPI.

### 3 Transversal Specialists
- **zeus-co-claude-expert** — Token efficiency, prompt caching, model routing, Skill/MCP/Subagent/Hook architecture.
- **zeus-co-naming-domain** — Brand naming (7 territories) + INPI trademark + Registro.br domain check.
- **zeus-co-pulse** — Portfolio health: ClickUp + Dash Financeiro + state on disk → actionable dashboard per company OR portfolio.

### 1 Meta
- **zeus-co-factory** — Skill Factory. Builds new LEPs on demand.

## Anatomy of each LEP

```
zeus-co-{name}/
├── .claude-plugin/plugin.json
├── README.md
└── skills/{name}/
    ├── SKILL.md            # Entry point
    ├── CORE.md             # Identity, frameworks, heuristics, orchestration logic
    ├── LITERATURE.md       # Bibliography in 4 layers (canonical / living / cases / Brazil)
    ├── RADAR.md            # MCPs/tools (installed / evaluating / wishlist)
    ├── EVOLUTION.md        # Changelog
    ├── WEEKLY_DIGEST.md    # Cron-updated weekly
    └── templates/          # 4-6 canonical artifact templates
```

## Founding principle

> **C-levels are OPERATORS, not judges.**
> Each LEP exists to MAKE the company work — not to issue contemplative reports.
> Verbs of execution, never of evaluation. Diagnosis only as bridge to action.

## Auto-evolution

Every department has a weekly cron that scans:
1. New literature (newsletters, blogs, papers)
2. New tools/MCPs (mcp-registry + Anthropic changelog)
3. Function trends
4. Cross-company learnings (synthesizes LEARNINGS.md from all companies)

Output: WEEKLY_DIGEST.md per LEP + entry in INBOX.md root for review.

## Install in Claude.ai/Cowork

1. Open Cowork → **Customize** → **Plugins pessoais** → **`+`** → **Criar plugin** → **Adicionar marketplace**
2. URL: `https://github.com/{your-username}/zeus-co`
3. Sync — all 11 plugins appear
4. Enable each plugin from the list

## License

Private. Built for Diego Martins's portfolio. Adapt at your own risk.
