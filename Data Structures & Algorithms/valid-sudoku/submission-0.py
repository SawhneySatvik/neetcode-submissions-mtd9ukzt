class Solution:
    def isValidRow(self, row: List[str]) -> bool:
        hash_table = {}
        for ele in row:
            hash_table[ele] = hash_table.get(ele, 0) + 1

        for key, val in hash_table.items():
            if key != "." and val > 1:
                return False
        return True
    
    def isValidCol(self, col: List[str]) -> bool:
        hash_table = {}
        for ele in col:
            hash_table[ele] = hash_table.get(ele, 0) + 1

        for key, val in hash_table.items():
            if key != "." and val > 1:
                return False
        return True

    def isValidBlock(self, block: List[List[str]]) -> bool:
        hash_table = {}
        for i in range(len(block)):
            for j in range(len(block[0])):
                val = block[i][j]
                hash_table[val] = hash_table.get(val, 0) + 1

        for key, val in hash_table.items():
            if key != "." and val > 1:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            if not self.isValidRow(board[i]):
                return False

        # Check columns
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not self.isValidCol(col):
                return False

        # Check blocks
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                block = []
                for i in range(3):
                    row = []
                    for j in range(3):
                        row.append(board[block_row + i][block_col + j])
                    block.append(row)

                if not self.isValidBlock(block):
                    return False

        return True

        