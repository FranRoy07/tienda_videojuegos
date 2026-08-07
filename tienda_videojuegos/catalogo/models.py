from django.db import models

# Create your models here.

class Juego(models.Model): #Herencia de modelos para que funcione bien django internamente
    nombre = models.CharField(max_length=100) #CharField sería como el varchar en sql
    
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    
    plataforma = models.CharField(max_length=200)
    
    imagen = models.CharField(max_length=200, default="default.jpg") #Si no se carga ninguna imagen en algún juego se pone la default.jpg
    
    def __str__(self):
        return self.nombre
    
    
    
    
    