from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
