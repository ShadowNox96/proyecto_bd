from django import forms 
from apps.puesto.models import Puesto

class PuestoForm(forms.ModelForm):

    class Meta:
        model = Puesto
        
        fields = [
            'nombre',
            'descripcion',
        ]

        labels = {
            'nombre': 'Nombre Puesto',
            'descripcion': 'Descripción',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Nombre del puesto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control ', 'rows':'4', 'placeholder':'Descripcion del puesto'}),
        }


