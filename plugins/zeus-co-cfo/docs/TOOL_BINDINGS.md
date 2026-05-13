# TOOL_BINDINGS — CFO Office

| Intenção | Ferramenta |
|---|---|
| **Spreadsheets financeiros** | `anthropic-skills:xlsx` |
| **Audit / clean data** | `financial-analysis:audit-xls` + `financial-analysis:clean-data-xls` |
| **3-statement model** | `financial-analysis:3-statement-model` |
| **DCF valuation** | `financial-analysis:dcf-model` |
| **Comps analysis** | `financial-analysis:comps-analysis` |
| **LBO model** | `financial-analysis:lbo-model` |
| **Variance analysis** | `finance:variance-analysis` |
| **Reconciliação bancária** | `finance:reconciliation` |
| **Journal entries** | `finance:journal-entry` + `finance:journal-entry-prep` |
| **Financial statements** | `finance:financial-statements` |
| **Close management** | `finance:close-management` |
| **SOX testing** | `finance:sox-testing` + `finance:audit-support` |
| **Dashfin (Plata-ou-Plomo)** | Direct FTP / dashboard.html | 
| **Tax planning** | `private-equity:returns` + WebSearch (regulação BR) |
| **Investor returns** | `private-equity:returns` |
| **Pulse cross-empresa** | `zeus-co-pulse:pulse` |

## Bindings por skill

- `cfo` (chief) → orquestra + Pulse
- `cfo-diretor` → xlsx + variance + reconciliation
- `cfo-controller` → finance:financial-statements + journal-entry + close-management
- `cfo-fpa` → 3-statement-model + DCF + variance-analysis + comps
- `cfo-treasury` → reconciliation + xlsx + Bradesco/BTG/banco APIs
- `cfo-tax` → WebSearch (Reforma Tributária BR) + private-equity:returns
- `cfo-assistente` → docx + xlsx + Gmail
- `cfo-orquestrador` ⭐ NEW → coordena todos
- `cfo-ap-specialist` ⭐ NEW → finance:journal-entry-prep + xlsx + workflow Slack/Gmail
- `cfo-ar-specialist` ⭐ NEW → xlsx + Klaviyo/Gmail (dunning) + Stripe/Pagar.me APIs
- `cfo-investimentos` ⭐ NEW → xlsx + WebSearch (CDI/Selic atualizado) + corretora APIs (XP/BTG)
