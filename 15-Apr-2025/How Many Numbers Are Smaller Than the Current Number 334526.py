# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        res = []
        hashmap = {}
        for i, v in enumerate(sorted_nums):
            if v not in hashmap:
                hashmap[v] = i
        
        res = [hashmap[i] for i in nums ]
        

        return res
        
            