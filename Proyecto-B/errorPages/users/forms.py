import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

#Primer formulario
class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'pattern':'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura, con al menos 8 caracteres, una mayúscula, un número y un símbolo (!, #, $, %, & o ?)',
                'required': True
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmación de contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'pattern':'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Ingrese de nuevo su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'required': True
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        #Si quiero editar la forma de los inputs necesito widgets
        widgets = {
            #Cada uno de los widgets del **MODEL**
            'email': forms.EmailInput(
                #Características del elemento visual
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo electrónico válido de la UTEZ',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required': True,
                    'minlength': 3,
                    'maxlength': 100,
                    'title': 'Debes ingresar un nombre real',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required': True,
                    'minlength': 3,
                    'maxlength': 100,
                    'title': 'Debes ingresar un apellido real',
                    'placeholder': 'Ingrese su apellido',
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required': True,
                    'minlength': 10,
                    'maxlength': 11,
                    'pattern': '^I?[0-9]{5}[A-Za-z]{2}[0-9]{3}$',
                    'title': 'Debes ingresar una matricula válida',
                    'placeholder': 'Ingrese su matrícula',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'required': True,
                    'min': '1',
                    'max': '150',
                    'pattern': '^[0-9]{3}$',
                    'title': 'Debes ingresar una edad válida',
                    'placeholder': 'Ingrese su edad',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required': True,
                    'minlength': 10,
                    'maxlength': 10,
                    'pattern': '^[0-9]{10}$',
                    'title': 'Debes ingresar un número de teléfono de 10 dígitos',
                    'placeholder': 'Ingrese su número de teléfono',
                }
            ),
      
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match('^[a-zA-Z0-9\\.)]+@utez\\.edu\\.mx$', email):
            raise forms.ValidationError("El correo debe ser del dominio @utez.edu.mx")
        return email
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3 or len(name) > 100:
            raise forms.ValidationError("El nombre debe tener entre 3 y 100 caracteres")
        return name
    
    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if len(surname) < 3 or len(surname) > 100:
            raise forms.ValidationError("El apellido debe tener entre 3 y 100 caracteres")
        return surname
    
    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not len(tel) == 10:
            raise forms.ValidationError("El número de teléfono debe tener 10 dígitos")
        return tel
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not re.match('^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$', password):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, incluir un número y un símbolo (!, #, $, %, & o ?)")
        return password

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match('^I?[0-9]{5}[A-Za-z]{2}[0-9]{3}$', control_number):
            raise forms.ValidationError("La matrícula debe tener 10 u 11 caracteres y seguir el formato de la UTEZ")
        return control_number
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
        

#Segundo formulario (inicio de sesión)
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[a-zA-Z0-9\\.)]+@utez\\.edu\\.mx$',
                'title': 'Escriba el correo electrónico de su usuario',
                'placeholder': 'Ingrese su correo electrónico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'pattern':'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Escriba la contraseña de su usuario',
                'required': True
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data