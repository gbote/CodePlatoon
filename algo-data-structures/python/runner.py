from linked_list import LinkList
from stack import Stack
from queue import Queue
from bst import Bst
import random

"""Testing Stack"""
# stack = Stack()
# # stack.pop()
# stack.push(1)
# stack.push(2)
# stack.push(4)
# stack.push(6)
# stack.push(8)
# stack.push(2)
# print(stack.size())
# print(stack)
# y = stack.pop()
# print(y)
# print(stack)

"""Testing Queue"""
# queue = Queue()
# # queue.dequeue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(4)
# queue.enqueue(6)
# queue.enqueue(8)
# queue.enqueue(2)
# print(queue.size())
# print(queue)
# y = queue.dequeue()
# print(y)
# print(queue)

"""Testing Linked List"""
# x = LinkList()
# x.add(1)
# x.add(2)
# x.add(3)
# print(x.get(0))
# print(x.get(1))
# print(x.get(2))
# print(x)
# x.remove(2)
# print(x)
# x.add(2)
# x.add(4)
# x.add(5)
# x.remove(1)
# print(x)

"""Testing BST"""
# bst = Bst()
# print(bst.contains(5))
# array = [6, 9, 13, 16, 14, 17, 3, 15, 12, 2, 10, 18, 11, 19, 5, 8, 1, 7, 4]
# for i in array:
#     bst.insert(i)

# def printTree(node, level=0):
#     if node != None:
#         printTree(node.left, level + 1)
#         print(' ' * 8 * level + '-> ' + str(node.data))
#         printTree(node.right, level + 1)
# # printTree(bst.parent)
# print(bst.contains(10))
# print(bst.contains(25))