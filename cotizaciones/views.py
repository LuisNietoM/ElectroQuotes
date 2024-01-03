from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Cotizacion
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def index(request):
    query = request.POST.get('query', '')
    all_results = Cotizacion.objects.filter(
        Q(nombre_proyecto__icontains=query)
        | Q(descripcion_proyecto__icontains=query)
        | Q(tipo_construccion__icontains=query)
    )
    # Ajusta este número según tu necesidad
    paginator = Paginator(all_results, 5)
    page = request.GET.get('page')
    datos = paginator.get_page(page)

    return render(request, 'home.html', {
        'title': '🕵️ PowerSearch',
        'datos': datos,
    })


def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'sign_up.html', {
                    'title': '🆕 Registrarse',
                    'form': UserCreationForm,
                    'msj': 'El usuario ya existe en la base de datos.'
                })
        else:
            return render(request, 'sign_up.html', {
                'title': '🆕 Registrarse',
                'form': UserCreationForm,
                'msj': 'Las contraseñas no coinciden.'
            })
    else:
        return render(request, 'sign_up.html', {
            'title': '🆕 Registrarse',
            'form': UserCreationForm
        })


def log_out(request):
    logout(request)
    return redirect('sign_in')


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html', {
            'title': '🆗 Iniciar sesión',
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'sign_in.html', {
                'title': '🆗 Iniciar sesión',
                'form': AuthenticationForm,
                'msj': 'El usuario y la contraseña no coinciden'
            })
        else:
            login(request, user)
            return redirect('index')
