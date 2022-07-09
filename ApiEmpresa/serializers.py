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
        fields = ['url', 'rut_emp', 'nom_emp', 'area_tra', 'cap_maq', 'cap_grua', 'cap_alt']