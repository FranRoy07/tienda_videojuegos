from django.db import models
from django.conf import settings

# Create your models here.

class Juego(models.Model): #Herencia de modelos para que funcione bien django internamente
    nombre = models.CharField(max_length=100) #CharField sería como el varchar en sql
    
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    
    plataforma = models.CharField(max_length=200)
    
    imagen = models.CharField(max_length=200, default="default.jpg") #Si no se carga ninguna imagen en algún juego se pone la default.jpg
    
    def __str__(self):
        return self.nombre


class Favorito(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favoritos'
    )
    juego = models.ForeignKey(
        Juego,
        on_delete=models.CASCADE,
        related_name='favoritos'
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'juego'],
                name='favorito_usuario_juego_unico'
            )
        ]
        ordering = ['-creado']

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.nombre}"
    
    
    
    
    