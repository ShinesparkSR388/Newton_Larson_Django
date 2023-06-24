from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms_ import *
from .models import user as user_, SESSION as session_, problem
from django.contrib.messages import constants as const_
from django.contrib import messages as message_
from .newton_solver import newton_rapson as nwt
import numpy as np
from io import BytesIO
import base64
MESSAGE_LEVEL = const_.DEBUG

# Create your views here.
#All solved problem views
def problem_solved(request, problem, x, error):
    if(len(session_.objects.get_queryset()) == 0):
        return redirect('/Login')
    #estructura de la pagina de la solucion empieza aqui
    problem_ = nwt(problem, float(x), float(error))
    problem_.__del__()
    if(len(problem_.return_data()) == 0):
        problem_.iterate()
    #Retorno de solucion
    answer = problem_.return_data()
    err_ = answer[len(answer)-1][3]
    err_ = round(err_, 9)
    if(err_ < 0):
        err_ *= -1
    #empieza a imprimir graficas
    img_error = problem_.generate_graphic_error()
    img_function = problem_.generate_graphic_function()
    #termina aqui
    f_raiz = answer[len(answer)-1][1]
    if(f_raiz != 0):
        f_raiz = '{:f}'.format(answer[len(answer)-1][1])
    if(err_ != 0):
        err_ = '{:f}'.format(err_)
    
    return render(request, 'solution/solution.html', {
        'problem': problem,
        'x': x,
        'error': error,
        'raiz': f_raiz,
        'iteration': len(answer),
        'final_error': err_,
        'img_error': img_error,
        'img_function': img_function,
        'data_table': answer,
    })
    #termina render final

#
def larson(request):
    #session_
    message__ = False
    session__ = True
    if(len(session_.objects.get_queryset()) == 0):
        session__ = False
            
    if(request.GET != {}):
        #evaluar si el problema es soluble
        try:
            val_problem = request.GET['problem']
            val_x = request.GET['x']
            val_error = request.GET['error']
            
            problem_ = nwt(val_problem, float(val_x), float(val_error))
            problem_.__del__()
            have_solution = True
            if(len(problem_.return_data()) == 0):
                have_solution = problem_.iterate()
            if(have_solution == False):
                message_.warning(request, 'Parece que el problema no tiene solucion⛔')
                return redirect('/Larson')
            answer = problem_.return_data()
            err_ = answer[len(answer)-1][3]
            err_ = round(err_, 9)
            if(err_ < 0):
                err_ *= -1
            percent = str(err_)
            if(err_ != 0):
                percent = str('{:f}'.format(err_))
            if(err_ > float(val_error)):
                message_.warning(request, 'Parece que el problema no tiene solucion⛔')
                return redirect('/Larson')
            
            message_.warning(request, 'El valor de la raiz aproximada obtenida de la funcion ingresada es: ' + str(answer[len(answer)-1][1]))
            message_.warning(request, 'con numero de iteracion: ' + str(len(answer)))
            message_.warning(request, 'Y el porcentaje final de error es: ' + percent + '%')
            
            message__ = True
            problem_.__del__()
            return render(request, 'newton.html',{
                'form_problem': form_problem(),
                'session_': session__,
                'message': message__,
                'problem': val_problem,
                'x':    val_x,
                'error': val_error,
            })
        except Exception as e:
            message_.warning(request, 'Por favor verifique los datos ingresados ya que el problema no tiene solución⛔')
            print(e)
        return redirect('/Larson')
        
    #if(len(session_.objects.get_queryset()) == 1):
    return render(request, 'newton.html',{
        'form_problem': form_problem(),
        'session_': session__,
        'message': message__,
    })
    #return redirect('/Login')
        

def login(request):
    session_.objects.all().delete()
    if(request.method == 'GET' and len(request.GET) != 0 ):
        users = user_.objects.get_queryset().filter(username=(request.GET)['username'])
        item = user_.objects.get_queryset().filter(username=(request.GET)['username'], password=(request.GET)['password'])
        if (len(users) == 1):
            if(len(item) == 1):
                session_.objects.create(id_user= item[0].id, username= item[0].username, superuser=item[0].superuser)
                return redirect('/Larson')
            else:
                message_.warning(request, 'El usuario nombre de usuario o contraseña incorrectos⛔')
        else:
            message_.warning(request, 'El usuario no existe⛔')
    return render(request, 'login.html', {
        'form': form_login()
    })

def signup(request):
    session_.objects.all().delete()
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