from django.db import models

class Producto(models.Model):
    numero_articulo = models.IntegerField(unique=True)
    nombre_producto = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
   
    def __str__(self) -> str:
        return f"{self.numero_articulo} - {self.nombre_producto} -> $ {self.precio}"
    

     

