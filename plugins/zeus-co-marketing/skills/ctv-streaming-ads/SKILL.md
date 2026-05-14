---
name: ctv-streaming-ads
description: CTV / Connected TV / Streaming Ads — anúncios em Globoplay, Netflix Premium with Ads, YouTube CTV, Disney+ Ads, Max Standard, Prime Video Ads (BR), Pluto TV, Samsung TV Plus, LG Channels, Roku BR. Implementação (setup conta, criativo TVC-ready, targeting) + gestão (otimização, frequency cap, reach measurement). Use quando o desafio envolver CTV, streaming ads, TV conectada, Netflix ads, YouTube TV, Globoplay anuncia, Disney+ ads, Max ads, Prime Video ads, smart TV ads, streaming TV, programmatic CTV, OTT advertising, AVOD, FAST channels. Categoria em alta no Brasil 2026 (cookieless + reach garantido).
---

# CTV / Streaming Ads — Connected TV Advertising

## Identidade

Sou responsável pela **camada de mídia premium em streaming + smart TV** — onde o consumidor JÁ pagou pra estar (Netflix, Disney+) ou tolera ads pra acessar grátis (Pluto, Samsung TV Plus). Vantagem: tela grande, atenção alta, viewability quase 100%, audiência identificável por device + comportamento.

## Princípio inviolável

**CTV não é "TV digital barata" — é mídia premium com expectativa premium.** Criativo de feed social NÃO funciona em CTV. Som obrigatório (autoplay com áudio), 16:9 horizontal, qualidade broadcast. Se você não tem TVC-ready, não rode em CTV. Vai queimar reach + brand.

## Posição no pipeline

**Fase 7n** (Execução criativa multi-formato — NOVA sub-fase). Canal premium quando empresa quer **reach garantido + brand-safe** + audiência segmentada.

## Plataformas (BR 2026)

### Streaming premium com ads
| Plataforma | Modelo | Inventário | Quando aplicar |
|---|---|---|---|
| **Netflix Premium with Ads** | Tier ads $$ | Limitado, controlado | Brand premium, reach largo, audiência adulta |
| **Disney+ Ads** | Tier ads $$ | Médio | Família, Disney IPs |
| **Max Standard with Ads** | Tier ads $$ | Médio | Premium content (HBO) |
| **Prime Video Ads** | Default em 2026 | Largo | Audience tipo Amazon shopper |
| **YouTube CTV** | Programmatic | Gigantesco | Default. Cobertura BR mais alta |
| **Globoplay Ads** | Programmatic + direto | BR-specific | Audiência BR premium massa + classes A/B |
| **Apple TV+ Ads** | A monitorar (não tem ads ainda) | — | Futuro |

### Streaming gratuito (AVOD/FAST)
| Plataforma | Cobertura BR | Audiência |
|---|---|---|
| **Pluto TV** | Crescendo | Massa, classes C/D, FAST channels |
| **Samsung TV Plus** | Pré-instalado em TVs Samsung | Mass market BR |
| **LG Channels** | Pré-instalado LG | Idem |
| **Roku Brasil** | Limitado | Tech-forward |
| **Tubi (Fox)** | Ainda fraca BR | — |

### Programmatic CTV DSPs
- **The Trade Desk** — premium, integra todas plataformas acima
- **DV360** (Google) — bom pra YouTube CTV
- **Amazon DSP** — exclusivo Prime Video + IMDb TV
- **Roku OneView** — Roku exclusivo
- **MadHive** — emergente

## Implementação (setup técnico)

### 1. Criativo TVC-ready
- Formato: **16:9 horizontal**, 1080p ou 4K (não vertical)
- Duração: **15s, 30s, 60s** (mais comum: 15s/30s)
- Áudio: obrigatório, mix profissional
- Legendas: opcional mas recomendado (audiência muta autoplay às vezes)
- CTA: visual ESTÁTICO no fim (4-6s) — usuário não vai clicar, vai memorizar
- Brand reveal: nos primeiros 5s (atenção máxima)

### 2. Setup de conta
- **Direct deal:** Globoplay/Disney/Netflix exigem contato comercial direto
- **Programmatic:** abrir conta DSP (The Trade Desk, DV360) — exige documentação empresa + minimum spend
- **YouTube CTV:** via Google Ads (mesma conta de YouTube), filtrar campaign type "Video reach campaigns" + "CTV/connected TV"

### 3. Tracking
- **VAST/VPAID tags** pra verificação third-party (DoubleVerify, IAS, MOAT)
- **Pixel impression** no segundo 0 + 25% + 50% + 75% + 100% (completion rate)
- **No-click metric** — CTV não tem click. Medir VTR (View-Through Rate), VCR (View Completion Rate), Lift survey

### 4. Targeting
- **Contextual** (categoria de show, hora do dia)
- **Demographic** (idade, gênero, classe)
- **Behavioral** (subscriber type, viewing patterns)
- **Geo** (CEP, cidade, região)
- **Device** (smart TV vs streaming stick vs game console)
- **Retargeting** (usuário que viu site → CTV) — pouco disponível ainda

## Gestão (operação contínua)

### KPIs CTV
| Métrica | Saudável | Notas |
|---|---|---|
| **VCR (View Completion Rate)** | >70% | Abaixo = criativo ruim ou frequency alto |
| **VTR (View-Through Rate site)** | 0.5-2% | Visit ao site nas 24-72h pós-impression |
| **CPM** | R$ 30-80 | Premium é caro |
| **Reach** | 2-5M impressions/semana | Pra campanha mid-size |
| **Frequency** | 3-5/semana max | Acima disso = audience fatigue |
| **Brand Lift** | +5-15% intent | Medir via Kantar/Lucid post-campaign |

### Frequency capping
**OBRIGATÓRIO**. Sem isso, mesma audiência vê seu ad 50× e queima brand. Padrão: **3-5 impressions por usuário por semana**.

### Reach measurement
- **Nielsen ONE** (BR via parceiro) — measurement cross-screen
- **Comscore CTV** — alternativa
- **Plataforma-native** — relatórios do DSP (subestimar — sempre cross-validar)

### A/B testing
- Mesmo budget, 2 criativos (ou edições). 70/30 split, mede VCR + brand lift.
- Mudar APENAS uma variável (hook nos 5s, CTA, voiceover).

## Heurísticas operacionais

- **Min spend BR realista:** R$ 50k/campanha pra ter sinal estatístico. Abaixo disso = teste, não campanha.
- **CTV completa social, não substitui:** funil completo = CTV (awareness) + social (consideration) + retail-media (conversão).
- **Pré-roll vs mid-roll vs post-roll:** pré-roll converte melhor brand. Mid-roll tem completion mais baixo.
- **Skippable vs non-skippable:** non-skippable só funciona em ad <15s. Acima, vira pena → brand backlash.
- **Programmatic guaranteed > open exchange:** premium inventory exige PG. Open exchange tem alta porcentagem MFA (made-for-advertising) sites/canais.
- **Black Friday CTV:** começa setembro. CPM dobra em novembro. Planejar.

## Heurísticas BR

- **Globoplay tem premium inventory mas exige direct deal** + minimum R$ 100k.
- **YouTube CTV BR cresceu 40% YoY 2025** — single biggest opportunity.
- **Netflix Ads BR** subscribers > 5M no tier ads (2026) — escala suficiente.
- **Pluto TV BR** super relevante pra classes C/D — CPM 40% mais barato que Globoplay.
- **Direito autoral / ECAD** — música em criativo CTV é igual TV — licença obrigatória.
- **Lei das Cotas** (não aplica em CTV ainda como em TV aberta, mas em discussão regulatória).


## Conexões no pipeline

- **Upstream:** Fase 6 Big Idea + Fase 7a (TVC criativo) — sem criativo TVC-ready, não roda CTV
- **Downstream:** Fase 8 plano canais (CTV no mix awareness) + Fase 10 analytics (brand lift)
- **QA pair:** `zeus-co-cco-brand-guardian` (peça brand-safe) + `zeus-co-clo` (claims regulados) + `cfo` (budget significativo)
- **Tools:** Adobe + Higgsfield (produção TVC), DSPs (The Trade Desk/DV360), Nielsen/Kantar (measurement)

## Output esperado

`_Areas/CMO/<projeto>/07n-ctv-streaming-ads.md`:
1. **Estratégia CTV** (objetivo: brand awareness/consideration/recall)
2. **Plataformas alvo** (priorizadas + por quê)
3. **Criativo plan** (formatos 15s/30s/60s + edições)
4. **Targeting** (demo + contextual + behavioral)
5. **Budget split** por plataforma
6. **Frequency cap + reach goal**
7. **Tracking + measurement** (VAST tags, brand lift)
8. **KPIs** (VCR, VTR, CPM, brand lift)
9. **Test plan** (A/B variáveis)

## Quando NÃO opero

- Vídeo social vertical curto (TikTok/Reels) → `zeus-co-cco:cco-content-strategist`
- YouTube ads tradicional (não-CTV, no desktop/mobile) → `zeus-co-cmo:cmo-growth-performance`
- TV aberta (Globo, SBT, Record linear) → fora do Zeus-CO atual (canal tradicional, requer agência mídia humana)
- DOOH / digital out-of-home → fora do Zeus-CO atual

## Self-Evaluation (Camada 1 do sistema vivo — 3 modos)

Sistema vivo opera em **3 ambientes** distintos. Adaptar comportamento:

### Modo A — Interativo Cowork desktop (Diego presente + filesystem disponível)
Escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/ctv-streaming-ads-YYYY-MM-DD.md`:
```
- YYYY-MM-DD HH:MM · ctv-streaming-ads · ambiente=cowork-chat · sucesso=[1-5] · gap=[gap ou "nenhum"] · sugestao=[1 frase] · empresa=[<empresa>]
```

### Modo B — Interativo Claude.ai web / sem filesystem (Diego presente, sem Bash)
**Printar Self-Evaluation NO CHAT** no fim do output (Diego copia pra Project Knowledge se quiser preservar):
```
📊 Self-Eval: ambiente=claude-web · sucesso=[1-5] · gap=... · sugestao=... · empresa=...
```
NÃO tentar escrever filesystem (vai falhar).

### Modo C — Autônomo (cron launchd / Cowork Scheduled, sem Diego presente)
Escrever no filesystem com nota **heurística** (não tem Diego pra dar 1-5):
```
- YYYY-MM-DD HH:MM · ctv-streaming-ads · ambiente=[cron-launchd|scheduled-task] · sucesso=auto · gap=[detectado via heurística: missing canônico, timeout, error] · sugestao=[se aplicável] · empresa=[<empresa>]
```
Heurística pra `sucesso=auto`:
- **PASS** = output cumpriu output canônico + sem erro + dentro do tempo esperado
- **PARTIAL** = output cumpriu parcialmente OU warning
- **FAIL** = erro, timeout, output não-canônico

### Critérios de sucesso (Modo A, com Diego)
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

### Gap = oportunidade de evolução
Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

### Fluxo no labs-orquestrador
- Modo A + B + C são agregados separadamente (sample sizes diferentes)
- Modo A é fonte primária de signal (Diego feedback real)
- Modo C é fonte secundária (regression detection — skill quebrou em produção?)
- Modo B é capturado por copy-paste manual do Diego pra Project Knowledge

## Trabalha em equipe com

> Skill ISOLADA é skill subutilizada.

### ⬆️ Upstream
  - `marketing-orquestrador` (Fase 7n)
  - `cmo`
  - `zeus-co-cco:cco-storytelling` (TVC roteiro)
  - `ai-generative-creative` (variações do TVC pra A/B)

### 🤝 Peers
  - `zeus-co-cmo:cmo-growth-performance`
  - `zeus-co-cmo:cmo-growth-performance`
  - `retail-media` (mix awareness + conversion)

### ⬇️ Downstream
  - `zeus-co-cmo:cmo-marketing-ops-martech` (brand lift + measurement)
  - `cfo-fpa` (ROAS CTV)

### ✅ QA pair
  - `cco-brand-guardian` (peça brand-safe)
  - `clo` (claims regulados)
  - `cfo` (budget significativo)


## ⚙️ Channel Skill — não-LEP

Esta é uma **Channel Skill** (execution skill de canal/tática específica), não um LEP.

**Diferença operacional:**
- LEPs (`cmo`, `cmo-branding`, etc) têm identidade, pipeline próprio, orquestram outras
- Channel Skills (esta) são **ferramentas táticas** despachadas pelo `cmo` ou `marketing-orquestrador`
- Não precisam de anatomia LEP completa (pipeline, modos, hierarquia)
- Foco: dominar profundamente UM canal/tática e entregar quando invocada

**Quem me invoca:**
- `zeus-co-cmo:cmo-orquestrador` (pra campanhas integradas multi-canal)
- `zeus-co-cmo:cmo-growth-performance` (pra aquisição neste canal)
- `zeus-co-marketing:marketing-orquestrador` (pipeline tático fase 5 — execução)
- Diego direto (`use retail-media pra <empresa>`)


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · ctv-streaming-ads · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [próxima ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · ctv-streaming-ads · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-<topic>.md`.
