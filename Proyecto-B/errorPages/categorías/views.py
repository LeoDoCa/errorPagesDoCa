from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm

#Vista que devuelve las categorias como JSON
def lista_categorias(request):
    #Obtener todos los objetos de categorias de la base de datos
    categorias = Categoria.objects.all()
    #Vamos a guardar los datos en un dict
    #este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias 
    ]
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, 'ver_categorias.html', status=200)

def agregar_categoria(request):
    #checar si vengo del form
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json')
    else:
        form = categoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})