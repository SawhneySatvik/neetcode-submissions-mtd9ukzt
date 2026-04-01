class Solution:
    def dfs(self, r, c, cells, heights):
        rows, cols = len(heights), len(heights[0])

        if (r,c) in cells:
            return
        cells.add((r, c))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in directions:
            er, ec = r + dr, c + dc
            if 0 <= er < rows and 0 <= ec < cols:
                if heights[r][c] <= heights[er][ec] and (er, ec) not in cells:
                    self.dfs(er, ec, cells, heights)
 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = [(r,0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        pacific_set = set()
        atlantic_set = set()

        for r, c in pacific:
            self.dfs(r, c, pacific_set, heights)

        for r, c in atlantic:
            self.dfs(r, c, atlantic_set, heights)

        return list(pacific_set & atlantic_set)
