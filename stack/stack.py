"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
from linked_list_stack import LinkedList

# Linked Link Impl
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.head = self.storage
#         self.head.add_to_head(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.tail = self.storage
#             self.size -= 1
#             return self.tail.remove_head()

# array Impl


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

# number 3 answer:
# The difference between using an array vs using a linked list is for one, the amount of setup needed to take place for the linkedlist, where as with arrays you have certain method already made for you to use. Another difference would be accessing the linked lists properties requires more though than using an array. for example, I found myself constantly looking at the linked list I built so I know which method are available to me.
