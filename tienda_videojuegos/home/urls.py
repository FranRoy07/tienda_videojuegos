from django.urls import path
from . import views

urlpatterns = [
    # ruta principal, llama a la vista index
    path('', views.index, name='home'), 
    
    # ruta contacto, llama a la vista contacto. 
    path('contacto/', views.contacto, name='contacto'), 
    
]

