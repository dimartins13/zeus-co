# TOOL_BINDINGS — CLO Office

| Intenção | Ferramenta |
|---|---|
| **Contratos drafting** | `anthropic-skills:docx` (templates) |
| **PDF revisão** | `anthropic-skills:pdf` |
| **Tracking contratos (CLM)** | Notion MCP + xlsx |
| **Decision memos legais** | `decision-memo-author` |
| **INPI/JUCESP/IBGE consultas** | WebSearch + WebFetch |
| **Compliance research** | WebSearch (legislação BR atualizada) |
| **Litigation tracking** | xlsx + Notion |
| **M&A due diligence** | `anthropic-skills:xlsx` + `financial-analysis:audit-xls` |
| **Termos de uso/Privacy** | `anthropic-skills:docx` (templates LGPD-compliant) |
| **Risk dashboard** | xlsx + Pulse cruzamento |

## Bindings por skill

- `clo` (chief) → orquestra
- `clo-compliance` → Notion (canal de denúncia) + docx
- `clo-contratos` → docx + Notion CLM
- `clo-ip` → INPI search + WebSearch + docx
- `clo-lgpd` → docx + WebSearch (ANPD) + cto-security cross
- `clo-trabalhista` → docx + cfo-controller cross (folha)
- `clo-setorial` → WebSearch setor + docx
- `clo-orquestrador` ⭐ NEW → coordena
- `clo-litigation` ⭐ NEW → xlsx + Notion + advogado externo (interface)
- `clo-ma` ⭐ NEW → financial-analysis + docx + private-equity:returns
