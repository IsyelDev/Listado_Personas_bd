from django.shortcuts import render
from django.http import HttpResponse

from empleados.models import Empleado

def home(request):
    empleados = Empleado.objects.all()
    
    contexto = {
        'empleados' : empleados
    }
    return render(request,'home.html', contexto)