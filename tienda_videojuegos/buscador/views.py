from django.shortcuts import render
from catalogo.models import Juego
from django.core.paginator import Paginator
from django.db.models import Q
from catalogo.models import Favorito

# Create your views here.
def buscar_juegos(request):
    query = request.GET.get('q', '') # obtener el término de búsqueda

    # Filtrar por nombre o plataforma que contenga la query
    resultados = Juego.objects.filter(
        Q(nombre__icontains=query) | Q(plataforma__icontains=query)).order_by('id')
    
    paginator = Paginator(resultados, 6) # 6 juegos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = {
        'query': query,
        'lista_juegos': page_obj,
        'favoritos_ids': set(Favorito.objects.filter(
            usuario=request.user,
            juego__in=page_obj.object_list
        ).values_list('juego_id', flat=True)) if request.user.is_authenticated else set(),
    }

    return render(request, 'resultados_busqueda.html', contexto)

