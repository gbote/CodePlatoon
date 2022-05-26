import csv
import os

class CsvHelper:
    FILE_PATH_BASE = os.path.abspath(os.path.dirname(__file__))

    @staticmethod
    def get_full_path(filename):
        return os.path.join(CsvHelper.FILE_PATH_BASE, filename)

    @staticmethod
    def read_all(filename, ClassName):
        items = []

        with open(CsvHelper.get_full_path(filename), "r") as csv_file:
            reader = csv.DictReader(csv_file)
            items.extend(ClassName(**data_dict) for data_dict in reader)
        return items

    @staticmethod
    def write_one(filename, item):
        with open(CsvHelper.get_full_path(filename), "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=item.__dict__.keys())
            writer.writerow(item.__dict__)


    def write_all(self, items):
        if len(items) == 0:
            return
        with open(CsvHelper.get_full_path(self), "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=items[0].__dict__.keys())
            for item in items:
                writer.writerow(item.__dict__)