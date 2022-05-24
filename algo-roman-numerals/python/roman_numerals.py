# I -> 1
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000

conversion_roman_lazy = [
    { "increment": 1000,  "roman": "M" },
    { "increment": 500,   "roman": "D" },
    { "increment": 100,   "roman": "C" },
    { "increment": 50,    "roman": "L" },
    { "increment": 10,    "roman": "X" },
    { "increment": 5,     "roman": "V" },
    { "increment": 1,     "roman": "I" },
]

conversion_roman_modern = [
    { "increment": 1000,  "roman": "M" },
    { "increment": 900,    "roman": "CM" },
    { "increment": 500,   "roman": "D" },
    { "increment": 400,    "roman": "CD" },
    { "increment": 100,   "roman": "C" },
    { "increment": 90,    "roman": "XC" },
    { "increment": 50,    "roman": "L" },
    { "increment": 40,    "roman": "XL" },
    { "increment": 10,    "roman": "X" },
    { "increment": 9,    "roman": "IX" },
    { "increment": 5,     "roman": "V" },
    { "increment": 4,     "roman": "IV" },
    { "increment": 1,     "roman": "I" },
]

global_value = "donuts" # new global variable
def to_roman(num):
    roman_num = ""
    new_num = num
    for conversion_data in conversion_roman_modern:
        #print("in loop, coversion data", conversion_data)
        # figure out how many times our increment goes into our current number
        copies = new_num // conversion_data["increment"]
        for i in range(copies):
            roman_num += conversion_data["roman"]
        # determine what part is left over
        new_num = new_num % conversion_data["increment"] 
    return roman_num

#print(to_roman(594))
#DXCIV