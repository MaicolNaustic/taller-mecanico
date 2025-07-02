from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'telefono', 'correo')
    search_fields = ('nombre', 'pais', 'correo')
