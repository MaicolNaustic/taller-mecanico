from django.contrib import admin
from .models import Trabajador

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'codigo_empleado', 'cargo', 'telefono')
    search_fields = ('nombre', 'correo', 'codigo_empleado', 'cargo', 'telefono')
