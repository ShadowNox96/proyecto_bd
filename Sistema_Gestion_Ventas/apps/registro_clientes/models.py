from django.db import models

# Create your models here.

class Cliente (models.Model):
    id_cliente = models.AutoField(primary_key=True,  null=False, default=False)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    nit = models.CharField(max_length=20)
