#Generar aqui todos los formularios HTML que vamos a ocupar
from django import forms
from .models import Alumnos

#Crear una clase para cada formulario que necesitemos
class alumnosForm(forms.ModelForm):

    class Meta:
        model = Alumnos
        #Que campos van a verse en el form
        fields = [ 'nombre', 'apellido', 'edad', 'matricula', 'correo']

        #Personalizar mis inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el nombre del alumno',
                    'required': True
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el apellido del alumno',
                    'required': True
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui la edad del alumno',
                    'required': True
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui la matricula del alumno',
                    'required': True,
                    'minlength': 10,
                    'maxlength': 11,
                    'pattern': '^I?[0-9]{5}[A-Za-z]{2}[0-9]{3}$',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el correo del alumno',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                }
            ),
        }

        #Etiquetas
        labels = {
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matrícula del alumno',
            'correo': 'Correo electrónico del alumno'
        }

        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El alumno debe tener un nombre',
            },
            'apellido': {
                'required': 'El alumno debe tener un apellido.',
            },
            'edad': {
                'required': 'El alumno debe tener una edad',
            },
            'matricula': {
                'required': 'El alumno debe tener una matricula',
            },
            'correo': {
                'required': 'El alumno debe tener un correo electrónico',
            },
        }