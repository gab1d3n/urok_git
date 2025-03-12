from django.contrib import admin
from .models import Person, Employee, Manager, EmployeeWithManager

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(EmployeeWithManager)
