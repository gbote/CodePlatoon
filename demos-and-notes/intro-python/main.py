# in python, don't use any keywords (let, const) for defining a variable
# variables are defined with 'snake_case', using lowercase letters and underscorse
a_small_number = '4.4'
a_real_number = float(a_small_number)

# print(type(a_real_number))

# print(.1 + .2)

a_string = 'hello world'
another_string = "welcome to the internet"
# print(type(a_string))

a_multiline_string = """
Look at all this text.
SO much text!
Wow, line after line.
"""
# print(a_multiline_string)

day = 'Friday'
activity = 'bowling'
# print(f'Let\'s go {activity} on {day} afternoon.')

# in js:  `Let's go ${activity} on ${day} afternoon."`

berries = ['grape', 'tomato', 'cucumber', 'eggplant', 'banana', 'watermelon', 'pumpkin']
# print(type(berries))
# print(berries[1])
# print(berries[-1]) # js version: berries[berries.length - 1]
# print(berries[2:4]) # ':' indicates a slice. 
# print(berries[:3]) # slice from the start to index 3
# print(berries[2:]) # slice from index 2 to the end

days_of_the_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
# print(type(days_of_the_week))
# days_of_the_week[6] = 'Caturday'

my_home_location = ( 34, 97 )



list_of_tuples = [
    (3,4),
    (5,6),
    (1,2),
    (5,6),
]
list_of_tuples[0] = (0,1) # this works
# list_of_tuples[1][0] = 0 # this does not work

# print(days_of_the_week[1:3])

# print(tuple(list_of_tuples))

a_string = 'hello'
# a_string[1] = 'a' # strings are immutable, you can't assign to them

small_list = [3]
small_tuple = tuple('hi') # you need a trailing comma in a 1-item tuple

# print((small_tuple))

alice = {
    'name': 'alice',
    'age': 44,
    'job': 'influencer',
}

# access dict values using bracket notation
# unlike in js, you cannot use dot-notation to access a dict
# print(alice['age'])
# print(alice.age)

prop = 'job'
# print(alice[prop])

people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 49,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]

# print(people[1]['name'])

def gimme_five():
    return 5
# print(gimme_five())

def add_one(n):
    return n + 1
# print(add_one(10))

# positional arguments must be passed in the correct order
# def describe_berries(n, color):
#     print(f"I have {n} {color}berries.")
# describe_berries(3, 'blue')
# describe_berries('black', 5) # this won't work correctly

def describe_berries(n=1, color="blue"):
    print(f"I have {n} {color}berries.")
# describe_berries(color="rasp", n=3)

# * means 'any number of positional arguments
def print_them_all(*args):
    print(args)
# print_them_all('alice', 'bob', 'carol')

# use **kwargs to accept any number of positional parameters
def who_am_i(**kwargs):
    for kwarg in kwargs:
        print(f"my {kwarg} is {kwargs[kwarg]}.")
# who_am_i(name="dan", age=20, job='skydiving instructor')

# in python, we use and, or, instead of &&, ||, no parens around if-statement, use 'elif' instead of else if
def can_drink_beer(age, country):
    if age >= 21 or (age >= 18 and country) == 'Canada':
        return True
    elif country == 'Antarctica':
        return True
    else:
        return False
# print(can_drink_beer(20, 'USA'))
# print(can_drink_beer(21, 'USA'))
# print(can_drink_beer(18, 'Canada'))
# print(can_drink_beer(8, 'Antarctica'))

my_list = ["a", "b", "c"]
# for x in my_list:
    # print(x)

for x in range(10, -1, -1):
    print(x)

# for i, x in enumerate(my_list):
#     print(i,x)

# for k in alice:
#     print(k)
#     print(alice[k])

x = 9
# while x > 0:
#     print(x)
#     x = x - 1

# print(reversed(range(10)))