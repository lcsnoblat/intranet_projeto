from django.conf.urls import urls
from . import views

urlspatterns = [
	url(r'^/perfil/(?P<perfil_id>[0-9]+)$', views.listar, name='listar_perfil'),
]