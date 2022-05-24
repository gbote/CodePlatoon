# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong_list = []

    # check each number in the array
    for num in numbers:

        # convert int number to string to access each digit individually
        num_str = str(num) 
        length = len(num_str)
        total = 0

        # calculate exponentiation for each digit and add them all up
        for i in range(length):
            total += int(num_str[i]) ** length

        if (total == int(num_str)):
            armstrong_list.append(total)

    return armstrong_list