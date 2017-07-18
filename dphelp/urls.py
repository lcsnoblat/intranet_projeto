from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_dphelp'),
    url(r'^cadastrar/$', views.cadastrar, name="cadastrar_dphelp"),
    url(r'^listar/$', views.listar, name="listar_dphelp"),
    url(r'^interacao/(?P<chamado_id>[0-9]+)$', views.interar, name="interar_dphelp"),
    url(r'^historico/(?P<chamado_id>[0-9]+)$', views.historico, name="historico_dphelp")

]
