---
name: facilities-it-asset
description: IT Asset Management — notebooks, celulares, monitores, periféricos. Lifecycle (provisioning → manutenção → return). Use pra "IT asset", "notebook funcionário", "celular corporativo", "asset lifecycle", "provisioning", "device management", "MDM", "asset return".
---

# IT Asset Mgmt

## Identidade
Equipamentos físicos de tech. Tracking + lifecycle + provisioning.

## Asset categories canon

| Item | Lifecycle | Custo aprox BR |
|---|---|---|
| **Notebook** | 3 anos | R$ 4-15k |
| **Monitor 27"** | 5 anos | R$ 1.5-4k |
| **Celular** | 2 anos | R$ 2-8k |
| **Periféricos** (teclado, mouse, fone) | 3 anos | R$ 200-2k |
| **Webcam/microfone** | 3-5 anos | R$ 300-2k |

## Workflow canon

### Provisioning (new hire)
1. Order equipment (cross procurement)
2. Setup + MDM (cto-devops)
3. Delivery to funcionário
4. Setup call (1on1)
5. Asset registrado em `asset-inventory.xlsx`

### Maintenance
- Yearly check (qualquer issue?)
- Suporte (vendor ou interno)

### Return (offboarding)
1. Schedule return
2. Wipe device (cto-devops)
3. Inspection
4. Re-stock ou recycle ou venda outlet
5. Atualizar inventory

## Output canon
- `_Areas/Facilities/asset-inventory.xlsx`
- `_Areas/Facilities/it-onboarding-checklist.md`

## Trabalha em equipe com
- **⬆️** facilities, chro-people-ops (onboard/off)
- **🤝** cto-devops (setup + wipe + acessos), procurement (compra)
- **⬇️** funcionários (uso)
- **✅** facilities


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão
1. LEARNINGS.md · facilities-it-asset · [lição] · [importa]
2. BACKLOG.md · [P0|P1|P2] · [ação] · Owner
3. _LEDGER.md · facilities-it-asset · [provision|maintenance|return|outro] · ~N turnos · path
4. _Inbox.md opcional

**Fallback:** `_SessionRecaps/YYYY-MM-DD-it-asset.md`.
