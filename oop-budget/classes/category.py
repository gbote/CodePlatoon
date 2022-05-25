from enum import Enum

class Category(Enum):
    FOOD = 1
    LIVING = 2
    TRAVEL = 3

    def get_name_from_value(self):
        for item in Category:
            if item.value == self:
                return item.name