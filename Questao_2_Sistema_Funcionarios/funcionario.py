from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Pagamento: R$ {self.calcular_pagamento():.2f}")

    @abstractmethod
    def calcular_pagamento(self):
        pass
