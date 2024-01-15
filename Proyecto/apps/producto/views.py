from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "producto/index.html")

def producto_list(request):
    consulta = models.Producto.objects.all()
    contexto = {"listado_produ": consulta}
    return render(request, "producto/producto_list.html", contexto) 


def producto_create(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:producto_list")
    
    else: 
        form = forms.ProductoForm()
    return render(request, "producto/producto_create.html", {"form": form})


