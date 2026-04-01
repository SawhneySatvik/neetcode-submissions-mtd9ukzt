class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, path):
            if total == target:
                res.append(path.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            dfs(i, total+nums[i], path)

            path.pop()
            dfs(i + 1, total, path)
        
        dfs(0, 0, [])
        return res