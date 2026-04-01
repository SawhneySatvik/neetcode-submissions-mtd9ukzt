class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        res = []
        for key, vals in hash_map.items():
            if vals > len(nums)//3:
                res.append(key)
        
        return res