
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("producto/list/", views.producto_list, name="producto_list"),
    path("producto/create/", views.producto_create, name="producto_create"),
]
