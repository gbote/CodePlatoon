from roman_numerals import to_roman

# lazy 
# print(to_roman(1) == 'I')
# print(to_roman(3) == 'III')
# print(to_roman(4) == 'IIII')
# print(to_roman(1254) == 'MCCLIIII')
# print(to_roman(2890) == 'MMDCCCLXXXX')
# add tests to cover different edge cases

# modern
print(to_roman(1) == 'I')
print(to_roman(3) == 'III')
print(to_roman(100) == 'C')
print(to_roman(1254) == 'MCCLIV')
print(to_roman(2890) == 'MMDCCCXC')