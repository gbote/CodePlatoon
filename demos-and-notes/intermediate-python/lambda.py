import functools

def add_one(x):
    return x+1

# print(add_one(4))

# lambda function: a simple one-line function

# the result of the body of the lambda function is automatically returned
add_numbers = lambda input_argument, other_arg : input_argument + other_arg

# print(add_numbers(2, 5))


# filter is a method you can call on a list, that returns a NEW LIST, with some of the items missing
# we'll use a lambda function to specify which elements should be filtered out
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = filter(lambda item : item % 3 == 0, my_list)

# print(my_list)
# print(list(new_list))

# ternary statement in python
num = 11
x = 'hello' if num > 10 else 'goobdye'
# print(x)


# the map function takes an list as input, an a function that describes how to change each element, 
# and then returns a new list of the same length, with each element transformed. 
bigger_numbers = list(map(lambda item : item + 2, my_list))
# print(bigger_numbers)

baby_names = ['alice', 'bob', 'carol']
people = list(map(lambda baby_name : {'name': baby_name, 'age': 0}, baby_names))
# print(people)

just_names = list(map(lambda person : person['name'], people))
# print(just_names)

my_name = 'raphael'
capitalized_name = list(map(lambda letter : letter.upper() ,my_name))
# print(capitalized_name)

# reduce takes a list, and returns a single value based on each item in the list
sum = functools.reduce(lambda agg, item: agg + item, my_list)
# print(sum)

numbers = [1,4,6,2,1,8,4]
print(sorted(numbers))