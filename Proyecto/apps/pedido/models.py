from django.db import models

from cliente.models import Cliente
from producto.models import Producto


class Pedido(models.Model):
    cliente_pedido = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    cantidad_articulos = models.IntegerField()
    articulo_pedido = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.SET_NULL)
    importe = models.DecimalField(max_digits=12, decimal_places=2) 
   
    def __str__(self) -> str:
        return f"{self.cantidad_articulos} - {self.cliente_pedido} PEDIDO: {self.articulo_pedido} $ {self.importe}"              

