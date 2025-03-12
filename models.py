from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class ProfileStudent(Student):
    grade = models.CharField(max_length=10)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.grade})"

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(Person):
    subject = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

class SeniorTeacher(Teacher):
    department = models.CharField(max_length=100)
    publications = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department} (Senior)"