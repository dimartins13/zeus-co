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

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/facilities-it-asset-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · facilities-it-asset · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
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

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

Antes de encerrar QUALQUER sessão deste LEP, escrever nessa ordem. Sem isso, sessão não fechou.

### 1. LEARNINGS.md (empresa atual)
Append 1-3 lições durables. Formato:
```
- YYYY-MM-DD · facilities-it-asset · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · facilities-it-asset · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · facilities-it-asset · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
```

### 4. _Inbox.md (opcional — quando vale)
Se nasceu sugestão proativa que Diego não pediu mas merece atenção dele, append bloco:
```
## [SUGESTÃO] [título curto] · YYYY-MM-DD
- **O quê:** 1 linha
- **Por quê (gatilho):** 1 linha
- **Próximo passo:** 1 linha
- **Status:** [aguarda Diego]
```

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-facilities-it-asset.md` no mesmo formato consolidado.

