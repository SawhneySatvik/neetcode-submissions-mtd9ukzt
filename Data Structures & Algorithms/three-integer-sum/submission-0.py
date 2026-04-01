class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0, len(nums)-2):
            l, r = i+1, len(nums)-1
            
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    print((nums[i], nums[l], nums[r]))
                    res.add((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
        
        res = [list(a) for a in res]
        return res