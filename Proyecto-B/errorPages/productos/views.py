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


#Función que agrega un producto con un objeto JSON

import json
def registrar_producto(request):
    #Checar si nuestra request es de tipo POST
    if request.method == 'POST':
        #Quiere decir que si estoy manejando el request
        try:
            data = json.loads(request.body) #Parametro es un texto que deberia ser un JSON
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            ) #Create directamente mete el objeto en la bd
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': producto.id
                }, status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status = 400
            )
    #Si no es POST el request    
    return JsonResponse(
        {'error':'El método no está soportado'}, status=405
    )