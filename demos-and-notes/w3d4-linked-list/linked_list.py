
# A simple example of a singly-linked list. Is not a totally OOP approach
# as list traversal and manipulation is handled with global variables and functions
# as opposed to a LinkedList class.

# Individual node in linked list
class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def set_next_node(self, next):
    self.next_node = next

# node_a is the 'head' of our list
node_a = Node('Hello')
#node_b = Node('World')
#node_c = Node('!')

# Connect nodes 
#node_a.set_next_node(node_b)
#node_b.set_next_node(node_c)

# Iterate thru list
pointer = node_a
while(pointer):
  #print(pointer.value)
  pointer = pointer.next_node

# Pass in the head of a linked list, and a value --
# this function will append a new node at the end of the list
# with desired value.
def add_to_list(head, new_value):
  new_node = Node(new_value)

  # Get to the end of the list
  # So I can append (add on) the new node
  pointer = head
  while pointer:
    # End of list, add new the node & exit loop
    if pointer.next_node is None:
      pointer.next_node = new_node
      break

    else:
      pointer = pointer.next_node

# Adding some nodes to our list 
add_to_list(node_a, 'World')
add_to_list(node_a, '!')
add_to_list(node_a, ' It is sunny')
add_to_list(node_a, ' and the weather is good.')

# Traverse through list and print value of each node
def print_list(head):
  pointer = head
  while(pointer):
    print(pointer.value)
    pointer = pointer.next_node

print_list(node_a)


# DO THIS FIRST
# Exercise: Remove *last node* from list.
# 1. Iterate thru list until pointer is pointing to the *second-to-last* node in the list
# 2. For the *second-to-last* node, set it's `next_node` property to None (so it doesn't point to anything).
# 3. Voila! Your second-to-last node is now the last node in the list. Test by printing out all the values in the list
# to confirm.

# Exercise: Remove *any desired node* from the list (except the head of the list; that is a special case)
# NOTE: This is a more complex task. I *highly* recommend drawing/using visual aids.
# You need *two* pointers, leading_pointer and trailing_pointer
# If leading_pointer is set to the *third* node in the list, *trailing_pointer* is set to the *second*.
# I recommend implementing this and testing with print statements before moving forward.
#
# 1. Iterate thru array until the leading_pointer is set to the node you want to remove, 
# and trailing_pointer is set to the node *before* the one you want to remove.
# 2. For trailing_pointer, set it's next_node to leading_pointer.next_node 
# For example if  our list is A B C D and we want to remove C, we do:
# B --> D
#   C
# We are *cutting out* the undesired node C from the list, and *stitching the list back together so B points to D.