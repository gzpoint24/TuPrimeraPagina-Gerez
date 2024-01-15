from django.db import models

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_provincia

class Tipo_documento(models.Model):
    tipo_documento = models.CharField(max_length=20)
   
    def __str__(self):
        return self.tipo_documento

class Condicion_iva(models.Model):
    condicion_iva = models.CharField(max_length=100)

    def __str__(self):
        return self.condicion_iva

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=200)
    provincia_id = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.SET_NULL)
    condicion_iva_id = models.ForeignKey(Condicion_iva, null=True, blank=True, on_delete=models.SET_NULL)
    tipo_documento_id = models.ForeignKey(Tipo_documento, null=True, blank=True, on_delete=models.SET_NULL)
    nro_documento = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

