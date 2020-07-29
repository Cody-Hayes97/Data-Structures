"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head and self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        self.length -= 1
        if self.head is None:
            return None
        elif self.head == self.tail:
            temp_val = self.head.value
            self.head = None
            self.tail = None
            return temp_val
        else:
            temp_val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return temp_val

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        self.length -= 1
        cur = self.tail
        if self.tail is None:
            return None
        elif self.tail == self.head:
            temp = self.tail.value
            self.head = None
            self.tail = None
            return temp

        self.tail = cur.prev
        self.tail.next = None
        return cur.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # delete()
        if self.length == 0:
            return None
        if self.head == node:
            return
        else:
            nxt = node.next
            pre = node.prev
            if node == self.tail:
                self.tail = pre
            else:
                nxt.prev = pre
            pre.next = nxt

            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        # save the value we deleted
        # add to head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return None
        if self.tail == node:
            return
        else:
            nxt = node.next
            pre = node.prev
            if node == self.head:
                self.head = nxt
            else:
                pre.next = nxt
            nxt.prev = pre
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.value == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.value == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        maxi = self.head.value
        cur = self.head.next
        while cur:
            if cur.value > maxi:
                maxi = cur.value
            cur = cur.next
        return maxi

    def __str__(self):
        cur = self.head
        output = ""
        while cur is not None:
            output += f'{cur.value} -> '
            cur = cur.next
        return output


ll = DoublyLinkedList()
ll.add_to_head(5)
ll.add_to_head(12)
ll.add_to_tail(2)
ll.add_to_tail(5)

# ll.move_to_end(ll.head)
# ll.move_to_end(ll.head)
# ll.move_to_front(ll.tail)
# print(ll.tail.next.value)
# ll.remove_from_head()
# ll.remove_from_tail()


print(ll.get_max())
# print(ll.head.value)
# print(ll)
