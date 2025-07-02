from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'iva')
    list_filter = ('iva',)
    search_fields = ('nombre',)
