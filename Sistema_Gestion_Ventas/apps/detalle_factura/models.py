from django.db import models
# importo las clases con las cuales voy a hacer relacion 
from apps.factura.models import Factura
from apps.producto.models import Producto
# Create your models here.
class Detalle_Factura (models.Model):
    id_detalle_factura = models.AutoField(primary_key=True, null=False)
    id_factura = models.ForeignKey(Factura, null=False, blank=False, on_delete= models.CASCADE)
    id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    