from .models import Carrito
from catalogo.models import Favorito

def carrito_total(request):
    total_items = 0
    total_favoritos = 0
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            total_items = carrito.total_items()
        total_favoritos = Favorito.objects.filter(usuario=request.user).count()
    return {
        'carrito_total_items': total_items,
        'favoritos_total': total_favoritos,
    }

