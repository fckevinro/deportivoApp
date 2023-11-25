from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, redirect


# Create your views here.

class LoginInterfaceView(LoginView):
    template_name = 'authenticate/sign-in.html'

    def get_success_url(self):
        if self.request.user.groups.filter(name='Player').exists():
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return '/psicologia/new'  # Reemplaza con la URL a la que deseas redirigir a los jugadores
        return super().get_success_url()
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')  # Reemplaza 'home' con la URL a la que deseas redirigir al usuario después de iniciar sesión
        return super().dispatch(request, *args, **kwargs)
    
    
    
class LogoutInterfaceView(LogoutView):
    template_name = 'authenticate/sign-out.html'

