from rest_framework import serializers
from .models import Person,Department

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','dni']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']