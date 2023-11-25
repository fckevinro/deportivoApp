import django_filters
from core.erp.models.psicologia.models import Cuestionarios

class CuestionariosFilter(django_filters.FilterSet):
    fecha_min = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Fecha mínima')
    fecha_max = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Fecha máxima')

    class Meta:
        model = Cuestionarios
        fields = []
