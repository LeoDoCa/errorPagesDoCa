from django.db import models

class Alumnos(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    matricula = models.CharField(unique=True, max_length=11)
    correo = models.CharField(unique=True, max_length=320)
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }
