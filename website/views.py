from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Registro


# Create your views here.
def home(request):
    registros = Registro.objects.all()
    #Checar pra ver o login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'home.html', {})

    else:
     return render(request, 'home.html', {'registros': registros})


def base(request):
    return render(request, 'base.html', {})

def login_user(request):
    
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('home')
        else:
            form = SignUpForm()
            messages.error(request, "Erro ao registrar usuário. Verifique os dados e tente novamente.")
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def registro_cliente(request, pk):
    if request.user.is_authenticated:
        registro_cliente = Registro.objects.get(id=pk)
        return render(request, 'registro.html', {'registro': registro_cliente})
    else:
        messages.error(request, "Você precisa estar logado para acessar este registro.")
        return redirect('login')