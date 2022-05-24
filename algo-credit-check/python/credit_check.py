# GAMEPLAN:
# Split number string into an array of its elements.
# Iterate backwards through the array as such:
#     For every other number:
#        Double every other number
#        If current number > 9, add 1 to (current number % 10)
#     for each number (odd) or result (even), add to sum total
# Verify sum total mod 10 equals 0

def credit_check(str):  # sourcery skip: avoid-builtin-shadow
    
    str = list(str)
    even = False
    sum = 0
    change_num = 0

    for i in range(len(str) - 1, -1, -1):
        change_num = int(str[i])
        if even:
            change_num *= 2
            if change_num > 9: 
                change_num = (change_num % 10) + 1
            even = False
        else:
            even = True
        sum += change_num

    return 'The number is valid!' if (sum % 10) == 0 else 'The number is invalid!'

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"