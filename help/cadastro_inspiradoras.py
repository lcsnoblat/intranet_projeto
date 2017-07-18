import xlrd
from django.contrib.auth.models import User, Group

class LeitorCriador:

    def get_user(self):
        self.path = input("Digite o path do arquivo: ")
        livro = xlrd.open_workbook(self.path)
        folha = livro.sheets()[0]
        numero_linhas = folha.nrows 
        linha_atual = 0
        grupo =  Group.objects.get(name="inspiradora")
        
        while linha_atual < numero_linhas:
            usuario_primeiro_nome = folha.cell_value(linha_atual, 0)
            usuario_segundo_nome = folha.cell_value(linha_atual, 1)
            usuario_cpf = folha.cell_value(linha_atual, 2)
            try:                
                usuario = User.objects.create_user(usuario_cpf, '', 'yenzah123')
                usuario.first_name = usuario_primeiro_nome
                usuario.last_name = usuario_segundo_nome
                usuario.groups.add(grupo)
                usuario.save()
                print('Usuario {} foi criado'.format(usuario_primeiro_nome))
            except:
                print('Erro no usuario {}',format(usuario_primeiro_nome))
            linha_atual += 1