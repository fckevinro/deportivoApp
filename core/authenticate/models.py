from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plantel(models.Model):
    division = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/media/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Plantel'
        verbose_name_plural = 'Planteles'

class UserRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    plantel = models.ForeignKey(Plantel, on_delete=models.PROTECT)
    estado_medico = models.CharField(max_length=100, default='Disponible')
    image = models.ImageField(upload_to='static/media/', blank=True, null=True)


def get_first_name(self):
    return f'{self.first_name} {self.last_name}'

User.add_to_class("__str__", get_first_name)