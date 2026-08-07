from django.shortcuts import render
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

