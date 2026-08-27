from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from catalogo.models import Juego, Favorito
from django.core.paginator import Paginator

# Create your views here.

def lista_juegos(request):
    
    #recibe el QuerySet con todos los datos que fueron guardados por la terminal interactiva, los ordena por id
    juegos = Juego.objects.all().order_by('id')
    
    #mostrar 6 juegos por página
    paginator = Paginator(juegos, 6)
    
    #obtener el número de página desde la URL (?page=2)
    page_number = request.GET.get('page')
    
    #obtener los juegos de esa página
    page_obj = paginator.get_page(page_number)
    
    #pasar a la plantilla como 'lista_juegos'
    
    

    favoritos_ids = set()
    if request.user.is_authenticated:
        favoritos_ids = set(Favorito.objects.filter(
            usuario=request.user,
            juego__in=page_obj.object_list
        ).values_list('juego_id', flat=True))

    contexto_catalogo_juegos = {
        'lista_juegos': page_obj,
        'favoritos_ids': favoritos_ids,
    }

    return render(request, "catalogo/lista_juegos.html", contexto_catalogo_juegos)

def detalle_juego(request, pk):
    
    #obtener el juego concreto o mostrar un 404
    juego = get_object_or_404(Juego, pk=pk)
    
    #crear el contexto que se le pasará a la plantilla
    contexto = {
        'juego': juego,
        'es_favorito': request.user.is_authenticated and Favorito.objects.filter(
            usuario=request.user, juego=juego
        ).exists(),
    }
    
    #renderizar la plantilla de detalle
    return render(request, 'catalogo/detalle_juego.html', contexto)


@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('juego')
    return render(request, 'catalogo/favoritos.html', {'favoritos': favoritos})


@login_required
def alternar_favorito(request, pk):
    juego = get_object_or_404(Juego, pk=pk)

    if request.method != 'POST':
        messages.info(request, 'Usá el botón del corazón para modificar tus favoritos.')
        return redirect('catalogo:detalle_juego', pk=juego.pk)

    favorito, creado = Favorito.objects.get_or_create(usuario=request.user, juego=juego)

    if creado:
        messages.success(request, f"'{juego.nombre}' se agregó a tus favoritos.")
    else:
        favorito.delete()
        messages.info(request, f"'{juego.nombre}' se quitó de tus favoritos.")

    destino = request.POST.get('next')
    if destino and destino.startswith('/') and not destino.startswith('//'):
        return redirect(destino)
    return redirect('catalogo:detalle_juego', pk=juego.pk)
    
    
    