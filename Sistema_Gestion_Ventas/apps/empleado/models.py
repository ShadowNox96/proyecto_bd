from django.db import models

# importo las clases para agregar las relaciones 
from apps.puesto.models import Puesto
# Create your models here.
class Empleado (models.Model):
    id_empleado = models.AutoField(primary_key=True,null=False)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    dpi = models.CharField(max_length=15)
    id_puesto = models.ForeignKey(Puesto, null=False, blank=False, on_delete=models.CASCADE)
