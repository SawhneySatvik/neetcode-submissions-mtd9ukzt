class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset = []
        
        def backtrack(start, path):
            self.subset.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
        backtrack(0, [])
        return self.subset