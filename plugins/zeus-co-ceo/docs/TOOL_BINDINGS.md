# TOOL_BINDINGS — CEO Office

## Tabela canônica

| Intenção | Ferramenta | Quando |
|---|---|---|
| **Lean Canvas / BMC visual** | `anthropic-skills:canvas-design` ou Figma MCP | Visualização do modelo |
| **OKRs spreadsheet** | `anthropic-skills:xlsx` | Tracking trimestral |
| **Modelo financeiro** | `financial-analysis:3-statement-model` + `zeus-co-cfo:cfo-fpa` | Runway + projeção |
| **DCF valuation** | `financial-analysis:dcf-model` | Decisão captação / venda |
| **Comps benchmarking** | `financial-analysis:comps-analysis` | Comparação setorial |
| **Pitch deck investor** | `investment-banking:pitch-deck` + Gamma MCP | Captação |
| **Initiating coverage** | `equity-research:initiating-coverage` | Quando empresa vira pública (futuro) |
| **Strategic narrative** | `anthropic-skills:docx` + `xpto-mk:copywriting` | Manifesto + posicionamento |
| **Board pack** | `zeus-co-board:board-pack-builder` | Reunião board mensal/trimestral |
| **Decision memo** | `zeus-co-board:decision-memo-author` | Type 1 irreversível |
| **Email comms** | Gmail MCP | Investor update mensal |
| **Calendar 1on1s** | Google Calendar MCP | Cadência fixa com C-Suite |
| **Pulse portfolio** | `zeus-co-pulse:pulse` | Estado cross-empresa |
| **Scout melhorias** | `zeus-co-scout:scout` | Auto-improvement |

## Bindings por skill

- `ceo` (chief) → orquestra demais + Pulse
- `ceo-bizops` → `anthropic-skills:xlsx` + cto-data (analytics cross-funcional)
- `ceo-chief-of-staff` → Gmail + Google Calendar + `pulse` + handoff matrix
- `ceo-comms` → `anthropic-skills:docx` + `xpto-mk:copywriting` + Gmail + `ceo-ir`
- `ceo-estrategia` → `financial-analysis:dcf-model` + `financial-analysis:comps-analysis` + `private-equity:returns`
- `ceo-ir` → Gamma + `investment-banking:pitch-deck` + Gmail
- `ceo-orquestrador` ⭐ NEW → coordena todos
- `ceo-okrs-keeper` ⭐ NEW → xlsx + Notion (se conectado)
- `ceo-fundraising` ⭐ NEW → `investment-banking:pitch-deck` + comps + Gamma
- `ceo-north-star-keeper` ⭐ NEW → xlsx + `zeus-co-cto:cto-data` (dashboard)
