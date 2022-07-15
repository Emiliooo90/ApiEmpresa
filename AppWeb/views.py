from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def empleados(request):
    #Se obtiene el url de la api que consumiremos
    response = requests.get("http://emiliosk11.pythonanywhere.com/empleado")


    #Se convierte la api a formato json
    empleados = response.json()
    print(empleados)

    return render(request, "empleados.html", {'empleados': empleados})
    pass

def mostrar_emp(request, rut):
    url = "http://emiliosk11.pythonanywhere.com/empleado/" + rut
    response = requests.get(url)
    empleados = response.json()
    return render(request, "mostrar_emp.html", {'empleados': empleados})
    pass
