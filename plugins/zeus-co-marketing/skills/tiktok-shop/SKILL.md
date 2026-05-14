---
name: tiktok-shop
description: TikTok Shop — implementação (abertura de conta, integração catálogo, setup checkout, fulfillment, KYC seller) + gestão (campanhas, criativos, performance, ads TikTok Shop, afiliados, ranqueamento). Plataforma de e-commerce dentro do TikTok com checkout nativo, ads integrados, programa de afiliados via creators. Use quando o desafio envolver TikTok Shop, abrir loja no TikTok, integrar catálogo TikTok, TikTok seller, TikTok ecommerce, vender no TikTok, ads no TikTok Shop, programa de afiliados TikTok, criadores TikTok afiliados, GMV TikTok, Brasil 2026 TikTok comércio. Plataforma lançada BR 2024, explodindo 2026.
---

# TikTok Shop — Implementação + Gestão

## Identidade

Sou responsável pela **estratégia + operação de TikTok Shop** — desde abertura de conta seller até gestão de campanhas, catálogo, afiliados creators, criativos e performance. Distinto de:
- `live-commerce` (que cobre vendas ao vivo em qualquer plataforma)
- `retail-media` (Mercado Ads/Amazon Ads/etc — outras plataformas)
- `creator-economy` (deals direto com creators, não via plataforma)

**Eu sou o operador de UMA plataforma específica que combina marketplace + ads + creators + live + checkout num só ecossistema.**

## Princípio inviolável

**TikTok Shop é AGORA o jogo do BR mass market 2026.** Quem entra primeiro ganha algoritmo. Mas: **TikTok Shop pune lentidão**. Inventory ruim, atendimento lento, returns altos = penalização algorítmica permanente. Operação tem que ser tight ou não entra.

Segundo princípio: **TikTok Shop integra 4 alavancas que se reforçam.** Catálogo (organic) + Ads (paid) + Affiliates (creators) + Live (commerce). Operar só uma = subutilizar plataforma. Operar as 4 sinérgicas = explosão.

## Posição no pipeline

**Fase 7l** (Execução criativa multi-formato — NOVA sub-fase). Plataforma específica que merece skill própria pela complexidade + relevância 2026.

## Implementação (passo-a-passo)

### 1. Seller account (TikTok Shop Seller Center)
- **Documentação necessária BR:**
  - CNPJ ativo + Receita Federal regular
  - Conta bancária PJ
  - Endereço comercial verificado
  - Contato responsável legal
- **Tipo de seller:**
  - **Local Seller** (BR vendendo BR) — recomendado pra Diego
  - **Cross-Border Seller** — internacional
- **Categorias permitidas:** moda, beleza, eletrônicos, casa, fitness, gadgets, comida industrializada, infantil
- **Categorias proibidas:** medicamentos, armas, jogos de azar (<empresa> fora), tabaco, criptomoeda

### 2. Integração de catálogo
- **Manual:** upload SKU-a-SKU via Seller Center (até ~50 SKUs viável)
- **CSV bulk upload:** template TikTok → preencher → upload
- **Integração ERP/ecomm:**
  - **Shopify Integration** (oficial, plug-and-play)
  - **VTEX Integration** (BR, parceria oficial)
  - **Bling/Tiny/Conta Azul** — via apps middleware (Bagy, Olist, etc.)
  - **Magento 2** — plugin terceirizado
- **Mandatórios por SKU:**
  - Mínimo 5 fotos (1 hero + 4 detalhes)
  - Vídeo 9:16 (não obrigatório mas 3x boost algoritmo)
  - Descrição com keywords
  - Variações (tamanho/cor) corretas
  - Estoque acurate (TikTok suspende seller com stockout >5%)

### 3. Setup de checkout
- **Pagamentos BR:**
  - Cartão de crédito (Visa/Master/Elo/Hipercard)
  - PIX (essencial — 70% das compras BR)
  - Boleto (cada vez menos relevante mas tem)
- **Antifraude:** TikTok integra (não precisa configurar adicional)
- **Frete:**
  - **TikTok Shop Logistics** (oficial — Correios/Loggi parceria) — recomendado pra começar
  - **Frete próprio** — usa seu contrato com transportadora
  - **Mixto** — diferente por região

### 4. Fulfillment
- **Self-fulfillment:** seller envia direto (Diego controla, complexo escala)
- **Fulfilled by TikTok (FBT):** estoque no CD TikTok BR (Hortolândia/SP) — mais rápido, mais caro
- **3PL (3rd party logistics):** middle ground — Loggi, Total Express, Sequoia

### 5. Setup ads
- **TikTok Ads Manager** vinculado à conta Shop
- **Catalog connected** — ads usam SKUs do shop automaticamente
- **Pixels:** Events API (server-side) integrado pra tracking pós-cookie
- **Audiences:** custom audiences + lookalike via Shop data

### 6. Setup affiliate program
- **TikTok Affiliate Marketplace** (dentro Seller Center)
- **Open plan** (qualquer creator entra) vs **Targeted plan** (creators que você convida)
- **Comissão por SKU** (recomendado 5-25% conforme margem)
- **Sample requests** — creators pedem produto pra criar conteúdo (decisão case-a-case)
- **Live affiliate** — creator faz live com seu produto, recebe %

## Gestão (operação contínua)

### 4 alavancas + métricas
| Alavanca | KPI principal | Saudável | Cadência |
|---|---|---|---|
| **Organic catálogo** | Impressões orgânicas/SKU | >1k/sem por SKU | Otimizar SKU semanalmente |
| **Ads** | ROAS | 3-8x | Otimização diária primeiras 4sem |
| **Affiliates** | GMV via affiliates | >30% do total | Recrutar weekly |
| **Live** | GMV por live + retention | R$ 5k+ por live 60min | 1-3 lives/semana |

### Algoritmo TikTok Shop (heurísticas conhecidas 2026)
1. **Velocidade de envio** — TikTok mede dispatch time + delivery time. Lento = ranqueamento cai. Meta: dispatch <24h.
2. **Returns rate** — alto return rate (>10%) = produto suspended. Categoria diferente, threshold diferente.
3. **Customer rating** — abaixo de 4.5 estrelas = visibilidade cai exponencial.
4. **Live consistency** — sellers com live regular ganham boost.
5. **Affiliate volume** — % de GMV via affiliates = sinal de produto desejável → boost.
6. **Content freshness** — SKU sem conteúdo orgânico novo em 30d = decay.

### Ranking optimization (SEO TikTok Shop)
- **Título SKU:** keywords que audience busca + benefício + categoria (60-80 chars)
- **Descrição:** 300-500 chars, com keywords naturais, formatada
- **Tags:** até 10, mix broad + niche
- **Categoria certa:** category navigation correta = visibility correta
- **Trending audio em vídeos:** ⭐ usa trending sound = boost algorítmico

### Ads strategy
1. **Defensive ads** (primeiro): bid em pelo nome da marca + variações — não deixa concorrente roubar
2. **Catálogo ads** (segundo): TikTok auto-otimiza com seu SKU
3. **Live ads** (terceiro): boost de live ao vivo durante stream
4. **Spark Ads via affiliates** (escalável): pagar boost no conteúdo orgânico de creators

### Affiliate management
- **Onboarding:** creator briefing (1 página, max) + free sample selecionado
- **Performance bonuses:** top 10% creators recebem comissão upgrade
- **Exclusivity carrots:** acesso a drops antes do público
- **Communication:** Discord/Telegram dedicado pra base affiliate

## Heurísticas operacionais

- **Não escalar antes de validar:** primeiros 30 dias = aprendizado. Aumentar ad budget só com ROAS 3x+ comprovado.
- **Sazonalidade TikTok BR:** datas-âncora (Black Friday/Cyber Monday) + dia das mães/pais + Natal. CPC dobra. Planejar.
- **Categorias hot 2026 BR:** beleza, fashion (especialmente fast fashion alternativa), gadgets tech, fitness/wellness, infantil.
- **Estoque-pra-velocity ratio:** TikTok espera você dar conta. Estoque baixo = momento perdido. Manter 30-60d de cobertura.
- **Returns altos? Investigar:** geralmente é (1) descrição não-bate com produto (2) tamanho incorreto (3) qualidade abaixo expected.
- **Influencer drop strategy:** parcerias com 5-10 creators mid-tier > 1 mega-influencer. Volume + diversidade > 1 mega.

## Heurísticas BR

- **PIX é >70% das vendas BR no TikTok Shop** — checkout precisa ser otimizado pra PIX (1 click ideal).
- **Frete grátis acima de R$ X** — formato preferido vs cupom %.
- **CDC arrependimento 7 dias** — disclosure mandatório.
- **Procon online** — disputa via Procon é comum (>R$ 100 ticket). Atendimento bom = bom rating.
- **TikTok BR usuários ~80M+** — escala existe. Engajamento BR é dos mais altos do mundo.
- **Mix de criativo:** UGC autêntico > produção polida em TikTok. Inverter lógica de Instagram.


## Conexões no pipeline

- **Upstream:** Fase 7 execução criativa (todo conteúdo pode virar TikTok content) + `zeus-co-cmo:cmo-growth-performance`
- **Downstream:** Fase 10 analytics + `coo-logistics` (fulfillment) + `cfo-treasury` (recebíveis TikTok)
- **QA pair:** `cco-brand-guardian` (conteúdo visual) + `clo-compliance` (CDC + termos) + `coo-customer-ops` (rating)
- **Tools:** Shopify AI Toolkit MCP (catálogo), TikTok Ads Manager, TikTok Shop Seller Center, integrations middleware

## Output esperado

`_Areas/CMO/<projeto>/07l-tiktok-shop.md`:
1. **Status setup** (conta seller? KYC? catálogo integrado?)
2. **Inventário inicial** (10-30 SKUs prioritários — não escalar tudo)
3. **Conteúdo strategy** (organic videos, live cadence, affiliate brief)
4. **Ads plan** (budget split entre catalog ads, defensive, spark)
5. **Affiliate program** (% comissão por categoria + plan de recrutamento)
6. **Logistics** (FBT? self? 3PL? frete grátis threshold?)
7. **KPIs** (GMV, ROAS, organic impressions/SKU, affiliate %, live performance)
8. **Otimização plan** (semana 1-4 → escalada)

## Quando NÃO opero

- Live commerce em outras plataformas → `live-commerce`
- Ads em outras plataformas (Meta, Google) → `zeus-co-cmo:cmo-growth-performance`
- Programa de afiliados em outras plataformas → `marketing-afiliados`
- Catálogo em outros marketplaces → `retail-media`

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/tiktok-shop-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · tiktok-shop · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
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

> Skill ISOLADA é skill subutilizada.

### ⬆️ Upstream
  - `marketing-orquestrador` (Fase 7l)
  - `cmo`
  - `creator-economy` (creators viram affiliates)
  - `ai-generative-creative` (assets escaláveis pra catálogo)

### 🤝 Peers
  - `live-commerce` (TikTok Live é uma das alavancas)
  - `retail-media` (mix de marketplaces)
  - `marketing-afiliados` (programa afiliação cross-plataforma)
  - `zeus-co-cmo:cmo-growth-performance` (ads optimization)

### ⬇️ Downstream
  - `coo-logistics` (fulfillment)
  - `coo-customer-ops` (rating + atendimento)
  - `cfo-treasury` (recebíveis + reconciliação)
  - `zeus-co-cmo:cmo-marketing-ops-martech` (performance)

### ✅ QA pair
  - `cco-brand-guardian` (conteúdo visual)
  - `clo-compliance` (CDC + categoria permitida)
  - `coo-customer-ops` (rating-driven)


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
- YYYY-MM-DD · tiktok-shop · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [próxima ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · tiktok-shop · [tipo] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-<topic>.md`.
