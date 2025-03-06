from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

#router = SimpleRouter()
#router.register(r'api',ProductoViewset)

urlpatterns = [
    #path('', include(router.urls)),
    path('api/get/', lista_productos, name='lista'),
    path('ver/', ver_productos, name='ver'),
    path('agregar/', agregar_producto, name='agregar'),
    path('api/post/', registrar_producto, name='post'),
]