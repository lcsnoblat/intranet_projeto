from escrever_planilha import CriarPlanilha
from leitor_planilha import manipulador_xlsx

class testar():
		
	def gogo(self):	
		manipulador = manipulador_xlsx()
		lista = manipulador.get_clientes()
		lista = manipulador.get_clientes_complemento(lista)
		escrever = CriarPlanilha()
		escrever.criar(lista)

ab = testar()
ab.gogo()