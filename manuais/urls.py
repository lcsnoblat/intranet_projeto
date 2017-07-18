from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/$', views.home, name='home_manual'),
	url(r'^/material/', views.material, name='material_comercial'),
	url(r'^/gente_e_gestao', views.gente_e_gestao, name='gente_e_gestao'),
	url(r'^/faq', views.faq, name="faq")
]
