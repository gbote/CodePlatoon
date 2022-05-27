from functools import cmp_to_key

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
        'age': 35,
        'job': 'life coach',
    },
]

# our sort function will look at list elements 2 at a time
# return any positive number to indicate that a gets sorted before b
# return any negative number to indicate that b gets sorted before a
# return 0 to indicate that you don't care which is first
def sort_by_age(a,b):
    # if a['age'] - b['age'] > 0:
    #     return 1
    # elif a['age'] - b['age'] < 0:
    #     return -1
    # elif a['age'] == b['age']:
    #     return 0
    return a['age'] - b['age']

# key is a 1-argument function that describes how to sort the list.
# in python2, you used cmp, which was a 2-argument function that describes how to sort the list
# sourcery skip: raise-specific-error
sorted_people = sorted(people, key=cmp_to_key(sort_by_age))
print(sorted_people)

# if you need to do something that you think might throw an error, put it in a 'try' block
try:
    a = 1
    b = 'hi'
    raise(Exception('oops'))
    c = a + b
    print('we did it!')
except Exception as e:
    print(e)

print('continuing...')

