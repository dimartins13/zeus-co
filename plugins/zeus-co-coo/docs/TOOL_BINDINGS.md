# TOOL_BINDINGS — COO Office

| Intenção | Ferramenta |
|---|---|
| **SOPs documentation** | `anthropic-skills:docx` + Notion MCP |
| **Inventory spreadsheet** | `anthropic-skills:xlsx` |
| **Process diagram (SIPOC, flowchart)** | Miro MCP ou Figma MCP |
| **Project tracking** | ClickUp MCP (já instalado) |
| **Customer comm** | WhatsApp Business API + Gmail MCP |
| **Vendor contracts** | `anthropic-skills:docx` + `zeus-co-clo:clo-contratos` |
| **Logistics tracking** | API transportadoras (Correios, JadLog, Loggi) |
| **Dashboard ops** | `zeus-co-cto:cto-data` + html dashboards |
| **Returns workflow** | ClickUp + ERP (Bling/Omie/Conta Azul) |
| **Quality metrics** | xlsx + dashboards |
| **Incident management** | ClickUp + Slack/Discord (alerts) |
| **Knowledge base** | Notion MCP |

## Bindings por skill

- `coo` (chief) → orquestra + Pulse
- `coo-diretor` → ClickUp + dashboards + 1on1s
- `coo-supply` → xlsx + ERP + forecast (cfo-fpa cross)
- `coo-vendor` → docx + clo-contratos + scorecard xlsx
- `coo-sops` → docx + Miro/Figma (diagramas)
- `coo-customer-ops` → WhatsApp API + Gmail + ClickUp tickets
- `coo-logistics` → API transportadora + xlsx tracking
- `coo-orquestrador` ⭐ NEW → coordena
- `coo-quality-ops` ⭐ NEW → xlsx + post-mortem docs
- `coo-returns` ⭐ NEW → ClickUp workflow + ERP returns + clo (CDC compliance)
- `coo-pmo` ⭐ NEW → ClickUp + RAID log xlsx + Notion (project space)
