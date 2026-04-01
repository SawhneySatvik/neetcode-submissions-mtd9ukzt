class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    er, ec = r+dr, c+dc
                    if 0 <= er < rows and 0 <= ec < cols and grid[er][ec] == 1:
                        grid[er][ec] = 2
                        queue.append((er, ec))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1 