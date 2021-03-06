from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all()
        self.students = Student.load_all()

    def list_students(self):
        print('\tNAME\tSCHOOL ID')
        for each in self.students:
            print(each)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student