from django import forms 
from apps.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        
        fields = [
            'nombre',
            'descripcion',
        ]

        labels = {
            'nombre': 'Nombre Categoria',
            'descripcion': 'Descripción',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Nombre categoria'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control ', 'rows':'4', 'placeholder':'Descripcion '}),
        }


