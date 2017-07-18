from django.contrib import admin

from .models import Processo, Linha, Produto, Pedido, PedidoProduto

admin.site.register(Processo)
admin.site.register(Linha)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(PedidoProduto)
