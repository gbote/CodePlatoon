from classes.school import School
import os

class SchoolInterface:
    menu1 = f"\
    What would you like to do?\n\
    Options:\n\
         1. List All Students\n\
         2. View Individual Student <student_id>\n\
         3. Add a Student\n\
         4. Remove a Student <student_id>\n\
         5. Quit\n\n>>>"

    menu2 = f"Press any key to return to menu\n"


    def __init__(self, school_name):
        self.school = School(school_name) 

    def run(self):  # sourcery skip: avoid-builtin-shadow
        if not self.authenticate_user():
            return None

        while True:
            os.system('clear')
            mode = input(self.menu1)
            if mode == '1':
                os.system('clear')
                self.school.list_students()
                input(self.menu2)

            elif mode == '2':
                os.system('clear')
                id = input('Enter student id\n\t>>> ')
                student = self.school.find_student_by_id(id)
                print('\n\n', student.print_details())
                input(self.menu2)

            elif mode == '3':
                student_data = self.get_student_info()
                self.school.add_student(student_data)

            elif mode == '4':
                key,val = self.del_student_info()
                if key == 'Q':
                    continue
                valid = self.school.delete_student(key, val)
                if not valid:
                    input('Sorry, student not found, press any key')

            elif mode == '5':
                break

            else: 
                print('Thats not a valid menu item. Please select an option 1-5')
                input(self.menu2)

    def get_student_info(self):
        os.system('clear')
        student_data = {'role': 'Student', 'name': input('Enter student name:\n')}
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        return student_data

    def del_student_info(self):
        os.system('clear')
        valid_choice = False
        while not valid_choice:
            choice = input('Do you want to delete student by:\n1 -- Name\n2 -- School ID?\nQ -- Quit to last menu\n>>>')
            if choice == '1':
                key = 'name'
                val = input('Enter student name: ')
                valid_choice = True
            elif choice == '2':
                key = 'school_id'
                val = input('Enter Student ID: ')
                valid_choice = True
            elif choice == 'Q':
                return 'Q','Q'
            else:
                os.system('clear')
                print('Sorry, invalid choice, try again\n')
            if valid_choice:   
                return key,val

    def authenticate_user(self):  # sourcery skip: avoid-builtin-shadow
        os.system('clear')
        id = input(f'Welcome to {self.school.name}\n----------------------------\nPlease enter a valid employee id: ')
        valid = False
        while not valid:
            if self.school.check_staff_id(id):
                valid = True
            else:
                id = input('That is not a valid id, please try again or press Q to quit: ')
                if id == 'Q': return False

        tries, valid = 0, False
        while (not valid) and tries < 3:
            pswd = input('Please enter your password: ')
            #validate this password against the id given
            valid = bool(self.school.check_password(id,pswd))
            tries += 1
            if not valid: print (f'Invalid password, you have {3-tries} attempts remaining')


        return valid