# TOOL_BINDINGS — Procurement

| Intenção | Ferramenta |
|---|---|
| **Spend analysis** | xlsx + cruza Dashfin (Plata-ou-Plomo) |
| **RFP/RFQ docs** | `anthropic-skills:docx` |
| **Contract** | cross `clo-contratos` |
| **Vendor scorecard** | xlsx + Notion |
| **Tail spend cards** | Cards corporativos (Caju/Conta Simples/Stark Bank) |
| **AI assistance** | `claude-api` + WebSearch |

## Bindings

- `procurement` → orquestra
- `procurement-orquestrador` → coordena
- `procurement-strategic-sourcing` → docx (RFP) + WebSearch (mercado fornecedor)
- `procurement-category-mgr` → xlsx (categoria analysis) + WebSearch
- `procurement-tail-spend` → API cards (Caju/Conta Simples) + claude-api (automação)
