from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregar_y_listar_materias, name='lista_materias'),
]
