from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        # instance attributes that we're creating here
        self.name = name
        self.staff = Staff.load_all()
        self.students = Student.load_all()

    def list_students(self):
        for num, student in enumerate(self.students, 1):
            print(f"{num}. {student.name} {student.school_id}")

    def find_student_by_id(self, school_id):
        return next((student for student in self.students if student.school_id == school_id), None)