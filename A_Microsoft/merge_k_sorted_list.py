from heapq import heappop, heapreplace, heapify

# KEY: tie-breaker: i guarantees uniqueness


class Solution:
    def merge_k_lists(self, lists):
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(heap)
        cur = dummy = ListNode(0)

        while heap:
            val, i, node = heap[0]

            if node.next:
                heapreplace(heap, (node.next.val, i, node.next))
            else:
                heappop(heap)

            cur.next = node
            cur = cur.next

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
