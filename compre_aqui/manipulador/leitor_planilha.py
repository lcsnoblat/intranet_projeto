import xlrd


class manipulador_xlsx:
	
	def get_clientes(self):
		livro = xlrd.open_workbook('Clientes.xlsx')
		# pegar a segunda folha da planilha
		folha = livro.sheets()[1]
		# como vou pular o cabeçalho necessito descrementar 1 no numero de linhas
		numero_linhas = folha.nrows - 1
		linha_atual = 2
		lista_cliente = []
		while linha_atual < numero_linhas:
			# pular o cabeçalho
			linha_atual +=1
			dicionario_aux = {}
			cliente_uf = folha.cell_value(linha_atual, 3)
			cliente_cidade = folha.cell_value(linha_atual, 4)
			cliente_razao = folha.cell_value(linha_atual, 5)
			cliente_fantasia = folha.cell_value(linha_atual, 6)
			cliente_cnpj = folha.cell_value(linha_atual, 7)
			cliente_can = folha.cell_value(linha_atual, 8)
			dicionario_aux['razao'] = cliente_razao
			dicionario_aux['fantasia'] = cliente_fantasia
			dicionario_aux['uf'] = cliente_uf
			dicionario_aux['cidade'] = cliente_cidade
			dicionario_aux['can'] = cliente_can
			dicionario_aux['cnpj'] = cliente_cnpj
			lista_cliente.append(dicionario_aux)
		return lista_cliente

	def get_clientes_complemento(self, clientes):
		livro = xlrd.open_workbook('Parceiros.xlsx')
		folha = livro.sheets()[0]
		numero_linhas = folha.nrows - 1
		numero_colunas = folha.ncols
		nova_lista = []
		contador = 0
		for cliente in clientes:
			linha_atual = 0
			razao_social = cliente['razao']
			while linha_atual < numero_linhas:
				linha_atual +=1
				razao = folha.cell_value(linha_atual, 3)
				if razao_social == razao:
					cliente['tipo_endereco'] = folha.cell_value(linha_atual, numero_colunas-23)
					cliente['endereco'] = folha.cell_value(linha_atual, numero_colunas-22)
					cliente['numero'] = folha.cell_value(linha_atual, numero_colunas-21)
					cliente['complemento'] = folha.cell_value(linha_atual, numero_colunas-20)
					cliente['bairro'] = folha.cell_value(linha_atual, 9)
					cliente['cep'] = folha.cell_value(linha_atual, 12)
					cliente['telefone'] = folha.cell_value(linha_atual, 14)
					nova_lista.append(cliente)
					linha_atual = 0
					contador += 1
					break
		print(contador)
		return nova_lista
