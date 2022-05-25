def caesar_cipher(string, shift_amount):
    cypher_string = ""
    for letter in string:
        if letter.isalpha():
            shifted = ord(letter) + shift_amount
            if letter.upper() == letter:
                if shifted > 90:
                    shifted -= 26
                elif shifted < 65:
                    shifted += 26
            elif shifted > 122:
                shifted -= 26
            elif shifted < 97:
                shifted += 26
            new_char = chr(shifted)
            cypher_string += new_char
        else:
            cypher_string += letter
    return cypher_string
