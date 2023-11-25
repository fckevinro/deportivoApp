from django.db import models
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint
from django.db.models import Q
from django.core.exceptions import ValidationError

class Cuestionarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    print(created_at)

    humor_matutino = models.CharField(max_length=50)
    horas_dormidas = models.IntegerField()
    minutos_dormidos = models.IntegerField()
    calidad_descanso = models.CharField(max_length=55)
    nivel_eustres = models.IntegerField()
    nivel_distres = models.IntegerField()
    preparacion_mental = models.IntegerField()
    enfoque_externo = models.CharField(max_length=2)
    enfoque_interno = models.CharField(max_length=2)
    comentarios_adicionales = models.TextField()

    class Meta:
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'
        db_table = 'erp_quiz_psicologia'


