from django.shortcuts import render
from .models import Student, Course, ProfileStudent, Teacher, SeniorTeacher

def student_list(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'school/student_list.html', {'students': students})

def teacher_list(request):
    teachers = SeniorTeacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})
