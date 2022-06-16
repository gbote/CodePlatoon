# Review Day

## Topics Covered / Goals
- Review Object Oriented Programming in Python
    - Understand Class Objects, Instance Variables, and Instance Methods

### Lesson

- Class Objects

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f"Hello my name is {self.first_name} {self.last_name} and I'm {self.age} years old."

    def celebrate_birthday(self):
        self.age = self.age + 1
        return f"Wooo! It's my birthday today! I'm {self.age}!"

    def my_age(self):
        return f"My age is {self.age}."
```

## Assessment
- [Assessment #1](https://github.com/quebecplatoon/assessment-1)

## Assignments
- [School Interface II](https://github.com/romeoplatoon/oop-school-interface-ii)
- [Budget](https://github.com/romeoplatoon/oop-budget)
- [Bowling](https://github.com/romeoplatoon/oop-bowling)


