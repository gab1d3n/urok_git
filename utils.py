from bboard.models import Student, Course

def get_students_in_courses():
    students = Student.objects.prefetch_related('courses').values('name', 'courses__title')
    for student in students:
        print(student)