# TOOL_BINDINGS — Board + Founders

> Ferramentas usadas por skills do zeus-co-board.

## Tabela canônica

| Intenção | Ferramenta | Quando |
|---|---|---|
| **Deck board pack** | Gamma (`mcp__2801b3d7-*__generate`) | Apresentação mensal/trimestral |
| **Deck investor** | Gamma ou `anthropic-skills:pptx` | Investor pitch, update visual |
| **Memo Word** | `anthropic-skills:docx` | Decision memo formal, governance charter |
| **Spreadsheet cap table** | `anthropic-skills:xlsx` ou `financial-analysis:audit-xls` | Cap table waterfall, vesting schedule |
| **PDF assinatura** | `anthropic-skills:pdf` | Contratos de advisor, term sheets |
| **Agenda Cal** | Google Calendar MCP | Schedule board meetings |
| **Email convocação** | Gmail MCP | Convite board + envio pack |
| **Diagrama org/cap** | `mcp-image` (quando disponível) ou Canva MCP | Organograma + waterfall visual |
| **Comps fundraise** | `financial-analysis:comps-analysis` + `private-equity:returns` | Valuation benchmarking |
| **Pitch deck investor** | `investment-banking:pitch-deck` + `equity-research:initiating-coverage` | Captação Series A+ |
| **Term sheet review** | `anthropic-skills:docx` + `zeus-co-clo:clo-contratos` | Negociação investidor |

## Bindings por skill

- `founders-office` → Gmail + Google Calendar (proteger agenda Diego)
- `board-governance` → `anthropic-skills:docx` (charter, statutes)
- `board-advisors-management` → Gmail + `anthropic-skills:docx` (advisor agreement template)
- `board-pack-builder` → Gamma + `anthropic-skills:xlsx` (métricas) + `pulse` (dados portfolio)
- `decision-memo-author` → `anthropic-skills:docx` (template ADR)
- `cap-table-keeper` → `anthropic-skills:xlsx` + `financial-analysis:audit-xls`
- `equity-vesting-manager` → `anthropic-skills:xlsx` + `zeus-co-clo:clo-trabalhista` (vesting CLT/PJ)
- `board-orquestrador` → coordena todas

## Princípios

- **Documentos formais = `docx` ou `pdf`.** Não markdown solto.
- **Cap table sempre em `xlsx`** com fórmulas vivas (não PDF estático — vesting muda).
- **Decision memo segue padrão ADR** (Architecture Decision Record adaptado pra governance).
- **Board pack: visual (Gamma deck) + documental (Docx memo) sempre os dois.**
