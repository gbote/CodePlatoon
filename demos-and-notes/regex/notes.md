# Regex

Regular Expressions. 
Not specific to any one language, but each language has its own implementation with minor differences.

# Goals
    - Basic idea of regular expressions
    - How to perform basic tasks with regex
        - Checking for valid phone number
        - Checking for valid social security number
        - Checking if a string is alphanumeric or not
        - Checking if a string contains special characters (such as "$")
        - Checking if a string has digits or letters
    - Strengths of regex
        - Pattern-matching strings!
    - Weaknesses of regex
        - Becomes complicated very quickly
        - Hard to debug
        - May not be performant, if you are concerned with performance.
    
## HIGHLIGHTS & BEST PRACTICES
    - ALWAYS test your regex in the actual system you will be using it.
        - Especially relevant when getting a regex from stack overflow.
    - Always try to make your regex as specfic as possible
        - Easier to debug
        - Easier for other programmers to understand the intent of the regex
        - Improves performance
    - Always add comments to your regex explaining it
        - What we are using it for
        - How it works
    - Build your regex one piece at a time, and test as you go.

## Regexes with Python
    - Always want to use a raw string, or r string, for our regex expression.
        - Raw string example: r"hello\$"
            - Raw strings don't escape based on slash
    - Import re module for python regex functions
        - re.match
            - If zero or more characters at the beginning of string match this regular expression, return a corresponding match object.
            - Most basic tasks can be done with re.match
        - re.search
            - Scan through string looking for the first location where this regular expression produces a match,
        - re.findall
            - Returns a List of all matches

## Regex Pattern Matching
    - Regex by default looks to see if a pattern exists WITHIN a given string.


## Regex Special Characters
    - Let us perform more sophisticated pattern-matching operations

### The "dot" Operator: `.`
    - The dot is a wildcard - it matches anything.

### The Escape Character: `\`
    - Use it to treat a special character like a normal character
    - Example: The regex `foo\.js` will match for "foo.js"

### The Optional Character: `?`
    - `?` is the Optional Character. The character *before* it, is considered optional.
        - Example: ab?c matches "abc" OR "ac", because "b" is optional

### Metacharacters
    - Any Digits: `\d`
        - Signifies any digit, zero thru nine, aka 0-9
    - Whitespace: `\s`
        - Literally a space: " "
    - Word character: `\w`
        - Any alphanumeric character:
            - "a", "b", "c" ... on to "z". Also "A", "B", "C"
            - Digits 0 thru 9
            - Underscor: "_"
    - Non-Alphanumeric character: \W

### Character Ranges
    - Using brackets we can indicate the *range* of characters to pattern match against
        - Examples 
            - [a-z] matches the lowercase characters "a" through "z"
            - [a-f] match lowercase characeters "a" through "f"
            - [0-9] matches digits "0" through "9"
            - [3-5] match digits "3" through "5"
    - We can include more than one character range in the brackets:
        - Example: Only characters a-z and A-z: [a-zA-z]

### Repeating Characters
    - Curly brackets indicate repetitions of a character
        - The curly brackets apply the repetion *before* our curly brackets.
        -Example: a{3} will match the character "a" exactly three times.

### Kleene Star / Kleene Plus
    - Kleene Star: *
        - Means "At least 0 or more of the preceding character"
        - Example: a*
            - At least 0 or more of "a"
    

    - Kleene Plus: +
        - Means "At least 1 or more of the preceding character"
            - Example: a+
                - At least 1 or more of "a"
                
    - The last name of the person who invented regex was "Kleene"

### Capture Groups: (x)
    - Defines a group of characters in the regex
    - Looks for *repetitions* of that group of characters
    - For more sophisticated use-cases, we can use capture groups to extract the group to do more work with them.
    - Example:
        - Phone number regex: \d{3}(-)\d{3}\1\d{4}
            - The capture group is defined by parethesis. The value of the capture is whats inside the parenthesis, in this case "-"
            - To refer back to a capture group, in this case we use \1
                - There could be more than one capture group. If we were referring back to a second capture group that we'd defined, we would do \2

## Brackets - The "OR" Statement of Regex
    - With brackets, we are pattern matching for ONE OF the characters inside the brackets.
        - Example: [abc]
            - Matches for "a" OR "b" OR "c"
### Common Use-Cases
    - Valid Date regex
        -\d{2}-\d{2}-\d{4}
        - Matches: "04-12-2022" format
    - Phone Number regex
        - Regex:\d{3}(-?)\d{3}\1\d{4} 
            - Explanation: 
                - Matches for three digits, optional "-", three more digits, optional "-", and then 4 digits.
                - We use a capture group to check for "-". It is optional, but the capture gorup enforces consistency. If there is a "-" after the first 3 digits, there must be another "-" after the next 3 digits. Or, no dash is used anywhere at all.
            - Matches:
                - "312-555-4444"
                - "3125554444"
    - Social Security Number regex
        - Regex: \d{3}(-?)\d{2}\1\d{4}
            - Explanation; Same as phone, except our middle group of digits is exactly 2 digits instead of exactly 3 digits. 
    - Matching file extensions:
        - JS file:
            - \w+\.js
                - Uses Kleene + to say there must be at least 1 alphanumeric character before the dot and the file extension.