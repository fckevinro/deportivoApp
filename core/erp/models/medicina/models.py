from django.db import models
from django.contrib.auth.models import User



class Consulta(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    motivo_consulta = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    fecha_de_consulta = models.DateField()
    fecha_posible_alta = models.DateField()
    close_date = models.DateTimeField(null=True)
    tag = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tratamiento_administrado = models.CharField(max_length=200)
    via_de_administracion = models.CharField(max_length=100)
    plan_de_manejo = models.TextField()
    
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        db_table = 'erp_consultas_medica'
        ordering = ['-created_at', 'estado']

    def __str__(self) -> str:
        return f'{self.motivo_consulta}'

class Evolucion(models.Model):
    consulta_id = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    comentarios = models.TextField()
    

    class Meta:
        verbose_name = 'Evolucion'
        verbose_name_plural = 'Evoluciones'
        db_table = 'erp_evolucion_medica'

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='medicina/imagenes/')
    evolucion_id = models.ForeignKey(Evolucion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        db_table = 'erp_evolucion_imagenes'

class Archivos(models.Model):
    archivo = models.FileField(upload_to='medicina/archivos/')
    evolucion_id = models.ForeignKey(Evolucion, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        db_table = 'erp_evolucion_archivos'

class Hallazgos(models.Model):
    consulta_id = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    nota = models.TextField()
    
    class Meta:
        verbose_name = 'hallazgo'
        verbose_name_plural = 'Hallazgos'
        db_table = 'erp_hallazgos_medicos'

    def __str__(self) -> str:
        return self.consulta_id.motivo_consulta

class Visita(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    observaciones = models.TextField()

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        db_table = 'erp_visitas_medicas'

    def __str__(self) -> str:
        return self.consulta_id.motivo_consulta
