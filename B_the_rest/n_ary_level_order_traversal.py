class Solution:
    def level_order(self, root):
        if not root:
            return None

        q, res = [root], []
        while len(q):
            _len, level = len(q), []

            for x in range(_len):
                n = q.pop(0)
                level.append(n.val)

                for c in n.children:
                    q.append(c)

            res.append(level)

        return res


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
