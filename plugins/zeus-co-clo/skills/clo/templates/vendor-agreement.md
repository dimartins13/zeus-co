# Vendor Agreement — Cláusulas Críticas Checklist

> Checklist de cláusulas que TODO contrato vendor precisa. Use antes de assinar contrato externo.

**Empresa contratante:** {nome}
**Vendor:** {nome}
**Tipo de serviço:** {SaaS / Logística / Fotografia / Marketing / etc}
**Data:** {YYYY-MM-DD}
**Valor mensal/anual:** R$ {valor}

---

## Cláusulas obrigatórias

### 1. Objeto + Escopo claro
- [ ] Descrição precisa do serviço/produto (sem "etc", "entre outros")
- [ ] O que está INCLUÍDO e o que NÃO está
- [ ] Critério de aceite (Definition of Done)

### 2. Preço + Pagamento
- [ ] Valor + forma de cálculo (fixo, variável, mix)
- [ ] Forma de pagamento (PIX, boleto, cartão)
- [ ] Prazo (D+0, D+15, D+30)
- [ ] Reajuste (índice IPCA/IGP-M, anual)
- [ ] Multa por atraso pagamento (1-2% + juros 1% am)
- [ ] Possibilidade de antecipação com desconto

### 3. SLA (Service Level Agreement)
- [ ] Tempo de resposta inicial
- [ ] Tempo de resolução
- [ ] Disponibilidade (% uptime se SaaS)
- [ ] Janela de manutenção
- [ ] **Penalidades por descumprimento** (sem isso, SLA não tem força)

### 4. Prazo + Renovação + Saída
- [ ] Prazo inicial (12-24 meses típico)
- [ ] Renovação automática? Se sim, com que aviso prévio (30/60/90 dias)
- [ ] Saída sem causa: prazo de aviso + multa rescisória (se houver)
- [ ] Saída por descumprimento: notificação + prazo cura + rescisão

### 5. Limitação de Responsabilidade (Liability Cap)
- [ ] **Cap de responsabilidade**: máximo limitado ao valor pago nos últimos 12 meses (padrão favorável a vendor) ou múltiplos (favorável ao contratante)
- [ ] **Indenização**: vendor indeniza se causar dano por culpa/dolo
- [ ] Exclusões (força maior, etc)

### 6. Confidencialidade + LGPD
- [ ] NDA embutido ou anexo
- [ ] Cláusulas LGPD se vendor processa dados pessoais (DPA)
- [ ] Vendor notifica incidentes de segurança em X horas
- [ ] Subcontratação requer aprovação prévia

### 7. Propriedade Intelectual
- [ ] **IP do output pertence a quem?** Se vendor cria pra você, output é seu (work-for-hire). Caso contrário, licença de uso.
- [ ] Vendor garante não infringir IP de terceiros
- [ ] Indenização IP infringement

### 8. Foro + Lei
- [ ] Comarca específica (preferir sua sede)
- [ ] Lei brasileira
- [ ] Mediação antes de judicial (CAM-CCBC ou outra)

### 9. Cláusulas anti-corrupção (Lei 12.846/13)
- [ ] Vendor declara conformidade com Lei Anticorrupção
- [ ] Direito de auditoria

### 10. Notificações
- [ ] Email designado para notificações formais
- [ ] Endereço físico para citação

---

## Red flags em contratos vendor

- ❌ Sem prazo de saída claro
- ❌ Renovação automática sem aviso prévio
- ❌ Liability cap inexistente ou ilimitado
- ❌ Foro vendor (você teria que litigar em outra cidade)
- ❌ IP vagamente definido
- ❌ Sem cláusulas LGPD se processa dados
- ❌ Multa rescisória excessiva (>3 meses)

## Próximos Movimentos

1. Negociar pontos red flag
2. **Revisar versão final com advogado humano** (se contrato grande / longo prazo)
3. Assinar via Clicksign/Autentique
4. Arquivar versão assinada + adicionar a vendor scorecard (`coo-templates/vendor-scorecard.md`)
