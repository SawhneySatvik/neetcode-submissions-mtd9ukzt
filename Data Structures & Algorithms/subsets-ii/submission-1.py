class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i: int, subset: List[int]) -> None:
            if i >= len(nums):
                res.append(subset.copy())
                return

            backtrack(i+1, subset+[nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res