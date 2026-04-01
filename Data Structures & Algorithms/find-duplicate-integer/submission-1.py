class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0

        for num in nums:
            if seen & (1 << num):
                return num
            seen |= (1 << num)
        
        return seen