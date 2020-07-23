class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # one item in list
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        # more than one item in list
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length - + 1
            return value

    def remove_tail(self):
        if not self.head:
            return None
        current = self.head
        prev = current
        while current.get_next() != None:
            prev = current
            current = current.get_next()

        prev.set_next(None)
        self.tail = prev
        return prev

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    # def get_max(self):
    #     # iterate through all elements
    #     cur_node = self.head
    #     while cur_node
