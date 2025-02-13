from django.urls import path
from .views import *

urlpatterns = [
    path('api/get', lista_categorias, name='lista'),
    path('json', ver_categorias, name='json'),
    path('registrar', agregar_categoria, name='registrar')
]