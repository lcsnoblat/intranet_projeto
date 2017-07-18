
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chamado, TipoChamado, Interacao
from .forms import ChamadoForm, InteracaoForm 
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.conf import settings

@login_required
def index(request):
    usuario = request.user
    chamados = Chamado.objects.filter(usuario_solicitante = usuario)
    return render(request, 'home_dphelp.html', {'usuario':usuario, 'chamados': chamados})

@login_required
def cadastrar(request):
    #pega todos os tipos de chamados
    tipos_chamados = TipoChamado.objects.order_by('nome')
    if request.method == "POST":
        form = ChamadoForm(request.POST)
        if form.is_valid():
            dados = form.data
            chamado = Chamado()
            chamado.tipo = TipoChamado.objects.get(id = dados['tipo'])
            chamado.descricao = dados['descricao']
            chamado.usuario_solicitante = request.user
            chamado.data_criacao = datetime.now()
            chamado.resolvido = False
            chamado.save()
            texto_email = "O código do chamado é: " + str(chamado.id) + "\nO chamado é do tipo: " + chamado.tipo.nome + "\n" + "A descrição do chamado é: " + chamado.descricao
            chamado.enviar_email("Novo chamado aberto" , texto_email, settings.EMAIL_YENZAH,[chamado.usuario_solicitante.email, chamado.tipo.usuario_executante.email] )
            return redirect('index')
    else:
        form = ChamadoForm()
    return render(request, 'cadastro_dphelp.html', {'form': form, 'tipos_chamados' : tipos_chamados, 'usuario':request.user})

@login_required
def listar(request):
    usuario = request.user
    #pega a lista de todos os chamados desse usuário
    lista_de_chamados_solicitante = Chamado.objects.filter(usuario_solicitante=usuario)
    lista_de_chamados_executante = Chamado.objects.filter(tipo__usuario_executante=usuario)

    #faz o filtro em todos os chamados desse usuário abertos
    lista_de_chamados_solicitante_limpa = lista_de_chamados_solicitante.filter(resolvido=False)
    lista_de_chamados_executante_limpa = lista_de_chamados_executante.filter(resolvido=False)

    #faz o filtro de todos os chamados desse usuário que estão com o status resolvido
    lista_de_chamados_solicitante_fechado = lista_de_chamados_solicitante.filter(resolvido=True)
    lista_de_chamados_executante_fechado = lista_de_chamados_executante.filter(resolvido=True)
    return render(request, 'lista_dphelp.html', {'lista_solicitante': lista_de_chamados_solicitante_limpa, 
                                            'lista_executante': lista_de_chamados_executante_limpa,
                                            'usuario':request.user,
                                            'lista_solicitante_fechado': lista_de_chamados_solicitante_fechado,
                                            'lista_executante_fechado': lista_de_chamados_executante_fechado})

@login_required
def interar(request, chamado_id):
    #Chamado pode não existir
    try:
        chamado = Chamado.objects.get(id=chamado_id)
    except:
        return redirect('index')
    if request.method =="POST":
        form = InteracaoForm(request.POST)
        if form.is_valid():
            dados = form.data
            interacao = Interacao()
            interacao.chamado = Chamado.objects.get(id=chamado_id) 
            interacao.descricao = dados['descricao']
            if dados.get("resolvido"):
                resolvido = True
            else:
                resolvido = False
            usuario = request.user

            #Só o usuário solicitante ou executante pode fazer uma interação
            if interacao.chamado.usuario_solicitante == usuario or interacao.chamado.tipo.usuario_executante == usuario:
                interacao.usuario = usuario
                interacao.data_interacao = datetime.now()
                chamado.ativar = True

                #reabrindo um chamado fechado
                if chamado.resolvido:
                    chamado.resolvido = False

                #fechando um chamado 
                if resolvido:
                    chamado.resolvido = True
                chamado.save()
                interacao.save()
                interacao.chamado.enviar_email("Yenzah Atende: Interação no chamado " + str(interacao.chamado_id), "Prezado usuário {0}, ocorreu a seguinte interação no chamado: \n {1} ".format(chamado.usuario_solicitante,interacao.descricao), settings.EMAIL_YENZAH,[interacao.chamado.usuario_solicitante.email, interacao.chamado.tipo.usuario_executante.email])
                return historico(request, chamado_id)
            else:
                return redirect(index)
    else:
        form = InteracaoForm()
    return render(request, 'interacao_dphelp.html', {'form' : form, 'chamado': chamado, 'usuario':request.user, 'chamado_id' : chamado_id })


@login_required
def historico(request, chamado_id):
    usuario = request.user
    #chamado pode não existir
    try:
        chamado = Chamado.objects.get(id=chamado_id)
    except:
        return redirect('index_dphelp')

    # bloqueia o acesso para os usuários que não podem ver esse chamado.
    if usuario.id == (chamado.usuario_solicitante.id) or usuario.id == (chamado.tipo.usuario_executante.id):
        lista_de_interacao = Interacao.objects.filter(chamado_id=chamado_id)
        return render(request, 'historico_dphelp.html', {'lista': lista_de_interacao, 'chamado': chamado, 'usuario':request.user})

    else:
        lista_de_interacao = None
        return redirect('index_dphelp')
    

