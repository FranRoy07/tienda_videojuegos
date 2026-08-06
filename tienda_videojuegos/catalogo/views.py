from django.shortcuts import render
from catalogo.models import Juego

# Create your views here.

def lista_juegos(request):
    juegos = Juego.objects.all() #recibe el QuerySet con todos los datos que fueron guardados por la terminal interactiva

    contexto_catalogo_juegos = { "lista_juegos": juegos }

    return render(request, "catalogo/lista_juegos.html", contexto_catalogo_juegos)