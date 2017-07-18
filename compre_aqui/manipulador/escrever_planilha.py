import xlsxwriter

class CriarPlanilha:

	def criar(self, lista_clientes):
		workbook = xlsxwriter.Workbook('lista_clientes.xlsx')
		worksheet = workbook.add_worksheet()
		linha = 0
		coluna = 0

		worksheet.write(linha, coluna, 'CNPJ')
		worksheet.write(linha, coluna+1, 'Razão Social')
		worksheet.write(linha, coluna+2, 'Nome Fantasia')
		worksheet.write(linha, coluna+3, 'UF')
		worksheet.write(linha, coluna+4, 'Cidade')
		worksheet.write(linha, coluna+5, 'Bairro')
		worksheet.write(linha, coluna+6, 'Endereço')
		worksheet.write(linha, coluna+7, 'Numero')
		worksheet.write(linha, coluna+8, 'Complemento')
		worksheet.write(linha, coluna+9, 'Telefone')
		worksheet.write(linha, coluna+10, 'Tipo')
		worksheet.write(linha, coluna+11, 'URL')
		for idx, cliente in enumerate(lista_clientes):
			idx +=1
			worksheet.write(idx, coluna, cliente['cnpj'])
			worksheet.write(idx, coluna+1, cliente['razao'])
			worksheet.write(idx, coluna+2, cliente['fantasia'])
			worksheet.write(idx, coluna+3, cliente['uf'])
			worksheet.write(idx, coluna+4, cliente['cidade'])
			worksheet.write(idx, coluna+5, cliente['bairro'])
			endereco = str(cliente['tipo_endereco'])
			endereco += " " + str(cliente['endereco'])
			worksheet.write(idx, coluna+6, endereco)
			if cliente['numero']:
				worksheet.write(idx, coluna+7, cliente['numero'])
			else:
				worksheet.write(idx, coluna+7, 'S/N')
			worksheet.write(idx, coluna+8, cliente['complemento'])
			worksheet.write(idx, coluna+9,cliente['telefone'])
			if cliente['can'] == '6':
				tipo = 'E-commerce'
				worksheet.write(idx, coluna+10, tipo)
				worksheet.write(idx, coluna+11, 'http')
			else:
				tipo = 'Venda no local'
				worksheet.write(idx, coluna+10, tipo)
				worksheet.write(idx, coluna+11, '---')
			

		workbook.close()


