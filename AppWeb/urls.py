from django.urls import path
from . import views

app_name = 'AppWeb'

urlpatterns = [
    path('empleados/', views.empleados, name="empleados"),
    path('mostrar_emp/<rut>/', views.mostrar_emp, name="mostrar_emp"),
]