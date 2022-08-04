import re
# takes a string as input, and then returns true/false if the string is 'password'
# literal characters in a regex will match that character in the input string

def is_at_least_12_characters(input):
    match = re.match("............", input)
    return bool(match)

