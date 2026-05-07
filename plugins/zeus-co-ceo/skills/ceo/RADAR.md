# RADAR — CEO/Founder

> Ferramentas, MCPs e connectors que este LEP usa, está avaliando, ou quer.
> Atualizado automaticamente pelo cron `ceo-weekly`.

## ✅ Instalados (em uso ativo)

Ferramentas que o CEO LEP **invoca diretamente** durante operação.

### Planejamento e estratégia
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Notion** | MCP (`mcp__plugin_brand-voice_notion__*`) | Repositório de OKRs trimestrais, board pack, planos estratégicos, decision memos. Single source of truth de governança. |
| **ClickUp** | MCP (`mcp__60f907d8...`) | Gestão de tarefas/sprints multi-empresa. Dashboard cross-portfolio. |
| **Linear** (plugin disponível) | MCP | Roadmap + OKRs tracking quando tech-product driven. Alternativa ao ClickUp pra empresas product-led. |
| **Asana** | plugin | Alternativa em projetos com múltiplos stakeholders externos. |

### Comunicação (orquestração + IR)
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Gmail** | MCP (`mcp__3a7681c7...`) | Investor updates, board emails, drafts importantes. Search threads pra contexto histórico. |
| **Google Calendar** | MCP (`mcp__3ca73a72...`) | Bloqueio de tempo do fundador, schedule de board, all-hands. |
| **Slack** | plugin | Team comms (quando empresa tem equipe humana além do Diego). |
| **WhatsApp / Telegram** | apps | Operacional. Diego prefere assíncrono. |

### Apresentação e narrativa
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Gamma** | MCP (`mcp__2801b3d7...`) | Geração rápida de decks (board, all-hands, investor). Templates já no padrão do Diego. |
| **Canva** | MCP | Peças visuais one-pager, deck refinado quando design importa mais. |
| **Adobe Marketing** | MCP | Suite completa quando precisa direção de arte sênior (raro pra CEO). |

### Modelagem (até CFO LEP existir)
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Skills `financial-analysis:*`** | skills | 3-statement model, DCF, comps, LBO. CEO usa quando precisa modelagem rápida sem chamar CFO. |
| **Skills `private-equity:*`** | skills | IC memo, returns IRR/MOIC, value creation 100-day plans. |
| **Skills `equity-research:*`** | skills | Thesis, sector analysis, initiating coverage (útil pra entrar em mercado novo). |
| **Skills `investment-banking:*`** | skills | Pitch deck institucional, teaser anônimo, CIM. |

### Brand foundation
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Skills `brand-voice:*`** | skills | Quando empresa precisa de brand voice formal pra externalizar narrativa. |

### Storage e arquivos
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **Google Drive** | MCP (`mcp__220c44d9...`) | Storage de docs, modelos financeiros, board pack arquivado. |
| **1Password** | app | Credentials de TODAS as plataformas (Diego nunca digita senha em arquivo). |

### Discovery e evolução
| Ferramenta | Tipo | Pra que serve |
|---|---|---|
| **mcp-registry** | MCP (`mcp__mcp-registry__*`) | Buscar novos connectors/MCPs. Cron semanal varre isso. |
| **scheduled-tasks** | MCP (`mcp__scheduled-tasks__*`) | Criar e gerenciar crons (incluindo o `ceo-weekly`). |
| **WebSearch + WebFetch** | tools | Research de mercado, competitive intel, validação de tese. |

## 🔍 Avaliando (testado, decisão pendente)

*Vazio na criação inicial. Cron semanal preencherá.*

## 🎯 Wishlist (gap identificado, sem solução ainda)

Funções que o CEO LEP precisaria fazer mas não tem ferramenta adequada hoje.

| Gap | Ferramenta ideal (se conhecida) | Workaround atual |
|---|---|---|
| **Cap table management** | Carta, Pulley, Capdesk | Spreadsheet manual em Google Sheets. Aceitável até série A. |
| **Board management formal** | BoardEffect, Boardable, Diligent | Notion + Gamma + Gmail. Fricção alta quando board > 5 pessoas. |
| **OKRs tracking visual** | Lattice, 15Five, WorkBoard | ClickUp + Notion manual. Falta visualização de progresso cross-empresa. |
| **Investor CRM** | Affinity, Visible, AngelList Stack | Notion manual. Crítico quando entrar em fundraising sério. |
| **Crypto/Token cap table** (Crazyflips NFT) | Coinbase Custody, Magna, Liquifi | Não resolvido. Risco real pra Crazyflips. |
| **Stock options / vesting** (quando hire) | Pulley, Carta Equity | N/A enquanto for solo. |
| **Investor data room** | DocSend, Brex Vault | Google Drive com permissões. Funcional mas sem analytics de quem leu. |

## 📅 Radar Semanal (novidades pendentes de avaliação)

*Vazio na criação inicial. Cron `ceo-weekly` preencherá.*

Padrão de entrada quando preenchido:
- `[YYYY-MM-DD]` **{Nome do tool}** — fonte: {mcp-registry / blog / changelog Anthropic / Product Hunt}. O que faz: {1 frase}. Próxima ação proposta: {testar em [empresa] / instalar direto / descartar}.

## 🚫 Descartados

*Vazio na criação inicial.*

## Princípio de adoção de ferramenta

CEO LEP segue 3 critérios pra adotar tool:

1. **Reduz tempo do fundador?** Se não economiza ≥30 min/semana de Diego, descarta.
2. **Funciona em portfolio?** Se serve uma empresa só e a outra ainda usa solução antiga, é fragmentação. Padronizar.
3. **MCP nativo?** Preferir tool com MCP — operação via Claude é o default. Tools sem MCP só se a alternativa for inviável.

---

*Atualização semanal automática pelo cron `ceo-weekly`.*
*Última varredura manual: 2026-05-06.*
