from django.urls import path
from taller_mecanico import views

urlpatterns = [
    path('', views.trabajadores_list_view, name='trabajadores_list'),
    path('agregar/', views.agregar_trabajador_view, name='agregar_trabajador'),
    path('editar/<int:pk>/', views.editar_trabajador_view, name='editar_trabajador'),
    path('eliminar/<int:pk>/', views.eliminar_trabajador_view, name='eliminar_trabajador'),
]
