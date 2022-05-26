def factorial(num):
    return 1 if num in [0, 1] else num * factorial(num - 1)


def palindrome(input):
    string = str(input)
    if not string:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])


def bottles(num=99):
    if num == 1:
        return f"{str(num)} bottle of beer on the wall, {str(num)}  bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
    bottle_word = "bottles"
    bottle_less = "bottle" if num == 2 else "bottles"
    print(
        f"{str(num)} {bottle_word} of beer on the wall, {str(num)} {bottle_word} of beer.\nTake one down and pass it around, {str(num - 1)} {bottle_less} of beer on the wall.\n"
    )
    return bottles(num - 1)


def to_roman(num):

    conversion_roman_modern = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    flag = None
    for symbol, number in conversion_roman_modern.items():
        if number == num:
            return symbol
        if num > number:
            flag = symbol

    remaining = num - conversion_roman_modern[flag]
    return flag + to_roman(remaining)