class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def clone_graph(self, node):
        if not node:
            return None

        dic = {}

        # 1st BFS: create node-to-node mapping
        q = [node]
        while(len(q)):
            n = q.pop(0)
            dic[n] = Node(n.val, [])

            for nb in n.neighbors:
                if nb not in dic:
                    q.append(nb)

        # 2nd BFS: associate nodes
        q = [node]
        s = set()
        while (len(q)):
            n = q.pop(0)

            if (n not in s):
                s.add(n)

                for nb in n.neighbors:
                    if nb not in s:
                        q.append(nb)
                    dic[n].neighbors.append(dic[nb])

        return dic[node]
