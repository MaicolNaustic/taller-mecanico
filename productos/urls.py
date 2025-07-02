from django.urls import path
from .views import productos_view, agregar_producto_view, editar_producto_view, eliminar_producto_view

urlpatterns = [
    path('', productos_view, name='productos'),
    path('agregar/', agregar_producto_view, name='agregar_producto'),
    path('editar/<int:pk>/', editar_producto_view, name='editar_producto'),
    path('eliminar/<int:pk>/', eliminar_producto_view, name='eliminar_producto'),  # <-- aquí
]
