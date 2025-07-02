from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from taller_mecanico.views import home_view, nosotros_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('nosotros/', nosotros_view, name='nosotros'),
    path('productos/', include('productos.urls')),
    path('trabajadores/', include('trabajadores.urls')),
    path('proveedores/', include('proveedores.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
