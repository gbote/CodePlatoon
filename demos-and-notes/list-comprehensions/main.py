# list comprehensions


# list comprehensions let you define a list in terms of some other list. it serves as a replacement for map and filter

# 1: iterable
# 2: 'member' or list var
# 3: expression to be returned
# 4: a condition


my_list = [i*2 for i in range(10)]

letters = ['a','b','c','d','e']

capitalized_letters = [letter.upper() for letter in letters]

# print(my_list)
# print(capitalized_letters)

# in range(10), for each number, return that number times 2, if that number mod 2 is not 0.
doubled_odd_numbers = [i*2 for i in range(10) if i % 2 != 0]
print(doubled_odd_numbers)