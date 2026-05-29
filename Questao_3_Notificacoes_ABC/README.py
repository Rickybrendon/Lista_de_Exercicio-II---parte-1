
---

# 🟢 QUESTÃO 3 – Sistema de Notificações (ABC)

📄 **`Questao_3_Notificacoes_ABC/README.md`**

```markdown
# Questão 3 – Sistema de Notificações com ABC

## Descrição
Sistema "multi-notificadores" utilizando contrato formal por herança.

## Perguntas teóricas

**Qual classe representa o contrato formal?**  
Notificador.

**Onde há polimorfismo?**  
No método `notificar()` chamado para objetos diferentes.

**Por que usar ABC?**  
Para garantir que todas as subclasses implementem `notificar()`.

**O que acontece se uma subclasse não implementar o método?**  
Ela não poderá ser instanciada.

## Execução
```bash
python main.py
