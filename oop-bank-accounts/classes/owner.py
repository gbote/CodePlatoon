from classes.read_csv import CsvHelper

class Owner:
    FILE_NAME = "../support/owners.csv"

    def __init__(self, id, last_name, first_name, street, city, state):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state

    def __repr__(self):
        return f"OWNER: {self.id}"

    @classmethod
    def load_all_owners(cls):
        return CsvHelper.read_all(cls.FILE_NAME, cls)

    @classmethod
    def save_owner(cls, new_owner):
        return CsvHelper.write_one(cls.FILE_NAME, new_owner)

    @classmethod
    def save_all_owners(cls, owners):
        return CsvHelper.write_all(cls.FILE_NAME, owners)