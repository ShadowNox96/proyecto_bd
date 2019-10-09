from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields =[
            'cod_producto',
            'nom_producto',
            'descripcion',
            'costo_compra',
            'precio_venta',
            'id_categoria',
        ]

        widgets = {
            'cod_producto' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Codigo de producto'}),
            'nom_producto' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre del producto'}),
            'descripcion'  : forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Descripcion del producto', 'rows':'3'}),
            'costo_compra' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej: 125.52'}),
            'precio_venta' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 150.55'}),
            'id_categoria' : forms.Select(attrs={'class': 'form-control'}),
        }