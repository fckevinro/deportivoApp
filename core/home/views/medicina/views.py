from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from core.authenticate.models import UserRelation
from core.erp.models.medicina.models import Consulta

class ExpedientesListView(LoginRequiredMixin, ListView):
    template_name = 'medicina/expedientes_list.html'
    model = UserRelation
    context_object_name = 'jugadores'
    login_url = '/login'


    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    

class ExpedienteDetailView(LoginRequiredMixin, View):
    template_name = 'medicina/expediente_detail.html'
    login_url = '/login'


    def get(self, request, first_name, last_name):
        jugador = UserRelation.objects.get(user__first_name=first_name ,user__last_name=last_name)
        id = jugador.user.id
        print(jugador.user.first_name + jugador.user.last_name)
        consultas = Consulta.objects.all().filter(user__id = id)
        context = {
            'consultas': consultas,
            'nombre': jugador.user.first_name + ' ' +jugador.user.last_name,
            'perfil': jugador.image,
            'estado': jugador.estado_medico,
            'player_id': id,
            'jugador': jugador
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        jugador_id = request.POST.get('jugador_id')
        nuevo_estado_medico = request.POST.get('nuevo_estado_medico')

        # Obtener el objeto UserRelation basado en el ID del jugador
        user_relation = UserRelation.objects.get(user__id=jugador_id)

        # Actualizar el campo "estado_medico"
        user_relation.estado_medico = nuevo_estado_medico
        user_relation.save()

        return HttpResponseRedirect(request.path)