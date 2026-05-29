class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}:")
        for f in self.funcionarios:
            f.mostrar_dados()
            print("-" * 30)

    def mostrar_folha_pagamento(self):
        total = 0
        for f in self.funcionarios:
            total += f.calcular_pagamento()

        print(f"Folha de pagamento total: R$ {total:.2f}")
