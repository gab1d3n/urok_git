from django.shortcuts import render
from .models import Student, Course

def student_list(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'school/student_list.html', {'students': students})
