from collections import deque


class Solution:
    def clone_graph(self, node):
        dic = {}

        # 1st BFS: create node-to-node mapping
        q = deque([node])
        while(len(q)):
            n = q.popleft()
            dic[n] = Node(n.val, [])

            for nb in n.neighbors:
                if nb not in dic:
                    q.append(nb)

        # 2nd BFS: associate nodes
        q = deque([node])
        s = set()
        while (len(q)):
            n = q.popleft()

            if (n not in s):
                s.add(n)

                for nb in n.neighbors:
                    if nb not in s:
                        q.append(nb)
                    dic[n].neighbors.append(dic[nb])

        return dic[node]


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
