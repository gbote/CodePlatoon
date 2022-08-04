import re

# .+ one or more characters
# .? zero or one characters
# .* zero or more characters
def does_not_repeat(input):
    match = re.match(r"(....).*\1", input)
    return False if match else True