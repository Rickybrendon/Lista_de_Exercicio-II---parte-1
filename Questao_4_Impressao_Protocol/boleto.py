class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self):
        print("Boleto")
        print(f"Código: {self.codigo}")
        print(f"Valor: R$ {self.valor:.2f}")
