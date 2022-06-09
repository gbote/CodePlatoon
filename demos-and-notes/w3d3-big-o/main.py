small_list = [4,9,5,12,2]
big_list = [4,9,5,12,2, 33,52, 9, 1, 0]

def append_to_list(my_list, new_item):
    my_list.append(new_item)

append_to_list(small_list, 77)
# O(1) - constant time


def find_item_greater_exists(my_list, value):
    for item in my_list:
        print(item)
        
    for item in my_list:
        if item > value:
            return True
    
    return False

# O(n) - linear time



def find_double_exists(my_list):
    for x in my_list:
        for y in my_list:
            if x * 2 == y:
                return True
    return False

# O(n^2) - quadratic time


def fibbonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibbonacci_recursive(n-1) + fibbonacci_recursive(n - 2)

# O(2^n)


# O(log n) - logarithmic time. doubling the size of the input adds one operation. binary search is a good example of this

# O(n log n) n log n. not as fast as linear time, but it's not as bad as quadratic time. 