class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_pos = 1
        hash_set = set()

        for num in nums:
            hash_set.add(num)
            if num > 0 and num == min_pos:
                min_pos += 1
                while min_pos in hash_set:
                    min_pos += 1
        
        return min_pos