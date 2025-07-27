from collections import deque
from typing import List

class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children else []

def bfs_n_ary_tree(root: Node) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            # Add all children to the queue
            for child in node.children:
                queue.append(child)

        result.append(level)

    return result

# 
from collections import deque
def bfs_nary_tree(root: Node) -> List[List[int]]:
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            cur = q.popleft()
            level.append(cur.val)
            for child in cur.children:
                q.append(child)
                
        res.append(level)

    return res

