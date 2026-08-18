from django.shortcuts import render, redirect

#Librerías importadas
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages

# Create your views here.
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid(): #verifica que se cumplan las condiciones para registrarse correctamente.
            usuario = form.save()
            login(request, usuario) #automáticamente inicia sesión si se pudo registrar (POST) el usuario
            return redirect('home')
    else: #el formulario cuando se apreta en registrarse tiene que estar vacío lógicamente (GET)
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

#POST = enviar datos

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid(): #Comprueba credenciales, el usuario debe coincidir con el que está registrado en bdd.
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')
        else:
            #mostrar errores generales en consola para debug
            print(form.errors)
            messages.error(request, "Usuario o contraseña incorrectos.")
    else: #GET, no se apretó en 'Ingresar'
        form = LoginForm() #mostrar el login vacío al apretar en loguearse.
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request) #lo hace internamente Django
    return redirect('login')

@login_required #Se activa si se logueó correctamente el usuario, si no se cumple Django lo envía a la página de login
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')

