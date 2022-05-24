# Write unit tests!
from pad_array import pad

print(pad([1, 2, 3], 5, 7) == [1, 2, 3, 7, 7])
print(pad([1, 2, 3, 4], 5, 'hi') == [1, 2, 3, 4, 'hi'])
print(pad([1, 2, 3, 4, 5], 4, 18) == [1, 2, 3, 4, 5])
print(pad([1], 3, None) == [1, None, None])
print(pad([1], 1, None) == [1])
print(pad([1,2,3], 5) == [1,2,3,None,None])
print(pad([1,2,3], 5, 'apple') == [1,2,3,'apple', 'apple'])
print(pad([1,2,3], 2) == [1,2,3])
print(pad([1,2,3], -1) == [1,2,3])
print(pad([1,2,3], 6) == [1,2,3, None, None, None])
print(pad([1,2,3], 4, "coffee") == [1,2,3, "coffee"])