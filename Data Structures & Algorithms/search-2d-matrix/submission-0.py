class Solution:
    def searchCol(self, matrix: List[List[int]], target:int) -> int:
        low, high = 0, len(matrix) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def searchRow(self, row:List[int], target:int) -> bool:
        low, high = 0, len(row)-1

        while low <= high:
            mid = (low+high)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row = self.searchCol(matrix, target)

        return self.searchRow(matrix[row], target)