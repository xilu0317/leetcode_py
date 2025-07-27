def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    provinces = set()
    for i in range(n):
        provinces.add(uf.find(i))

    return len(provinces)
