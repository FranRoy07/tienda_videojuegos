from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_juegos, name='buscar_juegos')
]



