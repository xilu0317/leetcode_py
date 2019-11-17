class Solution:
    def copy_random_list(self, head):
        dict_ = {}
        m = n = head

        # first traversal creates a mapping
        while m:
            dict_[m] = Node(m.val, None, None)
            m = m.next

        # second traversal sets up the proper relationship between nodes
        while n:
            dict_.get(n).next = dict_.get(n.next)
            dict_.get(n).random = dict_.get(n.random)
            n = n.next

        return dict_.get(head)


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
