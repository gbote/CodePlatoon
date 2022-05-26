class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.total = 0
    self.queue = []

  def __str__(self):
    return ''.join(f'{i} ' for i in self.queue)

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.total += 1
    self.queue += [data]

  def dequeue(self):  # sourcery skip: raise-specific-error
    # write your code to removes the data to the Queue following FIFO and return the Queue
    if self.size() == 0: raise Exception('Attempting to dequeue an empty Queue')
    data = self.queue[0]
    self.queue = self.queue[1:]
    self.total -= 1
    return data

  def size(self):
    # write your code that returns the size of the Queue
    return self.total