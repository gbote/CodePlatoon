from first_missing_positive_integer import first_missing_positive

print(first_missing_positive([1, 2, 3, 5, 6, 7]) == 4)
print(first_missing_positive([2, 7, -1, 3, 6, 5, 8, 1, 9]) == 4)
print(first_missing_positive([1, -1, 0, 3, 4, 5]) == 2)
print(first_missing_positive([-1, -2, -3, -5, -6, -7]) == 1)
print(first_missing_positive([-2, -1, 0, 1, 2, 3, 4, 5, 6]) == 7)
print(first_missing_positive([3, 4, 5, 6, 7, 8, 9]) == 1)
print(first_missing_positive([0, -1, 5, 4, 3, 2, 1, 14, 567]) == 6)
print(first_missing_positive([]) == 1)