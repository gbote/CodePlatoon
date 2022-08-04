import re

def is_valid_ssn(input):
    # \d matches any single digit
    #  \d{3} matches 3 digits
    match = re.match(r"\d{3}(-?)\d{2}\1\d{4}", input)
    return bool(match)