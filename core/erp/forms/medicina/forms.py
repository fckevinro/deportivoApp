from django import forms

from core.erp.models.medicina.models import Consulta
from core.erp.choices import sentimiento, NIVEL_CHOICES, talk


from django.contrib.auth.models import User, Group
from core.authenticate.models import UserRelation

class ConsultaForm(forms.ModelForm):

    motivo_consulta = forms.CharField(label='Motivo de la consulta', widget=forms.TextInput(attrs={
        "class":"form-control", "id":"basic-form-name", 'type':"text", "placeholder":"Motivo de la consulta"
    }))


    fecha_de_consulta = forms.DateField(
        label="Fecha de consulta",
        widget=forms.DateInput(attrs={
            "class": "form-control datetimepicker",
            "id": "datepickerVal",
            "type": "text",
            "placeholder": "d/m/y",
            "data-options": "{'disableMobile': true, 'allowInput': true}"
        })
    )
    fecha_posible_alta = forms.DateField(
        label="Fecha de posible alta",
        widget=forms.DateInput(attrs={
            "class": "form-control datetimepicker",
            "id": "datepickerVal",
            "type": "text",
            "placeholder": "d/m/y",
            "data-options": "{'disableMobile': true, 'allowInput': true}"
        })
    )

    tag = forms.ChoiceField(choices=(
        ('',''),
        ("Lesión", "Lesión"),
        ("Enfermedad", "Enfermedad"),
        ("Otro", "Otro"),
    ), label=('Tag:'), widget=forms.Select(attrs={
        'class':"form-select", 'id':"organizerSingle", 'data-choices':"data-choices", 'data-options':"{'removeItemButton':true,'placeholder':true}"
    }))

    estado = forms.ChoiceField(choices=(
        ('Activo', 'Activo'),
        ("Cerrado", "Cerrado"),
    ), label='Estado',widget=forms.Select(attrs={
        'class':"form-select", 'id':"organizerSingle", 'data-choices':"data-choices", 'data-options':"{'removeItemButton':true,'placeholder':true}"
    }))


    tratamiento_administrado = forms.ChoiceField(choices=(
        ('', ''),
        ('Disponible', 'Listado de Medicamentos'),
        ("Readaptación", "Readaptación"),
        ("Rehabilitación", "Rehabilitación"),
        ("No disponible", "No disponible")
    ), label='Tratamiento administrado',widget=forms.Select(attrs={
        'class':"form-select", 'id':"organizerSingle", 'data-choices':"data-choices", 'data-options':"{'removeItemButton':true,'placeholder':true}"
    }))

    via_de_administracion = forms.ChoiceField(choices=(
        ('',''),
        ('Oral', 'Oral'),
        ("Topica", "Topica"),
        ("Intra-Muscular", "Intra-Muscular"),
        ("Sub-Lingual", "Sub-Lingual"),
        ("Endovenosa/Intravenosa", "Endovenosa/Intravenosa")
    ), label='Via de administrado',widget=forms.Select(attrs={
        'class':"form-select", 'id':"organizerSingle", 'data-choices':"data-choices", 'data-options':"{'removeItemButton':true,'placeholder':true}"
    }))

    plan_de_manejo = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "id": "exampleTextarea",
            "rows":"9"
        })
    )


    class Meta:
        model = Consulta
        fields = ( 'motivo_consulta', 'user','fecha_de_consulta','fecha_posible_alta', 'tag', 'estado', 'tratamiento_administrado', 'via_de_administracion','plan_de_manejo')

        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-select custom-class',
                'id': 'organizerSingle',
                'data-choices': 'data-choices',
                'data-options': "{'removeItemButton': true, 'placeholder': true}",
                'data-custom-attribute': 'custom-value'
            })
        }
        

        