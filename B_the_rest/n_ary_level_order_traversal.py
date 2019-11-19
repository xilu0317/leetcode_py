from collections import deque


class Solution:
    def level_order(self, root):
        if not root:
            return None

        q, res = deque([root]), []
        while len(q):
            _len, level = len(q), []

            for x in range(_len):
                node = q.popleft()
                level.append(node.val)

                for c in node.children:
                    q.append(c)

            res.append(level)

        return res


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
