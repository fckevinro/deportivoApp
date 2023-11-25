from typing import Any
from django.db.models.query import QuerySet

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.models.medicina.models import Consulta
from core.erp.forms.medicina.forms import ConsultaForm
from core.authenticate.models import UserRelation
from django.http import HttpResponseRedirect


class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'medicina/consulta_delete.html'
    login_url = '/login'

class ConsultaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'medicina/consulta_form.html'

    login_url = '/login'

class ConsultaDetailView(LoginRequiredMixin, DetailView):
    model = Consulta
    template_name = 'medicina/consulta_detail.html'
    context_object_name = 'consulta'
    login_url = '/login'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(self.object.user)
        context['jugador'] = UserRelation.objects.get(user=self.object.user)
        return context
    
    def post(self, request, *args, **kwargs):
        try:    
            consulta_id = request.POST.get('consulta_id')
            if request.POST.get('estado_consulta'):
                estado_consulta = 'Cerrado'
            else:
                estado_consulta = 'Activo'
                
            print(request.POST)

            consulta = Consulta.objects.get(id=consulta_id)
            consulta.estado = estado_consulta
            consulta.save()
        except:
            pass

        # Obtener el objeto UserRelation basado en el ID del jugador
        try:

            jugador_id = request.POST.get('jugador_id')
            nuevo_estado_medico = request.POST.get('nuevo_estado_medico')
            user_relation = UserRelation.objects.get(user__id=jugador_id)
            # Actualizar el campo "estado_medico"
            user_relation.estado_medico = nuevo_estado_medico
            user_relation.save()
        except:
            pass

        return HttpResponseRedirect(request.path)

class ConsultasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'medicina/consulta_form.html'
    model = Consulta
    form_class = ConsultaForm

    login_url = '/login'
    success_url='/'

    

class ConsultasListView(LoginRequiredMixin, ListView):
    template_name = 'medicina/consultas_list.html'
    model = Consulta
    object_context_name = 'consultas'
    login_url = '/login'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        jugadores = UserRelation.objects.all()
        consultas = Consulta.objects.all()
        context['jugadores'] = jugadores
        context['consultas'] = consultas
        context['cerrados'] = Consulta.objects.all().filter(estado='Cerrado').count()
        context['activos'] = Consulta.objects.all().filter(estado='Activo').count()
        context['otros'] = Consulta.objects.all().exclude(estado='Activo').exclude(estado='Cerrado').count()

        return context