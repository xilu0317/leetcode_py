class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def clone_graph(self, node):
        if not node:
            return None

# first pass: create nodes
        dic = {}
        q = [node]
        while(len(q)):
            n = q.pop(0)
            m = Node(n.val, [])
            dic[n] = m

            for nb in n.neighbors:
                if nb not in dic:
                    q.append(nb)

# second pass: associate nodes
        q = [node]
        s = set()
        while (len(q)):
            n = q.pop(0)
            m = dic[n]
            if (n not in s):
                s.add(n)

                for nb in n.neighbors:
                    if nb not in s:
                        q.append(nb)
                    m.neighbors.append(dic[nb])

        return dic[node]
