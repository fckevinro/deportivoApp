from django.urls import path

from core.erp.views.psicologia.views import CuestionariosCreateView, CuestionarioCompletedView
from core.erp.views.medicina.views import ConsultasListView, ConsultasCreateView, ConsultaDetailView, ConsultaUpdateView, ConsultaDeleteView
from core.erp.views.futbol.views import InformePartidoCreate, InformePartidoList, InformePartidoDetail, InformeJugadorCreate, JugadorList, InformeJugadorDetail, JugadorInformesList
urlpatterns = [
    path('psicologia/new', CuestionariosCreateView.as_view(), name='cuestionario.new'),
    path('psicologia/success', CuestionarioCompletedView.as_view(), name='cuestionario.completed'),
    path('medicina/consultas/', ConsultasListView.as_view(), name='consultas.list'),
    path('medicina/consultas/new', ConsultasCreateView.as_view(), name='consulta.new'),
    path('medicina/consulta/<int:pk>', ConsultaDetailView.as_view(), name='consulta.detail'),
    path('medicina/consulta/<int:pk>/update', ConsultaUpdateView.as_view(), name='consulta.update'),
    path('medicina/consulta/<int:pk>/delete', ConsultaDeleteView.as_view(), name='consulta.delete'),
    # ----
    path('futbol/informes/partidos/new/', InformePartidoCreate.as_view(), name='informe.partido.new'),
    path('futbol/informes/partidos',  InformePartidoList.as_view(), name='informes.list'),
    path('futbol/informes/partidos/<int:pk>', InformePartidoDetail.as_view(), name='informes.detail'),
    # ----
    path('futbol/informes/partidos/jugadores/new', InformeJugadorCreate.as_view(), name='informes.jugador.new'),
    path('futbol/informes/partidos/jugadores', JugadorList.as_view(), name='informes.jugador.list'),
    path('fitbol/informes/partidos/jugadores/<int:pk>', InformeJugadorDetail.as_view(), name='informe.jugador.detail'),
    path('futbol/informes/partidos/player/<int:pk>', JugadorInformesList.as_view(), name='informes.list'),
]