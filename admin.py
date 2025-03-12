from django.contrib import admin
from .models import Student, ProfileStudent, Course, Person, Teacher, SeniorTeacher

admin.site.register(Student)
admin.site.register(ProfileStudent)
admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(SeniorTeacher)