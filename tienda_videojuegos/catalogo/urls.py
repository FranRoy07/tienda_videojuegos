from django.urls import path
from . import views

urlpatterns = [
    # ruta de catalogo, llama a la vista del diccionario de contexto lista_juegos
     path('', views.lista_juegos, name='lista_juegos'), 
]
    
