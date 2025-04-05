# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:        
        i = 0
        j = 1
        while i < len(nums)  and j < len(nums) :

            if nums[i] == nums[j]:
                nums[i] = nums[i] * 2
                nums[j] = 0
            i += 1
            j += 1
        
        zero_count = 0
        while 0 in nums:
            zero_count += 1
            nums.remove(0)

        return nums + [0] * zero_count