class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        max_len = 0
        curr_len = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                curr_len += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                max_len = max(curr_len, max_len)
                curr_len = 1
        return max(max_len, curr_len)