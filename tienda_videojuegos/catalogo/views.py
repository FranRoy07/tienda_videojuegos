from django.shortcuts import render

# Create your views here.

def lista_juegos(request):
    juegos = [
        {
            "nombre": "The Witcher 3: Wild Hunt",
            "precio": 39.99,
            "plataforma": "PC, PlayStation 4"
        },
        {
            "nombre": "God of War Ragnarök",
            "precio": 69.99,
            "plataforma": "PlayStation 5"
        },
        {
            "nombre": "Forza Horizon 5",
            "precio": 59.99,
            "plataforma": "Xbox Series X/S"
        },
        {
            "nombre": "Hollow Knight",
            "precio": 14.99,
            "plataforma": "Nintendo Switch, PlayStation 4, PlayStation 5, PC"
        },
        {
            "nombre": "Cyberpunk 2077",
            "precio": 49.99,
            "plataforma": "PC, PlayStation 4, PlayStation 5"
        }
    ]

    contexto_catalogo_juegos = {
        "lista_juegos": juegos
    }

    return render(request, "catalogo/lista_juegos.html", contexto_catalogo_juegos)