from django.db import models

# Create your models here.


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    salario = models.DecimalField(max_digits=8,decimal_places=2)
    create_Ac = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
