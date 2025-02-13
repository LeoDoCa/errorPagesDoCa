from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse
from .forms import productoForm

#Vista que devuelve los Productos como JSON
def lista_productos(request):
    #Obtener todos los objetos de productos de la base de datos
    productos = Producto.objects.all()
    #Vamos a guardar los datos en un dict
    #este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos 
    ]
    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html', status=200)

def agregar_producto(request):
    #checar si vengo del form
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})