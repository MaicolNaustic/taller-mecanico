from django.shortcuts import render
from .models import Empresa

def nosotros_view(request):
    empresa = Empresa.objects.first()
    return render(request, 'nosotros.html', {'empresa': empresa})
