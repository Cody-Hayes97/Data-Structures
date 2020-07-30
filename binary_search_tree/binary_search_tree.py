"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # planning
        # start at root and loop until self is None
        # if value <= self
        #  if self.left is None
        # insert our value
        # else
        # go left (update self to be self.left)
        # elif value > self
        # if self.right is None
        # insert our value
        # else
        # go right (update self to be self.right)
        cur_node = self
        while cur_node is not None:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BSTNode(value)
                else:
                    cur_node.left.insert(value)
            elif value >= cur_node.value:
                if cur_node.right is None:
                    cur_node.right = BSTNode(value)
                else:
                    cur_node.right.insert(value)
            return value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # compare target value to cur value
        # 1. == return True
        # 2. < we go left
        # 3. > we go right
        # 4. if cant go left or right (not found, return false)
        cur_node = self
        if cur_node is not None:
            is_found = self._find(target, cur_node)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, target, cur_node):
        if target > cur_node.value and cur_node.right:
            return self._find(target, cur_node.right)
        elif target < cur_node.value and cur_node.left:
            return self._find(target, cur_node.left)
        if target == cur_node.value:
            return True

        # Return the maximum value found in the tree

    def get_max(self):
        # right most node will always be the biggest
        cur_node = self
        if cur_node is None:
            return None
        while cur_node.right is not None:
            cur_node = cur_node.right
        return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursion method
        cur_node = self
        fn(cur_node.value)
        if cur_node.left is not None:
            cur_node.left.for_each(fn)
        if cur_node.right is not None:
            cur_node.right.for_each(fn)

        # # iterative method
        # fn(cur_node.value)
        # while cur_node.left:
        #     cur_node = cur_node.left
        #     fn(cur_node)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)

            if self.right:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            cur_node = q.dequeue()
            print(cur_node.value)
            if cur_node.left:
                q.enqueue(cur_node.left)
            if cur_node.right:
                q.enqueue(cur_node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.size > 0:
            cur_node = s.pop()
            print(cur_node.value)
            if cur_node.right:
                s.push(cur_node.right)
            if cur_node.left:
                s.push(cur_node.left)

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(15)

bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(12)
bst.insert(18)
bst.insert(25)

bst.dft_print(bst)


# bst.in_order_print()
# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
