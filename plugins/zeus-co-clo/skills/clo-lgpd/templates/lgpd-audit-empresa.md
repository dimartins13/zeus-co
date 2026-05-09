# LGPD Audit — {Empresa}

> Audit completo de compliance LGPD. Rodar 1x/semestre + após mudanças relevantes (novo módulo, novos vendors com dados, vazamento).

**Empresa:** {nome}
**Data audit:** {YYYY-MM-DD}
**Auditor:** clo-lgpd LEP + revisão CLO + (Diego como Founder-DPO se sem DPO formal)
**Próximo audit:** {YYYY-MM-DD + 6 meses}

---

## Classificação de risco

- **Setor:** {moda / iGaming / saúde / fintech / etc}
- **Trata dados sensíveis?** {SIM/NÃO} — {se SIM: quais — saúde, biométrico, financeiro, infantil}
- **Volume titulares ativos:** {N}
- **Tratamento automatizado relevante** (decisão que afeta titular)? {SIM/NÃO}
- **Compartilha dados com terceiros?** {SIM/NÃO} — {se SIM: lista}
- **Score de risco:** {Baixo / Médio / Alto / Crítico}

## 1. Documentação obrigatória

- [ ] **Política de Privacidade** publicada e acessível
  - URL: {link}
  - Última revisão: {data}
  - Cobre: bases legais? direitos? compartilhamento? retenção? cookies?
- [ ] **Termos de Uso** publicados
- [ ] **Cookie Banner** com consentimento granular (se site)
- [ ] **RoPA** (Record of Processing Activities) documentado
- [ ] **Bases legais** identificadas para CADA tratamento
- [ ] **Política Interna** de privacidade (funcionários + operadores)
- [ ] **Procedimento resposta titular** (canal + 15 dias)
- [ ] **Procedimento resposta incidente** (72h ANPD)

## 2. Controles técnicos (orquestrar com CTO LEP)

- [ ] HTTPS em tudo (Let's Encrypt funcionando)
- [ ] Encriptação em repouso (banco + backups)
- [ ] Controle de acesso (princípio menor privilégio)
- [ ] Logs de auditoria de acesso a dados pessoais
- [ ] Backup com encriptação
- [ ] Anonimização/pseudonimização onde possível
- [ ] Retenção definida (não guardar pra sempre)
- [ ] Eliminação ao fim do tratamento
- [ ] Segregação de dados (sandbox vs prod)

## 3. Contratos

- [ ] **Contratos com Operadores** (vendors que processam dados em nome) com cláusulas LGPD
- [ ] **DPA** (Data Processing Agreement) com plataformas (Stripe, Mailchimp, AWS, etc)
- [ ] **Cláusulas LGPD** em contratos B2B
- [ ] **Cláusulas confidencialidade** com funcionários/PJs

## 4. DPO (Encarregado)

- [ ] **DPO designado:** {nome / "Diego Founder-DPO"}
- [ ] **Email DPO publicado:** dpo@{empresa}.com (precisa funcionar)
- [ ] DPO obrigatório? Avaliar:
  - Tratamento alto risco? {sim/não}
  - Volume alto? {sim/não}
  - Dados sensíveis? {sim/não}
  - Decisões automatizadas relevantes? {sim/não}

## 5. Direitos do titular implementados

Procedimento documentado e funcional para cada um dos 9 direitos:
- [ ] Confirmação de tratamento
- [ ] Acesso aos dados
- [ ] Correção de dados
- [ ] Anonimização/bloqueio/eliminação
- [ ] Portabilidade
- [ ] Eliminação ao fim
- [ ] Informação sobre compartilhamento
- [ ] Informação sobre não consentimento
- [ ] Revogação de consentimento

## 6. Plano de resposta a incidente

- [ ] Pessoa designada pra coordenar incidente
- [ ] Comunicação modelo pra titular afetado
- [ ] Comunicação modelo pra ANPD
- [ ] Procedimento pra avaliar materialidade (todo incidente comunica? só os relevantes?)
- [ ] Forensics pra identificar escopo
- [ ] Lessons learned + correção

## 7. Riscos identificados nesta auditoria

| Risco | Probabilidade | Impacto | Plano de mitigação | Owner | Prazo |
|---|---|---|---|---|---|
| | | | | | |

## 8. Multas potenciais (referência ANPD)

- Advertência (leve)
- Multa simples: até 2% faturamento, limite R$ 50M por infração
- Multa diária: limite R$ 50M
- Publicização da infração
- Bloqueio dos dados
- Eliminação dos dados

## 9. Foco ANPD 2025-2026 (verificar exposição)

- [ ] Trato dados de crianças/adolescentes? → atenção EXTRA
- [ ] Uso AI ou biometria? → atenção EXTRA
- [ ] Faço data scraping? → revisar urgentemente
- [ ] Sou ad-tech / cookies third-party? → reavaliar consentimento

## Próximos Movimentos

1. Resolver gaps P0 (riscos críticos) em 30 dias
2. P1 (riscos altos) em 90 dias
3. Próximo audit: {YYYY-MM-DD}
4. Atualizar `LEARNINGS.md` da empresa com gaps recorrentes
