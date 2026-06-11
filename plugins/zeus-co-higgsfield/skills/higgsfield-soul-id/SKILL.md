---
version: 1.0.0
name: higgsfield-soul-id
description: |
  Treina um Soul Character — modelo personalizado no rosto de uma pessoa que
  o Higgsfield usa pra gerar imagem e vídeo face-faithful (identidade fiel).
  Use quando: "treina meu rosto", "cria meu Soul", "faz meu gêmeo digital",
  "monta um avatar pra mim", "aprende minha aparência", "cria personagem com
  meu rosto", "configura identidade pra vídeo", "quero meu rosto em imagens
  geradas", "treina rosto do <sócio>", "treina rosto do influenciador X".
  Fluxo: treinar Soul (one-time, retorna reference_id) → usar no
  higgsfield-generate via `--soul-id <id>` com modelos como
  `text2image_soul_v2` ou `soul_cinema_studio`. NÃO use para: face swap
  single-shot (use higgsfield-generate com --image), avatares de personagem
  fictício / não-foto (use higgsfield-generate com prompt).
argument-hint: "[nome] [paths das fotos...]"
allowed-tools: Bash
---

# Higgsfield Soul Character (wrapper Zeus-CO)

## Identidade

Treina um modelo face-faithful de identidade. Reutilizável em todas as gerações Soul-powered (text2image_soul_v2, soul_cinema_studio, etc.).

Wrapper Zeus-CO sobre a skill oficial [`higgsfield-soul-id`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT).

## Pré-requisito one-time

```bash
npm install -g @higgsfield/cli
higgsfield auth login
higgsfield account status     # Soul training exige plano pago (Basic+)
```

Se `account status` mostrar plano free, AVISAR Diego antes de submeter.

## UX Rules

1. Conciso. Sem IDs crus no chat. Falar "Soul pronto" com referência ao nome.
2. Responder em pt-BR. Flags CLI ficam em inglês.
3. Pedir o conjunto MÍNIMO de inputs: nome + fotos. Escolher variant sensato.
4. Polling silencioso — treino leva minutos. Não repetir status updates.

## Workflow

1. **Pegar nome.** Uma palavra, usado pra referência depois. Perguntar se faltou.
2. **Pegar fotos.** 5-20 fotos do rosto, ângulos e iluminações variados. Paths locais OU IDs já uploadados — `--image` aceita os dois.
3. **Escolher variant:**
   - `--soul-2` — pra geração de imagem (default)
   - `--soul-cinematic` — pra trabalho cinemático / vídeo
   Default `--soul-2` salvo se Diego falar explicitamente "vídeo".
4. **Submeter** e aguardar silenciosamente.
5. **Entregar** `reference_id` salvo (formato: `soul_<nome>_<timestamp>`).

Guia de fotos detalhado em `references/photo-guide.md`. Troubleshooting em `references/troubleshooting.md`.

## Use cases canônicos no portfolio Zeus-CO

### UC1 — Sócios celebridades das empresas
- 2ndStreet/dope street: Neymar + Akkari (com autorização contratual via `clo-ip`)
- Crazyflips: founders, talents da produtora
Cross com `clo-ip` (rights) + `cco-brand-guardian`.

### UC2 — Influencers em programa de creator-economy
Treina rosto do creator → gera variações pra A/B test sem precisar nova sessão de foto. Cross com `creator-economy` + `clo-contratos`.

### UC3 — Brand persona / avatar mascote
Marca cria avatar consistente que aparece em campanhas. Cross com `cco-art-director` + `zeus-co-cmo:cmo-branding`.

### UC4 — Diego em comms institucional
Pra LinkedIn / podcast art / palestras. Cross com `ceo-comms`.

## Self-Evaluation (3 modos)

### Modo A — Cowork desktop
`~/Documents/Claude/Projects/_Pulse/skill-feedback/higgsfield-soul-id-YYYY-MM-DD.md`

### Modo B — Claude.ai web
Printar Self-Eval no chat.

### Modo C — Autônomo
PASS/PARTIAL/FAIL heurístico.

## Trabalha em equipe com

### Upstream
- `cco-art-director` (decide identidade necessária)
- `creator-economy` (treina rostos de creators)
- `ceo-comms` (treina rosto Diego pra comms)

### Peers
- `higgsfield-generate` (consome o `reference_id` que eu produzo)
- `higgsfield-product-photoshoot` (modo `virtual_model_tryout` pode usar Soul)

### Downstream
- `higgsfield-generate` (recebe o Soul-ID pronto)

### QA pair
- `clo-ip` (rights de uso de rosto de terceiros)
- `clo-contratos` (creator agreement antes de treinar)
- `cco-brand-guardian` (consistência da identidade gerada com brand)

## Channel Skill — não-LEP

Despachada por: `cco-art-director`, `creator-economy`, `zeus-co-cmo:cmo-branding`, Diego direto.

## Skill genérica — context vem da empresa

Antes de treinar rosto de **alguém que não é Diego**:
1. Ler `_Areas/CLO/contratos/` da empresa pra confirmar autorização de uso de imagem
2. Se não há contrato — BLOQUEAR e escalar pra `clo-contratos`
3. Documentar `reference_id` em `_Areas/CCO/soul-ids.md` da empresa

## Fim de sessão

### LEARNINGS.md
- YYYY-MM-DD · higgsfield-soul-id · [lição treino] · [importa pra próximos]

### BACKLOG.md
- [P0|P1|P2] · [próximo Soul ou geração derivada] · Owner

### _LEDGER.md
- YYYY-MM-DD HH:MM · higgsfield-soul-id · [UC1..UC4] · ~N turnos · reference_id

### _Areas/CCO/soul-ids.md (catálogo de identidades treinadas)
- YYYY-MM-DD · `soul_<nome>_<ts>` · [pessoa] · [contrato/autorização ref] · [usado em: empresa X campanha Y]

---

## Crédito + atribuição

Skill original: [`higgsfield-ai/skills`](https://github.com/higgsfield-ai/skills) (Higgsfield AI, MIT). Wrapper Zeus-CO com gatilhos pt-BR + integração com `clo-ip`/`clo-contratos` + catálogo de identidades por empresa.
