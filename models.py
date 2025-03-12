from django.db import models, transaction

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(Person):
    position = models.CharField(max_length=100)

class Manager(Employee):
    department = models.CharField(max_length=100)


def create_employee_with_error():
    try:
        with transaction.atomic():
            emp = Employee.objects.create(name='John Doe', position='Developer')
            raise ValueError("Ошибка, откат транзакции")
    except ValueError:
        print("Транзакция отменена")

class EmployeeManager(models.Manager):
    def developers(self):
        return self.filter(position='Developer')

class EmployeeQuerySet(models.QuerySet):
    def managers(self):
        return self.filter(position='Manager')

class EmployeeWithManager(Employee):
    objects = EmployeeManager.from_queryset(EmployeeQuerySet)()