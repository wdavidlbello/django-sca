from rest_framework import serializers
from .models import Person,Department,PersonDepart

#Muestra las personas que tienen acceso a un departamento en particular
class PersondepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDepart
        fields = ['person']
        depth = 1
#Muestra los departamentos a que tiene acceso una persona
class DepPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDepart
        fields = ['department']
        depth = 1
#Muestra personas
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','dni']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']
