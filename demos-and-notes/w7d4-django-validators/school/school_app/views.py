from django.shortcuts import render
from .models import Course, Professor, Student, Locker

# Create your views here.


# Examples of how to manipulate models
# NOTE: This code would go in a view, for example, NOT In models.py
my_course = Course.objects.get(pk=3)
print(my_course.professor) # prints the courses profesor
# professor of my_course
professor = Professor.objects.get(pk=my_course.professor.id)
print(professor.courses.all()) # prints ALL courses professor is teaching

my_student = Student.objects.get(pk=1)
print(my_student.locker) # Would give us the locker object itself

# Get student of a locker
a_locker = Locker.objects.get(pk=7)
student_who_owns_locker = a_locker.student

