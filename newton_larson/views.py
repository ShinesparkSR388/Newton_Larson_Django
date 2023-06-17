from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms_ import *
from .models import user as user_, SESSION as session
from django.contrib.messages import constants as const_
from django.contrib import messages as message_
MESSAGE_LEVEL = const_.DEBUG

# Create your views here.
def larson(request):
    if(len(session.objects.get_queryset()) == 1):
        return render(request, 'newton.html')
    return redirect('/Login')
        

def login(request):
    session.objects.all().delete()
    if(request.method == 'GET' and len(request.GET) != 0 ):
        users = user_.objects.get_queryset().filter(username=(request.GET)['username'])
        item = user_.objects.get_queryset().filter(username=(request.GET)['username'], password=(request.GET)['password'])
        if (len(users) == 1):
            if(len(item) == 1):
                session.objects.create(id_user= item[0].id, username= item[0].username, superuser=item[0].superuser)
                return redirect('/Larson')
            else:
                message_.warning(request, 'El usuario nombre de usuario o contraseña incorrectos⛔')
        else:
            message_.warning(request, 'El usuario no existe⛔')
    return render(request, 'login.html', {
        'form': form_login()
    })

def signup(request):
    session.objects.all().delete()
    if(request.method == 'GET' and len(request.GET) != 0 ):
        users = user_.objects.get_queryset().filter(username=(request.GET)['username'])
        emails = user_.objects.get_queryset().filter(email=(request.GET)['email'])
        if(len(users) == 0):
            if (len(emails) == 0):
                user_.objects.create(username=(request.GET)['username'], email=(request.GET)['email'], password=(request.GET)['password'])
                message_.success(request, 'Registro completado correctamente ✅')
                return redirect('/Login')
            else:
                message_.warning(request, 'El email ingresado ya existe ⛔')
        else:
            message_.warning(request, 'El usuario ingresado ya existe ⛔')
    return render(request, 'signup.html',{
        'form': form_signup()
    })
def index(request):
    data = 'aaaaaaaaaaaaaaaaaaa'
    return render(request, 'index.html', {'data':data})