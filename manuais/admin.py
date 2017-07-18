from django.contrib import admin
from .models import Manual, TipoManual


class ManualAdmin(admin.ModelAdmin):
	list_display = ['nome', 'descricao', 'usuario_criador', 'arquivo', 'tipo', 'file_link']

admin.site.register(Manual, ManualAdmin)
admin.site.register(TipoManual)

admin.site.site_header = 'Intranet Yenzah'
