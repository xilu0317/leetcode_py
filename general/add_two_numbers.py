# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        cur1 = l1, cur2 = l2
        cur = dummy = ListNode(0)
        sum = 0

        while (cur1 or cur2):
            sum = sum // 10

            if (cur1):
                sum += cur1.val
                cur1 = cur1.next

            if (cur2):
                sum += cur2.val
                cur2 = cur2.next

            cur.next = ListNode(sum % 10)
            cur = cur.next

        if (sum >= 10):
            cur.next = ListNode(1)

        return dummy.next
