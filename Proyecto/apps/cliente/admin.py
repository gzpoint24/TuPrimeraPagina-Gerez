from django.contrib import admin

from . import models

admin.site.register(models.Provincia)
admin.site.register(models.Condicion_iva)
admin.site.register(models.Tipo_documento)
admin.site.register(models.Cliente)

