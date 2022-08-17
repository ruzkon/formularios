from django.shortcuts import render
from proyecto.models import Remera, Pantalon, Cliente
from django.http import HttpResponse


def inicio(request):
    return render(request, 'proyecto/index.html')

def remera(request):
    return render(request, 'proyecto/remera.html')

def pantalon(request):
    return render(request, 'proyecto/pantalon.html')

def cliente(request):
    cliente = Cliente.objects.all()
    lista_clientes = []
    for persona in cliente:
        lista_clientes.append(persona.nombre)
        return HttpResponse(lista_clientes)
       #return render(request, 'proyecto/index.html', )


def formulario(request):
    return render(request, 'proyecto/formulario.html')


def info_formulario(request):
    print(request.GET)

    return HttpResponse(f" Acceso confirmado: {request.POST['nombre']}")


