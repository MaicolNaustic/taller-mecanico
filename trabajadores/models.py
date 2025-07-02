from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    codigo_empleado = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100)  # <-- debe estar aquí
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='trabajadores/', null=True, blank=True)
