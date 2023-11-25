from django import forms

from core.erp.models.psicologia.models import Cuestionarios
from core.erp.choices import sentimiento, NIVEL_CHOICES, talk


class CuestionariosForm(forms.ModelForm):
    

    humor_matutino = forms.ChoiceField(label= '¿Qué tipo de humor tenías al despertar?', 
                                       choices=sentimiento,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    
    calidad_descanso = forms.ChoiceField(label='¿Qué tan reparador fue tu descanso?',
                                         choices=sentimiento,
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    
    nivel_eustres = forms.ChoiceField(
        label= '¿Cuál es tu nivel de eustrés (+) en este momento?',
        choices=NIVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    nivel_distres = forms.ChoiceField(
        label= '¿Cuál es tu nivel de distres (-) en este momento?',
        choices=NIVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    preparacion_mental = forms.ChoiceField(
        label= '¿Mentalmente que tan listo te sientes para el entrenamiento?',
        choices=NIVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    enfoque_externo = forms.ChoiceField(
        label= '¿Hay alguna situación externa que no te permita estar enfocado en el entrenamiento?',
        choices=talk,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    enfoque_interno = forms.ChoiceField(
        label= '¿Hay alguna situación individual que no te permita estar enfocado en el entrenamiento?',
        choices=talk,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    comentarios_adicionales = forms.CharField(
        label='Gracias por responder el cuestionario, si hay otra situación que quieras platicar, lo puedes escribir aquí',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
        required=False,  # Establecer required en False para que no sea requerido
    )

    class Meta:
        model = Cuestionarios
        fields = ('humor_matutino', 'horas_dormidas', 'minutos_dormidos', 
                  'calidad_descanso', 'nivel_eustres','nivel_distres', 'preparacion_mental',
                  'enfoque_externo', 'enfoque_interno', 'comentarios_adicionales')
        labels = {
            'horas_dormidas'            : 'Horas',
            'minutos_dormidos'          : 'Minutos',
            'calidad_descanso'          : '¿Qué tan reparador fue tu descanso?',
            'preparacion_mental'        : '¿Mentalmente que tan listo te sientes para el entrenamiento?',
            'comentarios_adicionales'   : '¿Gracias por responder el cuestionario, si hay otra situación que quieras platicar, lo puedes escribir aquí',
        } 

        widgets = {
            'horas_dormidas'            : forms.TextInput(attrs={'class': 'form-control', 'type':'int'}),
            'minutos_dormidos'            : forms.TextInput(attrs={'class': 'form-control', 'type':'int'}),
            'calidad_descanso'          : forms.TextInput(attrs={'class': 'form-control'}),
            'comentarios_adicionales': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
        }

