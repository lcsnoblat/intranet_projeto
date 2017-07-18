from django.db import models
from django.contrib.auth.models import User
from help.enviar_email import EnviarEmail
from django.conf import settings
from datetime import datetime
from decimal import Decimal

class Processo(models.Model):
    nome = models.CharField('Nome do Processo', max_length=50)
    usuarios = models.ManyToManyField(User)
    limite_produtos = models.IntegerField('Limite de produtos para venda')

    def __str__(self):
        return self.nome

class Linha(models.Model):
    nome = models.CharField('Nome', max_length = 50)
    descricao = models.CharField('Descição', max_length = 250)
    ativa = models.BooleanField('Ativo')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField('Nome', max_length = 100)
    descricao = models.CharField('Descição', max_length = 2500)
    linha = models.ForeignKey('Linha', null=False ,related_name='produtos')
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    ativo = models.BooleanField('Ativo')

    def __str__(self):
        return '{} - {}'.format(self.nome, self.linha)

class Pedido(models.Model):
    # SEM_ESTADO = 'SEM_ESTADO'
    SOLICITADO = 'SOLICITADO'
    RECUSADO = 'RECUSADO'
    ACEITO = 'ACEITO'
    ENVIADO = 'ENVIADO'
    DISPONIVEL = 'DISPONIVEL'


    ESTADO_PEDIDO = (
        # (SEM_ESTADO, 'Sem estado'),
        (SOLICITADO, 'Pedido solicitado'),
        (RECUSADO, 'Pedido recusado'),
        (ACEITO, 'Pedido aceito'),
        (ENVIADO, 'Pedido enviado'),
        (DISPONIVEL, 'Pedido disponível')
    )

    numero = models.AutoField(primary_key=True)
    solicitante = models.ForeignKey(User, related_name='pedidos')
    data_abertura = models.DateTimeField('Data de abertura')
    valor = models.DecimalField('Valor total dos produtos', max_digits=8, decimal_places=2, default = 0.0)
    processo = models.ForeignKey('Processo')
    estado = models.CharField(
        max_length=25,
        choices = ESTADO_PEDIDO,
        default=SOLICITADO,
    )

    @classmethod
    def create(cls, solicitante, processo):
        pedido = cls(solicitante = solicitante, processo = processo, data_abertura = datetime.now())
        return pedido

    def inserir_produtos(self, dicionario_produto):
        self.save()
        quantidade = 0
        for dicionario in dicionario_produto:
            quantidade += int(dicionario['quantidade'])
        if self.processo.limite_produtos >= quantidade:
            for dicionario in dicionario_produto:
                pedido_produto = PedidoProduto.create(dicionario['produto'], dicionario['quantidade'], self)
                pedido_produto.save()
            self.save()
            return True
        else:
            return False

    def enviar_email(self):
        assunto_solicitante = 'Solicitação de produtos Yenzah'
        descricao_solicitante = 'Você solicitou produtos da Yenzah, e numero da sua solicitação é {}.'.format(self.numero)
        EnviarEmail(assunto_solicitante, descricao_solicitante, settings.EMAIL_YENZAH, [self.solicitante.email])

        assunto_executante = 'Foi criada uma nova solicitação de produtos no Yenzah Atende'
        descricao_executante = 'O usuário {} de nome {} solicitou novos produtos, esse é o código da nova solicitação {}.'.format(self.solicitante.username, self.solicitante.get_full_name(), self.numero)

        lista_usuarios = [usuario.email for usuario in self.processo.usuarios.all()]
        EnviarEmail(assunto_executante, descricao_executante, settings.EMAIL_YENZAH, lista_usuarios)

    def save(self, *args, **kwargs):
        if self.estado is 'SEM_ESTADO':
            self.estado = 'SOLICITADO'
        valor = Decimal(0)
        for pedidoproduto in self.produtos.all():
            valor += Decimal(pedidoproduto.quantidade) * pedidoproduto.preco_unitario
        self.valor = valor
        super(Pedido, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.numero)

class PedidoProduto(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, null=False, blank= False, related_name='produtos')
    quantidade = models.IntegerField('quantidade')
    produto = models.ForeignKey('Produto', null=False, blank=False)
    preco_unitario = models.DecimalField('Preço unitário', max_digits=6, decimal_places=2, null= False, blank=False)

    @classmethod
    def create(cls, produto, quantidade, pedido):
        pedido_produto = cls(produto=produto, quantidade=quantidade, preco_unitario = produto.preco, pedido = pedido)
        return pedido_produto

    def __str__(self):
        return '{} - {}'.format(self.pedido, self.produto)
