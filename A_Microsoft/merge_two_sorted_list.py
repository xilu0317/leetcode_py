class Solution:
    def merge_two_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        cur = dummy = ListNode(-1)
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
