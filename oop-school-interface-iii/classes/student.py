from classes.person import Person

class Student(Person):
    DATA_FILE = "../data/students.csv"

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    def __str__(self):
        return f'\t{self.name}\t{self.school_id}'

    def print_details(self):
        return f'\t{self.name}\n\t--------------------\n\tAge:\t\t{self.age}\
            \n\tSchool ID:\t{self.school_id}'

    # no "load_all()" class method exists here!!!

# LISA
# ---------------
# age: 25
# id: 13345

