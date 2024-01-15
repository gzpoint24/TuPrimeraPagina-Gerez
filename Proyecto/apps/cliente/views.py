from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "cliente/index.html")

def cliente_list(request):
    consulta = models.Cliente.objects.all()
    contexto = {"listado_clientes": consulta}
    return render(request, "cliente/cliente_list.html", contexto) 


def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    
    else: 
        form = forms.ClienteForm()
    return render(request, "cliente/cliente_create.html", {"form": form})

