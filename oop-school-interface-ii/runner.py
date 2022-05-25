from classes.school import School

# create an instance
school = School('Ridgemont High')

# print(school.staff)
# print(school.students)

mode = None

while mode != '5':
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    print("\n")

    if mode == '1':
        school.list_students() 

    elif mode == '2':
        student_id = input('Enter student id:')
        print("\n")
        if student := school.find_student_by_id(student_id):
            print(student)
        else:
            print(f"Student with {student_id} not found!!!!!") 


print("== Have a nice day! Come back soon :) ==")