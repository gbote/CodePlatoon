# Data structures

- a data structure is a data organization, management, and storage format that enables efficient access and modification of that data
- in other words, a collection of values, the relationships between them, and functions/operations that can be performed on them.



common data structures:
- arrays
    - a contiguous data structure, because all the data is next to each other physically on your machine.
- linked-list
    - a non-contiguous data structure. each element can be anywhere physically in memory, because each elemetn has a reference to the next
    - a singly-linked list each previous node has a reference to the next
    - a doubly-linked list each node has a reference to the next node and the previous node
- queues and stacks
    - a stack is an array or linked list where you can only add or remove to one end (filo)
    - a queue is an array or linked list where you can only add to one end, and only remove from the other (fifo)
- hash tables
    - allows you to create a list of key-value pairs. after creating a pair, you can retrieve the value using the key
    - no matter how large the hash table is, it takes the same amount of time to find a value for a key
    - under the hood, hash tables are often implemented using arrays

- hashing
    - a hashing function takes some value as input, and returns a hash, an integer in this case.
    - hashing is a one-way operation. while it's generally fast to hash a single value, there's no straightforward way to reverse a hash
    - hashing the same input always produces the same output ( no randomness )
    - it is possible, but unlikely, that multiple values will have the same hash (hash collision)

- trees
    a data structure with a root node, which can have many child nodes, which each have many child nodes
    a binary tree is a tree in which each node has at most 2 children
    a binary search tree is a binary tree that is sorted. for example, each node has its larger child on the left, and the smaller child on the right

"Bad programmers worry about the code. good programmers worry about the datastructures and their relationships" - Linus Torvalds

