from django.db import models
from django.contrib.auth.models import User
from help.enviar_email import EnviarEmail


class TipoChamado(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    usuario_executante = models.ForeignKey(User, verbose_name="Usuário atendente", related_name='tipo_chamado')

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    descricao = models.CharField(max_length=750, verbose_name="Faça uma descrição do chamado")
    resolvido = models.BooleanField()
    data_criacao = models.DateTimeField('Data da criação')
    data_prevista_conclusao = models.DateTimeField('Data prevista de conclusão', null=True)
    data_conclusao = models.DateTimeField('Data da conclusão', null=True)
    tipo = models.ForeignKey(TipoChamado, verbose_name="Tipo de chamado")
    usuario_solicitante = models.ForeignKey(User, verbose_name="Usuário solicitante", related_name='chamado')

    def __str__(self):
        return self.descricao

    def enviar_email(self, assunto, descricao, de, para):
        EnviarEmail(assunto, descricao, de, para)


class Interacao(models.Model):
    descricao = models.CharField(max_length=700)
    chamado = models.ForeignKey(Chamado)
    usuario = models.ForeignKey(User, verbose_name="Usuário", related_name='interacao')
    data_interacao = models.DateTimeField('Data da interacao')

    def __str__(self):
        return self.descricao
