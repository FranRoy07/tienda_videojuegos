from django.http import HttpResponse
from django.shortcuts import render
from catalogo.models import Juego, Favorito


def _favoritos_del_usuario(request):
    if not request.user.is_authenticated:
        return set()
    return set(Favorito.objects.filter(usuario=request.user).values_list('juego_id', flat=True))

# Create your views here.

## Vista de la página principal
def index(request):
    juegos_destacados = Juego.objects.all().order_by('id')[:6]
    return render(request, 'home/index.html', {
        'juegos_destacados': juegos_destacados,
        'favoritos_ids': _favoritos_del_usuario(request),
    })

## Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

def ofertas(request):
    juegos_oferta = Juego.objects.all().order_by('precio', 'id')[:6]
    return render(request, 'home/ofertas.html', {
        'juegos_oferta': juegos_oferta,
        'favoritos_ids': _favoritos_del_usuario(request),
    })

def novedades(request):
    juegos_novedades = Juego.objects.all().order_by('-id')[:6]
    return render(request, 'home/novedades.html', {
        'juegos_novedades': juegos_novedades,
        'favoritos_ids': _favoritos_del_usuario(request),
    })


def health_check(request):
    return HttpResponse('ok')
