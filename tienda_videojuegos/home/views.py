from django.shortcuts import render

# Create your views here.

## Vista de la página principal
def index(request):
            # render lo que hace es tomar el request y el archivo HTML que se quiere mostrar.
    return render(request, 'home/index.html')

## Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
