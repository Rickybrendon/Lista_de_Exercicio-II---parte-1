
---

# 🟢 QUESTÃO 2 – Sistema de Funcionários (ABC)

📄 **`Questao_2_Sistema_Funcionarios/README.md`**

```markdown
# Questão 2 – Sistema de Funcionários

## Descrição
Sistema que calcula pagamentos de diferentes tipos de funcionários
utilizando classe abstrata e polimorfismo.

## Hierarquia
- Funcionario (classe abstrata)
- FuncionarioAssalariado
- FuncionarioHorista
- FuncionarioComissionado

## Perguntas teóricas

**Qual é a superclasse da hierarquia?**  
Funcionario.

**Quais são as subclasses?**  
Assalariado, Horista e Comissionado.

**Onde ocorre sobrescrita?**  
No método `calcular_pagamento()`.

**Onde ocorre polimorfismo?**  
Ao calcular o pagamento de diferentes funcionários usando o mesmo método.

**Qual a vantagem de usar ABC?**  
Garantir que todo funcionário implemente o método de cálculo de pagamento.

## Execução
```bash
python main.py
