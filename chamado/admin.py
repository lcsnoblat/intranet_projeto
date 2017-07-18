from django.contrib import admin

from .models import ChamadoDP, ChamadoMKT, ChamadoTI, ChamadoNConformidade, InteracaoDP, InteracaoMKT, InteracaoTI, InteracaoNCorformidade, TipoChamadoDP, TipoChamadoMKT, TipoChamadoTI, TipoChamadoNConformidade

admin.site.register(ChamadoDP)
admin.site.register(ChamadoTI)
admin.site.register(ChamadoMKT)
admin.site.register(ChamadoNConformidade)
admin.site.register(TipoChamadoDP)
admin.site.register(TipoChamadoTI)
admin.site.register(TipoChamadoMKT)
admin.site.register(TipoChamadoNConformidade)
admin.site.register(InteracaoDP)
admin.site.register(InteracaoTI)
admin.site.register(InteracaoMKT)
admin.site.register(InteracaoNCorformidade)
