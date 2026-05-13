# TOOL_BINDINGS — Zeus-CO Labs

| Intenção | Ferramenta |
|---|---|
| **Log analysis** | Bash + grep + Python scripts em `~/.zeus-co/scripts/labs/` |
| **Papers research** | WebSearch + WebFetch (arXiv, HuggingFace papers, Anthropic blog) |
| **Prompt analysis** | Read SKILL.md + claude-api |
| **Experiments** | Custom Python scripts + xlsx |
| **Safety monitoring** | Bash + Read LEARNINGS/LEDGER + claude-api eval |
| **ADRs** | `anthropic-skills:docx` + `decision-memo-author` template |
| **Reporting** | docx + Gamma (executive summary) |

## Bindings

- `labs-director` → orquestra
- `labs-orquestrador` → coordena
- `llm-researcher` → WebSearch (arXiv) + claude-expert cross
- `prompt-architect` → Read SKILL.md + claude-api + Bash grep
- `skill-effectiveness-analyst` → Bash (parse logs) + xlsx + claude-api
- `safety-alignment-monitor` → Read LEARNINGS/LEDGER + claude-api eval scripts
