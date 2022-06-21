from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from .models import School, Student # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {
        "all_staff": my_school.staff # a list of staff instances
    }
    return render(request, "pages/list_staff.html", my_data)


def staff_detail(request, employee_id):
    print("id", employee_id)
    staff = my_school.find_staff_by_id(employee_id)
    print("staff", staff)
    my_data = {
        "staff": staff
    }
    return render(request, "pages/staff_detail.html", my_data)

def list_students(request):
    my_data = {
        "all_students": my_school.students # a list of staff instances
    }
    return render(request, "pages/list_students.html", my_data)


def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)
    my_data = {
        "student": student
    }
    return render(request, "pages/student_detail.html", my_data)



def student_new(request):
    ## POST request
    if request.method == "POST": # case here seems to matter
        print(request.POST)
        # grabbing the user input from the form that was submitted
        input_data = {
            "name": request.POST["name"],
            "school_id": request.POST["id"], # key = class parameter name, and value = the form name attribute
            "age": request.POST["age"],
            "password": request.POST["password"],
            "role": "Student"
        }

        # create a new student instance
        new_student = Student(**input_data)

        # update our internal (and extrnal data)
        my_school.add_student(new_student)

        # redirect to the student detail page
        return redirect(reverse("student_detail", args=[new_student.school_id]))

    ## GET request
    return render(request, "pages/student_new.html")