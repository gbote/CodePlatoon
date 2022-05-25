import csv
import os.path
from classes.person import Person

class Student(Person):
    DATA_FILE = "../data/students.csv"

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id