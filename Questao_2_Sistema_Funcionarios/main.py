from empresa import Empresa
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado

# criar a empresa
empresa = Empresa("Tech Solutions")

# criar funcionários
assalariado = FuncionarioAssalariado("Ana", "111.111.111-11", 3000)
horista = FuncionarioHorista("Bruno", "222.222.222-22", 160, 25)
comissionado = FuncionarioComissionado("Carlos", "333.333.333-33", 10000, 0.1)

# adicionar funcionários
empresa.adicionar_funcionario(assalariado)
empresa.adicionar_funcionario(horista)
empresa.adicionar_funcionario(comissionado)

# listar funcionários
empresa.listar_funcionarios()

# mostrar folha de pagamento
empresa.mostrar_folha_pagamento()
