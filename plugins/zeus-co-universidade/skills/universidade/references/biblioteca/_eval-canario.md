---
type: eval
status: rascunho
confianca: alta
updated: 2026-07-11
---

# 🧪 Eval Canário — Universidade Zeus-CO

**TL;DR:** As ~35 perguntas reais que Diego faria, cada uma com a(s) ficha(s) que a busca DEVERIA trazer no top 5. Roda a cada reindexação do zeus-mem para medir **recall@5** (quantas das perguntas trazem a ficha esperada nos 5 primeiros). É o detector de "a biblioteca parou de achar o que sabe".

## Protocolo
1. **recall@5** por pergunta: a ficha esperada aparece no top 5 da busca? (sim/não). Meta inicial: ≥ 85%.
2. Rodar a cada mudança de indexação (chunk size, filtro de status, reranker).
3. **Juiz ≠ gerador:** quem avalia a resposta final é um modelo/instância diferente de quem a gerou (padrão Morgan Stanley/Harvey).
4. **Prova de valor A/B:** mesma pergunta COM biblioteca vs SEM, julgada às cegas — única forma honesta de responder "o especialista-com-fichas é melhor?".

## Perguntas → ficha(s) esperada(s)

### CMO — Marketing / Branding
1. Fidelizar os atuais ou conquistar novos? → `marketing/penetracao-vence-lealdade` · `marketing/double-jeopardy`
2. Como dividir verba entre marca e performance? → `marketing/regra-60-40`
3. O que é posicionamento e por onde começo? → `marketing/posicionamento-comeca-na-categoria` · `marketing/stp-segmentar-mirar-posicionar`
4. Como descubro o que meu cliente quer de verdade? → `marketing/jobs-to-be-done` · `marketing/pesquisa-observar-nao-perguntar`
5. Preciso ser diferente ou ser reconhecível? → `branding/distintividade-nao-diferenciacao` · `marketing/diferenciacao-vs-distintividade`
6. Vale mudar minha identidade visual? → `branding/ativos-distintivos-sao-patrimonio`
7. O que é brand equity? → `branding/brand-equity-o-que-e`
8. Como ser lembrado na hora da compra? → `branding/category-entry-points` · `branding/marca-e-ativo-de-disponibilidade`
9. Marca nova ou estender a atual? → `branding/extensao-de-marca` · `branding/arquitetura-de-marca`
10. Propósito de marca vende? → `branding/golden-circle-comecar-pelo-porque` · `branding/salience-fama-vence-persuasao`

### CMO — Growth
11. Meu funil está furado, o que faço? → `growth/growth-e-loop-nao-funil` · `growth/equacao-de-crescimento`
12. Qual canal de aquisição escolher? → `growth/aquisicao-canal-modelo-fit` · `growth/quatro-fits-do-crescimento`
13. Usuários somem após o cadastro? → `growth/ativacao-aha-moment`
14. Como sei se minha retenção é boa? → `growth/cohorts-e-curva-de-retencao` · `growth/retencao-e-a-fundacao`
15. Como precificar? → `growth/pricing-de-valor`
16. Novos clientes ou expandir os atuais? → `growth/expansao-e-nrr`
17. Que métrica-mãe acompanhar? → `growth/north-star-metric`
18. Como rodar experimentos de growth? → `growth/experimentacao-velocidade`

### CMO — Tráfego Pago
19. Como escalo anúncios sem quebrar? → `trafego-pago/escala-por-sinal`
20. Criativo ou segmentação importa mais? → `trafego-pago/criativo-vence-segmentacao`
21. Por que os números do Ads não batem? → `trafego-pago/mensuracao-e-o-campo-minado` · `trafego-pago/capi-e-sinal-de-servidor`
22. Como fazer criativo de performance? → `trafego-pago/hook-nos-tres-segundos` · `trafego-pago/angulos-de-criativo` · `trafego-pago/nativo-e-ugc-vencem`
23. Search ou PMax? → `trafego-pago/google-search-vs-pmax`

### CMO — Publicidade
24. Como escrever headline que funciona? → `publicidade/tecnicas/oito-estruturas-de-headline` · `publicidade/swipe/headlines`
25. Como achar o insight de uma campanha? → `publicidade/tecnicas/seis-tipos-de-insight`
26. O que é uma big idea de verdade? → `publicidade/tecnicas/anatomia-da-big-idea` · `publicidade/swipe/big-ideas`
27. Meu texto parece de IA, como melhorar? → `publicidade/tecnicas/os-big-donts` · `publicidade/tecnicas/niveis-de-consciencia-schwartz`
28. Como estruturar a narrativa de um filme? → `publicidade/tecnicas/seis-arcos-narrativos`

### CFO
29. Vou sobreviver com o caixa que tenho? → `cfo/tesouraria/default-alive-or-dead` · `cfo/tesouraria/runway-e-burn`
30. Meu negócio fecha a conta? → `cfo/fpa/unit-economics-primeiro` · `cfo/fpa/cac-ltv-payback` · `cfo/fpa/margem-de-contribuicao`
31. Vale a pena esse projeto/investimento? → `cfo/fpa/viabilidade-vpl-tir`
32. Qual regime tributário escolher? → `cfo/tributario-br/regime-simples-presumido-real`
33. Quanto vale minha empresa numa rodada? → `cfo/captacao/valuation-early-stage` · `cfo/captacao/diluicao-e-cap-table`

### CEO
34. Como decido algo difícil sem dados? → `ceo/estrategia/decisao-sob-incerteza` · `ceo/lideranca/the-hard-thing`
35. Minha estratégia é boa? → `ceo/estrategia/boa-estrategia-tem-nucleo` · `ceo/estrategia/sete-poderes`
36. Ainda não tenho PMF, no que foco? → `ceo/estrategia/product-market-fit-primeiro`
37. Como faço acordo de sócios e divido equity? → `ceo/socios-governanca/dilema-do-fundador` · `ceo/socios-governanca/acordo-de-socios` · `ceo/socios-governanca/vesting-protege-a-sociedade`
38. Como escalar meu time? → `ceo/lideranca/escala-de-time-contratar-delegar`

## Observação
Perguntas propositalmente em linguagem de Diego (fundador), não em jargão — testa se a busca acha a doutrina mesmo quando a pergunta não usa o termo técnico. Diego deve revisar/editar/adicionar perguntas: é o gabarito da casa.
