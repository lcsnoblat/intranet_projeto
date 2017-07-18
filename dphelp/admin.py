from django.contrib import admin
from .models import TipoChamado, Chamado, Interacao

class ChamadoAdmin(admin.ModelAdmin):
    fields = ['tipo','descricao','data_criacao','usuario_solicitante', 'resolvido']

admin.site.register(TipoChamado)
admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(Interacao)