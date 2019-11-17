class Solution:
    def level_order(self, root):
        if not root:
            return None

        q, res = [root], []
        while len(q):
            len_, level = len(q), []

            for x in range(len_):
                node = q.pop(0)
                level.append(node.val)

                for c in node.children:
                    q.append(c)

            res.append(level)

        return res


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
