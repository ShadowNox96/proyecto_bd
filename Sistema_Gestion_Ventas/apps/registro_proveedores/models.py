from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveerdor = models.AutoField(primary_key=True,  null=False)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
