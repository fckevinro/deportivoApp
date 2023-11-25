from django.db import models
from django.contrib.auth.models import User

class InformeDeJugador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_calendario = models.DateField()
    rival = models.CharField(max_length=100)
    jornada = models.CharField(max_length=100)
    notas_partido = models.TextField()

    class Meta:
        verbose_name = 'Informe Individual'
        verbose_name_plural = 'Informes Individuales'
        db_table = 'erp_informes_individuales'

class InformeDePartido(models.Model):
    equipo_casa = models.CharField(max_length=200)
    equipo_visita = models.CharField(max_length=200)
    fecha_calendario = models.DateField()
    jornada = models.CharField(max_length=100, null=True)
    generalidades = models.TextField(null=True)
    fase_ofensiva = models.TextField(null=True)
    fase_defensiva = models.TextField(null=True)
    abp = models.TextField(null=True)
    notas_partido = models.TextField(null=True)

    class Meta:
        verbose_name = 'Informe de partido'
        verbose_name_plural = 'Informe de partidos'
        db_table = 'erp_informes_de_partidos'
    