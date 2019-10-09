from django.db import models

# Create your models here.

class Puesto (models.Model):
    id_puesto = models.AutoField(primary_key=True, null= False)
    nombre = models.CharField(max_length= 45)
    descripcion = models.CharField(max_length=120)
 
    def __str__(self):
        return '{}'.format(self.nombre)
