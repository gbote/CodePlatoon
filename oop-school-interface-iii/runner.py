from classes.school import School
import os

school = School('Ridgemont High')
menu1 = f"\
    What would you like to do?\n\
    Options:\n\
         1. List All Students\n\
         2. View Individual Student <student_id>\n\
         3. Add a Student\n\
         4. Remove a Student <student_id>\n\
         5. Quit\n\n"

menu2 = f"\n\n\tPress any key to return to menu\n\t>>>"

def run_school_menu():  # sourcery skip: avoid-builtin-shadow
    mode = 0
    while mode != '5':
        os.system('clear')
        print(menu1)
        mode = input("\t>>>")
        if mode == '1':
            os.system('clear')
            school.list_students()
            input(menu2)
        elif mode == '2':
            os.system('clear')
            id = input('\tEnter student id\n\t>>> ')
            student = school.find_student_by_id(id)
            print('\n\n', student.print_details())
            input(menu2)
        elif mode == '3':
            os.system('clear')
            student_data = {'role': 'Student', 'name': input('Enter student name:\n')}
            student_data['age']       = input('Enter student age: \n')
            student_data['school_id'] = input('Enter student school id: \n')
            student_data['password']  = input('Enter student password: \n')
            school.add_student(student_data)
        elif mode == '4':
            os.system('clear')
            choice = input('Do you want to delete student by:\n1 -- Name\n2 -- School ID?\n>>>')
            if choice == '1':
                key = 'name'
                val = input('Enter student name: ')
            elif choice == '2':
                key = 'school_id'
                val = input('Enter Student ID: ')
            else:
                input('Sorry, invalid choice, try again')
            if choice in ['1', '2']:
                valid = school.delete_student(key, val)
                if not valid:
                    input('Sorry, student not found, try again')
        elif mode == '5':
            return None
        else: 
            print('Thats not a valid menu item. Please select an options 1-5')
            os.system('clear')
            input(menu2)

run_school_menu()