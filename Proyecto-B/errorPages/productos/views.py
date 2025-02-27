from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    #Esta variable me dice de donde saco el modelo y la información de base de datos
    queryset = Producto.objects.all()

    #Como serializar la información
    serializer_class = ProductoSerializer

    #Como renderizar mis respuestas
    renderer_classes = [JSONRenderer]

    #Permite filtrar que métodos HTTP se pueden usar
    #GET, POST, PUT, DELETE
    #Por defecto si no lo declaro se usan todos
    #http_method_names = ['GET', 'POST']