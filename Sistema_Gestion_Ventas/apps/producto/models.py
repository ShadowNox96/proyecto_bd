from django.db import models

#importo los modelos que necesitare para las llaves foraneas
from apps.categoria.models import Categoria
# Create your models here.
class Producto (models.Model):
    id_producto = models.AutoField(primary_key=True,  null=False, serialize=True)
    cod_producto = models.CharField(max_length=45)
    nom_producto = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    costo_compra = models.DecimalField(max_digits=12, decimal_places=2)
    # llave foranea de categoria productos
    id_categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)