def numIslands(grid: List[List[str]]) -> int:
    if not grid: 
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '0'       # mark as visited
        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count
