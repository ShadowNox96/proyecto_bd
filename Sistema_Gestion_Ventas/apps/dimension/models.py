from django.db import models
from apps.producto.models import Producto
from apps.unidad_medida.models import Unidad_Medida
# Create your models here.
class Dimension(models.Model):
    id_dimension = models.AutoField(primary_key=True, null=False)
    nombre_dimension = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    #Relaciones
    id_unidad_medida = models.ForeignKey(Unidad_Medida, null=False, blank=False, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    