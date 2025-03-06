from django.db import models
from categorías.models import Categoria


class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=200)

#clase de productos
class Producto(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.URLField()

    #Primer parametro es el modelo a relacionar, y despues la estrategia de borrado
    detalles_producto = models.OneToOneField(DetallesProducto, null= True, blank= True, on_delete=models.CASCADE)
    proveedor = models.ManyToManyField(Proveedor)
    categoria = models.ForeignKey(Categoria, null= True, blank= True, on_delete=models.CASCADE)
    #Cuando se requiera usar una relación se usa un campo:
    #OneToOneField (1:1)
    #ForeignKey (1:M)
    #ManyToManyField (M:M)
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
    

