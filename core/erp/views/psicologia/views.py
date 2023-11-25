from django.views.generic import  CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect


from core.erp.models.psicologia.models import Cuestionarios
from core.erp.forms.psicologia.forms import CuestionariosForm



class CuestionarioCompletedView(LoginRequiredMixin, TemplateView):
    template_name = 'psicologia/formulario_completado.html'

class CuestionariosCreateView(LoginRequiredMixin, CreateView):
    model = Cuestionarios
    form_class = CuestionariosForm
    template_name = 'psicologia/psicologia_form.html'
    success_url = '/logout'
    login_url = '/login'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())