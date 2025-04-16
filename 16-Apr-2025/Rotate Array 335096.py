# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums) 

        k %=  size
        
        x = nums[size - k: ]
        y = nums[:size - k]

        nums[:] = x + y


