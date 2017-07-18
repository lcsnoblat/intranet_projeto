from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cadastrar/$', views.CadastrarSolicitacaoView.as_view(), name='cadastrar_pedido'),
    url(r'^listar/$', views.ListarSolicitacoesView.as_view(), name ='listar_pedidos'),
    url(r'^historico/(?P<numero>[0-9]+)$', views.HistoricoView.as_view(), name='historico_pedido')
]
