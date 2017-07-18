from django.shortcuts import render
from manipulador.http_requisicao import requisicao
from manipulador.leitor_planilha import manipulador_xlsx
# Create your views here.
def home(request):
	manipulador = manipulador_xlsx()
	lista = manipulador.get_parceiros()
	req = requisicao()
	req.login()
	resposta = req.enderecos(lista)
	req.logout()