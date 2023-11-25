from django.urls import path


from core.home.views.home.views import HomeView
from core.home.views.planteles.views import *

from core.home.views.psicologia.views import (
    CuestionariosPorJugadorView, 
    CuestionariosPorJugadorPDFView, 
    PsicologiaDivisionListView, 
    PsicologiaPlayersListView, 
    RespuestasPorDivisionListView, 
    RespuestasListView,
    ExportCSVView,
)       

from core.home.views.medicina.views import (
    ExpedientesListView,
    ExpedienteDetailView
)

urlpatterns = [
    path('', HomeView.as_view()),
    # Generales
    path('planteles/', DivisionListView.as_view(), name='planteles.list'),
    path('planteles/<str:division>/jugadores/', PlayersListView.as_view(), name='plantel.jugadores'),
    # Psicologia
    path('psicologia/planteles/', PsicologiaDivisionListView.as_view(), name='psicologia.planteles.list'),
    path('psicologia/planteles/<str:division>/jugadores/', PsicologiaPlayersListView.as_view(), name='psicologia.plantel.jugadores'),
    path('psicologia/planteles/jugadores/<str:first_name>/<str:last_name>', CuestionariosPorJugadorView.as_view(), name='jugador.detail'),
    path('psicologia/planteles/jugadores/<str:first_name>/<str:last_name>/pdf', CuestionariosPorJugadorPDFView.as_view(), name='jugador.detail.pdf'),
    # Respuestas
    path('psicologia/respuestas/<str:division>', RespuestasPorDivisionListView.as_view(), name='respuestas.division'),
    path('psicologia/all/respuestas/', RespuestasListView.as_view(), name='respuestas'),
    path('psicologia/all/respuestas/export_csv/', ExportCSVView.as_view(), name='export_csv'),  # Agrega esta línea
    
    # Medicina
    path('medicina/expedientes', ExpedientesListView.as_view(), name='expedientes'),
    path('medicina/expedientes/<str:first_name>/<str:last_name>', ExpedienteDetailView.as_view(), name='expediente.detail')
]