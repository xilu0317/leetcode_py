from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        
        # ▶️ Process the current node
        print(node.val)  # or store in result list

        # ▶️ Add children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
