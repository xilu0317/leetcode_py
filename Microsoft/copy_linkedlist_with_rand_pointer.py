class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        dic = dict()
        m = n = head

        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next

        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next

        return dic.get(head)
