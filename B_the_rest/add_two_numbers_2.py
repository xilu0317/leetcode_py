class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        arr1, arr2 = [], []
        cur = l1
        while cur:
            arr1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            arr2.append(cur.val)
            cur = cur.next

        _sum, _list = 0, []
        while len(arr1) or len(arr2):
            _sum //= 10
            if len(arr1):
                _sum += arr1.pop() or 0
            if len(arr2):
                _sum += arr2.pop() or 0
            _list.append(_sum % 10)
        if _sum >= 10:
            _list.append(1)

        cur = dummy = ListNode(-1)
        while len(_list):
            cur.next = ListNode(_list.pop())
            cur = cur.next

        return dummy.next
