class Bst:
  def __init__(self):
    self.parent = None

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    new_node = Node(value)

    if self.parent is None:
      self.parent = new_node
      return

    inserted = False
    current = self.parent
    while not inserted:
      #looking left
      if value < current.data:
        #inserting
        if current.left is None:
          current.left = new_node
          inserted = True
        else:
          current = current.left
      elif current.right is None:
        current.right = new_node
        inserted = True
      else:
        current = current.right

  def contains(self, value):
    # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
    if self.parent is None: return False
    elif self.parent.data == value: return True

    found = False
    current = self.parent
    while not found:
      #looking left
      if value < current.data:
        #no value left, value not in tree
        if current.left is None:
          return False
        elif current.left.data == value:
          return True
        else:
          current = current.left
      elif current.right is None:
        return False
      elif current.right.data == value:
        return True
      else:
        current = current.right

  def remove(self, value):  # sourcery skip: avoid-builtin-shadow
    # this is where you will remove a value from the BST
    if self.parent is None: return False
    is_parent = False
    #region if the head is the node to remove
    if self.parent.data == value:
      is_parent = True
      #if no branches, set head to None
      if self.parent.left is None and self.parent.right is None:
        self.parent = None
      elif self.right is None:
        self.parent = self.parent.left
      elif self.left is None:
        self.parent = self.parent.right
      else:
        #move down into first node of right branch
        next = self.parent.right
        previous = self.parent.right
        #look as far left to find the next largest value for the node to remove
        while next.left != None:
          previous = next
          next = next.left
        #found lowest left, but need to reassign its right branch
        previous.left = next.right
        #found the lowest left, its a leaf, swap
        next.left = self.parent.left
        next.right = self.parent.right
        self.parent = next
    #endregion

    found = False
    current = self.parent # this is going to be the node to remove
    prev = current # this will be the node just above the node to remove
    repl = current  # this will be the node to replace the removed node with
    prev2 = current # this will be the node above the replacement node
    while not found:
      #region looking left
      if value < current.data:
        #no value left, value not in tree
        if current.left is None:
          return False
        elif current.left.data == value:
          #if leaf, just remove
          if current.left.left is None and current.left.right is None:
            current.left = None
          elif current.left.left != None and current.left.right is None:
            current.left = current.left.left
          elif current.left.left is None:
            current.left = current.left.right
        else:
          current = current.left
      elif current.right is None:
        return False
      elif current.right.data == value:
        return True
      else:
        current = current.right
      #endregion


# ----- Node ------
class Node:
  def __init__(self, value):
    self.data = value
    self.right = None
    self.left = None

  def __str__(self):
    return f'{self.data}\nL:{self.left}\tR:{self.right}'