from django.contrib import admin
from django.urls import path
from proyecto.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', inicio, name= 'inicio'),
    path('remeras/', remera, name= 'remeras'),
    path('pantalones/', pantalon, name= 'pantalones'),
    path('clientes/', cliente, name= 'clientes'),
    path('formulario/', formulario, name= 'formulario'),
    path('infoformulario/', info_formulario, name= 'infoformulario'),

]   