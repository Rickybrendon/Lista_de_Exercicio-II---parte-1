from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem
from funcoes import executar_salvamento_formal, executar_salvamento_flexivel

arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("=== Salvamento FORMAL (ABC) ===")
executar_salvamento_formal(arquivo, "dados1.txt")
executar_salvamento_formal(banco, "dados2.txt")
# executar_salvamento_formal(nuvem, "dados3.txt")  # NÃO funciona

print("\n=== Salvamento FLEXÍVEL (Protocol) ===")
executar_salvamento_flexivel(arquivo, "dados1.txt")
executar_salvamento_flexivel(banco, "dados2.txt")
executar_salvamento_flexivel(nuvem, "dados3.txt")
