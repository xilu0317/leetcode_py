from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        dict = {}

        queue = deque([node])
        dict[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in dict:
                    dict[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                dict[curr].neighbors.append(dict[neighbor])

        return dict[node]
