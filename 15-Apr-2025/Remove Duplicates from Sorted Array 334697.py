# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return nums


        len_nums = len(nums)
        j=0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
            
        return j+1
