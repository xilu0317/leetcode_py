class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head):
        dic = dict()
        m = n = head

        # first traveral create a mapping
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next

        # second traversal sets up the relationship between nodes
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next

        return dic.get(head)
