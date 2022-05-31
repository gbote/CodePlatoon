# use capital letters to name classes in python
from unicodedata import name

class Dog:
    # the self parameter refers to the dog object we're about to create
    # dunder-init is a dunder method (Double UNDERscores)
    def __init__(self, name, color, sound='woof'):
        self.name = name
        self.species = 'Canine'
        self.color = color
        self.sound = sound
        self.barks = 0
        # print('initialising!')

    def __str__(self):
        return f"""
        {self.name}
        {self.species}
        {self.color}
        {self.sound}
        {self.barks}
        """
        # return f"I am a {self.color} {self.species} named {self.name}."


    def speak(self):
        self.barks += 1
        return f"{self.name} says: {self.sound}!"

    def yell(self):
        return self.speak().upper()

    def fetch(self, item):
        return f"{self.name} fetched the {item}."

# just like we call functions, classes are also CALLABLE in python. 

# i'm calling the class itself, i never call the __init__() method, python calls it for me.
# fido is an INSTANCE of the dog CLASS
fido = Dog('Fido', 'golden', sound='bork bork')
# fido.color = 'brown'
lassie = Dog('Lassie', 'more golden', sound="yap yap")

# print(Dog)
# use dot-notation to access properties of objects
# print(fido)
# excited_greeting = fido + '!!'
# print(excited_greeting)
# a dog dictionary
# some_dog = {
#     'name': 'lassie',
#     'color': 'brown',
# }

print(fido.speak())
print(fido.yell())
# fido.fetch('bones')


class Person:
    def __init__(self, name, dog_name):
        self.name = name
        self.dog = Dog(dog_name, 'black', 'bark')


alice = Person('alice', 'boney')
print(alice)
print(alice.dog)
