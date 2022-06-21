from django.db import models
import csv
import os


# Create your models here.
class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def load_all(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, cls.DATA_FILE)

        people = []

        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                person = cls(**row)
                people.append(person)

        return people


class Student(Person):
    DATA_FILE = "../data/students.csv"

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = int(school_id)

    def __str__(self):
        return f"{self.name.upper()}\n--------------\nage: {self.age}\nid: {self.school_id}"


class Staff(Person):
    DATA_FILE = "../data/staff.csv"

    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = int(employee_id)

    def __repr__(self):
        return f"staff: {self.name}"


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all()
        self.students = Student.load_all()

    def find_student_by_id(self, school_id):
        return next((student for student in self.students if student.school_id == school_id), None)

    def find_staff_by_id(self, employee_id):
        return next((staff for staff in self.staff if staff.employee_id == employee_id), None)

    def add_student(self, new_student):
        # update internal 
        self.students.append(new_student)
        ## TODO: add csv file updating