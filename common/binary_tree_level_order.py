from collections import deque

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        res.append(level)
        
    return res
