# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))


        sorted_nums = sorted(nums, key=lambda x: x * 10, reverse=True)


        largest_number = ''.join(sorted_nums)

        if largest_number[0] == '0':
            largest_number = '0'

        return largest_number