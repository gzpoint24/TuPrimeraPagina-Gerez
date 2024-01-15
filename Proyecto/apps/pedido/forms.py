from django import forms

from . import models

class PedidoForms(forms.ModelForm):
    class Meta:
        model = models.Pedido
        fields = "__all__"