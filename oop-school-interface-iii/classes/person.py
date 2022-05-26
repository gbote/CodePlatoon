import csv
import os

class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def load_all(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, cls.DATA_FILE)

        people = []

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            people.extend(cls(**row) for row in reader)
        return people

    @classmethod
    def save_all(cls, people):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, cls.DATA_FILE)

        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            #write header row
            writer.writerow(people[0].__dict__.keys())
            for person in people:
                writer.writerow(person.__dict__.values())