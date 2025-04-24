# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_arr = float('inf')
        total = 0

        arr_size = len(nums)

        for right in range(arr_size):
            total += nums[right]

            while total >= target:
                min_arr = min(right - left + 1, min_arr)
                total -= nums[left]
                left += 1

        
        return 0 if min_arr == float('inf') else min_arr