from django import forms 
from apps.empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        
        fields = [
            'nombres',
            'apellidos',
            'dpi',
            'id_puesto',
        ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'dpi': 'No. DPI',
            'id_puesto':'Puesto',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Nombres de la persona'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Apellidos de la persona'}),
            'dpi': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'DPI'}),
            'id_puesto' : forms.Select(attrs={'class':'form-control'}),
        }


