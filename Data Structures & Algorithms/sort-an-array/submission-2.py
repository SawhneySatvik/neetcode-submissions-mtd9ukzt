class Solution:

    # INSERTION SORT
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

    # BUBBLE SORT
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)-1, -1, -1):
    #         for j in range(i):
    #             if nums[j]>nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #     return nums


    # SELECTION SORT
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] > nums[j]:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #     return nums