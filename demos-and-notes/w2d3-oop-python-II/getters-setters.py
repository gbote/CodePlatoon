from re import A


class Person:
    def __init__(self, name):
        self.name = name
        self._age = 0
        self.dead = False


    @property
    def age(self):
        print('getter method called')
        return self._age

    @age.setter
    def age(self, a):
        print('setter method called')
        self._age = a
        if a > 100:
            self.dead = True





alice = Person('alice')
print(alice.age)

alice.age = 101
print(alice.age)
print(alice.dead)

print(Person)