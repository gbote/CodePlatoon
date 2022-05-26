from classes.person import Person

class Staff(Person):
    DATA_FILE = "../data/staff.csv"

    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    def __str__(self):
        return f'\t{self.name}\t{self.school_id}'