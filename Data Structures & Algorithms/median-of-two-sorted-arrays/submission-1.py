class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []

        n, m = len(nums1), len(nums2)
        i ,j = 0, 0

        median1, median2 = 0, 0

        total = (n+m)

        for count in range((total//2)+1):
            median2 = median1
            if i<n and j<m:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < n:
                median1 = nums1[i]
                i+=1
            else:
                median1 = nums2[j]
                j+=1

        if total%2==0:
            return (median1+median2) / 2
        else:
            return median1