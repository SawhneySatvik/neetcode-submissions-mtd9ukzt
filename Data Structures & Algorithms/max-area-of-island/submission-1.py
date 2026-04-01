class Solution:
    def dfs(self, r, c, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        area = 1
        for dr, dc in directions:
            area += self.dfs(r+dr, c+dc, grid)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.dfs(r, c, grid)
                    max_area = max(max_area, area)
        
        return max_area