class Animal:
    def __init__(self, name, color, daily_meals=1):
        self.name = name
        self.color = color
        self.daily_meals = daily_meals

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def speak(self):
        return "I am an animal!"



# the Cat class inherits from Animal
class Cat(Animal):

    def speak(self):
        print("meow meow!")

# we can still create a cat and make him eat, even though our cat class no longer has __init__ or eat methods.
garfield = Cat('garfield', 'orange')
# print(garfield.name)
# garfield.eat('lasagna')

# both the parent class and the child class have a method called speak, so the child's version overrides the parent version
# garfield.speak()

# the Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, color, daily_meals=2, is_service_animal=False):
        parent_instance = super() # this returns an instance of the animal class
        parent_instance.__init__(name, color, daily_meals=daily_meals)
        # super().__init__(name) # this is exactly the same as the above two lines, just condensed into one line

        self.is_service_animal = is_service_animal



    def speak(self):
        parent_speech = super().speak()
        print(parent_speech.upper())
        print("but more specifically, ")
        if self.is_service_animal:
            print(f"My name is {self.name}, and I'm here to help!")
        else:
            print("BARK BARK!")

spot = Dog('Spot', 'blue', is_service_animal=True)
print(spot.is_service_animal)

# tiny = Dog('tiny', 'teal', daily_meals=5, is_service_animal=False)
# print(tiny.daily_meals)
# tiny.daily_meals = 3
# print(tiny.daily_meals)
# print(tiny.is_service_animal)
# spot.eat('kibble')

# print(spot.name)
# print(spot.color)
# spot.speak()