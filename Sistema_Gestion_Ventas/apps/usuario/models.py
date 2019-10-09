from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.empleado.models import Empleado
# Create your models here.
class Usuario (AbstractUser):
    id_empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
