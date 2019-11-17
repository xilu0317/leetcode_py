class Solution:
    def add_two_numbers(self, l1, l2):
        cur1, cur2 = l1, l2
        cur = dummy = ListNode(0)
        _sum = 0

        while cur1 or cur2:
            _sum = _sum // 10

            if cur1:
                _sum += cur1.val
                cur1 = cur1.next

            if cur2:
                _sum += cur2.val
                cur2 = cur2.next

            cur.next = ListNode(_sum % 10)
            cur = cur.next

        if _sum >= 10:
            cur.next = ListNode(1)

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
