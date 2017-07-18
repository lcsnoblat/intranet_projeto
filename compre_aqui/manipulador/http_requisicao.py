import requests
from montador_xml import montar
import sys

class requisicao():

	def __init__(self):
		self.monta = montar()
		self.login()
		self.header_padrao = {'Content-Type': 'text/xml;charset=ISO-8859-1', 'Cookie': 'JSESSIONID=' + self.monta.sessionId}

	def login(self):
		xml = self.monta.montar_xml_autenticacao()
		url = "http://187.191.96.191:8080/mge/service.sbr?serviceName=MobileLoginSP.login"
		header = {'Content-Type': 'text/xml;charset=ISO-8859-1'}
		resposta = requests.post(url,headers=header, data=xml)
		self.monta.resposta_login(resposta)

	def logout(self):
		url = "http://187.191.96.191:8080/mge/service.sbr?serviceName=MobileLoginSP.logout"
		header = {'Cookie': self.monta.sessionId}
		reposta = requests.post(url, headers=header)


	def enderecos(self, lista_cliente):
		regi_cod_nome = {}
		url = "http://187.191.96.191:8080/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords"
		nova_lista = []
		quantidade = 0
		for val in lista_cliente:
			xml = self.monta.consulta_parceiros_endereco(val['cnpj'])
			resposta = requests.post(url, headers=self.header_padrao,data=xml)
			endereco = self.monta.recebe_resposta_enderecos(resposta)
			if endereco is not None:
				val['telefone'] = endereco['telefone']
				val['cep'] = endereco['cep']
				val['numero'] = endereco['num']
				val['complemento'] = endereco['complemento']
				val['bairro'] = endereco['bairro']
				val['nome'] = endereco['nome']
				val['tipo'] = endereco['tipo']
				nova_lista.append(val)
				quantidade += 1
				print(quantidade)
		print(nova_lista)
