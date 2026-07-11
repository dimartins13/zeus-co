# zeus-co-watch — Claude assiste vídeo

Skill canônica de vídeo do Zeus-CO. Dá ao Claude um input de vídeo real: baixa, extrai frames, transcreve e entrega tudo pro Claude responder sobre o que está no vídeo — **vê** os frames e **ouve** a transcrição.

Fork de [bradautomates/claude-video](https://github.com/bradautomates/claude-video) (MIT), patcheado pro stack do Diego.

## O que muda vs upstream

| Aspecto | Upstream | Esta build (Zeus-CO) |
|---|---|---|
| Transcrição | Cloud Whisper (Groq/OpenAI), pede API key, manda áudio pra nuvem | **faster-whisper LOCAL** (`~/.zeus-co/venv-whisper`), grátis, privado, auto-detecta PT/EN |
| YouTube | Sem cookies → muro "confirm you're not a bot" | **`--cookies-from-browser chrome`** por padrão (com fallback sem cookie) |
| Legendas | Só EN | **PT + EN** (prefere PT) |
| Cloud | Padrão | Dormente (só com `--whisper groq\|openai` + key) |

## Arquitetura

- **Contrato** (este plugin, no marketplace): `SKILL.md` + `plugin.json`. É o que o Cowork descobre e dispara.
- **Engine** (estável, fora do cache de plugin): `~/.zeus-co/watch/scripts/` — junto do `venv-whisper`. Imune ao cache `plugin_XXXX` do Cowork.

Scripts: `watch.py` (entry) · `download.py` (yt-dlp + cookies) · `frames.py` (ffmpeg) · `transcribe.py` (VTT) · `whisper_local.py` (faster-whisper local) · `whisper.py` (cloud dormente) · `setup.py` (preflight).

## Uso

```
/watch https://youtu.be/<id> o que acontece no minuto 2?
/watch ~/Movies/screen-recording.mov quando a UI quebra?
/watch https://www.tiktok.com/@user/video/123 resume isso
```

Foco em trecho (mais frames, menos token): `--start 2:15 --end 2:45`.

## Dependências

`ffmpeg` + `yt-dlp` (Homebrew) · `~/.zeus-co/venv-whisper` (faster-whisper, modelo `small` já cacheado). Tudo já presente na máquina do Diego.

## Pré-requisito YouTube

Estar logado no YouTube **no Chrome** (os cookies são lidos read-only pra autenticar o yt-dlp). Safari não funciona (sandbox do macOS bloqueia leitura dos cookies).
