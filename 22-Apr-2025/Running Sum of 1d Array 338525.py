# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            res.append(current_sum)
        
        return res
