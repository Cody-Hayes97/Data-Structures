"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from linked_list_queue import LinkedList

# with Linked List


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.back = self.storage
        self.back.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.front = self.storage
            self.size -= 1
            return self.front.remove_head()

# array Impl


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()

# Number 3 Answer
# The difference between using an array vs using a linked list is for one, the amount of setup needed to take place for the linkedlist, where as with arrays you have certain method already made for you to use. Another difference would be accessing the linked lists properties requires more though than using an array. for example, I found myself constantly looking at the linked list I built so I know which method are available to me.
