class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            curr_sum = 0
            for col in range(len(matrix[0])):
                curr_sum += matrix[row][col]
                self.prefixSum[row][col] = curr_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1, row2+1):
            if col1 > 0:
                sum_ += self.prefixSum[i][col2] - self.prefixSum[i][col1-1]
            else:
                sum_ += self.prefixSum[i][col2]
        return sum_

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)