import csv
import os.path
from classes.person import Person

class Student(Person):
    DATA_FILE = "../data/students.csv"

    def __init__(self, name, age, password, role, school_id, major):
        super().__init__(name, age, password, role)
        self.school_id = school_id
        self.major = major

    def __str__(self):
        return f"{self.name.upper()}\n--------------\nage: {self.age}\nid: {self.school_id}"

    # no "load_all()" class method exists here!!!

# LISA
# ---------------
# age: 25
# id: 13345

