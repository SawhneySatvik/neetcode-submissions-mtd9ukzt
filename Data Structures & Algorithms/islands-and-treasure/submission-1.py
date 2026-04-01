class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        dist = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                er, ec = r+dr, c+dc

                if 0 <= er < rows and 0 <= ec < cols and grid[er][ec] == INF:
                    grid[er][ec] = grid[r][c] + 1
                    queue.append((er, ec))