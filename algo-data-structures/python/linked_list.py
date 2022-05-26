class LinkList:
  # write your __init__ method here that should store a 'head' value which is the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    self.head = None
    self.length = 0

  def __str__(self):
    if self.head is None: return None
    if self.head.next is None: return f'{self.head}'
    current = self.head
    string = ''
    while current != None:
      string += f'{current.value} - '
      current = current.next
    return string

  def add(self, data):
    # write your code to ADD an element to the Linked List
    new_Node = Node(data)

    if self.head is None: 
      self.length += 1
      self.head = new_Node
      return

    current = self.head
    while current.next != None:
      current = current.next
    current.next = new_Node
    self.length += 1

  def remove(self, data):  # sourcery skip: raise-specific-error
    # write your code to REMOVE an element from the Linked List
    if self.head is None: raise Exception('Cant remove from empty list')
    if self.head.value == data: 
      self.length -= 1
      self.head = self.head.next
      return

    current = self.head
    while current.next != None:
      if current.next.value == data:
        current.next = current.next.next
        self.length -= 1
        return

  def get(self, element_to_get):
    # write your code to GET and return an element from the Linked List
    current = self.head
    for _ in range(element_to_get):
      current = current.next
    return current.value

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, value):
    self.value = value
    self.next = None
    def __str__(self):
        return f'{self.value}'