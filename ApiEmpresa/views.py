from django.contrib.auth.models import User, Group
from AppWeb.models import Empleado
from rest_framework import viewsets
from ApiEmpresa.serializers import UserSerializer, GroupSerializer, EmpleadoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer