from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    mision = models.TextField()
    vision = models.TextField()
    anio_fundacion = models.PositiveIntegerField()
    ruc = models.CharField(max_length=13)
    imagen = models.ImageField(upload_to='empresa/', null=True, blank=True)

    def __str__(self):
        return self.nombre
