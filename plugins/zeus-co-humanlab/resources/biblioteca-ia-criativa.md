# Biblioteca de Técnicas de IA Criativa — Zeus-CO

> **Lugar canônico** desta literatura. Skills referenciam este arquivo — nunca copiam o conteúdo.
> Fonte: técnicas absorvidas dos cursos da Human Academy (app.academypass.ai), dos quais Diego é membro. Foco em **padrão reutilizável** + exemplo representativo condensado — não cópia da plataforma. Vídeos são protegidos; aqui ficam só técnicas/prompts em texto, de uso interno.
> Consumidores: HumanLab (human-image, human-cinematic, human-dna, human-style-lock), Design-Lab (image-generation, poster-key-visual, landing-page, deck), CCO (copy-master, storytelling), Cérebro Criativo, playbook de ads CrazyFlips.

---

# PARTE I — Técnicas por caso de uso

## §1. Fundamentos de prompt

**Framework universal (texto/conteúdo):** papel · objetivo · tema · público · tom · estilo/referência · formato · evitar · exemplo · nº de opções.
> "Você é um(a) [papel]. Sua tarefa é [objetivo]. Sobre [tema], para [público]. Tom [tom], estilo [referência]. Formato [post/email/roteiro/imagem]. Evite [x]. Me explique a lógica e me dê [n] opções."

**Anatomia de prompt de IMAGEM:** sujeito + ação + ambiente + luz + **câmera/lente/filme**. Os finalizadores de câmera puxam realismo:
`shot on alexa 35mm` · `leica q2` · `FUJIFILM X100F 28mm` · `portra 400` · `shallow depth of field, bokeh` · `cinematic, high dynamic range`.

## §2. Still de produto

**a) E-commerce limpo:** "Gere versão em alta qualidade de [produto, material, detalhes, logo]. Fundo branco neutro, iluminação de estúdio suave, sombras realistas, sem reflexos excessivos, composição centralizada, premium."

**b) Ambientado / campanha:** colocar o produto numa cena com mood. "Coloque [produto] em [cenário detalhado: mid-century, parede verde-oliva, piso madeira escura]. [Luz: harsh flash / golden hour]. [Mood: editorial, grão visível, analógico, urbano]. Fundo levemente desfocado, energia e movimento." (ex.: garrafa numa pista de corrida ao entardecer.)

**Técnica-chave: mesmo produto, dois usos** — versão e-commerce (fundo branco) + versão campanha (ambientada). Reaproveita o ativo.

## §3. Ensaio / retrato realista (pessoas)

Use **imagens de referência** + prompt cinematográfico detalhado:
> "Use essas imagens como referência e crie a imagem: Ultra-realistic photo of [pessoa + roupa] in [cenário + hora/luz]. [neon/golden-hour], reflexos, sombras moody, [Fujifilm, shallow DOF, bokeh], realistic skin texture and fabric detail, HDR lighting."

Eixos a variar: roupa, cenário, hora do dia, luz, textura de pele/tecido, câmera.

## §4. Marca: logo & efeitos visuais

**Textura → logo 3D:** "Aplique a textura da imagem à esquerda no logo da direita, preservando formato/cores/orientação. Faça parecer 3D, fundo transparente, alto contraste, sombras marcantes, realce de volumes." → depois ambientar o logo 3D ("ambiente de areia/deserto", "pedra flutuando no espaço").

## §5. Poster / banner com lettering (meta-prompting)

Técnica: peça à IA pra **CRIAR o prompt** da arte (não a arte direto):
> "Crie um prompt para gerar [cartaz minimalista estética TEDx, fundo preto, vetores vermelhos]. Headline [X], subtítulo [Y], data/local em pequeno nas extremidades, formas espalhadas estilo Bauhaus."

Funciona pra: poster de evento, campanha de moda urbana (logo de marca grande ao fundo), imagem dividida ao meio. Lettering + layout descritos em linguagem natural.

## §6. Personagem & consistência ⭐

**Criar por atributos estruturados:** Tipo · Função · Personalidade · Aparência (cabelo, roupa peça-a-peça, acessórios) · Estilo visual (3D/Pixar-inspired).
> "A confident teenage protagonist in 3D style on white background, short curly hair, royal blue oversized hoodie, beige cargo pants, neon green sneakers, headphones around neck, playful expression, vibrant palette, soft lighting, stylized animation aesthetic, Pixar-inspired."

**Manter consistência (variação idêntica):** "Crie uma variação do personagem seguindo as características e o estilo de ilustração **de forma idêntica**, mas agora [virado de perfil pra esquerda / andando numa rua ao entardecer]." → trava identidade, muda só pose/cena.

**Método "character bible" — hierarquia de consistência (silhouette-lock):**
1. **Trava a SILHUETA primeiro** — é a âncora: forma da cabeça, orelhas, proporção do torso/membros. Tem que ser legível em 2D e escalável pra ícone pequeno.
2. **Cor/material mínimos** — paleta limpa, pouca textura, toon shading + **1 cor de marca de acento** só nos acessórios.
3. **Acessórios destacáveis que NÃO alteram a silhueta** — cachecol/coleira/boné/headset que você troca sem quebrar a identidade.
4. **Pose default + biblioteca de expressões intercambiáveis** — varia expressão (sorriso/piscada/curioso) e pose, mantendo o resto travado.

Detalhamento operacional: `zeus-co-humanlab/skills/human-dna/references/character_lock.md`.

## §7. Edição / variação mantendo layout (renders, decoração)

"Crie variação mantendo **exatamente o mesmo layout**, trocando só [material / iluminação / estilo de decoração]." Eixos: material (cimento queimado, madeira escura), luz (pôr do sol pela janela), estilo (industrial: tijolo aparente, tubulação exposta, paleta sóbria).

---

# PARTE II — Motores absorvidos (frameworks)

## §9. Style Lock — decodificar referência → estilo replicável

**Pega 1 imagem de referência → vira padrão de estilo aplicável em qualquer gerador.** Skill nativa: `/human-style-lock`.

**Os 7 componentes que SEMPRE se extrai** (cada um: o que olhar → como descrever em termos precisos de foto/design):
1. **Paleta** — dominantes, secundárias, acento, saturação, brilho, contraste. _("vibrante e saturada, ciano dominante + amarelo quente, contraste alto, brancos nuançados")_
2. **Iluminação** — hard/soft, direção, temperatura (K), qualidade, sombras. _("soft difusa, de cima-esquerda, ~5500K")_
3. **Composição** — enquadramento, regra (terços/simetria), profundidade, ponto focal, equilíbrio.
4. **Textura** — grão, nitidez, acabamento (matte/gloss), ruído.
5. **Lente/câmera** — tipo de lente, DOF, distorção, formato/filme.
6. **Mood/atmosfera** — emoção, gênero estético.
7. **Pós** — color grading, vinheta, efeitos.

**Passo-a-passo:** observar holístico (que cores dominam? luz dura ou suave? textura? composição? que emoção?) → decompor cada componente numa descrição precisa → **sintetizar numa "receita"** (1 frase/parágrafo que une tudo) → virar token reutilizável → testar e ajustar mantendo consistência.

**Token reutilizável** — MJ: `<estilo resumido>, iluminação <tipo/direção/temp>, paleta <…>, textura <…>, composição <…>, atmosfera <…> --sref <tag>`. Freepik/GPT/Nano Banana: a mesma receita em descrição natural.

**Quebra-consistência (evitar):** descrição vaga; misturar moods entre peças; trocar componentes de uma peça pra outra; focar só em cor e esquecer luz/textura/composição.

## §10. Cinema Shot — prompt cinematográfico por 5 eixos

Prompt cinematográfico = especificar **5 eixos técnicos + a cena**. Vocabulário curado:
- **Câmera** (modelo real): ARRI Alexa 35 · IMAX MK IV 65mm · Alexa Mini LF / 65 · Sony Venice · RED V-Raptor / Komodo 6K · Canon C500 II · Blackmagic URSA 12K · Phantom Flex4K · ARRICAM ST (35mm film).
- **Lente** (caráter): Cooke Speed Panchro / Panchro-i (vintage) · Panavision C/E (anamórfica) · ZEISS Supreme Prime Radiance · ARRI Signature Primes · Leica Thalia · Canon K35 · Helios 44-2 58mm (vintage) · LOMO Anamorphic.
- **Ângulo**: eye-level / low / high / dutch / overhead.
- **Abertura**: f/1.4 (DOF raso, bokeh, isola sujeito) → f/2.8 → f/4 → f/16 (tudo em foco).
- **Luz**: os 7 setups calibrados do human-image (Golden Hour, Low Key, Spotlight, Chiaroscuro, Cutter Lights, Hard Flash, Silhouette).

Teaching: escolher **câmera + lente reais** dá o look cinematográfico instantâneo; vintage/anamórfica = caráter orgânico.

## §11. Copy Agent — copy persuasivo com storytelling

Estrutura base: **Hook → Problema → Tensão → Solução → Prova → CTA**.
- **Hook** — provocativo / pergunta / dado chocante; prende na hora.
- **Problema** — dor específica e concreta; o leitor se reconhece.
- **Tensão** — eleva a dor: consequência, prazo, perda, risco de não agir (urgência emocional).
- **Solução** — produto como resposta; **benefícios concretos, não características**.
- **Prova** — casos reais, depoimentos, números.
- **CTA** — ação clara.

Regras de ouro: benefício > feature; urgência emocional; prova sustenta a promessa.

## §12. Brief Studio — briefing bruto → direção criativa

**Sempre extrair de um briefing (8):** Objetivo (vender/informar/engajar/posicionar) · Público (demográfico + emocional + comportamental) · Problema/Need · Tom · Restrições (visual/linguagem/formato/prazo) · KPI/sucesso · Referências · Contexto (posicionamento, campanha anterior, timing, mercado). Lacuna vaga → pergunta objetiva ("que mudança/ação específica quer provocar no público?"). É a Fase 0 / discovery dos projetos criativos.

## §13. Script AI — ideia → roteiro cinematográfico

Estrutura de **3 atos com timing** (pra produção com IA, adaptável a curta/Reels/institucional):
- **Ato 1 — Preparação + gatilho** (incidente incitante): mundo, personagem, desejo/necessidade. **15-25%**.
- **Ato 2 — Confronto**: obstáculos, antagonista, turning point, quebra de expectativa. **50-60%**.
- **Ato 3 — Resolução**: clímax + mudança no protagonista/mundo. **15-25%**.

Pra **ad curto (30s/Reels)**: comprimir os 3 atos — hook nos primeiros segundos → tensão no meio → payoff + CTA no fim.

## §14. AI Director — direção de vídeo (imagem → cena viva)

- **Objetivo emocional** = fio condutor (tensão/curiosidade/serenidade/surpresa), mantido em todos os elementos.
- **Câmera**: shots (Wide/Medium/Close — progressão pra revelar informação); movimento (estático · Dolly/Push · Tracking · Crane · Handheld=immediacy · Zoom); angulação (eye-level=identificação · low=empoderamento · high=vulnerabilidade).
- **Ritmo**: lento=introspecção, rápido=urgência/consequência.
- **Blocking**: posição inicial de personagens/objetos no espaço.

## §15. Veo3 / vídeo — anatomia de prompt de vídeo

Componentes: **Subject** (foco) · **Context** (onde/quando/tom) · **Action** (o que acontece, objetivo da tomada) · **Camera** (setup, lente, ângulo, enquadramento — ex "two-shot, eye-level, 50mm") · **Movement** (deslocamento + **DURAÇÃO** — ex "push-in over 2s") · **Audio** (ambiência, sons diegéticos, efeitos) · **Dialogue** · **Style** · **Duration**. **JSON** = os mesmos campos como chaves. Vale pra Veo3 e Seedance (mesma anatomia).

## §16. Landing Page — estrutura de conversão

Ordem: **Hero → Prova Social → Oferta → Objeções → CTA**.
- **Hero** (1ª dobra): promessa principal + benefício único; define valor e tom.
- **Prova Social** (logos, depoimentos, números): valida, reduz ceticismo.
- **Oferta**: exatamente o que recebe, o que inclui.
- **Objeções**: derruba dúvidas antes do CTA.
- **CTA**: ação clara, sem fricção.

Princípios: 1 foco só; menos fricção; prova sustenta a promessa; urgência.

## §17. GPT Builder — construir um assistente do zero

**Diagnóstico inicial (7 perguntas antes de construir):** propósito · one-shot vs reutilizável · público (perfil/nível/tom) · acesso a recursos (arquivos/código/dados) · métrica de sucesso · exemplos? · estilo/referência. → System prompt em **5 blocos**: (1) **Papel/Propósito/Foco** + guarda ética; (2) **Estilo/Tom/Vocabulário/Formato de saída**; (3) **Regras & Fluxo**; (4) **Exemplos**; (5) **Output format**. Usar pra construir as próprias skills do Zeus-CO — e como QA: toda SKILL.md deveria cobrir esses 5 blocos.

## §18. Creative Deck — estrutura de deck criativo

Estrutura canônica: **Capa → Contexto → Problema/Desafio → Big Idea → Conceito (territórios) → Execução (peças/canais) → Resultados esperados/KPI → Próximos passos.** Por slide: 1 ideia + racional curto + referência visual.

---

# PARTE III — Mapa de aplicação

| Seção | Skill que consome | Quando |
|---|---|---|
| §1, §3, §10 | `human-image`, `human-cinematic` | toda geração de still/frame |
| §2, §4, §5, §7 | `design-lab-image-generation`, `design-lab-poster-key-visual` | produto, marca, poster, render |
| §6 | `human-dna` (character_lock.md), playbook ads CrazyFlips | mascote/personagem consistente |
| §9 | `human-style-lock` | decodificar referência visual |
| §11 | `cco-copy-master`, `cco-storytelling` | copy de ads/landing/email |
| §12 | `design-lab-discovery`, Fase 0 de qualquer projeto criativo | briefing bruto |
| §13, §14, §15 | `human-cinematic`, `design-lab-video-generation` | roteiro e prompt de vídeo |
| §16 | `design-lab-landing-page` | estrutura de LP |
| §17 | `lep-builder`, `skill-creator` (QA de skills) | construir assistentes/skills |
| §18 | `design-lab-deck`, `board-pack-builder` | deck criativo |
| §1 (framework universal) | `cerebro-criativo` | estruturar prompts de ideação |

# Mapa-fonte (pra colher mais on-demand)

ChatGPT Pro > "Criação Visual" (16 aulas texto): falta colher Logo/Identidade, Ícones, Mockups, UI Design, Thumbnail YT, Ilustrações/Estilos, Renders arquitetura, Simulação de decoração. Image Creator Pro (módulos Still de Produto 8, Ads p/ Marcas 7, Fashion 7, Consistência Visual 9). Workflows de operação de ferramenta = vídeo, não extraível. Colheita via Claude in Chrome (sessão logada).
