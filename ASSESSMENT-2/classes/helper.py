import csv
import os

class Helper:
    FILE_PATH_BASE = os.path.abspath(os.path.dirname(__file__))

    @staticmethod
    def get_full_path(filename):
        return os.path.join(Helper.FILE_PATH_BASE, filename)

    @staticmethod
    def read_all(filename, ClassName):

        data = []

        with open(Helper.get_full_path(filename), "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for data_dict in reader:
                data.append(ClassName(**data_dict))

        return data

    @staticmethod
    def write_one(filename, item):
        with open(Helper.get_full_path(filename), "a") as csv_file:
            header = item.get_vars() if hasattr(item, 'get_vars') else item.__dict__.keys()
            writer = csv.DictWriter(csv_file, fieldnames=header, extrasaction='ignore')
            writer.writerow(item.__dict__)

    @staticmethod
    def write_all(filename, items):
        if len(items) == 0:
            return

        with open(Helper.get_full_path(filename), "w") as csv_file:
            
            # this line gets a custom variables method if it exists or
            # just uses the objects dict keys if not
            header = items[0].get_vars() if hasattr(items[0], 'get_vars') else items[0].__dict__.keys()

            writer = csv.DictWriter(csv_file, fieldnames=header,extrasaction='ignore')
            writer.writeheader()
            for item in items:
                writer.writerow(item.__dict__)

    @staticmethod
    def clear_console():
        command = 'clear' if os.name not in ('nt','dos') else 'cls'
        os.system(command)

    @staticmethod
    def main_menu(name):
        Helper.clear_console()
        menu = f'''== Welcome to {name} Video! ==
  1. View store video inventory
  2. Display all customers
  3. View customer rented videos
  4. Add new customer
  5. Rent video
  6. Return video
  7. Upgrade/downgrade customer account
  8. Delete customer account
  9. Add titles to inventory
  10. Remove titles from inventory
  11. Exit

  >>> '''
        return menu

    @staticmethod
    def get_id(id, ClassName):
        """Class method to maintain stack of next id available. Allows for multiple store usage of shared video database without duplicate IDs. Note: csv/lists must stay sorted"""
        if id != None: id = int(id)
        #if no ID passed in, pop/replace the last id
        if id == None:
            new_id = ClassName.NEXT_ID.pop(0)
            if ClassName.NEXT_ID == []:
                ClassName.NEXT_ID.append(new_id+1)
            return new_id
        #if id passed in, move NEXT_ID to next value
        elif id >= ClassName.NEXT_ID[-1]:
            while id > ClassName.NEXT_ID[-1]:
                ClassName.NEXT_ID.append(ClassName.NEXT_ID[-1] + 1)
            ClassName.NEXT_ID[-1] += 1
            return id
        else:
            raise Exception('Lower id passed than expected. List likely not sorted')
    
    @staticmethod
    def return_id(id, ClassName):
        """puts ID back into available ids when customer deleted"""
        ClassName.NEXT_ID.append(id)
        ClassName.NEXT_ID = sorted(ClassName.NEXT_ID)