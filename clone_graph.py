from collections import deque

# The core idea is to create a map and do a bfs traversal on it.
# The map will store the original node as the key and map to the new node.

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        dict = {}

        queue = deque([node])
        dict[node] = Node(node.val)

        while queue:
            cur = queue.popleft()

            for nb in cur.neighbors:
                #  Check if the nb has already been visited
                if nb not in dict:
                    dict[nb] = Node(nb.val)
                    # this is needed for the traversal to work
                    queue.append(nb)
                
                dict[cur].neighbors.append(dict[nb])

        return dict[node]
