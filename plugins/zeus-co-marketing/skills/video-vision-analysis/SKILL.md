---
name: video-vision-analysis
description: Video Vision Analysis — análise estruturada de vídeos via plugin externo `claude-video-vision` (Jordan Vasconcelos, MIT). Frame extraction (ffmpeg) + audio transcription (Whisper/Gemini/OpenAI). Use SEMPRE pra "analisar vídeo", "watch video", "análise YouTube", "análise filme publicitário", "análise creator content", "análise drop", "análise live commerce gravada", "análise comportamento jogador <empresa>", "extrair narrativa de vídeo", "video reference analysis", "Cannes case video breakdown". Suporta arquivo local OU URL YouTube.
---

# Video Vision Analysis

## Identidade

Análise estruturada de **conteúdo audiovisual** — referências criativas, drops gravados, lives commerce, creator UGC, vídeos de concorrentes, cases premiados.

Eu **NÃO** sou o motor de análise — sou o **WRAPPER ZEUS-CO** que define use cases canônicos + prompts adequados pra invocar o plugin externo [`claude-video-vision`](https://github.com/jordanrendric/claude-video-vision) (Jordan Vasconcelos, MIT).

## Princípio inviolável

**Análise de vídeo SEM brief = lista descritiva inútil.** Antes de pedir análise:
1. Empresa atual + brand-guide + writing-guide (Fase 0 Descoberta Interna)
2. Objetivo da análise (referência criativa? competitive intel? performance? case study?)
3. O que extrair especificamente (narrativa? técnica visual? mensagem? CTA?)

Sem brief, output vira "vídeo mostra pessoa falando com fundo X." Inútil.

## Pré-requisito (one-time setup)

### Instalação plugin externo (Diego executa 1×)
```
/plugin marketplace add https://github.com/jordanrendric/claude-video-vision
/plugin install claude-video-vision
```

Setup wizard:
```
/setup-video-vision
```

### Dependências de sistema
- **Node 20+** (já tem)
- **ffmpeg** — `brew install ffmpeg` (frame extraction)
- **yt-dlp** — `brew install yt-dlp` (YouTube URLs)
- **Audio backend** (escolher 1):
  - Gemini API (free tier — recomendado start)
  - Whisper local via Homebrew (`brew install whisper-cpp`)
  - OpenAI API (Whisper)

### Config canon (`~/.claude-video-vision/config.json`)
```json
{
  "backend": "gemini",
  "frame_format": "jpeg",
  "frame_resolution": 512,
  "default_fps": "auto",
  "max_frames": 100,
  "enable_index": true,
  "session_max_age_days": 7
}
```

## 8 Use cases canônicos pro Zeus-CO

### Use case 1: ANÁLISE DE REFERÊNCIA CRIATIVA (Cannes/Effie/D&AD)
**Quando:** Fase 4b do pipeline marketing (processo criativo).
**Cross com:** `processo-criativo-pesquisa`, `cerebro-criativo`.

**Prompt template:**
```
/watch-video <URL ou path do filme premiado>

Analise como SE FOSSE um diretor de criação estudando autoria.

Extraia:
1. Estrutura narrativa (3 atos? Save the Cat? Hero's Journey?)
2. Hook nos primeiros 5s (visual + áudio)
3. Beats emocionais (timestamps onde tom muda)
4. Big Idea identificável (1 frase)
5. Técnicas visuais distintivas (cor, ritmo, framing)
6. Música/sound design role
7. CTA implícito ou explícito
8. Por que ganhou Cannes/Effie (hipótese)

Output: `_Areas/CMO/<projeto>/04b-processo-criativo/<case>.md`
```

### Use case 2: ANÁLISE DE DROP CELEBRITY (<empresa> específico)
**Quando:** <sócio>/<sócio> postou orgânico usando peça.
**Cross com:** `live-marketing`, `creator-economy`.

**Prompt template:**
```
/watch-video <URL post Instagram/TikTok>

Contexto: <empresa> drop, peça <sócio>/<sócio>.

Extraia:
1. Identificar peça (NFC cataloging cross-ref)
2. Contexto físico (onde foi gravado, evento, ambiente)
3. Autenticidade do uso (peça aparece naturalmente vs forçada)
4. Engagement signals visuais (reação celebs presentes)
5. Hashtags + menções no vídeo
6. Quotables (frases que podem virar caption nossa)
7. UGC opportunity (vale pedir permissão pra repost?)

Output: `_Areas/CCO/dropdetect/<celeb>-<data>.md`
QA: clo-ip (rights de uso da imagem)
```

### Use case 3: ANÁLISE DE LIVE COMMERCE GRAVADA
**Quando:** Pós-live TikTok/IG/Shopee analisar performance.
**Cross com:** `live-commerce`, `xpto-mk:analista-marketing`.

**Prompt template:**
```
/watch-video <gravação da live>

Contexto: live commerce <empresa>/<empresa>, GMV = R$ X, viewers = N.

Extraia timestamps de:
1. Primeiros 60s — hook que segurou audience
2. Momentos de pico (concurrent viewers — verificar com plataforma)
3. Drops na audience (que produto/momento perdeu people?)
4. Calls que mais geraram comments
5. Produtos com mais clicks (cross-ref com dados plataforma)
6. CTAs que converteram (transcrição exata)
7. Tom + energia host (queda? consistência?)

Output: `_Areas/CMO/<projeto>/lives/post-mortem-YYYY-MM-DD.md`
```

### Use case 4: ANÁLISE DE CREATOR UGC
**Quando:** Creator entregou conteúdo pago — validar antes de boost.
**Cross com:** `creator-economy`, `cco-brand-guardian`.

**Prompt template:**
```
/watch-video <vídeo creator entregue>

Contexto: deal creator-economy, briefing era [resumo brief].

Valida:
1. Mandatórios do brief cumpridos? (hashtag, claim, link, etc.)
2. Tom alinhado com writing-guide?
3. Visual alinhado com brand-guide? (cores, peça correta, ambiente)
4. CONAR disclosure presente? (#publi visível)
5. Mensagem proibida usada? (cross writing-guide palavras proibidas)
6. Hook qualidade
7. Engagement signals (energy, autenticidade)

Decision: aprovar pra boost / pedir ajuste / rejeitar
Output: `_Areas/CCO/creator-deliverables/<creator>/<vídeo>.md`
QA: cco-brand-guardian + clo-contratos (usage rights)
```

### Use case 5: COMPETITIVE INTEL VIDEO
**Quando:** Concorrente lançou campanha — entender o que estão fazendo.
**Cross com:** `xpto-mk:tendencias-criativas-br`, `cino-tech-scouting`.

**Prompt template:**
```
/watch-video <URL filme/campanha concorrente>

Contexto: análise competitiva, concorrente = X.

Extraia:
1. Posicionamento manifesto (qual território estratégico?)
2. Target inferido (visualmente)
3. Tom + voz da marca
4. Produção budget estimado (cinematografia, casting, locação)
5. Insight central (1 frase)
6. Hooks usados
7. Quanto investiram em mídia (estimar baseado em produção)
8. Gap deles que <empresa>/empresa nossa pode atacar

Output: `_Areas/CMO/<projeto>/competitive/<concorrente>-<data>.md`
```

### Use case 6: ANÁLISE DE GAMEPLAY (<empresa> iGaming)
**Quando:** Vídeo de gameplay próprio ou concorrente — entender padrões.
**Cross com:** `kp-gambling-techniques`, `kp-brazil-player-behavior`, `clo-setorial`.

**Prompt template:**
```
/watch-video <gameplay vídeo>

Contexto: iGaming <empresa>, análise UX + comportamento.

Extraia:
1. Game mechanics observáveis (RTP visual, near-miss frequency)
2. UI/UX clarity (clareza apostas, payouts)
3. Behavioral nudges identificáveis (cross kp-gambling-techniques)
4. Player emotional journey (frustration peaks? excitement peaks?)
5. Stopping points naturais
6. Compliance signals (jogo responsável visível?)

⚠️ ATENÇÃO: análise interna apenas. NÃO usar pra marketing externo (CONAR + SECAP restrições).
Output: `<empresa>/_Areas/Research/gameplay-analysis/<vídeo>.md`
QA: clo-setorial (compliance)
```

### Use case 7: ANÁLISE DE FILME PUBLICITÁRIO PRÓPRIO (PÓS-EXIBIÇÃO)
**Quando:** Nossa campanha foi ao ar — análise post-mortem.
**Cross com:** `xpto-mk:analista-marketing`, `cco-brand-guardian`.

**Prompt template:**
```
/watch-video <filme próprio>

Contexto: campanha [nome] da [empresa], objetivo era [KPI].

Análise pós-exibição:
1. Hook funcionou? (atenção primeiros 5s)
2. Mensagem central foi clara? (recall test mental)
3. Brand presence balanceada? (não-invasiva nem omissa)
4. CTA executável? (audience sabe o que fazer?)
5. Pacing (tédio? confusão?)
6. Lições pra próxima

Cross-ref com performance real (CTR, conversão, brand lift se mediu).
Output: `_Areas/CMO/<projeto>/post-mortems/<campanha>.md`
```

### Use case 8: TRANSCRIÇÃO + LEGENDAGEM DE EVENTOS DIEGO
**Quando:** Diego deu entrevista, palestra, podcast — extrair quotables.
**Cross com:** `ceo-comms`, `cco-storytelling`.

**Prompt template:**
```
/watch-video <YouTube URL palestra/podcast Diego>

Contexto: comunicação externa Diego.

Extraia:
1. Quotables fortes (frases que podem virar post)
2. Insights que valem virar tweet thread
3. Momentos memoráveis (timestamps)
4. Storytelling que aparece (manter pra reuso)
5. Tom + voz Diego (validação consistência cross-aparições)

Output: `_Areas/CEO/comms/quotables/<evento>-YYYY-MM-DD.md`
```

## Heurísticas operacionais

### Backend choice (recomendação)
- **Inicio:** Gemini API (free tier, sem setup local)
- **Volume alto:** Whisper local cpp (zero custo recorrente, requer setup macOS)
- **Premium quality:** OpenAI Whisper API (mais preciso PT-BR)

### FPS strategy
- **Análise estética / visual:** alta fps (8-12) — capta movimento
- **Análise de fala / conteúdo:** baixa fps (1-2) — frames suficientes
- **YouTube longa duração:** "auto" deixa Claude decidir

### Token economy
- Cada frame = ~500 tokens vision
- Análise de 60s a 8fps = 480 frames = 240k tokens de input
- **Cap responsável:** max 100 frames default (configurable)
- Pra vídeos longos, dividir em segmentos OU usar baixa fps

## Limitações conhecidas

- ⚠️ Frames são amostras — perdem motion entre frames
- ⚠️ Whisper PT-BR pode errar gírias regionais — validar
- ⚠️ YouTube auto-captions podem estar ruins — preferir manual subtitles quando existe
- ⚠️ Análise emocional via frames é limitada — áudio + transcrição compensam
- ⚠️ Custo escala com duração + fps — guarda-rail necessário


## Trabalha em equipe com

### ⬆️ Upstream
- `marketing-orquestrador` (qualquer fase que precise análise vídeo)
- `processo-criativo-pesquisa` (UC1 Cannes/Effie)
- `cco-brand-guardian` (UC4 validação creator)

### 🤝 Peers
- `xpto-mk:tendencias-criativas-br` (UC5 competitive)
- `xpto-mk:analista-marketing` (UC3 e UC7 — cross dados quanti)
- `cerebro-criativo` (transformar análise em ideia nova)
- `live-commerce` (UC3 specific)
- `creator-economy` (UC4 specific)
- `ai-generative-creative` (gerar vídeos pós-análise referência)

### ⬇️ Downstream
- `cco-brand-guardian` (QA output)
- `processo-criativo-pesquisa` (UC1 alimenta)
- `clo-setorial` (UC6 <empresa> compliance)
- `clo-ip` (UC2 rights uso imagem celeb)

### ✅ QA pair
- `cco-brand-guardian` (output alinhado brand)
- `clo` (UC2/UC6 — rights + compliance)


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · video-vision-analysis · [lição da análise] · [importa pra próximos]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação derivada da análise] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · video-vision-analysis · [UC1|UC2|UC3|UC4|UC5|UC6|UC7|UC8] · ~N turnos · path

### 4. _Inbox.md (opcional — quando análise gerou sugestão proativa)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-video-analysis.md`.

---

## Crédito + atribuição

Skill plugin externo: [`claude-video-vision`](https://github.com/jordanrendric/claude-video-vision) por Jordan Vasconcelos (@jordanrendric), licença MIT. Esta skill é **wrapper Zeus-CO** que define use cases + prompts canônicos pra aproveitar o plugin no portfolio Diego.
