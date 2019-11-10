
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# TODO: error in code


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        dic = {}
        q = [node]
        while(len(q)):
            n = q.pop(0)
            m = Node(n.val, [])
            dic[n] = m

            for nb in n.neighbors:
                if nb not in dic:
                    q.append(nb)

        q = [node]
        s = set()
        while (len(q)):
            n = q.pop(0)
            m = dic[n]
            s.add(n)

            for nb in n.neighbors:
                if nb not in s:
                    q.append(nb)
                m.neighbors.append(dic[nb])

        return dic[node]
