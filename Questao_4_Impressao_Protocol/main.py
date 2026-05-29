from boleto import Boleto
from etiqueta import Etiqueta
from relatorio_simples import RelatorioSimples
from processamento import processar_impressao

# criar objetos
boleto = Boleto("ABC123", 250.50)
etiqueta = Etiqueta("Rick Brendon", "Manaus - AM")
relatorio = RelatorioSimples("Relatório Financeiro")

# processar impressão
processar_impressao(boleto)
processar_impressao(etiqueta)
processar_impressao(relatorio)
