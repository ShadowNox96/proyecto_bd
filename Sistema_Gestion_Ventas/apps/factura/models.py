from django.db import models
# importo la clases para las relaciones
from apps.registro_clientes.models import Cliente
from apps.usuario.models import Usuario
# Create your models here.
class Factura (models.Model):
    id_factura = models.AutoField(primary_key=True, null=False)
    fecha = models.DateField()
    # estado de la factura si es 1 esta activa, si es 0 es que la factura fue devuelta y esa tabla se anula y no se toma en cuenta a la hora de verificar el stock
    estado = models.BooleanField(default=True)
    #llave foranea de cliente facturas
    id_cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    # llave foranea de user facturas
    id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)