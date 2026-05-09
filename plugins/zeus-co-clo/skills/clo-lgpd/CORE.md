# CORE — LGPD / DPO
> **By design. Auditável. Responsivo a titular + ANPD.**

## Lei 13.709/18 — fundamentos
- 6 bases legais (consentimento, contrato, legítimo interesse, etc)
- 9 direitos do titular
- Tratamento de dados sensíveis (saúde, biometria, infantil) = base legal restrita
- DPO obrigatório quando volume + sensibilidade justifica
- Multa: até 2% faturamento, R$50M por infração

## Documentação obrigatória
- Política de Privacidade (publicada e atualizada)
- Termos de Uso
- Cookie Banner com consentimento granular
- RoPA (Record of Processing Activities)
- Política Interna pra funcionários
- Procedimento resposta titular (15d prazo)
- Procedimento resposta a incidente (72h notificar ANPD)
- DPA (Data Processing Agreement) com vendors operadores

## Por empresa
- **Dash Financeiro:** dados financeiros = sensíveis Art 5º II. DPO obrigatório (Diego Founder-DPO inicialmente). users.json bcrypt obrigatório.
- **TarjaPreta:** saúde mental = sensível. Base legal restrita. RIPD (Relatório Impacto) obrigatório.
- **KingPanda:** KYC iGaming = identificação + dados financeiros. Compliance reforçada.
- **2ndStreet:** dados clientes + NFC peças = pseudo-identificáveis. Tratamento padrão.
- **Crazyflips:** wallet crypto = dado pessoal. KYC se fiat envolvido.

## Foco ANPD 2025-2026 (do roadmap publicado)
1. Dados de crianças/adolescentes
2. AI / biometria
3. Data scraping
4. Ad-tech / cookies

## Heurísticas
- Política Privacidade modelo + customização específica setor
- Coletar mínimo necessário (data minimization)
- Retenção definida (não guardar pra sempre)
- Anonimização sempre que possível
- Incidente: timer de 72h começa quando descoberto
