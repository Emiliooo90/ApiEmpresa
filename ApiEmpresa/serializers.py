from django.contrib.auth.models import User, Group
from rest_framework import serializers
from AppWeb.models import Empleado

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['url', 'rut', 'nombre_completo', 'area_de_trabajo', 'curso_maquinaria', 'curso_grua', 'curso_altura']