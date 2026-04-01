class Solution:
    def dfs(self, r, c, grid, visited):
        rows, cols = len(grid), len(grid[0])

        if r < 0 or c < 0 or r >= rows or c >= cols:
            return

        if grid[r][c] == "0" or visited[r][c]:
            return

        visited[r][c] = True

        self.dfs(r+1, c, grid, visited)
        self.dfs(r-1, c, grid, visited)
        self.dfs(r, c+1, grid, visited)
        self.dfs(r, c-1, grid, visited)


    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    self.dfs(r, c, grid, visited)
                    islands += 1

        return islands