class Solution:
    def dfs(self, r: int, c: int, board) -> None:
        rows, cols = len(board), len(board[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        
        board[r][c] = 'Y'
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr, dc in directions:
            self.dfs(dr+r, dc+c, board)

    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            self.dfs(r, 0, board)
            self.dfs(r, cols-1, board)
        
        for c in range(cols):
            self.dfs(0, c, board)
            self.dfs(rows-1, c, board)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'Y':
                    board[r][c] = 'O'
