from typing import Any
from django import http
from django.views.generic import ListView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from core.authenticate.models import UserRelation, Plantel, User


from django.shortcuts import redirect

# Decorador personalizado para verificar si el usuario pertenece al grupo "Player"
def user_is_player(user):
    return user.groups.filter(name='Player').exists()

# Vista de inicio que redirige al usuario si pertenece al grupo "Player"
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = 'login/'

    # Sobreescribe el método dispatch para realizar la verificación y la redirección
    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args: Any, **kwargs: Any):
        context = {}
        first_div_players = UserRelation.objects.all().filter(plantel__id = 1)

        context['jugadores'] = first_div_players

        return render(request,self.template_name, context)