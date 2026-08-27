from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # ruta de catalogo, llama a la vista del diccionario de contexto lista_juegos
     path('', views.lista_juegos, name='lista_juegos'), 
     
     # para el la página de detalle de los juegos
     path('<int:pk>/', views.detalle_juego, name='detalle_juego'),
]
    
