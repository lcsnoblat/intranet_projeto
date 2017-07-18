import xlrd
from django.contrib.auth.models import User

class LeitorCriador:

	path =''

	def __init__(self):
		self.path = input("Digite o path do arquivo: ")

	def get_user(self):
		livro = xlrd.open_workbook(self.path)
		folha = livro.sheets()[0]
		numero_linhas = folha.nrows 
		linha_atual = 0

		while linha_atual < numero_linhas:
			usuario_primeiro_nome = folha.cell_value(linha_atual, 1)
			usuario_segundo_nome = folha.cell_value(linha_atual, 2)
			usuario_email = folha.cell_value(linha_atual, 3)
			try:
				nome_usuario = '{0}.{1}'.format(usuario_primeiro_nome.lower(), usuario_segundo_nome.lower())
				usuario = User.objects.create_user(nome_usuario, usuario_email, 'yenzah123')
				usuario.first_name = usuario_primeiro_nome
				usuario.last_name = usuario_segundo_nome
				usuario.save()
				print('Usuario {} foi criado'.format(usuario_primeiro_nome))
			except:
				print('Erro no usuario {}',format(usuario_primeiro_nome))
			linha_atual += 1