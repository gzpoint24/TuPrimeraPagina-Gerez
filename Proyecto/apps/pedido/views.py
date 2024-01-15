from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "pedido/index.html")

def pedido_list(request):
    consulta = models.Pedido.objects.all()
    contexto = {"listado_pedidos": consulta}
    return render(request, "pedido/pedido_list.html", contexto) 


def pedido_create(request):
    if request.method == "POST":
        form = forms.PedidoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido:pedido_list")
    
    else: 
        form = forms.PedidoForms()
    return render(request, "pedido/pedido_create.html", {"form": form})
