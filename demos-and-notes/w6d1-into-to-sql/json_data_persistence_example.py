# sourcery skip: avoid-builtin-shadow
import json
from os import path

print("** WELCOME TO THE ACME SCHOOL DATABASE **")

# get student ID from user input
id = input('Enter a student id: ')


# open the student's data file
id = f'{id}.json'
filename = path.join('data', id)


student_data = json.load(open(filename, 'r'))



# print student's data
print (f"{student_data['first_name']} {student_data['last_name']}")
print (f"Birthdate: {student_data['birthdate']}")

address = student_data['address']
print("Mailing Address")
print(f"{address['line_1']}")
print(f"{address['city']}, {address['state']}")
print(f"{address['zip']}")

print("Classes")
for class_name in student_data["classes"]:
    print(f"{class_name}")