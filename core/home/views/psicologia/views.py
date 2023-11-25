from typing import Any
from django.http import  HttpResponse
from django.http.response import HttpResponse
from django.views.generic import  ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from datetime import datetime, timedelta, date
from django.db.models import Q, Prefetch, QuerySet

from core.authenticate.models import UserRelation
from core.erp.models.psicologia.models import Cuestionarios
from core.authenticate.models import UserRelation, Plantel

from core.home.graphs.psicologia import graphs
from core.home.utils import *

from django.shortcuts import redirect
import csv
# Decorador personalizado para verificar si el usuario pertenece al grupo "Player"
def user_is_player(user):
    return user.groups.filter(name='Player').exists()

def user_is_psico(user):
    return user.groups.filter(name='Psicologia').exists()

class RespuestasListView(LoginRequiredMixin, ListView):
    model = Cuestionarios
    template_name = 'psicologia/respuestas_list.html'
    login_url = '/login'

    context_object_name = 'respuestas'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        elif not user_is_psico(request.user):
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        
        # Excluir las instancias con user_id = 1
        queryset = queryset.exclude(user_id=1)


        return queryset
    
class ExportCSVView(View):
    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        elif not user_is_psico(request.user):
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        # Obtener todos los registros de Cuestionarios excluyendo user_id = 1
        respuestas = Cuestionarios.objects.exclude(user_id=1)
        
        # Crear un objeto de respuesta HTTP con el contenido CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="respuestas.csv"'

        # Crear un escritor CSV y escribir los datos
        writer = csv.writer(response)

        # Obtener los nombres de todas las columnas del modelo Cuestionarios
        fields = [field.name for field in Cuestionarios._meta.fields]

        # Escribir los encabezados del CSV
        writer.writerow(fields)

        # Escribir los datos de las respuestas
        for respuesta in respuestas:
            row = [getattr(respuesta, field) for field in fields]
            writer.writerow(row)

        return response


class RespuestasPorDivisionListView(LoginRequiredMixin, ListView):
    model = Cuestionarios
    template_name = 'psicologia/respuestas_x_division_list.html'

    login_url = '/login'

    def get(self, request, division):
        plantel = Plantel.objects.get(division = division)
        fecha_actual = date.today()

        # Obtener la fecha de inicio del día actual (a las 00:00:00)
        fecha_inicio_dia_actual = datetime.combine(fecha_actual, datetime.min.time())

        # Obtener la fecha de finalización del día actual (a las 23:59:59)
        fecha_fin_dia_actual = fecha_inicio_dia_actual + timedelta(days=1) - timedelta(seconds=1)
        
        respuestas_hoy = Cuestionarios.objects.filter(
        Q(created_at__range=(fecha_inicio_dia_actual, fecha_fin_dia_actual)) &
        Q(user__userrelation__plantel=plantel)
)

        # Utiliza prefetch_related para cargar los objetos relacionados de manera eficiente
        respuestas_hoy = respuestas_hoy.prefetch_related(
            Prefetch('user__userrelation_set', queryset=UserRelation.objects.filter(plantel=plantel), to_attr='user_relations')
        )

        usuarios_en_plantel = UserRelation.objects.filter(plantel=plantel)

        # Obtén los IDs de usuarios que han respondido a cuestionarios hoy
        usuarios_con_respuestas = Cuestionarios.objects.filter(
            created_at__range=(fecha_inicio_dia_actual, fecha_fin_dia_actual),
            user_id__in=[usuario.user.id for usuario in usuarios_en_plantel]
        ).values_list('user_id', flat=True)

        # Filtra los usuarios que no han respondido a cuestionarios hoy
        usuarios_sin_responder = usuarios_en_plantel.exclude(user__id__in=usuarios_con_respuestas)


        context = {
            'respuestas': respuestas_hoy,
            'sin_respuesta': usuarios_sin_responder,
            'plantel' : plantel.division,
            'cuenta_success': respuestas_hoy.count(),
            'cuenta_pendiente': usuarios_sin_responder.count()
        }

        return render(request, self.template_name, context) 

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        elif not user_is_psico(request.user):
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class PsicologiaDivisionListView(LoginRequiredMixin, ListView):
    model = Plantel
    template_name = 'psicologia/divisiones_list.html'
    context_object_name = 'divisiones'

    login_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'

        return super().dispatch(request, *args, **kwargs)

class PsicologiaPlayersListView(LoginRequiredMixin, View):
    template_name = 'psicologia/jugadores_list.html'
    login_url = '/login'

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

class CuestionariosPorJugadorView(LoginRequiredMixin,View):
    template_name = 'psicologia/psicologia_player_detail.html'
    login_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, first_name, last_name):
        try:
            # Busca el jugador por el primer nombre
            jugador = UserRelation.objects.get(user__first_name=first_name ,user__last_name=last_name)
            id = jugador.user.id
            
            # Calcula la fecha hace 7 días atrás desde la fecha actual
            fecha_limite = datetime.now() - timedelta(days=7)
            
            # Filtra los cuestionarios relacionados con el jugador y creados en los últimos 7 días
            
            cuestionarios_query = Cuestionarios.objects.filter(user_id=id, created_at__gte=fecha_limite)
            
            cuestionarios_total = cuestionarios_query.count()
            externo = cuestionarios_query.filter(enfoque_externo=2).count()
            interno = cuestionarios_query.filter(enfoque_interno=2).count()
            hablar = cuestionarios_query.filter(enfoque_interno=1).count() + cuestionarios_query.filter(enfoque_externo=1).count()
            no_hablar = cuestionarios_query.filter(enfoque_interno = 3).count() + cuestionarios_query.filter(enfoque_externo=3).count()
            plantel = jugador.plantel.division

        except UserRelation.DoesNotExist:
            print('Entro aqui')
            jugador = None
            cuestionarios_query = None
            cuestionarios_total = 0
            externo = 0
            interno = 0
            hablar = 0
            no_hablar = 0
            plantel = ''


        context = {
            'jugador': jugador,
            'cuestionarios': cuestionarios_query,
            'cuenta' : cuestionarios_total,
            'externo': externo,
            'interno': interno,
            'hablar': hablar,
            'no_hablar' : no_hablar,
            'plantel' : plantel

        }
        len(context['cuestionarios'])
        grapher = graphs.JugadorDetailViewGraphs(context, 'cuestionarios')

        context['nivel_eustres'] = grapher.lines('created_at', 'nivel_eustres', 'Fecha', 'Nivel Eustres', 'Grafica de nivel de Eustres')
        context['nivel_distres'] = grapher.lines('created_at', 'nivel_distres', 'Fecha', 'Nivel Distres', 'Grafica de nivel de Distres')
        context['preparacion_mental'] = grapher.lines('created_at', 'preparacion_mental', 'Fecha', 'Preparacion Mental', 'Grafica de preparacion mental')
        context['humor_matutino'] = grapher.lines('created_at', 'humor_matutino', 'Fecha', 'Humor Matutino', 'Grafica de humor matutino')
        context['horas_dormidas'] = grapher.lines('created_at', 'horas_dormidas', 'Fecha', 'Horas Dormidas', 'Grafica de horas dormidas')
        

        return render(request, self.template_name, context)


class CuestionariosPorJugadorPDFView(LoginRequiredMixin,View):
    template_name = 'psicologia/psicoligia_player_detail_pdf.html'
    login_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if user_is_player(request.user):
            # Si el usuario pertenece al grupo "Player", redirígelo a la URL deseada
            return redirect('cuestionario.new')  # Redirige al usuario a la URL 'psicologia/new'

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, first_name, last_name):
        try:
            # Busca el jugador por el primer nombre
            
            jugador = UserRelation.objects.get(user__first_name=first_name ,user__last_name=last_name)
            id = jugador.user.id            
            # Calcula la fecha hace 7 días atrás desde la fecha actual
            fecha_limite = datetime.now() - timedelta(days=7)
            
            # Filtra los cuestionarios relacionados con el jugador y creados en los últimos 7 días
            cuestionarios_query = Cuestionarios.objects.filter(user_id=id, created_at__gte=fecha_limite)
            
            cuestionarios_total = cuestionarios_query.count()
            
            externo = cuestionarios_query.filter(enfoque_externo=2).count()
            
            interno = cuestionarios_query.filter(enfoque_interno=2).count()
            
            hablar = cuestionarios_query.filter(enfoque_interno=1).count() + cuestionarios_query.filter(enfoque_externo=1).count()
            
            no_hablar = cuestionarios_query.filter(enfoque_interno = 3).count() + cuestionarios_query.filter(enfoque_externo=3).count()
            
            # try:
            #     with open('static/assets/img/bg/PORTADA-PRESENTACIONES-AP-2023.png', 'rb') as file:
            #         image_bytes2 = file.read()
            # except FileNotFoundError:
            #     # Manejar la excepción si la imagen no se encuentra
            #     pass
            

        except UserRelation.DoesNotExist:
            jugador = None
            cuestionarios_query = None
            cuestionarios_total = 0
            externo = 0
            interno = 0
            hablar = 0
            no_hablar = 0

            
            
        context = {
            'jugador': jugador,
            'portada': 'NA',
            'cuestionarios': cuestionarios_query,
            'cuenta' : cuestionarios_total,
            'externo': externo,
            'interno': interno,
            'hablar': hablar,
            'no_hablar' : no_hablar

        }

        grapher = graphs.JugadorDetailViewGraphs(context, 'cuestionarios', 1)
        context['nivel_eustres'] = grapher.lines('created_at', 'nivel_eustres', 'Fecha', 'Nivel Eustres', 'Grafica de nivel de Eustres',1)
        context['nivel_distres'] = grapher.lines('created_at', 'nivel_distres', 'Fecha', 'Nivel Distres', 'Grafica de nivel de Distres',1)
        context['preparacion_mental'] = grapher.lines('created_at', 'preparacion_mental', 'Fecha', 'Preparacion Mental', 'Grafica de preparacion mental',1)
        context['humor_matutino'] = grapher.lines('created_at', 'humor_matutino', 'Fecha', 'Humor Matutino', 'Grafica de humor matutino',1)
        context['horas_dormidas'] = grapher.lines('created_at', 'horas_dormidas', 'Fecha', 'Horas Dormidas', 'Grafica de horas dormidas',1)
        
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')
        #return render(request, self.template_name, context)
