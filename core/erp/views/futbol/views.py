from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from core.erp.models.futbol.models import InformeDeJugador, InformeDePartido
from django.contrib.auth.models import User
from core.erp.forms.futbol.forms import InformePartidoForm, InformeJugadorForm
from core.authenticate.models import UserRelation
# ------
class InformePartidoCreate(LoginRequiredMixin, CreateView):
    model = InformeDePartido
    form_class = InformePartidoForm
    template_name = 'futbol/create_informe_partido.html'
    login_url = 'login/'
    success_url = '/'

class InformePartidoList(LoginRequiredMixin, ListView):
    model = InformeDePartido
    template_name = 'futbol/informes_partidos_list.html'
    context_object_name = 'informes'
    login_url = 'login/'
    
    

class InformePartidoDetail(LoginRequiredMixin, DetailView):
    model = InformeDePartido
    template_name = 'futbol/informe_partido_detail.html'
    context_object_name = 'informe'
    login_url = 'login/'
    

class InformePartidoDelete(LoginRequiredMixin, DeleteView):
    pass

## ------
class InformeJugadorCreate(LoginRequiredMixin, CreateView):
    model = InformeDeJugador
    form_class = InformeJugadorForm
    template_name = 'futbol/create_informe_partido_player.html'
    success_url = '/'
    login_url = 'login/'

class JugadorList(LoginRequiredMixin, ListView):
    model = UserRelation
    template_name = 'futbol/listado_jugadores.html'
    context_object_name = 'jugadores'
    login_url = 'login/'

class JugadorInformesList(LoginRequiredMixin, ListView):
    model = InformeDeJugador
    template_name = 'futbol/informes_jugador_list.html'
    context_object_name = 'informes'
    login_url = 'login/'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        jugador_id = self.kwargs.get('pk')
        print(jugador_id)
        jugador = User.objects.get(id = jugador_id)

        print(jugador)
        context['informes_jugador'] = InformeDeJugador.objects.all().filter(user=jugador)
        print(context['informes_jugador'])
        return context

class InformeJugadorDetail(LoginRequiredMixin, DetailView):
    model = InformeDeJugador
    context_object_name = 'informe'
    template_name = 'futbol/informe_jugador_detail.html'
    login_url = 'login/'
    
class InformeJugadorDelete(LoginRequiredMixin, DeleteView):
    model = InformeDeJugador




