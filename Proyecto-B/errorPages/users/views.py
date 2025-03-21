from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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
    

class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        fields = {}

        for field in form.fields:
            fields[field] = {
                'label': form[field].label,
                'input': form[field].field.widget.attrs,
                'type': form[field].field.widget.input_type,
            }

        return Response(fields)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.data)

        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password1'],
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )

            return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)