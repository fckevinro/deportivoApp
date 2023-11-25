from django.contrib import admin
from core.erp.models.psicologia.models import Cuestionarios
from core.erp.models.medicina.models import Consulta, Visita, Hallazgos
from core.erp.models.futbol.models import InformeDePartido, InformeDeJugador
# Register your models here.

class CuestionariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id',)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'motivo_consulta')

class VisitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta')

class HallazgosAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta_id')


admin.site.register(Cuestionarios, CuestionariosAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Hallazgos, HallazgosAdmin)
admin.site.register(InformeDePartido)
admin.site.register(InformeDeJugador)
