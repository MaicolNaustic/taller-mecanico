from django.urls import path
from .views import proveedores_view, agregar_proveedor_view, editar_proveedor_view, eliminar_proveedor_view

urlpatterns = [
    path('', proveedores_view, name='proveedores'),
    path('agregar/', agregar_proveedor_view, name='agregar_proveedor'),
    path('editar/<int:pk>/', editar_proveedor_view, name='editar_proveedor'),
    path('eliminar/<int:pk>/', eliminar_proveedor_view, name='eliminar_proveedor'),
]
