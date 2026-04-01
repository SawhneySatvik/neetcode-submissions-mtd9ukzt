class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []

        n, m = len(nums1), len(nums2)
        i ,j = 0, 0

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                new_arr.append(nums1[i])
                i += 1
            else:
                new_arr.append(nums2[j])
                j += 1
        
        if i < n:
            new_arr.extend(nums1[i::])
        if j < m:
            new_arr.extend(nums2[j::])
        
        o = len(new_arr)
        if o%2 == 0:
            return (new_arr[(o//2)-1]+new_arr[(o//2)])/2
        else:
            return new_arr[(o//2)]