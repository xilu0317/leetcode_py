class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def max_area_of_island(self, grid):
        self.m, self.n = len(grid), len(grid[0])

        max_ = -float('inf')
        for i in range(self.m):
            for j in range(self.n):
                max_ = max(max_, self.dfs(grid, i, j))

        return max_

    def dfs(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        area = 1

        area += self.dfs(grid, i + 1, j)
        area += self.dfs(grid, i - 1, j)
        area += self.dfs(grid, i, j + 1)
        area += self.dfs(grid, i, j - 1)

        return area
