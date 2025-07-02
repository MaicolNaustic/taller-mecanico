from django.shortcuts import render, redirect, get_object_or_404
from empresa.models import Empresa
from trabajadores.models import Trabajador
from productos.models import Producto

from django import forms

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'correo', 'codigo_empleado', 'cargo', 'telefono', 'imagen']

def trabajadores_list_view(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajadores.html', {'trabajadores': trabajadores})

def agregar_trabajador_view(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trabajadores_list')
    else:
        form = TrabajadorForm()
    return render(request, 'agregar_trabajador.html', {'form': form})

def editar_trabajador_view(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, request.FILES, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajadores_list')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'editar_trabajador.html', {'form': form})

def eliminar_trabajador_view(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajadores_list')
    return render(request, 'eliminar_trabajador.html', {'trabajador': trabajador})

def home_view(request):
    return render(request, 'home.html')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'iva', 'imagen']

def productos_view(request):
    mostrar_formulario = request.GET.get('mostrar_formulario') == '1'
    productos = Producto.objects.all()
    form = ProductoForm()
    producto_a_editar = None

    if request.method == 'POST':
        # Agregar producto
        if 'agregar' in request.POST:
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('productos')

        # Editar producto (mostrar datos en formulario)
        elif 'editar_id' in request.POST:
            producto_a_editar = get_object_or_404(Producto, pk=request.POST.get('editar_id'))
            form = ProductoForm(instance=producto_a_editar)

        # Confirmar edición
        elif 'editar' in request.POST:
            producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('productos')

        # Eliminar producto
        elif 'eliminar_id' in request.POST:
            producto = get_object_or_404(Producto, pk=request.POST.get('eliminar_id'))
            producto.delete()
            return redirect('productos')

    context = {
        'productos': productos,
        'form': form,
        'producto_a_editar': producto_a_editar,
        'mostrar_formulario': mostrar_formulario,
    }
    return render(request, 'productos.html', context)


def agregar_producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def nosotros_view(request):
    empresa = Empresa.objects.first()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ruc = request.POST.get('ruc')
        direccion = request.POST.get('direccion')
        mision = request.POST.get('mision')
        vision = request.POST.get('vision')
        anio_fundacion = request.POST.get('anio_fundacion')

        if empresa:
            empresa.nombre = nombre
            empresa.ruc = ruc
            empresa.direccion = direccion
            empresa.mision = mision
            empresa.vision = vision
            empresa.anio_fundacion = anio_fundacion
            empresa.save()
        else:
            Empresa.objects.create(
                nombre=nombre,
                ruc=ruc,
                direccion=direccion,
                mision=mision,
                vision=vision,
                anio_fundacion=anio_fundacion
            )
        return redirect('nosotros')

    return render(request, 'nosotros.html', {'empresa': empresa})
