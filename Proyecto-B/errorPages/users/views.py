from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication

#Hacer las vistas del API_REST de usuarios 
class UserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    #Si quieres agregar la parte de seguridad pon estas 2 variables
    authentication_classes = [JWTAuthentication] #Si es un token
    permission_classes = [IsAuthenticated]  #Si tengo la sesión activa

    #Que métodos va a proteger
    def get_permissions(self):
        if self.request.method in ['POST','PUT','DELETE']:
            return [IsAuthenticated()]
        return []

from rest_framework_simplejwt.views import TokenObtainPairView
#Hacer una vista que me devuelva mi token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    