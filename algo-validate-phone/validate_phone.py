import re

phone_regex = r"\d{3}-\d{3}-\d{4}"

phone_regex_adv = r"\(?(\d{3})\)?\s?[-.]?(\d{3})[-.]?(\d{4})" 
# \(  ... escape to use parens
# ? ... match one or more times
# [-.] ... select one of these characters


# Does a string contain a phone number?
def has_phone_number(input_string):
    return re.search(phone_regex_adv, input_string) != None



# Get a phone number back from a string
def get_phone_number(input_string):
    if matches := re.findall(phone_regex, input_string):
        return matches[0]
    return None


# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    return re.findall(phone_regex, input_string)



# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    pattern = r"\d{3}-\d{3}-(\d{4})"
    return re.sub(pattern, r"XXX-XXX-\1", input_string)


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):    
    phone_regex_new = r"\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})"
    replace_with = r"\1-\2-\3"
    return re.sub(phone_regex_new, replace_with, input_string)


