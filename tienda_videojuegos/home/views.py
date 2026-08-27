from django.shortcuts import render
from catalogo.models import Juego

# Create your views here.

## Vista de la página principal
def index(request):
    juegos_destacados = Juego.objects.all().order_by('id')[:6]
    return render(request, 'home/index.html', {'juegos_destacados': juegos_destacados})

## Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

def ofertas(request):
    juegos_oferta = Juego.objects.all().order_by('precio', 'id')[:6]
    return render(request, 'home/ofertas.html', {'juegos_oferta': juegos_oferta})

def novedades(request):
    juegos_novedades = Juego.objects.all().order_by('-id')[:6]
    return render(request, 'home/novedades.html', {'juegos_novedades': juegos_novedades})
