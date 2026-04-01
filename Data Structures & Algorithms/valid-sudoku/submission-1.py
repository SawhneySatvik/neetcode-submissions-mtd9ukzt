class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                block_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in blocks[block_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                blocks[block_index].add(val)

        return True
