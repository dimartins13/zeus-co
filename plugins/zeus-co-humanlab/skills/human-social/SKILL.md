---
name: human-social
description: Desdobra uma pasta de input (texto + imagens soltas + briefing fraco) em peças NATIVAS de Instagram Feed, Instagram Stories e LinkedIn, prontas pra postar — sem pedir briefing perfeito, sem aguardar copywriter, sem template genérico. Pega o que tem (1 foto crua de celular + 1 frase, ou 5 imagens + texto longo, ou só link de artigo) e devolve - (a) IG Feed 4:5 carrossel 3-6 slides ou single, headline + bullets curtas + CTA, copy de feed pronta com hooks e quebras de linha calibradas + 30 hashtags brasileiras segmentadas; (b) IG Stories 9:16 sequência de 3-8 frames com sticker positions sugeridas (enquete, caixa de perguntas, link), texto em camada por frame, transições; (c) LinkedIn post nativo - opening hook curto / desenvolvimento em 4-7 parágrafos com quebra forte / CTA / sem hashtag stuffing (3-5 max), versão long-form se o conteúdo pedir; (d) opcionalmente versão pra X/Twitter thread quando o input renderiza fio. Princípios duros — NÃO inventa fato (se input não tem dado, não chuta); NÃO usa AI-slop ("Em um mundo cada vez mais...", "É inegável que...", "Vamos mergulhar"); NÃO repete a mesma copy nos 3 canais (cada plataforma tem gramática própria - IG é visual-first, Stories é frame-a-frame, LinkedIn é texto-first com autoridade); NÃO pergunta o que dá pra inferir; respeita o DNA da marca se houver `DNA.md` no projeto, senão usa default editorial limpo. Output em `human-output/human-social/{run_slug}/` com subpastas `ig-feed/`, `ig-stories/`, `linkedin/`, cada uma com copy.md + assets renomeados/recortados quando viável (crop automático 4:5 → 9:16, redimensionamento via Pillow). Use SEMPRE para "/social", "/human-social", "desdobra essa pasta", "transforma isso em post", "post para IG e LinkedIn", "stories nativo", "publica isso", "preciso postar X em Y canais", "monta as peças sociais", "social pack", "kit de social", "carrossel sem ser de notícia", "desdobra texto em redes sociais", "tenho fotos e texto, quero virar post", "publica em IG Feed Stories e LinkedIn", "social media autorrelatável a partir de pasta", "vira essa pauta em peça nativa", colar pasta/arquivos + pedir post, ou colar artigo/texto longo pedindo "vira post pra IG e LinkedIn".
---

# Human Social — Desdobramento Nativo Multi-Canal

Você recebe uma **pasta** (texto solto + imagens + às vezes link de artigo) e devolve **3 entregáveis nativos**: IG Feed, IG Stories, LinkedIn. Cada um na gramática do canal. Sem AI-slop, sem template, sem chutar fato.

## A regra dura

- **Você não inventa fato.** Se a pessoa não disse o número, você não escreve número. Se não disse o nome, você não inventa nome. Lacuna vira pergunta curta ou some.
- **Você não repete a mesma copy nos 3 canais.** IG é visual-first (a copy serve a imagem), Stories é frame-a-frame (texto em camada por frame), LinkedIn é texto-first (autoridade, parágrafos com quebra forte).
- **Você não usa AI-slop.** Banido: "Em um mundo cada vez mais...", "É inegável que...", "Vamos mergulhar", "no fim do dia", "game-changer", "transformador" como adjetivo solto, emoji decorativo sem função.
- **Você não pergunta o que dá pra inferir.** Olha a pasta, lê o que tem, decide. Pergunta só se faltar algo que muda a peça (CTA destino, data de campanha, restrição de marca).

## Pré-requisitos

```bash
which jq && python3 -c "from PIL import Image; print('ok')"
```

`jq` pra parsear manifests; `Pillow` pra crop/resize. Se faltar, dirija a pessoa pra instalar antes de rodar (não bloqueie a peça por isso — entrega texto e marca asset como "pendente recorte").

DNA da marca: se existir `DNA.md` na pasta do projeto atual (`pwd`) ou em `~/{brand-slug}/DNA.md`, **leia e aplique**. Tom, palavras proibidas, palavras-âncora, paleta. Sem DNA: usa default editorial limpo (frase média 12-18 palavras, voz ativa, zero adjetivo decorativo).

## Pasta de trabalho

Output sempre em:

```
human-output/human-social/{YYYY-MM-DD-tema-slug}/
├── ig-feed/
│   ├── copy.md          ← headline + corpo + CTA + 30 hashtags
│   ├── slide-01.jpg     ← 4:5 (1080×1350)
│   ├── slide-02.jpg
│   └── ...
├── ig-stories/
│   ├── copy.md          ← texto por frame + sticker positions
│   ├── frame-01.jpg     ← 9:16 (1080×1920)
│   ├── frame-02.jpg
│   └── ...
├── linkedin/
│   ├── copy.md          ← post nativo + variante long-form se aplicável
│   ├── image-01.jpg     ← 1:1 ou 1.91:1 (1200×1200 ou 1200×627)
│   └── ...
└── manifest.json        ← input, decisões, assets originais → finais
```

Crop/resize automático: input 4:5 → 9:16 com smart crop centralizado; input quadrado → 4:5 com fundo borrado (gaussian blur do próprio asset). Se a foto não couber: avise e gere placeholder visual em vez de empurrar imagem distorcida.

---

## Fluxo

### 1. Leia a pasta

```bash
ls -la {pasta-input}
file {pasta-input}/*       # detectar tipo real (jpeg, png, txt, md, pdf)
```

Separe mentalmente:
- **Textos** (.txt, .md, .pdf, .docx, link colado em chat) → fonte editorial
- **Imagens** (.jpg, .png, .heic) → assets visuais
- **Vídeo** (.mp4, .mov) → ignore aqui (manda pra `/human-cinematic` ou `/human-motion`)
- **Briefing solto** (frase do usuário) → intent

### 2. Diagnostique em uma frase

Antes de gerar qualquer peça, devolva ao usuário **uma frase** com o diagnóstico:

> "Você tem 4 fotos de produto + 1 parágrafo sobre lançamento. Vou montar carrossel de 4 slides pro Feed, sequência de 5 frames pros Stories com enquete no frame 3, e LinkedIn texto-first com 1 imagem hero. CTA: link na bio. Confirma?"

Espera **um sim curto** antes de rodar tudo. Não pergunte 5 coisas — confirma o pacote em uma frase.

### 3. Gere as 3 peças em paralelo

**IG Feed (copy.md)**
- Linha 1: hook curto (≤8 palavras), específico, sem clichê
- Linhas 2-N: corpo curto (até 4 parágrafos), quebra dupla entre blocos
- Última linha: CTA explícito (1 ação só)
- Bloco final: 30 hashtags brasileiras segmentadas (5 marca / 10 nicho / 10 cauda longa / 5 lugar quando aplicável)
- Slides: headline grande em slide 1; bullets curtas (≤7 palavras) em slides 2-N; slide final = recap + CTA

**IG Stories (copy.md)**
- 1 frame = 1 mensagem. Não enfia parágrafo inteiro num frame.
- Frame 1: hook visual + 1 frase
- Frames 2 a N-1: dado/insight/imagem com texto em camada
- Frame com sticker: marque `[ENQUETE: pergunta]` ou `[CAIXA DE PERGUNTAS: prompt]` ou `[LINK: destino]`
- Frame final: CTA + sticker

**LinkedIn (copy.md)**
- Opening: 1-2 linhas que param o scroll (zero hashtag, zero emoji aqui)
- Quebra forte (linha em branco) entre todo parágrafo
- 4-7 parágrafos curtos (1-3 frases cada)
- Sem listas com bullet-point genérico — se for lista, numera e justifica
- CTA final: pergunta aberta pra comentário OU link no primeiro comentário (avisa no post)
- 3-5 hashtags no rodapé, segmentadas por tópico, não por busca

Se o conteúdo couber em texto longo (autoral, contraintuitivo, com dado), gere também **variante long-form** (800-1500 palavras) em `linkedin/long-form.md`.

### 4. Recorte os assets

Use Pillow para gerar os formatos:

```python
from PIL import Image, ImageFilter

def to_4x5(img_path, out_path):
    # smart crop centralizado pra 1080x1350
    pass

def to_9x16(img_path, out_path):
    # crop pra 1080x1920, se source não cabe usa fundo blurred do próprio
    pass

def to_linkedin(img_path, out_path):
    # 1:1 default (1200x1200) ou 1.91:1 (1200x627) se source é wide
    pass
```

Salve cada asset no formato nativo do canal. Não force tudo no mesmo crop.

### 5. Entregue + próximo passo

Devolva pasta pronta + uma linha:

> "Pacote em `human-output/human-social/2026-06-02-lancamento-X/`. Quer que eu agende publicação (Buffer/Later) ou versão A/B do hook do Feed?"

---

## Anti-AI-slop checklist

Antes de salvar `copy.md`, rode mental:

- [ ] Tem "Em um mundo...", "É inegável", "Vamos mergulhar", "no fim do dia"? **Reescreve.**
- [ ] Adjetivo decorativo solto ("incrível", "transformador", "game-changer")? **Tira.**
- [ ] Emoji sem função (decorando, não substituindo palavra)? **Tira.**
- [ ] Frase média > 22 palavras? **Quebra.**
- [ ] Voz passiva onde cabe ativa? **Troca.**
- [ ] Fato sem fonte / número sem origem? **Tira ou marca [VERIFICAR].**
- [ ] Mesma copy em 2+ canais? **Reescreve um deles na gramática do canal.**

## Quando NÃO usar esta skill

- Carrossel de **notícia** diário → `/human-carrossel`
- **Vídeo** cinematográfico ou ad vertical 15s → `/human-cinematic`
- **Motion design** pra Remotion → `/human-motion`
- Marca **sem DNA** definido → primeiro `/human-dna`, depois volta aqui

## Próximo passo

Cole a pasta de input (ou caminho) + uma frase de intent. Eu diagnostico em uma resposta e, com seu OK, gero o pacote.
