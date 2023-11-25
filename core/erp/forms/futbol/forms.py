from django import forms

from core.erp.models.medicina.models import Consulta
from django.contrib.auth.models import User, Group
from core.erp.models.futbol.models import InformeDeJugador, InformeDePartido
from core.erp.choices import jornadas, equipos

class InformeJugadorForm(forms.ModelForm):
    user = forms.CharField(
        label='Jugador',
        
    )
    class Meta:
        model = InformeDeJugador
        fields = (
            'user',
            'jornada',
            'rival',
            'fecha_calendario',
            'notas_partido'
        )

        

        widgets = {
            'user': forms.Select(

                attrs={
                    'class': 'form-select custom-class',
                    'id': 'organizerSingle',
                    'data-choices': 'data-choices',
                    'data-options': "{'removeItemButton': true, 'placeholder': true}",
                    'data-custom-attribute': 'custom-value'
                }
            ),
            'jornada': forms.Select(
                choices= jornadas,
                attrs={
                    'class': 'form-control',
                }
            ),
            'rival': forms.Select(
                choices= equipos,
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha_calendario': forms.DateInput(attrs={
                "class": "form-control datetimepicker",
                "id": "datepickerVal",
                "type": "text",
                "placeholder": "d/m/y",
                "data-options": "{'disableMobile': true, 'allowInput': true}"
            }),
            'notas_partido': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-area', 
            })
        
        }

    def __init__(self, *args, **kwargs):
        super(InformeJugadorForm, self).__init__(*args, **kwargs)
        # Configura required=False para equipo_casa
        self.fields['notas_partido'].required = False

class InformePartidoForm(forms.ModelForm):
    

    class Meta:
        # Pasar a un archivo de choices
        

        model = InformeDePartido
        fields = (
            'equipo_casa', 
            'equipo_visita', 
            'jornada', 
            'fecha_calendario', 
            'generalidades', 
            'fase_ofensiva', 
            'fase_defensiva', 
            'abp',
            'notas_partido',
        )

        widgets = {
            'equipo_casa': forms.Select(
                choices=equipos,
                attrs={
                'class': 'form-control',
                }
            ),
            'equipo_visita': forms.Select(
                choices=equipos,
                attrs={
                'class': 'form-control',
                }
            ),
            'jornada': forms.Select(
                choices=jornadas,
                attrs={
                'class': 'form-control'
                }
            ),
            'fecha_calendario': forms.DateInput(attrs={
                "class": "form-control datetimepicker",
                "id": "datepickerVal",
                "type": "text",
                "placeholder": "d/m/y",
                "data-options": "{'disableMobile': true, 'allowInput': true}"
            }),
            'generalidades': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-generalidades', 
            }),
            'fase_ofensiva': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-ofensive', 
            }),
            'fase_defensiva': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-defensive', 
            }),
            'abp': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-abp', 
            }),
            'notas_partido': forms.Textarea(attrs={
                'class':"form-control",
                'id':'text-area', 
            })
        
        }

    def __init__(self, *args, **kwargs):
        super(InformePartidoForm, self).__init__(*args, **kwargs)
        # Configura required=False para equipo_casa
        self.fields['notas_partido'].required = False
        self.fields['generalidades'].required = False
        self.fields['fase_ofensiva'].required = False
        self.fields['fase_defensiva'].required = False
        self.fields['abp'].required = False

        