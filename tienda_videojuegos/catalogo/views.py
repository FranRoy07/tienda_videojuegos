from django.shortcuts import render, get_object_or_404
from catalogo.models import Juego
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
    
    

    contexto_catalogo_juegos = {"lista_juegos": page_obj}

    return render(request, "catalogo/lista_juegos.html", contexto_catalogo_juegos)

def detalle_juego(request, pk):
    
    #obtener el juego concreto o mostrar un 404
    juego = get_object_or_404(Juego, pk=pk)
    
    #crear el contexto que se le pasará a la plantilla
    contexto = {'juego': juego}
    
    #renderizar la plantilla de detalle
    return render(request, 'catalogo/detalle_juego.html', contexto)
    
    
    