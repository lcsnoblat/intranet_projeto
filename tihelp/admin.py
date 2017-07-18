from django.contrib import admin

# Register your models here.
from .models import TipoChamado, Chamado, Interacao, ChamadoAnonimo


class ChamadoAdmin(admin.ModelAdmin):
    fields = ['tipo','descricao','data_criacao','usuario_solicitante', 'resolvido']

admin.site.register(TipoChamado)
admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(Interacao)
admin.site.register(ChamadoAnonimo)

