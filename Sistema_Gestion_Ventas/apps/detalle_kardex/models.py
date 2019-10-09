from django.db import models
from apps.producto.models import Producto
from apps.kardex.models import Kardex
# Create your models here.
class Detalle_Kardex(models.Model):
    id_detalle_kardex = models.AutoField(primary_key=True, null=False)
    cantidad = models.IntegerField()
    precio_unitario= models.DecimalField(max_digits=8, decimal_places=2)
    #llaves foraneas
    id_producto = models.ForeignKey(Producto, blank=False, null=False, on_delete= models.CASCADE)
    id_kardex = models.ForeignKey(Kardex, null=False, blank=False, on_delete= models.CASCADE)
    