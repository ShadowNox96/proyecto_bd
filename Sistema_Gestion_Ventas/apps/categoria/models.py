from django.db import models

# Create your models here.
class Categoria (models.Model):
    id_categoria = models.AutoField(primary_key=True, null=False, serialize=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.nombre)