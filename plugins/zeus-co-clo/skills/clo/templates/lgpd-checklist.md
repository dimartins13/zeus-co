# LGPD Checklist — {Empresa}

> Compliance LGPD baseline + monitoramento contínuo. Atualizar trimestralmente.

**Empresa:** {nome}
**CNPJ:** {N}
**Data audit:** {YYYY-MM-DD}
**Próximo audit:** {data + 90 dias}

---

## Setor + risco

- **Setor:** {moda / iGaming / saúde / fintech / etc}
- **Trata dados sensíveis?** {SIM/NÃO} — {se SIM: quais — saúde, biométrico, infantil, etc}
- **Volume de dados:** {N titulares ativos}
- **Tratamento automatizado relevante?** {SIM/NÃO}
- **Risco**: {Baixo / Médio / Alto / Crítico}

## Documentação obrigatória

- [ ] **Política de Privacidade** publicada e acessível em todas as interfaces
- [ ] **Termos de Uso** publicados
- [ ] **Cookie Banner** com consentimento granular (se site)
- [ ] **Mapeamento de tratamentos (RoPA — Record of Processing Activities)** documentado
- [ ] **Bases legais identificadas** para cada tratamento (uma das 6 da LGPD)
- [ ] **Política Interna de Privacidade** para funcionários
- [ ] **Procedimento de resposta a titulares** (canal + prazo 15 dias)
- [ ] **Procedimento de resposta a incidentes** (notificação ANPD em 72h)

## Controles técnicos (orquestrar com CTO LEP)

- [ ] Encriptação em trânsito (HTTPS em tudo)
- [ ] Encriptação em repouso (banco)
- [ ] Controle de acesso (princípio do menor privilégio)
- [ ] Logs de auditoria de acesso a dados pessoais
- [ ] Backup com criptografia
- [ ] Anonimização/pseudonimização onde possível
- [ ] Retenção definida (não guardar dado sem necessidade)
- [ ] Eliminação ao fim do tratamento

## Contratos

- [ ] **Contratos com Operadores** (vendors que processam dados em nome da empresa) com cláusulas LGPD
- [ ] **Cláusulas LGPD** em contratos com clientes B2B
- [ ] **DPA — Data Processing Agreement** com plataformas (Stripe, Mailchimp, etc)

## DPO (Encarregado)

- [ ] DPO nomeado: {nome / "ainda Diego como Founder-DPO"}
- [ ] Email do DPO publicado: dpo@{empresa}.com
- [ ] DPO obrigatório? Avaliar:
  - [ ] Tratamento de alto risco
  - [ ] Volume alto de dados
  - [ ] Dados sensíveis
  - [ ] Decisões automatizadas relevantes

## Direitos do titular implementados

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

## Riscos identificados nesta auditoria

| Risco | Probabilidade | Impacto | Plano de mitigação |
|---|---|---|---|
| | | | |

## Multas potenciais (fonte: ANPD)

- Advertência (leve)
- Multa simples: até 2% do faturamento, limite R$ 50M por infração
- Multa diária: limite R$ 50M
- Publicização da infração
- Bloqueio dos dados
- Eliminação dos dados

## Próximos Movimentos

1. {ação P0 — risco crítico}
2. {ação P1 — gap importante}
3. Próximo audit: {data}
