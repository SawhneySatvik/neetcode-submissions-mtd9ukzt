class Solution:
    def merge(self, nums:List[int], low:int, mid:int, high:int) -> None:
        temp = []
        left = low
        right = mid + 1

        while (left <= mid and right <= high):
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
       
        while left <= mid:
            temp.append(nums[left])
            left += 1

        
        while right <= high:
            temp.append(nums[right])
            right += 1

        nums[low:high + 1] = temp

    def mergeSort(self, nums:List[int], low:int, high:int) -> None:
        if low >= high:
            return
        mid = (low + high) //2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums

    # INSERTION SORT
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     for i in range(1, len(nums)):
    #         key = nums[i]
    #         j = i - 1
    #         while j >= 0 and nums[j] > key:
    #             nums[j + 1] = nums[j]
    #             j -= 1
    #         nums[j+1] = key
    #     return nums

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