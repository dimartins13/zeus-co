---
name: facilities-vendor-soft-services
description: Soft Services Vendor Management — cleaning, catering, recepção, mailroom, jardinagem, pest control, segurança patrimonial vendor. Contratos, SLA, performance review. Cross com `procurement-category-mgr` (sourcing estratégico) e `coo-vendor` (vendors operacionais). Use pra contratar serviço de limpeza, catering, recepção, jardinagem, pest control, monitorar SLA de vendor de prédio, renegociação contrato facilities.
---

# Soft Services Vendor Management

Reporta a `zeus-co-facilities:facilities` e `facilities-orquestrador`.

Detalhes em [`CORE.md`](./CORE.md).

## Princípio
**Soft services parecem commodity, mas SLA ruim = experiência ruim no escritório.** Vendor management = quality at source via contrato.

## Output canônico

1. **Vendor list por categoria** (cleaning, catering, recepção, mailroom, etc)
2. **SLAs específicos** (frequência, response time, quality threshold)
3. **Performance dashboard** (NPS interno, complaint rate, on-time)
4. **Contract calendar** (renovações, breakpoints)
5. **Budget allocation** (% por categoria)
6. **Vendor RFP templates** quando aplicável

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Características próprias da empresa — usar essas

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · facilities-vendor-soft-services · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · facilities-vendor-soft-services · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-vendor-soft.md`.

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

Sistema vivo opera em **3 ambientes** distintos. Adaptar comportamento:

### Modo A — Interativo Cowork desktop (Diego presente + filesystem disponível)
Escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/facilities-vendor-soft-services-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · facilities-vendor-soft-services · ambiente=cowork-chat · sucesso=[1-5] · gap=[gap ou "nenhum"] · sugestao=[1 frase] · empresa=[<empresa>]
```

### Modo B — Interativo Claude.ai web / sem filesystem (Diego presente, sem Bash)
**Printar Self-Evaluation NO CHAT** no fim do output (Diego copia pra Project Knowledge se quiser preservar):
```
📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=... · empresa=...
```
NÃO tentar escrever filesystem (vai falhar).

### Modo C — Autônomo (cron launchd / Cowork Scheduled, sem Diego presente)
Escrever no filesystem com nota **heurística** (não tem Diego pra dar 1-5):
```
- YYYY-MM-DD HH:MM · facilities-vendor-soft-services · ambiente=[cron-launchd|scheduled-task] · sucesso=auto · gap=[detectado via heurística: missing canônico, timeout, error] · sugestao=[se aplicável] · empresa=[<empresa>]
```
Heurística pra `sucesso=auto`:
- **PASS** = output cumpriu output canônico + sem erro + dentro do tempo esperado
- **PARTIAL** = output cumpriu parcialmente OU warning
- **FAIL** = erro, timeout, output não-canônico

### Critérios de sucesso (Modo A, com Diego)
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

### Gap = oportunidade de evolução
Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

### Fluxo no labs-orquestrador
- Modo A + B + C são agregados separadamente (sample sizes diferentes)
- Modo A é fonte primária de signal (Diego feedback real)
- Modo C é fonte secundária (regression detection — skill quebrou em produção?)
- Modo B é capturado por copy-paste manual do Diego pra Project Knowledge

## Trabalha em equipe com

### ⬆️ Upstream
  - `facilities`, `facilities-orquestrador`

### 🤝 Peers
  - `facilities-workspace` (vendor é executor do que workspace projeta)
  - `procurement-category-mgr` (sourcing estratégico)
  - `procurement-tail-spend` (compras pequenas recorrentes)
  - `clo-contratos` (contratos vendor)
  - `cfo-controller` (custo)

### ⬇️ Downstream
  - Vendors (OCS, Millennium Group, ISS, Compass Group BR)

### ✅ QA pair
  - `procurement-category-mgr`, `clo-contratos`

**Princípio operacional:** quando minha saída implica em ação de outra função, eu **delego explicitamente** invocando a skill correta.
