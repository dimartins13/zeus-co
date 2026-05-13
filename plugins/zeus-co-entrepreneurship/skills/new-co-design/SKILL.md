---
name: new-co-design
description: New Co Design — design completo de empresa nova end-to-end. Lean Canvas → modelo → cap table inicial → estrutura societária → setup CNPJ+bank+plataforma → Zeus-CO replicado → handoff CEO. Use pra "criar empresa nova", "new co design", "MVP company setup", "Lean Canvas inicial", "estrutura societária nova", "CNPJ setup", "day 1 empresa".
---

# New Co Design

## Identidade
Crio empresa nova do zero. Output: empresa funcional + estrutura Zeus-CO ativada.

## Princípio inviolável
**Setup ruim = passivo eterno.** CNPJ errado, regime fiscal errado, sócio mal escolhido = arrasta empresa anos. Vale 2 semanas a mais pra fazer certo.

## Workflow canon (4 semanas)

### Semana 1: Modelo de negócio
- Lean Canvas detalhado
- Unit economics rascunhadas (cross `cfo-fpa`)
- Persona + JTBD (cross `cino-research`)

### Semana 2: Estrutura
- Cap table inicial (Diego sozinho? co-founder? % split?)
- Estrutura societária (LTDA simples / LTDA com holding / SA)
- Acordo de quotistas (se mais de 1 sócio)

### Semana 3: Setup operacional
- CNPJ + JUCESP
- Bank PJ (Nubank/Conta Simples/Stark Bank)
- Contador (mensal)
- Conta de luz + endereço comercial
- Domínio + email empresarial
- Logo + identidade inicial (cross `cco` + `naming-domain`)

### Semana 4: Zeus-CO ativado
- Pasta `~/Documents/Claude/Projects/<empresa>/`
- Estrutura canon (CLAUDE.md + 00_INDEX + 00_STAGE + LEARNINGS + BACKLOG + _LEDGER + _Inbox + _Areas/)
- Heartbeat launchd configurado
- Mirror GitHub configurado
- Pulse cross-empresa atualizado
- Day 0 with CEO LEP active

## Output canon
- `_Areas/Entrepreneurship/new-cos/<empresa>/birth-memo.md`
- `_Areas/Entrepreneurship/new-cos/<empresa>/lean-canvas.md`
- `_Areas/Entrepreneurship/new-cos/<empresa>/cap-table-initial.xlsx`
- `_Areas/Entrepreneurship/new-cos/<empresa>/setup-checklist.md`

## Heurísticas BR

- **MEI primeiro** (até R$ 81k/ano) pra teste minimal
- **LTDA via Simples Nacional** pra primeiro R$ 4.8M revenue
- **LTDA Presumido** quando Simples vira gargalo (margem alta)
- **SA** SÓ se planeja IPO ou complexity high
- **Holding** quando portfolio Diego >R$ 1-2M agregado

## Trabalha em equipe com
- **⬆️** entrepreneurship-orquestrador
- **🤝** cino-research (validation), naming-domain, cco (brand)
- **⬇️** cap-table-keeper, ceo-orquestrador da empresa nova, cfo-tax (regime)
- **✅** Diego, clo-contratos (legal), cfo


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão
1. LEARNINGS.md · new-co-design · [lição] · [importa]
2. BACKLOG.md · [P0|P1|P2] · [ação] · Owner
3. _LEDGER.md · new-co-design · [canvas|structure|setup|launch|outro] · ~N turnos · path
4. _Inbox.md opcional

**Fallback:** `_SessionRecaps/YYYY-MM-DD-new-co.md`.
