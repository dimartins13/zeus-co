---
name: watch
description: Dá ao Claude a capacidade de ASSISTIR vídeo (a "cegueira a vídeo" resolvida). Baixa o vídeo com yt-dlp (usa cookies do Chrome → fura o muro anti-bot do YouTube), extrai frames auto-escalados com ffmpeg, pega transcrição (legendas nativas grátis PT/EN → faster-whisper LOCAL do Zeus-CO como fallback, grátis e privado), e entrega frames + transcript pro Claude responder sobre o que está no vídeo. Use SEMPRE que o Diego colar uma URL de vídeo (YouTube, TikTok, Instagram, Vimeo, X, Loom, Twitch e centenas de sites yt-dlp) OU apontar um arquivo local (.mp4/.mov/.mkv/.webm) e perguntar algo, OU pedir "assiste esse vídeo", "vê esse vídeo", "analisa esse vídeo", "o que acontece em tal minuto", "resume esse vídeo", "que hook esse criador usou", "transcreve esse vídeo", "/watch". Transcrição é LOCAL por padrão (sem API key, sem custo, áudio não sai da máquina).
argument-hint: "<url-ou-caminho-do-video> [pergunta]"
allowed-tools: Bash, Read, AskUserQuestion
homepage: https://github.com/bradautomates/claude-video
license: MIT
user-invocable: true
---

# /watch — Claude assiste um vídeo

Você não tem input de vídeo nativo; esta skill te dá um. Um script Python baixa o vídeo, extrai frames como JPEGs, pega uma transcrição com timestamp (legendas nativas primeiro, depois faster-whisper LOCAL), e imprime os caminhos dos frames. Você então usa `Read` em cada caminho de frame pra VER as imagens e combina com a transcrição pra responder o Diego.

**Engine (local estável, NÃO no cache do plugin):** todos os scripts vivem em `$HOME/.zeus-co/watch/scripts/`. Sempre chame por esse caminho absoluto — o plugin no marketplace é só o contrato; o motor mora junto do `venv-whisper` em `~/.zeus-co/` (estável, imune ao cache de plugin do Cowork).

## Stack desta build (Zeus-CO)

- **Transcrição LOCAL por padrão:** faster-whisper rodando em `~/.zeus-co/venv-whisper/bin/python` (modelo `small`, CPU/int8, auto-detecta PT e EN). Grátis, privado, sem API key. O áudio NUNCA sai da máquina.
- **Cookies do Chrome:** `download.py` passa `--cookies-from-browser chrome` por padrão pra furar o "Sign in to confirm you're not a bot" do YouTube. Se falhar com cookie, refaz sem cookie automaticamente. Override via env `WATCH_COOKIES_FROM_BROWSER` (`none` desliga).
- **Legendas PT + EN:** puxa faixas em português e inglês; prefere PT quando existe.
- **Cloud Whisper (Groq/OpenAI) = dormente:** só entra se você forçar `--whisper groq|openai` e houver key em `~/.config/watch/.env`. Default é sempre local.

## Passo 0 — Preflight (roda a cada invocação, silencioso no sucesso)

```bash
python3 "$HOME/.zeus-co/watch/scripts/setup.py" --check
```

Lookup de <100ms. Exit 0 = nada impresso → siga pro Passo 1 sem comentar. **NÃO anuncie "setup completo".** Único output aceitável aqui é quando precisa remediar.

| Exit | Significado | Ação |
|------|-------------|------|
| `0` | ffmpeg + yt-dlp presentes | seguir |
| `2` | Falta binário (`ffmpeg`/`ffprobe`/`yt-dlp`) | rodar instalador: `python3 "$HOME/.zeus-co/watch/scripts/setup.py"` (auto-instala via brew no macOS) |

Não há mais gate de API key — a transcrição é local. Se o venv-whisper sumir, legendas ainda funcionam de graça; só vídeos sem legenda voltam frames-only (o report avisa).

Dentro de uma mesma sessão, pode pular o Passo 0 em chamadas `/watch` seguintes.

## Quando usar

- Diego cola URL de vídeo (YouTube, TikTok, Instagram, Vimeo, X, Loom, Twitch, +centenas) e pergunta algo.
- Diego aponta arquivo local (`.mp4`, `.mov`, `.mkv`, `.webm`, etc.) e pergunta.
- Diego digita `/watch <url-ou-caminho> [pergunta]`, ou pede "assiste/vê/analisa/resume/transcreve esse vídeo".

## Limites recomendados

- **Melhor precisão: vídeos < 10 min.** Cobertura de frames cai inversamente com a duração.
- **Tetos duros: 100 frames, 2 fps.** Custo de token cresce com nº de frames; o script mira budget por duração:
  - ≤30s → ~30 frames · 30s-1min → ~40 · 1-3min → ~60 · 3-10min → ~80 · >10min → 100 esparsos (warning impresso)
- Vídeo longo → considere perguntar ao Diego qual trecho antes de gastar token num scan esparso.

## Como invocar

**Passo 1 — separe a fonte da pergunta.** `/watch https://youtu.be/abc o que ele diz no início?` → fonte = `https://youtu.be/abc`, pergunta = `o que ele diz no início?`.

**Passo 2 — rode o script.** Passe a fonte literal:

```bash
python3 "$HOME/.zeus-co/watch/scripts/watch.py" "<fonte>"
```

Flags opcionais:
- `--start T` / `--end T` — foca num trecho. Aceita `SS`, `MM:SS`, `HH:MM:SS`. Ativa budget de frames mais denso.
- `--max-frames N` — baixa o teto pra economizar token (ex: `--max-frames 40`).
- `--resolution W` — largura do frame em px (default 512; suba pra 1024 só se precisar ler texto na tela: slides, terminal, código).
- `--fps F` — sobrescreve auto-fps (capado em 2 fps).
- `--out-dir DIR` — guarda os arquivos de trabalho em lugar específico (default: tmp auto).
- `--whisper local|groq|openai` — força backend. Default: legendas → local faster-whisper → cloud.
- `--no-whisper` — desliga transcrição (local e cloud); frames-only se não houver legenda.

Env vars (override sem editar código):
- `WATCH_COOKIES_FROM_BROWSER` — browser p/ cookies (default `chrome`; `none` desliga; `safari` exige Full Disk Access).
- `WATCH_WHISPER_MODEL` — modelo faster-whisper (default `small`; `medium`/`large-v3` mais precisos, mais lentos).
- `WATCH_WHISPER_LANG` — força idioma (ex `pt`); default auto-detecta.

### Focando num trecho (mais frames)

Quando o Diego nomeia um momento ("no minuto 2", "os primeiros 10 segundos", "de 0:45 a 1:00"), passe `--start`/`--end`. O script usa budget focado (mais denso, ainda capado a 2 fps). Transcrição é auto-filtrada pro mesmo range. Timestamps dos frames são absolutos (linha do tempo real).

```bash
python3 "$HOME/.zeus-co/watch/scripts/watch.py" video.mp4 --start 50 --end 60
python3 "$HOME/.zeus-co/watch/scripts/watch.py" "$URL" --start 2:15 --end 2:45
```

**Passo 3 — Read em CADA caminho de frame que o script listou.** O Read renderiza JPEGs direto como imagem pra você. Leia todos os frames numa única mensagem (chamadas Read em paralelo) pra ver tudo junto. Frames vêm em ordem cronológica com `t=MM:SS` (timestamp absoluto) pra alinhar com a transcrição.

**Passo 4 — responda.** Você tem dois fluxos de evidência: **frames** (o que está na tela em cada timestamp) e **transcript** (o que é dito). O header mostra a fonte (`captions` = legenda nativa yt-dlp; `whisper (local faster-whisper)` = transcrito local; `whisper (cloud ...)` = nuvem). Se houve pergunta, responda direto citando timestamps. Se não, resuma estrutura, momentos-chave, visuais e fala.

**Passo 5 — limpe.** O script imprime um working dir no final. Se o Diego não vai fazer follow-up sobre esse vídeo, apague com `rm -rf <dir>`. Se pode perguntar mais, deixe.

## Tratamento de falhas

- **Preflight exit 2** → `python3 "$HOME/.zeus-co/watch/scripts/setup.py"` (auto-instala ffmpeg/yt-dlp via brew no macOS).
- **YouTube "Sign in to confirm you're not a bot"** → o cookie do Chrome resolve (já é default). Se persistir, garanta que o Diego está logado no YouTube **no Chrome**. Safari é bloqueado pelo sandbox do macOS.
- **Sem transcrição** → legenda ausente E venv-whisper indisponível E sem key cloud. Siga frames-only e avise.
- **Warning de vídeo longo** → reconheça na resposta; ofereça re-rodar focado com `--start`/`--end`.
- **Download falha** (login/região) → o erro do yt-dlp vai pra stderr. Diga ao Diego claramente; não fique retentando.

## Eficiência de token

Custo é dominado por frames (cada frame é uma imagem). ~80 frames a 512px ≈ 50-80k tokens de imagem. Transcript é barato. `--resolution 1024` ~4× o custo por frame — só quando necessário. **Se já assistiu um vídeo nesta sessão e o Diego faz follow-up, NÃO re-rode o script — você já tem frames e transcript em contexto.**

## Segurança & Permissões

**O que esta skill faz:** roda `yt-dlp` localmente p/ baixar o vídeo + legendas nativas (usa cookies do Chrome só pra autenticar requests do próprio yt-dlp); roda `ffmpeg`/`ffprobe` localmente p/ extrair frames e (quando preciso) áudio mono 16kHz; transcreve LOCALMENTE via faster-whisper (`~/.zeus-co/venv-whisper`) — **áudio não sai da máquina**; grava vídeo/frames/áudio num working dir sob o tmp do sistema (ou `--out-dir`).

**O que NÃO faz:** não envia o vídeo nem o áudio pra nenhuma API por padrão (transcrição é local); só manda áudio pra nuvem se você forçar `--whisper groq|openai` com key configurada; não faz login em conta de plataforma (cookies são lidos read-only só pra requests yt-dlp, nunca postados/compartilhados); não loga nem grava chaves; não persiste nada fora do working dir (+ `~/.config/watch/.env` se você optar por cloud).

**Scripts (em `~/.zeus-co/watch/scripts/`):** `watch.py` (entry), `download.py` (yt-dlp + cookies), `frames.py` (extração ffmpeg), `transcribe.py` (parse de legenda VTT), `whisper_local.py` (faster-whisper local — Zeus-CO), `whisper.py` (cloud Groq/OpenAI — dormente), `setup.py` (preflight + instalador).
