import datetime
from django.db import models
from django.core.validators import MinLengthValidator

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=30)
    dni = models.CharField(validators=[MinLengthValidator(11)],max_length=11)

    def __str__(self):
        return self.name

class PersonDepart (models.Model):
    person = models.ForeignKey(Person,related_name='persons',on_delete=models.CASCADE)
    department = models.ForeignKey(Department,related_name='departments',on_delete=models.CASCADE)

class Log(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    date = models.DateTimeField()
    authorized = models.BooleanField(default=False)