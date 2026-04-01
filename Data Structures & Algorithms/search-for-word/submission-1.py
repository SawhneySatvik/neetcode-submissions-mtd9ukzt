class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set() 
        def search(index, row, col):
            if (row, col) in seen:
                return False
            if index>=len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            seen.add((row, col))
            if board[row][col] == word[index] and (search(index+1, row+1, col) or search(index+1, row-1, col) or search(index+1, row, col+1) or search(index+1, row, col-1) ):
                return True
            else:
                seen.remove((row, col))
                return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(0, r, c):
                    return True

        return False