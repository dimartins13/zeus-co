---
name: design-lab-email-html
description: Emails HTML transacionais e marketing — welcome, cart abandonment, win-back, newsletter, drop announce. Skill detalhada do marketing-creative + integração com cmo-crm-lifecycle (Klaviyo/HubSpot). Use pra 'email HTML', 'newsletter', 'welcome email', 'drop email', 'transacional', 'email marketing'.
---

# Design Lab Email Html

## Princípio
Email = mobile-first + low cognitive load. Hero clear, 1 CTA, scannable.

## Quando uso
- Drop announcement (D2C)
- Welcome flow (CRM lifecycle)
- Cart abandonment
- Newsletter editorial
- Transacional (compra, envio, devolução)

## Output canônico
1. HTML responsivo (table-based pra max compat)
2. Plain-text fallback
3. Subject line (3-5 variants)
4. Pre-header optimization
5. Test render Litmus-ready

## Resources (orquestrador puxa on-demand)
- `resources/skills-detalhadas/marketing-creative/` (email skills)
- `resources/integracoes/freepik-pipeline.md` (hero image)

## Skill genérica — context vem da empresa
Fase 0 Descoberta Interna obrigatória: ler `CLAUDE.md` + `00_INDEX.md` + `_Areas/CCO/brand-guide.md` da empresa atual antes de criar nada.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

### Modo A — Cowork desktop (Diego presente + filesystem)
Append em `~/Documents/Claude/Projects/_Pulse/skill-feedback/design-lab-email-html-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · design-lab-email-html · ambiente=cowork-chat · sucesso=[1-5] · gap=... · sugestao=... · empresa=<X>
```

### Modo B — Claude.ai web / Chat tab (Diego presente, sem fs)
Printa no fim do chat: `📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=...`

### Modo C — Autônomo (cron/scheduled)
Append fs com `sucesso=auto` (PASS/PARTIAL/FAIL via heurística).

## Trabalha em equipe com

### ⬆️ Upstream
- `design-lab-orquestrador`

### 🤝 Peers
- `cmo-crm-lifecycle` (Klaviyo/HubSpot ops)
- `cco-copy-master` (subject + body)

### ⬇️ Downstream
- Klaviyo/HubSpot MCP (deploy)

### ✅ QA pair
- `cco-brand-guardian`, `cmo-crm-lifecycle`

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · design-lab-email-html · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · design-lab-email-html · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-design-lab-email-html.md`.
