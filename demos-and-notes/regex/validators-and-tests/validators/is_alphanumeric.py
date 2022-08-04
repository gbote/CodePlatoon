import re

def is_alphanumeric(input):
    # \w matches any 'word' character, like letters, numbers, underscores, etc
    # + repeats the previous character 1 or more times
    # brackets in regex are like an 'or' expression. match one thing inside the brackets
    # we don't want python to escape the backslash
    # use a raw-string to treat is as a regular backslash, a regex character
    match = re.match(r"[a-zA-Z]\w+", input)
    return bool(match)