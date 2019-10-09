from django.db import models
from apps.registro_proveedores.models import Proveedor
# Create your models here.
class Kardex (models.Model):
    id_kardex = models.AutoField(primary_key=True, null=False)
    fecha_factura = models.DateField()
    num_factura = models.IntegerField()
    serie_factura = models.CharField(max_length=20)
    #Tipo opeacion booleana donde 1 es entrada y cero es salida del inventario
    tipo_operacion = models.BooleanField()
    id_proveedor = models.ForeignKey(Proveedor, blank=False, null=False, on_delete= models.CASCADE)
