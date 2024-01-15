
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pedido/list/", views.pedido_list, name="pedido_list"),
    path("pedido/create/", views.pedido_create, name="pedido_create"),
]
