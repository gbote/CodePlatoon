# Write your unit tests here
from recursion_challenge import to_roman, palindrome, factorial

print(factorial(3) == 6)

print(factorial(6) == 720)

print(factorial(9) == 362880)

print(factorial(1) == 1)

print(palindrome("hello") == False)

print(palindrome("doggod") == True)

print(palindrome("abcdefgfedcba") == True)

print(palindrome(123454321) == True)

print(to_roman(152) == "CLII")

print(to_roman(597) == "DXCVII")

print(to_roman(2954) == "MMCMLIV")