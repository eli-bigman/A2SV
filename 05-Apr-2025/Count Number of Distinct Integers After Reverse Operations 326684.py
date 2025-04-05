# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev_arr = [int(str(i)[::-1]) for i in nums]
        return len(set(nums+rev_arr))
