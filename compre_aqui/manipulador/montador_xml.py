from xml.etree.ElementTree import Element, SubElement, tostring, fromstring, dump
from seguranca import geracao_md5

class montar():

	def __init__(self):
		seguranca = geracao_md5()
		self.senha = seguranca.gerar()

	def montar_xml_autenticacao(self):
		valor = self.monta_xml(service_name="MobileLoginSP.login", dataSet=None)
		return valor

	def resposta_login(self, resposta):
		valor  = fromstring(resposta.content)
		response = valor.find('responseBody')
		self.sessionId = response.find('jsessionid').text

	def recebe_resposta_enderecos(self, venda):
		val = fromstring(venda.content)
		lista_cod = set()
		if val.find('responseBody').find('entities'):
			lista_entity = val.find('responseBody').find('entities')
			indice_telefone = 0
			indice_cep = 0
			indice_num = 0
			indice_complemento = 0
			indice_bairro = 0
			indice_nome_end = 0
			indice_tipo = 0
			dic_endereco = {}
			if lista_entity[0].find('entity'):
				fo
				for idx, val in enumerate(cid.find('metadata').find('fields').getchildren()):
					meta = val
					nome = meta.get('name')
					if nome == 'TELEFONE':
						indice_telefone = idx
					elif nome == 'CEP':
						indice_cep = idx
					elif nome == 'NUMEND':
						indice_num = idx
					elif nome == 'COMPLEMENTO':
						indice_complemento = idx
					elif nome == 'Bairro_NOMEBAI':
						indice_bairro = idx
					elif nome == 'Endereco_NOMEEND':
						indice_nome_end = idx
					elif nome == 'Endereco_TIPO':
						indice_tipo = idx
				dic_endereco['telefone'] = lista_entity.find('entity').find('f'+str(indice_telefone)).text
				dic_endereco['cep'] = lista_entity.find('entity').find('f'+str(indice_cep)).text
				dic_endereco['num'] = lista_entity.find('entity').find('f'+str(indice_num)).text
				dic_endereco['complemento'] = lista_entity.find('entity').find('f'+str(indice_complemento)).text
				dic_endereco['bairro'] = lista_entity.find('entity').find('f'+str(indice_bairro)).text
				dic_endereco['nome'] = lista_entity.find('entity').find('f'+str(indice_nome_end)).text
				dic_endereco['tipo'] = lista_entity.find('entity').find('f'+str(indice_tipo)).text
			return dic_endereco
			else:
				return None
		else:
			return None

	def consulta_parceiros_endereco(self, cod):
		entitys = {}
		root_field = ['TELEFONE', 'CEP', 'NUMEND', 'COMPLEMENTO']
		entitys['Bairro'] = ['NOMEBAI']
		entitys['Endereco'] = ['NOMEEND', 'TIPO']
		criteria = True
		expression = 'this.CGC_CPF= ?'
		parameter = [["I", cod]]
		valor = self.monta_xml(service_name="CRUDServiceProvider.loadRecords", dataSet=True, rootEntity="Parceiro", root_field=root_field,entity_field=entitys, criteria=True, expression=expression, parameter=parameter)
		return valor

	def monta_xml(self, service_name=None, dataSet=None, rootEntity=None, root_field=None,entity_field=None, criteria=None,expression=None,parameter=None):
		service = Element("serviceRequest", serviceName=service_name)
		body = SubElement(service, "requestBody")
		if dataSet is None:
			nome = SubElement(body, "NOMUSU")
			nome.text = "APITESTE"
			senha = SubElement(body, "INTERNO2")
			senha.text = self.senha
		else:
			dataSet = SubElement(body,"dataSet", rootEntity=rootEntity, includePresentationFields="S", parallelLoader="false")
			entity = SubElement(dataSet, "entity", path="")
			if root_field is not None:
				for value in root_field :
						fiel = SubElement(entity, "field", name=value)
			for key,value in entity_field.items():
				entity = SubElement(dataSet,"entity", path=key)
				for va in value:
					fiel = SubElement(entity, "field", name=va)
			if criteria is not None:
				criteria = SubElement(dataSet,"criteria")
				expression_tag = SubElement(criteria, "expression")
				expression_tag.text = expression
				if parameter is not None:
					for val in parameter:
						parameter_tag = SubElement(criteria, "parameter", type=val[0])
						parameter_tag.text = val[1]
		valor = tostring(service)
		return valor
