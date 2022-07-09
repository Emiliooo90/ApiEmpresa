from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def empleados(request):
    #Se obtiene el url de la api que consumiremos
    response = requests.get("http://127.0.0.1:8000/empleado")


    #Se convierte la api a formato json
    empleados = response.json()
    print(empleados)

    return render(request, "empleados.html", {'empleados': empleados})
    pass
