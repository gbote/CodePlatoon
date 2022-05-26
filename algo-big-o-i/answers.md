# Big O Answers

## Snippet 1 -
### Big O: O(n)
### Explanation: Looping is linear; also, if and return statement are constant.
```python
def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 
```


## Snippet 2 - 
### Big O: O(n)
### Explanation: Each loop is looping over same data.

```python
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
  
```

## Snippet 3 -
### Big O: O(1)
### Explanation: Getting specific index of array is constant; increasing the input data size will not add time to the operation.

```python
def first_element_is_red(array):
  return array[0] == 'red' 
```

## Snippet 4 - 
### Big O: O(n^2)
### Explanation: each loop is O(n) so n*n = O(n^2); Conditional statemnts and return statements do not add more time.

```python
def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
``` 

## Snippet 5 -
### Big O: O(1)
### Explanation: There are nested loops; however, since the 2 lists are fixed/have fixed lengths, there is no change in input.

```python
words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)

```

## Snippet 6 -
### Big O: O(n)
### Explanation: O(n) grows proportionately in size based on size of input. Here, this one loop is linear.

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)

```

## Snippet 7 -
### Big O: O(n^2)
### Explanation: There are nested loops. I think the outer is O(n) but since the inner loop is only looking at part of the list (divide and conquer), it would be only O(log n). If that is correct, the total algo would be O(n log n). HOWEVER, J loop is going to be smaller than i loop. It's not fully n^2, but a worst case scenario can likely round up to O(n^2).

```python
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
```

## Snippet 8 -
### Big O: O(n^2)
### Explanation: 
### With 5 items in list: First loop goes through length of entire list and seems to go through 5 iterations and second loop goes through entire list and seems to go through 10 iterations. 
### With 10 items in list: First loop goes through 10 iterations (doubled as length of list doubled = linear) but second loop goes through 45 iterations (45/10 = 4.5 times as many). 
### With 20 items/length of list doubled, first loop doubles again to 20 iterations. Second loop goes through 190 iterations, about 4 times as many as when list was half this length. 
### The outer loop is O(n) and inner loop is at least O(n) if not slower so I am guessing the time complexity of this is at least On^2.
```python
for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
```