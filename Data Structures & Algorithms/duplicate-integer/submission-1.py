class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ = set()
        for num in nums:
            if num in hash_:
                return True
            hash_.add(num)
        return False