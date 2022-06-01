class Dog:
    # this is a class-attribute in python. it belongs to the Dog class itself, not any specific dog
    species = "Canis Lupus Familiaris"
    all_dogs = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.all_dogs.append(self)
    
    def __str__(self):
        return self.name
    
fido = Dog('Fido', 'wolf')
lassie = Dog('lassie', 'sheepdog')
# print(fido.name)
# print(Dog.all_dogs)
# for dog in Dog.all_dogs:
    # print(dog.breed)
# print(fido.species) # this property doesn't exist on the instance, so python will check the class instead
# print(Dog.species) # this property exists directly on the class

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(radius):
        return radius ** 2 * math.pi

    
    @classmethod
    def margherita(cls):
        return cls(8, ['mozzarella', 'tomatoes'])

mushroom_pizza = Pizza(10, ['mushrooms'])

marg_pizza = Pizza.margherita()
print(marg_pizza.ingredients)
# print(mushroom_pizza.area())

# our Pizza class knows how to calculate the area of a circle, without respect to an individual pizza, so we can reuse that functionality
# print(Pizza.circle_area(4))


