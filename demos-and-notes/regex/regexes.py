# re module gives us our regex functions
import re


# Basic pattern matching with re.match
is_match = re.match(r"abc", r"abc")

# Example of a validator-type function using a regex
def is_abc_match(input):
    match = re.match(r"abc", input)
    return bool(match)

print(is_abc_match("abc"))

# Example of using a match in an if statement
if is_match:
    print("Regex matches")
else:
    print("No match")