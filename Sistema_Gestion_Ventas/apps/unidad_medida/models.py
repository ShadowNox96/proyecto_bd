from django.db import models

# Create your models here.
class Unidad_Medida (models.Model):
    id_unidad_medida = models.AutoField(null=False,primary_key=True)
    nom_unidad = models.CharField(max_length=45)
    abreviatura = models.CharField(max_length=10)
