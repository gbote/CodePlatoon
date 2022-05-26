class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.total = 0
    self.stack = []

  def __str__(self):
    return ''.join(f'{i} ' for i in self.stack)

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.total += 1
    self.stack += [data]

  def pop(self):  # sourcery skip: raise-specific-error
    # write your code to removes the data following LIFO and return the Stack
    if self.total == 0: raise Exception('Trying to pop from empty stack')
    self.total -= 1
    end = self.size()-1
    data = self.stack[end]
    self.stack = self.stack[:end]
    self.total -= 1
    return data

  def size(self):
    # write your code that returns the size of the Stack
    return self.total