---
name: facilities-real-estate
description: Corporate Real Estate — portfolio físico, leases, hub-and-spoke decisions, due-diligence localização, occupancy planning, lease management, exit strategy. Distinto de `facilities-workspace` (operação do escritório) — real estate é a decisão de TER/CONTRATAR/ENCERRAR o espaço. Use pra alugar escritório, renovar contrato, abrir filial, rescindir aluguel, hub-and-spoke decision, occupancy planning, sale-leaseback.
---

# Corporate Real Estate

Reporta a `zeus-co-facilities:facilities` e `facilities-orquestrador`.

Detalhes em [`CORE.md`](./CORE.md).

## Princípio
**Lease é compromisso multi-anual. Decisão de real estate amarra OPEX por 3-10 anos.** Cuidado.

## Output canônico

1. **Portfolio map** (sedes, hubs, satélites, coworking, virtual)
2. **Lease calendar** (renovações, breakpoints, exit)
3. **Hub-and-spoke decision matrix** (cidades, fit, custo)
4. **Site selection criteria** (proximidade talento, custo, infra, regulação)
5. **Occupancy planning** (capacity vs forecast)
6. **Exit strategy** quando lease termina ou empresa shrink

## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Características próprias da empresa — usar essas

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · facilities-real-estate · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · facilities-real-estate · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-real-estate.md`.

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/facilities-real-estate-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · facilities-real-estate · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
```

**Critérios de sucesso:**
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

**Gap = oportunidade de evolução.** Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

Esse arquivo é lido semanalmente pelo `zeus-co-labs:labs-orquestrador` e pelo `<lep>-self-feedback` correspondente.

## Trabalha em equipe com

### ⬆️ Upstream
  - `facilities`, `facilities-orquestrador`
  - `cfo-fpa` (impacto financeiro multi-year)
  - `ceo-estrategia` (decisão de geografia)

### 🤝 Peers
  - `facilities-workspace` (depois de lease assinado, ele projeta)
  - `facilities-sustainability-esg` (critério verde no site selection)
  - `clo-contratos` (lease negotiation legal)
  - `clo-setorial` (regulação local, IPTU, ITBI)

### ⬇️ Downstream
  - Vendors (JLL, CBRE, Cushman, Newmark, brokers locais)
  - Landlords / sublocadores

### ✅ QA pair
  - `cfo-fpa`, `clo-contratos`

**Princípio operacional:** quando minha saída implica em ação de outra função, eu **delego explicitamente** invocando a skill correta.
