from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RegistroForm
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
        return redirect('home')

def deletar_registro(request, pk):
    if request.user.is_authenticated:
        registro = Registro.objects.get(id=pk)
        registro.delete()
        messages.success(request, "Registro excluído com sucesso!")
        return redirect('home')
    else:
        messages.error(request, "Você precisa estar logado para excluir este registro.")
        return redirect('home')

def registrar_cliente(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro ao registrar cliente. Verifique os dados e tente novamente.")
            return render(request, 'registrar_cliente.html', {'form': form})
    return render(request, 'registrar_cliente.html', {'form': form})

def atualizar_registro(request, pk):
    
    if request.user.is_authenticated:
        registro_atual = Registro.objects.get(id=pk)
        form = RegistroForm(request.POST or None, instance=registro_atual)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Registro atualizado com sucesso!")
                return redirect('home')
            else:
                messages.error(request, "Erro ao atualizar registro. Verifique os dados e tente novamente.")
                return render(request, 'atualizar_registro.html', {'form': form})
        return render(request, 'atualizar_registro.html', {
    'form': form,
    'registro': registro_atual
})
    else:
        messages.error(request, "Você precisa estar logado para atualizar este registro.")
        return redirect('home')
    
