class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):
        if not head:
            return False

        slow = fast = head

        while True:
            if fast.next == None or fast.next.next == None:
                break

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
