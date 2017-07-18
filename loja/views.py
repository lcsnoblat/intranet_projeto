from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import *


@method_decorator(login_required, name = 'dispatch')
class CadastrarSolicitacaoView(View):

    template = 'cadastrar_pedido.html'


    def get(self, request,*args, **kwargs):
        linha = Linha.objects.filter(ativa = True, produtos__ativo = True).distinct()
        return render(self.request, self.template, {'usuario': request.user, 'linha': linha })

    def post(self, request,*args, **kwargs):
        linha = Linha.objects.filter(ativa = True, produtos__ativo = True).distinct()
        usuario = request.user
        data = request.POST
        data = dict(data)
        lista_produtos = []
        for key, values in data.items():
            if key == 'csrfmiddlewaretoken':
                continue
            if values[0] is not '':
                produto= Produto.objects.get(id=key)
                dicionario = {}
                dicionario['produto'] = produto
                dicionario['quantidade'] = values[0]
                lista_produtos.append(dicionario)
        if len(lista_produtos) == 0:
            msg = 'Você não solicitou nenhum produto.'
            return render(self.request, self.template, {'usuario': request.user, 'linha': linha, 'erro': msg})
        pedido = Pedido.create(usuario, Processo.objects.get(nome='RH'))
        estado = pedido.inserir_produtos(lista_produtos)
        if estado == True:
            pedido.enviar_email()
            msg = 'Pedido cadastrado com sucesso.'
            return render(self.request, self.template, {'usuario': request.user, 'linha': linha, 'msg': msg})
        else:
            pedido.delete()
            msg = 'Erro ao cadastrar o pedido, foram solicitados mais de 5 produtos.'
            return render(self.request, self.template, {'usuario': request.user, 'linha': linha, 'erro': msg})



@method_decorator(login_required, name='dispatch')
class ListarSolicitacoesView(View):

    template = 'listar_pedidos.html'

    def get(self, request,*args,**kwargs):
        pedidos = Pedido.objects.filter(solicitante = request.user).order_by('-data_abertura')
        pedidos_admin = Pedido.objects.filter(processo__usuarios = request.user ).order_by('-data_abertura')
        return render(self.request, self.template, {'usuario': request.user, 'pedidos': pedidos, 'pedidos_admin' : pedidos_admin})

@method_decorator(login_required, name='dispatch')
class HistoricoView(View):

    template ='historico_pedido.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        numero = int(kwargs['numero'])
        try:
            pedido = Pedido.objects.get(numero =numero)
        except:
            redirect('home')

        if pedido.solicitante.id == usuario.id or usuario in pedido.processo.usuarios.all():
            return render(self.request, self.template, {'usuario': request.user, 'pedido': pedido})
        else:
            redirect('home')

    def post(self, request, *args, **kwargs):
        usuario = request.user
        numero = int(kwargs['numero'])
        try:
            pedido = Pedido.objects.get(numero =numero)
        except:
            redirect('home')
        data = request.POST
        data = dict(data)
        estado = data['estado']
        pedido.estado = estado[0]
        pedido.save()
        return render(self.request, self.template, {'usuario': request.user, 'pedido': pedido})
