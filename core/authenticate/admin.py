from django.contrib import admin
from . import models

# Register your models here.

class PlantelAdminView(admin.ModelAdmin):
    list_display = ('id', 'division', 'gender',)

class GeneralData(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'plantel_id', 'image')

admin.site.register(models.UserRelation, GeneralData)
admin.site.register(models.Plantel, PlantelAdminView)