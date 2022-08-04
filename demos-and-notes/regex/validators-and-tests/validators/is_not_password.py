import re
# takes a string as input, and then returns true/false if the string is 'password'
# literal characters in a regex will match that character in the input string

def is_not_password(input):
    match = re.match(r"password", input.lower())
    return not match
