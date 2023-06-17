#url list
from django.urls import path
from . import views as vs

urlpatterns = [
    path('Login', vs.login),
    path('NewtonLarson', vs.index),
    path('SignUp', vs.signup),
    path('Larson', vs.larson),
]