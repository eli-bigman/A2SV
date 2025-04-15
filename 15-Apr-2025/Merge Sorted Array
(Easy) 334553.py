# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_cp = nums1.copy()
        i = j = k = 0

        while i < m and j < n:
            if nums1_cp[i] <= nums2[j]:
                nums1[k] = nums1_cp[i]
                i += 1

            else:
                nums1[k] = nums2[j]
                j += 1
            
            k += 1

        while i < m:
            nums1[k] = nums1_cp[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1


