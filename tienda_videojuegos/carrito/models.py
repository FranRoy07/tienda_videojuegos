from django.db import models
from django.conf import settings
from catalogo.models import Juego

# Create your models here.
class Carrito(models.Model):
    
    # Carrito asociado a un usuario
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carrito'
    )
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Carrito de compra {self.usuario.username}"
    
    def total_items(self):
        # Cantidad total de juegos en el carrito
        return sum(item.cantidad for item in self.items.all())
    
    def total_precio(self):
        # Precio total del carrito
        return sum(item.subtotal() for item in self.items.all())


class ItemCarrito(models.Model):
    # Elemento individual del carrito (un juego y su cantidad)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('carrito', 'juego')
        
    def __str__(self):
        return f"{self.juego.nombre} x {self.cantidad}"
        
    def subtotal(self):
        # Subtotal del item (precio * cantidad)
        return self.juego.precio * self.cantidad
    
    
    