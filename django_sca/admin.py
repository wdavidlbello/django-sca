from django.contrib import admin
from .models import Person,Department,PersonDepart,Log

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(PersonDepart)
admin.site.register(Log)