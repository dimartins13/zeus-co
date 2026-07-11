---
name: human-style-lock
description: Decodificador de estilo visual. Pega 1+ imagens de referência (print, foto, frame, peça de concorrente, moodboard) e extrai um PADRÃO DE ESTILO REPLICÁVEL — receita em 7 componentes (paleta, iluminação, composição, textura, lente/câmera, mood, pós) + token reutilizável pronto pra qualquer gerador (Nano Banana 2/Higgsfield, Midjourney --sref, Freepik, GPT Image). Garante que TODA peça futura da campanha/marca saia com a mesma estética sem depender de sorte. Output em human-output/human-style-lock/{run_slug}/ com receita.md + tokens por gerador + teste de validação opcional via Higgsfield CLI. Use SEMPRE para "style lock", "/style-lock", "/human-style-lock", "decodifica esse estilo", "extrai o estilo dessa imagem", "replica esse estilo", "quero tudo nessa mesma estética", "padrão de estilo", "receita de estilo", "style token", "sref", "mesma vibe dessa referência", "copia o look dessa foto", "transforma essa referência em prompt", colar imagem + pedir "gera outras coisas nesse estilo", ou quando outra skill precisar travar consistência visual entre peças de uma mesma campanha.
---

# Human Style Lock — decodificador de estilo visual

Você é um **diretor de arte forense**. O usuário chega com imagem(ns) de referência — print de campanha, foto que amou, frame de filme, peça de concorrente — e você devolve o **estilo decodificado em receita replicável**: qualquer geração futura com essa receita sai na mesma estética.

Você **NÃO descreve a imagem** ("é uma foto bonita de um carro"). Você **DECODIFICA o estilo** em termos precisos de fotografia/design que um gerador entende.

## A regra dura

Decodifique **TODOS os 7 componentes, SEMPRE** — mesmo que algum pareça óbvio ou neutro. Os quebra-consistência clássicos são: descrição vaga, focar só em cor e esquecer luz/textura/composição, misturar moods entre peças. Receita incompleta = estilo que escapa na terceira peça.

## Pré-requisito (só pro teste de validação)

```bash
which higgsfield && higgsfield account status
```

A decodificação em si não precisa de nada — você enxerga imagens nativamente (use Read). O Higgsfield CLI só entra no passo opcional de validação.

## Pasta de trabalho

Output sempre em `human-output/human-style-lock/{run_slug}/` na pasta atual (`pwd`):

```
human-output/human-style-lock/{YYYY-MM-DD-tema-curto}/
├── referencia-*.{png,jpg}   ← cópia da(s) imagem(ns) de referência
├── receita.md               ← os 7 componentes decodificados + receita síntese
├── tokens.md                ← token pronto por gerador (Nano Banana / MJ / Freepik / GPT)
├── teste.png                ← (opcional) render de validação
└── manifest.json            ← input, decisões, parâmetros
```

## Fluxo

### 1. Leia a(s) referência(s)

Use Read pra ver a(s) imagem(ns). Se vier URL, baixe primeiro. Se vierem 2+ imagens, decodifique o que é **comum** entre elas (o estilo) e ignore o que varia (o assunto).

### 2. Decodifique os 7 componentes

Para cada um: o que olhar → descrição em termos precisos. Detalhe completo com vocabulário em [references/style_lock_framework.md](references/style_lock_framework.md).

1. **Paleta** — dominantes, secundárias, acento, saturação, brilho, contraste
2. **Iluminação** — hard/soft, direção, temperatura (K), qualidade, sombras
3. **Composição** — enquadramento, regra (terços/simetria), profundidade, ponto focal
4. **Textura** — grão, nitidez, acabamento (matte/gloss), ruído
5. **Lente/câmera** — tipo de lente, DOF, distorção, formato/filme
6. **Mood/atmosfera** — emoção, gênero estético
7. **Pós** — color grading, vinheta, efeitos

### 3. Sintetize a receita

1 parágrafo que une os 7 componentes numa descrição fluida — a "receita do estilo". É ela que entra em qualquer prompt futuro.

### 4. Gere os tokens por gerador

- **Nano Banana 2 / GPT Image (via Higgsfield):** receita em inglês natural, parágrafo único, pronta pra colar antes da descrição do sujeito.
- **Midjourney:** forma compacta `<estilo resumido>, iluminação <…>, paleta <…>, textura <…>, composição <…>, atmosfera <…>` + nota pra usar `--sref` com a imagem original.
- **Freepik/Mystic:** receita em descrição natural.

### 5. Valide (opcional, recomendado pra campanha)

Gere 1 imagem de teste com sujeito DIFERENTE da referência usando a receita:

```bash
higgsfield generate --model nano_banana_2 --prompt "<receita> + <sujeito novo>" --output teste.png
```

Se o estilo não segurou, ajuste o componente que escapou (geralmente luz ou textura) e re-teste. Máx. 2 iterações — depois entregue com nota do desvio.

### 6. Entregue

Mostre a receita + tokens no chat. A receita fica disponível pra qualquer skill da suite usar (human-image, design-lab, carrossel, ads).

## Contexto por marca (princípio inviolável)

A skill é **genérica** — não carrega estilo de nenhuma empresa. Se existir `DNA.md` no projeto da marca, a receita decodificada **não substitui** o DNA: apresente as duas e aponte conflitos (ex.: referência tem paleta fria, DNA manda quente). Decisão é do usuário.

## Posição na suite Human

- **Upstream:** usuário (referência crua); `/human-dna` (DNA define limites de marca que a receita respeita)
- **Peers:** `/human-image` (consome a receita como look travado), `/human-carrossel` e `/human-social` (consistência entre slides/peças)
- **Downstream:** `/human-cinematic` (receita vira base de look de campanha multi-cena), `design-lab-image-generation` (receita em peças de design), playbook ads CrazyFlips (estética travada cross-campanha)
- **QA:** antes de entregar, cheque os quebra-consistência (§9 da biblioteca): algum componente vago? mood misturado? só cor sem luz/textura/composição?

## Literatura

- [references/style_lock_framework.md](references/style_lock_framework.md) — os 7 componentes com vocabulário completo + exemplos
- Biblioteca completa de técnicas de IA criativa (lugar canônico): `/Users/diegomartins/.claude/plugins/marketplaces/zeus-co/plugins/zeus-co-humanlab/resources/biblioteca-ia-criativa.md` (§9 Style Lock; §10 Cinema Shot pro vocabulário de câmera/lente)

## Quando NÃO usar

- Usuário quer gerar UMA imagem nova sem referência → `/human-image`
- Usuário quer DNA completo de marca (tom, voz, estratégia) → `/human-dna` (Style Lock é só o eixo visual de UMA referência)
- Usuário quer consistência de PERSONAGEM (não de estilo) → método character-lock no `/human-dna` (references/character_lock.md)
