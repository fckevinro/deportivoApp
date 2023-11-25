from typing import Any
from django.views.generic import ListView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from core.authenticate.models import UserRelation, Plantel
from django.shortcuts import render, redirect, redirect


# Create your views here.
def user_is_player(user):
    return user.groups.filter(name='Player').exists()

class DivisionListView(LoginRequiredMixin, ListView):
    model = Plantel
    template_name = 'divisiones/divisiones_list.html'
    context_object_name = 'divisiones'

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        return super().dispatch(request, *args, **kwargs)

class PlayersListView(LoginRequiredMixin, View):
    template_name = 'divisiones/jugadores_list.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, division):
        plantel = Plantel.objects.get(division = division)
        jugadores = UserRelation.objects.all().filter(plantel__id = plantel.id)
        context = {
            'jugadores': jugadores,
            'plantel': plantel.division
        }

        return render(request, self.template_name, context)