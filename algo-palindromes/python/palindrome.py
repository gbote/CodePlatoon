import re
def remove_special_characters(letter):
    return re.match("[a-z0-9]", letter)

def palindrome(word):  # sourcery skip: avoid-builtin-shadow
    # Write code here
    input = list(filter(remove_special_characters, (f"{word}".lower())))
    return input == list(reversed(input))
